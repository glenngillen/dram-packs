"""Synthetic temporary pack trees for structural-validation tests.

Every file written here is invented test data. Nothing models a real Dram
schema field beyond file names already used by the pack conventions.
"""

from __future__ import annotations

from pathlib import Path


def write_tree(root: Path, files: dict[str, str]) -> Path:
    """Write ``files`` (relative POSIX path -> text) under ``root``."""
    for rel, text in files.items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    return root
