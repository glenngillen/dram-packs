"""Structural validation of a pack and its repository index.

Mirrors the pinned Dram loader (``internal/pack``: ``pack.go``, ``schema.go``,
``registry.go``, ``set.go``, ``index.go``) closely enough that a pack passing
here is expected to load there; the pinned CLI itself remains the authority
and is exercised separately. Validation is not evaluation: nothing here runs
a detector or produces a recognition verdict.
"""

from __future__ import annotations

import functools
import json
import posixpath
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import jsonschema
import jsonschema.validators

from .diagnostics import Diagnostic, PackContentError
from .docs import placeholders
from .pinned import Pinned
from .readers import load_jsonl, load_yaml

PACK_FILES = {"pack.yaml": "pack", "groups.yaml": "groups", "outcomes.yaml": "outcomes", "progress.yaml": "progress"}
PATTERN_FILES = {"pattern.yaml": "pattern", "text.yaml": "text", "kinds.yaml": "kinds", "effects.yaml": "effects", "writes.yaml": "writes"}
FILE_DEFS = {"pack": "packFile", "groups": "groupsFile", "outcomes": "outcomesFile", "progress": "progressFile"}
PATTERN_DEFS = {"pattern": "patternFile", "text": "textFile", "kinds": "kindsFile", "effects": "effectsFile", "writes": "writesFile"}
INDEX_NAME = "dram.yaml"
INDEX_VERSION = 1

# Pinned at bdea6f6: internal/blocks/checks/checks.go ``Implemented`` and
# ``GateImplemented``. Every other registry block validates but does not run.
IMPLEMENTED_CHECKS = frozenset({"tool_call_matches", "tool_call_sequence"})
IMPLEMENTED_GATES = frozenset({"tool_call_matches"})

# docs/pack-schema.md, text.yaml: the placeholders code fills, per field.
# Every other text field takes none.
PLACEHOLDERS: dict[tuple[str, ...], set[str]] = {
    ("report", "seen"): {"cases", "applicable"},
    ("report", "not_seen"): {"count"},
    ("report", "slipped"): {"session"},
}


@dataclass(frozen=True)
class BlockRef:
    field: str
    name: str
    kind: str
    params: dict[str, Any] | None


def _list(v: Any) -> list[Any]:
    return v if isinstance(v, list) else []


def _dict(v: Any) -> dict[str, Any]:
    return v if isinstance(v, dict) else {}


def block_refs(pattern: dict[str, Any]) -> list[BlockRef]:
    """Every block a pattern.yaml names, in the loader's order."""
    out: list[BlockRef] = []

    def add(field: str, v: Any, kind: str, key: str = "block") -> None:
        if isinstance(v, dict) and isinstance(v.get(key), str):
            out.append(BlockRef(field, v[key], kind, v))

    add("applies_to", pattern.get("applies_to"), "check")
    det = _dict(pattern.get("detection"))
    for i, c in enumerate(_list(det.get("code"))):
        add(f"detection.code[{i}]", c, "check")
    model = det.get("model")
    add("detection.model", model, "model")
    for i, e in enumerate(_list(_dict(model).get("may_cite"))):
        field = f"detection.model.may_cite[{i}]"
        if isinstance(e, str):
            out.append(BlockRef(field, e, "signal", None))
        elif isinstance(e, dict):
            for name, params in e.items():
                out.append(BlockRef(field, name, "signal", _dict(params)))
    for i, c in enumerate(_list(_dict(pattern.get("continuous")).get("mechanisms"))):
        add(f"continuous.mechanisms[{i}]", c, "check")
    for i, m in enumerate(_list(pattern.get("moments"))):
        add(f"moments[{i}]", m, "moment", key="signal")
    return out


