"""Strict YAML and JSONL readers that report positioned diagnostics.

Strictness is deliberate: duplicate keys, multiple YAML documents, blank JSONL
lines and non-standard JSON constants are rejected so that a file the Dram
loader might read differently can never pass local checks.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .diagnostics import Diagnostic, PackContentError

_MERGE_TAG = "tag:yaml.org,2002:merge"


class _DuplicateKey(yaml.MarkedYAMLError):
    pass


class _StrictLoader(yaml.SafeLoader):
    """SafeLoader that rejects repeated keys within one mapping."""

    def construct_yaml_timestamp(self, node):
        try:
            return super().construct_yaml_timestamp(node)
        except (ValueError, OverflowError) as err:
            raise yaml.constructor.ConstructorError(
                "while constructing a timestamp", node.start_mark, str(err), node.start_mark
            ) from None

    def flatten_mapping(self, node):
        merge_node = None
        for key_node, _ in node.value:
            if key_node.tag == _MERGE_TAG:
                if merge_node is not None:
                    raise _DuplicateKey(
                        problem=f"duplicate key '<<' (first defined on line {merge_node.start_mark.line + 1})",
                        problem_mark=key_node.start_mark,
                    )
                merge_node = key_node
        return super().flatten_mapping(node)

    def construct_mapping(self, node, deep=False):  # noqa: D401 - PyYAML hook
        if isinstance(node, yaml.MappingNode):
            seen: dict[Any, yaml.Node] = {}
            for key_node, _ in node.value:
                if key_node.tag == _MERGE_TAG:
                    continue
                key = self.construct_object(key_node, deep=True)
                try:
                    hash(key)
                except TypeError:
                    raise yaml.constructor.ConstructorError(
                        "while constructing a mapping", node.start_mark, "found unhashable key", key_node.start_mark
                    ) from None
                if key in seen:
                    raise _DuplicateKey(
                        problem=f"duplicate key {key!r} (first defined on line {seen[key].start_mark.line + 1})",
                        problem_mark=key_node.start_mark,
                    )
                seen[key] = key_node
        return super().construct_mapping(node, deep=deep)


_StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _StrictLoader.construct_mapping)
_StrictLoader.add_constructor("tag:yaml.org,2002:timestamp", _StrictLoader.construct_yaml_timestamp)


def _read_text(path: Path) -> str:
    try:
        return path.read_bytes().decode("utf-8")
    except FileNotFoundError:
        raise PackContentError([Diagnostic(str(path), "missing-file", "file does not exist")]) from None
    except IsADirectoryError:
        raise PackContentError([Diagnostic(str(path), "missing-file", "expected a file, found a directory")]) from None
    except UnicodeDecodeError as err:
        raise PackContentError([Diagnostic(str(path), "encoding", f"not valid UTF-8: {err.reason}")]) from None


def parse_yaml(text: str, source: str) -> Any:
    """Parse one YAML document safely, rejecting duplicate keys."""
    try:
        return yaml.load(text, Loader=_StrictLoader)  # noqa: S506 - strict SafeLoader subclass
    except _DuplicateKey as err:
        mark = err.problem_mark
        raise PackContentError(
            [Diagnostic(source, "yaml-duplicate-key", err.problem, mark.line + 1, mark.column + 1)]
        ) from None
    except yaml.YAMLError as err:
        mark = getattr(err, "problem_mark", None) or getattr(err, "context_mark", None)
        message = " ".join(str(p) for p in (getattr(err, "context", None), getattr(err, "problem", None)) if p)
        raise PackContentError(
            [
                Diagnostic(
                    source,
                    "yaml-syntax",
                    message or str(err),
                    mark.line + 1 if mark else None,
                    mark.column + 1 if mark else None,
                )
            ]
        ) from None
    except RecursionError:
        raise PackContentError([Diagnostic(source, "yaml-syntax", "document nesting too deep")]) from None


def load_yaml(path: Path) -> Any:
    path = Path(path)
    return parse_yaml(_read_text(path), str(path))


def _reject_constant(name: str):
    raise ValueError(f"non-standard JSON constant {name}")


class _DuplicateJsonKey(ValueError):
    pass


def _unique_pairs(pairs):
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise _DuplicateJsonKey(f"duplicate key {key!r}")
        out[key] = value
    return out


def parse_jsonl(text: str, source: str) -> list[dict[str, Any]]:
    """Parse JSON Lines where every line is one JSON object.

    All problems are collected so a single run reports every bad line.
    """
    records: list[dict[str, Any]] = []
    problems: list[Diagnostic] = []
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()  # trailing newline terminates the last record
    for number, raw in enumerate(lines, start=1):
        line = raw[:-1] if raw.endswith("\r") else raw
        if not line.strip():
            problems.append(Diagnostic(source, "jsonl-blank-line", "blank line", number))
            continue
        try:
            value = json.loads(line, object_pairs_hook=_unique_pairs, parse_constant=_reject_constant)
        except _DuplicateJsonKey as err:
            problems.append(Diagnostic(source, "jsonl-duplicate-key", str(err), number))
            continue
        except (ValueError, RecursionError) as err:
            problems.append(Diagnostic(source, "jsonl-syntax", f"invalid JSON: {err}", number))
            continue
        if not isinstance(value, dict):
            problems.append(Diagnostic(source, "jsonl-not-object", f"expected an object, found {type(value).__name__}", number))
            continue
        records.append(value)
    if problems:
        raise PackContentError(problems)
    return records


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    path = Path(path)
    return parse_jsonl(_read_text(path), str(path))
