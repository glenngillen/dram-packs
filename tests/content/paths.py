"""Locations of this repository's real content (read-only in tests)."""

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CATALOGUE = REPO / "tools" / "catalogue.yaml"
SPECS = REPO / "specs"
PACK = REPO / "core"
PATTERNS = PACK / "patterns"