def executable_refs(pattern: dict[str, Any]) -> list[BlockRef]:
    """Blocks the pinned build would actually run for fixed-pattern detection.

    Empty unless at least one ``detection.code`` check is implemented. An
    ``applies_to`` gate the build does not run narrows the pattern to nothing,
    so nothing is executable behind it.
    """
    refs = block_refs(pattern)
    gate = [r for r in refs if r.field == "applies_to"]
    if gate and gate[0].name not in IMPLEMENTED_GATES:
        return []
    code = [r for r in refs if r.field.startswith("detection.code[") and r.name in IMPLEMENTED_CHECKS]
    return (gate + code) if code else []


@functools.lru_cache(maxsize=None)
def _validator(schema_json: str, definition: str) -> Any:
    schema = json.loads(schema_json)
    root = {"$ref": f"#/$defs/{definition}", "$defs": schema["$defs"]}
    cls = jsonschema.validators.validator_for(schema, default=jsonschema.Draft202012Validator)
    return cls(root)


def _schema_errors(pinned: Pinned, definition: str, value: Any, source: str, line: int | None = None) -> list[Diagnostic]:
    if definition not in pinned.schema["$defs"]:
        return [Diagnostic(source, "schema", f"pinned schema has no definition {definition!r}", line)]
    v = _validator(json.dumps(pinned.schema, sort_keys=True), definition)
    out = []
    for err in sorted(v.iter_errors(value), key=lambda e: list(map(str, e.absolute_path))):
        where = ".".join(str(p) for p in err.absolute_path) or "<root>"
        out.append(Diagnostic(source, "schema", f"{where}: {err.message}", line))
    return out


@dataclass
class Assembled:
    data: dict[str, Any]
    patterns: dict[str, dict[str, Any]]
    prose: dict[str, str]


def assemble(pack_dir: Path) -> Assembled:
    """Read a pack directory the way the loader does, strictly."""
    pack_dir = Path(pack_dir)
    problems: list[Diagnostic] = []
    data: dict[str, Any] = {}
    if not (pack_dir / "pack.yaml").is_file():
        raise PackContentError([Diagnostic(str(pack_dir / "pack.yaml"), "missing-file", "a pack needs pack.yaml")])
    for name, key in PACK_FILES.items():
        path = pack_dir / name
        if path.is_file():
            try:
                data[key] = load_yaml(path)
            except PackContentError as err:
                problems += err.diagnostics
    prose = {p.name: p.read_text(encoding="utf-8") for p in sorted(pack_dir.glob("*.md")) if p.is_file()}
    patterns: dict[str, dict[str, Any]] = {}
    patterns_dir = pack_dir / "patterns"
    if patterns_dir.is_dir():
        for d in sorted(p for p in patterns_dir.iterdir() if p.is_dir()):
            one: dict[str, Any] = {}
            for name, key in PATTERN_FILES.items():
                if (d / name).is_file():
                    try:
                        one[key] = load_yaml(d / name)
                    except PackContentError as err:
                        problems += err.diagnostics
            cases = d / "eval" / "cases.jsonl"
            if cases.is_file():
                try:
                    one["cases"] = load_jsonl(cases)
                except PackContentError as err:
                    problems += err.diagnostics
            for md in sorted(d.glob("*.md")):
                prose[f"{d.name}/{md.name}"] = md.read_text(encoding="utf-8")
            patterns[d.name] = one
    if problems:
        raise PackContentError(problems)
    return Assembled(data, patterns, prose)


def _lookup(pinned: Pinned, field: str, name: str, kind: str, source: str) -> tuple[dict[str, Any] | None, list[Diagnostic]]:
    """Find a registry block, refusing an unknown name or the wrong kind (``registry.block``)."""
    b = pinned.registry["blocks"].get(name)
    if not isinstance(b, dict):
        return None, [Diagnostic(source, "block-unknown", f"{field} names block {name!r}, which the pinned CLI does not have")]
    if b.get("kind") != kind:
        return None, [Diagnostic(source, "block-kind", f"{field} names {name!r}, a {b.get('kind')} block, not a {kind} block")]
    return b, []


