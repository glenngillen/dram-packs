"""Hand-off documentation: installation guidance, readiness inventory, checks record.

Checks wording and coverage only; the claims themselves rest on the commands
recorded in core/reference/compatibility.md.
"""

from __future__ import annotations

import re

import pytest

from dram_pack_tools.catalogue import load_catalogue
from dram_pack_tools.readers import load_yaml
from tests.content.paths import CATALOGUE, PACK, PATTERNS, REPO

pytestmark = pytest.mark.content

README = REPO / "README.md"
READINESS = PACK / "reference" / "readiness.md"
COMPAT = PACK / "reference" / "compatibility.md"

STABLE_AREAS = [
    "Copy",
    "Guides",
    "Model evaluation",
    "Recognition precision",
    "Recognition recall",
    "Opportunities",
    "Verification",
    "Cost",
    "Held cases",
    "Case advice",
    "Code fixtures",
    "Real configurations",
]
ACTIVATION_CANDIDATES = [
    "give-it-instructions",
    "mind-the-cache",
    "gate-done",
    "gate-each-step",
    "keep-secrets-out",
    "scope-permissions",
    "guard-destructive",
    "isolate-the-run",
]
OVERCLAIMS = re.compile(r"\b(is|are) (signed|published|stable|official)\b|officially|runnable preview|\b41 working\b", re.I)


def section(text, heading):
    match = re.search(rf"^##+ {re.escape(heading)}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    assert match, f"missing section {heading!r}"
    return match.group(1)


def test_readme_gives_verified_and_unverified_installation_separately():
    text = README.read_text(encoding="utf-8")
    assert "glenngillen/core" in text and "bdea6f6" in text
    for cmd in ("dram pack validate .", "dram pack show --dir core", "dram pack eval core"):
        assert cmd in text, cmd
    install = section(text, "Install from the registry")
    assert "dram pack registry add glenngillen/dram-packs" in install
    assert "dram pack install glenngillen/core" in install
    assert "not been verified" in install


def test_readme_separates_availability_validation_evaluability_and_activation():
    text = README.read_text(encoding="utf-8")
    body = section(text, "What installing gives you")
    for term in ("Content available", "Structurally valid", "Evaluable", "Active"):
        assert f"**{term}**" in body, term
    assert "disabled" in body and "red" in body


def test_hand_off_docs_make_no_release_overclaims():
    for path in (README, READINESS, COMPAT):
        text = path.read_text(encoding="utf-8")
        match = OVERCLAIMS.search(text)
        assert not match, f"{path.name}: {match.group(0)!r}"


def test_readiness_records_versions_and_one_row_per_pattern_with_its_version():
    text = READINESS.read_text(encoding="utf-8")
    assert "glenngillen/core` 0.1.0" in text and "bdea6f6" in text and "2026-11-27" in text
    rows = re.findall(r"^\| `([a-z-]+)` \|.*\| (\d+) \| [^|]+ \|$", text, re.M)
    catalogue = load_catalogue(CATALOGUE)
    assert [r[0] for r in rows] == list(catalogue.ids)
    for pid, version in rows:
        assert int(version) == load_yaml(PATTERNS / pid / "pattern.yaml")["version"], pid


def test_readiness_preserves_stable_bars_and_activation_candidates_as_future_work():
    text = READINESS.read_text(encoding="utf-8")
    bars = section(text, "Stable-quality bars (future work)")
    for area in STABLE_AREAS:
        assert re.search(rf"^\| {re.escape(area)} \|", bars, re.M), area
    first = section(text, "First activation candidates (future work)")
    for pid in ACTIVATION_CANDIDATES:
        assert f"`{pid}`" in first, pid


def test_readiness_records_copy_review_and_unresolved_dependencies():
    text = READINESS.read_text(encoding="utf-8")
    review = section(text, "Copy review")
    assert "Performed" in review and "Outstanding" in review and "owner" in review
    deps = section(text, "Unresolved dependencies")
    for item in ("min_cli", "recognizer", "held cases"):
        assert item in deps, item
    assert "## Open questions" in text


def test_compatibility_records_the_integration_and_eval_results():
    text = COMPAT.read_text(encoding="utf-8")
    checks = section(text, "Checks run")
    assert "--state-dir" in checks and "infracost/right-size-it" in checks
    assert "607 unevaluable" in checks and "exit 1" in checks
    assert "verification.md" in checks
