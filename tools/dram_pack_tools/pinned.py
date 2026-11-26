"""The pinned Dram CLI compatibility source.

The schema and block registry are read, never copied, from a Dram CLI
checkout at the recorded revision. Nothing here invents a field or a block.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .diagnostics import Diagnostic, PackContentError

PINNED_REVISION = "bdea6f678399b3684519d41cc65645b4a42d53ef"
DEFAULT_CHECKOUT = Path("/Volumes/Development/infracost/dram")
CHECKOUT_ENV = "DRAM_CLI_CHECKOUT"
SCHEMA_PATH = "internal/pack/schema.json"
BLOCKS_PATH = "internal/pack/blocks.json"


@dataclass(frozen=True)
class Pinned:
    schema: dict[str, Any]
    registry: dict[str, Any]
    revision: str | None


def checkout_path() -> Path:
    return Path(os.environ.get(CHECKOUT_ENV, str(DEFAULT_CHECKOUT)))


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise PackContentError([Diagnostic(str(path), "pinned-missing", "pinned CLI file not found")]) from None
    except (OSError, ValueError) as err:
        raise PackContentError([Diagnostic(str(path), "pinned-invalid", f"cannot read pinned CLI file: {err}")]) from None


def checkout_revision(checkout: Path) -> str | None:
    """The commit a checkout's HEAD names, read from ``.git`` without running git."""
    git = Path(checkout) / ".git"
    try:
        head = (git / "HEAD").read_text(encoding="utf-8").strip()
    except OSError:
        return None
    if not head.startswith("ref:"):
        return head or None
    ref = head[len("ref:") :].strip()
    try:
        return (git / ref).read_text(encoding="utf-8").strip() or None
    except OSError:
        pass
    try:
        packed = (git / "packed-refs").read_text(encoding="utf-8")
    except OSError:
        return None
    for line in packed.splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1] == ref and not line.startswith(("#", "^")):
            return parts[0]
    return None


def load_pinned(checkout: Path, revision: str | None = None) -> Pinned:
    """Read ``schema.json`` and ``blocks.json`` from a CLI checkout."""
    checkout = Path(checkout)
    schema = _read_json(checkout / SCHEMA_PATH)
    registry = _read_json(checkout / BLOCKS_PATH)
    if not isinstance(schema, dict) or not isinstance(schema.get("$defs"), dict):
        raise PackContentError([Diagnostic(str(checkout / SCHEMA_PATH), "pinned-invalid", "schema has no $defs")])
    if not isinstance(registry, dict) or not isinstance(registry.get("blocks"), dict):
        raise PackContentError([Diagnostic(str(checkout / BLOCKS_PATH), "pinned-invalid", "registry has no blocks")])
    return Pinned(schema=schema, registry=registry, revision=revision)