def _check_params(block: dict[str, Any], field: str, name: str, params: dict[str, Any], source: str, *, slot_keys: bool = True) -> list[Diagnostic]:
    """Validate parameters against a block's schema, as the loader's resolved schema does."""
    schema = dict(_dict(block.get("params")))
    props: dict[str, Any] = {"id": {"type": "string"}, "block": {"type": "string"}, "signal": {"type": "string"}} if slot_keys else {}
    props.update(_dict(schema.get("properties")))
    schema["properties"] = props
    errs = list(jsonschema.Draft202012Validator(schema).iter_errors(params))
    if errs:
        return [Diagnostic(source, "block-params", f"{field} ({name}): {errs[0].message}")]
    return []


def _check_blocks(pinned: Pinned, pattern: dict[str, Any], source: str) -> list[Diagnostic]:
    out = []
    for ref in block_refs(pattern):
        b, problems = _lookup(pinned, ref.field, ref.name, ref.kind, source)
        out += problems
        if b is None or ref.params is None:
            continue
        out += _check_params(b, ref.field, ref.name, ref.params, source, slot_keys=not ref.field.startswith("detection.model.may_cite"))
    return out


def _check_effects(pinned: Pinned, effects: Any, source: str) -> list[Diagnostic]:
    """``registry.checkEffects``: each effect names a savings block and, optionally, a signal."""
    out = []
    for i, e in enumerate(_list(_dict(effects).get("effects"))):
        e = _dict(e)
        for key, kind in (("block", "savings"), ("signal", "signal")):
            if isinstance(e.get(key), str):
                out += _lookup(pinned, f"effects[{i}].{key}", e[key], kind, source)[1]
    return out


def _check_outcomes(pinned: Pinned, outcomes: Any, source: str) -> list[Diagnostic]:
    """``registry.checkOutcomes``: each outcome names a measure block and passes it parameters it takes."""
    out = []
    for i, o in enumerate(_list(_dict(outcomes).get("outcomes"))):
        o = _dict(o)
        field = f"outcomes[{i}].measure"
        name = o.get("measure") if isinstance(o.get("measure"), str) else ""
        b, problems = _lookup(pinned, field, name, "measure", source)
        out += problems
        if b is not None and isinstance(o.get("params"), dict):
            out += _check_params(b, field, name, o["params"], source)
    return out


def _check_text(text: Any, source: str) -> list[Diagnostic]:
    out = []

    def visit(path: tuple[str, ...], v: Any) -> None:
        if isinstance(v, dict):
            for k, child in v.items():
                visit(path + (str(k),), child)
        elif isinstance(v, str):
            allowed = PLACEHOLDERS.get(path, set())
            for name in placeholders(v):
                if name not in allowed:
                    where = ".".join(path)
                    ok = ", ".join("{" + a + "}" for a in sorted(allowed)) or "none"
                    out.append(Diagnostic(source, "placeholder", f"{where} uses {{{name}}}; supported here: {ok}"))

    visit((), text)
    return out


