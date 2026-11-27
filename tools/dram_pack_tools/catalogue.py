"""Authoring catalogue and incremental pattern-coverage tracking.

The catalogue lists the source IDs the core pack must eventually contain.
Until ``require_complete`` is switched on (the complete-catalogue slice),
pending patterns are reported rather than failing, and are never hidden.
Coverage is authoring progress only: it says nothing about whether a
detector runs or passes evaluation.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .diagnostics import Diagnostic, PackContentError
from .readers import load_yaml

_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_TOP_KEYS = {"require_complete", "groups"}
_GROUP_KEYS = {"name", "patterns"}


@dataclass(frozen=True)
class Group:
    name: str
    patterns: tuple[str, ...]


@dataclass(frozen=True)
class Catalogue:
    groups: tuple[Group, ...]
    require_complete: bool

    @property
    def ids(self) -> tuple[str, ...]:
        return tuple(p for g in self.groups for p in g.patterns)

    def group_of(self, pattern_id: str) -> str:
        for g in self.groups:
            if pattern_id in g.patterns:
                return g.name
        raise KeyError(pattern_id)


def parse_catalogue(data: Any, source: str) -> Catalogue:
    def bad(code: str, message: str) -> PackContentError:
        return PackContentError([Diagnostic(source, code, message)])

    if not isinstance(data, dict):
        raise bad("catalogue-shape", "catalogue must be a mapping")
    extra = set(data) - _TOP_KEYS
    if extra or set(data) != _TOP_KEYS:
        raise bad("catalogue-shape", f"catalogue keys must be exactly {sorted(_TOP_KEYS)}")
    if not isinstance(data["require_complete"], bool):
        raise bad("catalogue-shape", "require_complete must be true or false")
    raw_groups = data["groups"]
    if not isinstance(raw_groups, list) or not raw_groups:
        raise bad("catalogue-shape", "groups must be a non-empty list")

    groups: list[Group] = []
    seen_ids: set[str] = set()
    seen_groups: set[str] = set()
    for raw in raw_groups:
        if not isinstance(raw, dict) or set(raw) != _GROUP_KEYS:
            raise bad("catalogue-shape", f"each group needs exactly {sorted(_GROUP_KEYS)}")
        name, patterns = raw["name"], raw["patterns"]
        if not isinstance(name, str) or not name.strip():
            raise bad("catalogue-shape", "group name must be a non-empty string")
        if name in seen_groups:
            raise bad("catalogue-duplicate-group", f"group {name!r} listed twice")
        seen_groups.add(name)
        if not isinstance(patterns, list) or not patterns:
            raise bad("catalogue-shape", f"group {name!r} needs a non-empty patterns list")
        for pid in patterns:
            if not isinstance(pid, str) or not _ID.fullmatch(pid):
                raise bad("catalogue-invalid-id", f"{pid!r} is not a kebab-case source ID")
            if pid in seen_ids:
                raise bad("catalogue-duplicate-id", f"{pid!r} appears in more than one place")
            seen_ids.add(pid)
        groups.append(Group(name, tuple(patterns)))
    return Catalogue(tuple(groups), data["require_complete"])


def load_catalogue(path: Path) -> Catalogue:
    return parse_catalogue(load_yaml(path), str(path))


@dataclass(frozen=True)
class CoverageReport:
    catalogue: Catalogue
    authored: tuple[str, ...]
    pending: tuple[str, ...]
    unknown: tuple[str, ...]
    patterns_dir: str

    def problems(self) -> list[Diagnostic]:
        out = [
            Diagnostic(self.patterns_dir, "catalogue-unknown-pattern", f"{pid} is not in the catalogue")
            for pid in self.unknown
        ]
        if self.catalogue.require_complete:
            out += [
                Diagnostic(self.patterns_dir, "catalogue-pending-pattern", f"{pid} has no pattern.yaml yet")
                for pid in self.pending
            ]
        return out

    def summary(self) -> str:
        total = len(self.catalogue.ids)
        text = f"catalogue coverage: {len(self.authored)}/{total} authored"
        if self.pending:
            text += f"; pending ({len(self.pending)}): " + ", ".join(self.pending)
        if self.unknown:
            text += "; unknown: " + ", ".join(self.unknown)
        mode = "required" if self.catalogue.require_complete else "incremental (not yet required)"
        return text + f"; completeness {mode}"


def coverage(catalogue: Catalogue, patterns_dir: Path) -> CoverageReport:
    """A pattern counts as authored once ``<id>/pattern.yaml`` exists."""
    patterns_dir = Path(patterns_dir)
    present: set[str] = set()
    if patterns_dir.is_dir():
        present = {p.name for p in patterns_dir.iterdir() if p.is_dir() and (p / "pattern.yaml").is_file()}
        present |= {p.name for p in patterns_dir.iterdir() if p.is_dir()} - set(catalogue.ids)
    authored = tuple(i for i in catalogue.ids if i in present)
    pending = tuple(i for i in catalogue.ids if i not in present)
    unknown = tuple(sorted(present - set(catalogue.ids)))
    return CoverageReport(catalogue, authored, pending, unknown, str(patterns_dir))