def validate_pack(pack_dir: Path, pinned: Pinned) -> list[Diagnostic]:
    """Schema, block-registry, reference and placeholder diagnostics."""
    pack_dir = Path(pack_dir)
    try:
        a = assemble(pack_dir)
    except PackContentError as err:
        return err.diagnostics
    out: list[Diagnostic] = []
    for key, definition in FILE_DEFS.items():
        if key in a.data:
            out += _schema_errors(pinned, definition, a.data[key], str(pack_dir / f"{key}.yaml"))
    for name, one in a.patterns.items():
        pdir = pack_dir / "patterns" / name
        before = len(out)
        for key, definition in PATTERN_DEFS.items():
            if key in one:
                out += _schema_errors(pinned, definition, one[key], str(pdir / f"{key}.yaml"))
        for line, case in enumerate(one.get("cases", []), start=1):
            out += _schema_errors(pinned, "caseLine", case, str(pdir / "eval" / "cases.jsonl"), line)
        if len(out) == before:
            out += _schema_errors(pinned, "patternDir", one, str(pdir))
    if out:
        return out

    pack_id = a.data["pack"]["id"]
    scope = pack_id.split("/", 1)[0] + "/"
    groups = {g["id"]: g for g in _list(_dict(a.data.get("groups")).get("groups"))}
    for gid, g in groups.items():
        for pname in _list(g.get("patterns")):
            if pname not in a.patterns:
                out.append(Diagnostic(str(pack_dir / "groups.yaml"), "ref-group-pattern", f"group {gid} lists {pname}, which has no pattern directory"))
    for name, one in a.patterns.items():
        pdir = pack_dir / "patterns" / name
        pattern = _dict(one.get("pattern"))
        src = str(pdir / "pattern.yaml")
        if not str(pattern.get("id", "")).startswith(scope):
            out.append(Diagnostic(src, "pattern-unscoped", f"id {pattern.get('id')} is not scoped by the pack id {pack_id}"))
        group = pattern.get("group")
        if group and group not in groups:
            out.append(Diagnostic(src, "ref-group", f"group {group} is not one groups.yaml defines"))
        model = _dict(_dict(pattern.get("detection")).get("model"))
        for key in ("prompt", "agents"):
            ref = model.get(key)
            if isinstance(ref, str) and f"{name}/{ref}" not in a.prose:
                out.append(Diagnostic(src, "ref-prose", f"detection.model.{key} names {ref}, which is not in the pattern"))
        out += _check_blocks(pinned, pattern, src)
        if "effects" in one:
            out += _check_effects(pinned, one["effects"], str(pdir / "effects.yaml"))
        if "text" in one:
            out += _check_text(one["text"], str(pdir / "text.yaml"))
    if "outcomes" in a.data:
        out += _check_outcomes(pinned, a.data["outcomes"], str(pack_dir / "outcomes.yaml"))
    announcement = _dict(a.data["pack"]).get("announcement")
    if announcement and announcement not in a.prose:
        out.append(Diagnostic(str(pack_dir / "pack.yaml"), "ref-prose", f"announcement names {announcement}, which is not in the pack"))
    return out


def _entry_path_problem(p: str) -> str | None:
    if p.startswith("/") or posixpath.isabs(p):
        return f"{p} is absolute"
    if any(seg in (".", "..") for seg in p.split("/")):
        return f"{p} leaves the repository"
    return None


def validate_index(repo_root: Path, pinned: Pinned) -> list[Diagnostic]:
    """``dram.yaml``: format version, schema, contained paths, matching ids."""
    repo_root = Path(repo_root)
    src = str(repo_root / INDEX_NAME)
    try:
        raw = load_yaml(repo_root / INDEX_NAME)
    except PackContentError as err:
        return err.diagnostics
    version = _dict(raw).get("index")
    if isinstance(version, int) and not isinstance(version, bool) and version > INDEX_VERSION:
        return [Diagnostic(src, "index-version", f"index {version}, but the pinned CLI reads index {INDEX_VERSION}")]
    out = _schema_errors(pinned, "registryIndex", raw, src)
    if out:
        return out
    seen: set[str] = set()
    for i, e in enumerate(raw["packs"]):
        problem = _entry_path_problem(e["path"])
        if problem:
            out.append(Diagnostic(src, "index-path", f"packs[{i}].path: {problem}"))
            continue
        if e["id"] in seen:
            out.append(Diagnostic(src, "index-duplicate", f"packs[{i}]: {e['id']} is listed twice"))
            continue
        seen.add(e["id"])
        if e.get("repo"):
            continue
        manifest = repo_root / e["path"] / "pack.yaml"
        try:
            pack = _dict(load_yaml(manifest))
        except PackContentError as err:
            out += err.diagnostics
            continue
        if pack.get("id") != e["id"]:
            out.append(Diagnostic(src, "index-id-mismatch", f"offers {e['id']}, but that pack calls itself {pack.get('id')}"))
    return out
