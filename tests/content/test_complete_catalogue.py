"""Complete-catalogue gate over the real pack (structural only).

From the integration slice on, every one of the 41 catalogue patterns must be
present, in order, explicitly disabled and free of runtime bindings. Passing
here is content lint, never an evaluation verdict.
"""

from __future__ import annotations

import re

import pytest

from dram_pack_tools.catalogue import coverage, load_catalogue
from dram_pack_tools.pack import block_refs
from dram_pack_tools.readers import load_jsonl, load_yaml
from dram_pack_tools.references import find_code_files, find_executables, find_symlinks
from tests.content.paths import CATALOGUE, PACK, PATTERNS

pytestmark = pytest.mark.content

VERIFICATION = PACK / "reference" / "verification.md"
# Rejections the evidence contract demands of any future recognizer
# (specs/pattern-evidence.md, specs/evaluation-readiness.md).
REQUIRED_REJECTIONS = {
    "fabricated-citation",
    "changed-quote",
    "agent-only-attribution",
    "agent-only-opportunity",
    "out-of-window",
}


@pytest.fixture(scope="module")
def catalogue():
    return load_catalogue(CATALOGUE)


def test_completeness_is_now_required_and_nothing_is_pending(catalogue):
    assert catalogue.require_complete is True
    report = coverage(catalogue, PATTERNS)
    assert report.pending == () and report.unknown == ()
    assert report.problems() == []


def test_pack_holds_exactly_41_unique_qualified_ids_in_catalogue_order(catalogue):
    ids = [load_yaml(PATTERNS / pid / "pattern.yaml")["id"] for pid in catalogue.ids]
    assert len(ids) == len(set(ids)) == 41
    assert ids == [f"glenngillen/{pid}" for pid in catalogue.ids]
    dirs = sorted(p.name for p in PATTERNS.iterdir() if p.is_dir())
    assert dirs == sorted(catalogue.ids)


def test_groups_yaml_lists_every_catalogue_pattern_in_source_order(catalogue):
    groups = load_yaml(PACK / "groups.yaml")["groups"]
    assert [(g["name"], g["patterns"]) for g in groups] == [(g.name, list(g.patterns)) for g in catalogue.groups]


def test_every_pattern_is_explicitly_disabled_and_binds_nothing(catalogue):
    for pid in catalogue.ids:
        pattern = load_yaml(PATTERNS / pid / "pattern.yaml")
        assert pattern.get("enabled") is False, pid
        assert block_refs(pattern) == [], pid
        assert all(c.get("unevaluable") for c in load_jsonl(PATTERNS / pid / "eval" / "cases.jsonl")), pid


def test_packaged_tree_is_declarative_only():
    assert find_symlinks(PACK) == []
    assert find_executables(PACK) == []
    assert find_code_files(PACK) == []


def _verification_scenarios():
    text = VERIFICATION.read_text(encoding="utf-8")
    out = {}
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        head = block.splitlines()[0]
        m = re.match(r"(ver-\d+)\b", head)
        if not m:
            continue
        fields = dict(re.findall(r"^- (rejects|expect|unevaluable): (.+)$", block, re.M))
        out[m.group(1)] = fields
    return out


def test_verification_rejections_are_preserved_as_unevaluable_scenarios():
    scenarios = _verification_scenarios()
    assert REQUIRED_REJECTIONS <= {s.get("rejects") for s in scenarios.values()}
    for sid, s in scenarios.items():
        assert s.get("expect") == "rejected", sid
        reason = s.get("unevaluable", "")
        assert "bdea6f6" in reason and len(reason) > 80, f"{sid}: unevaluable reason must name the pinned gap"


def test_evidence_contract_links_the_verification_scenarios():
    assert "verification.md" in (PACK / "reference" / "evidence.md").read_text(encoding="utf-8")


# Copy review: safety prerequisites the autonomy guides must keep
# (specs/coaching-content.md), checked as required phrases.
SAFETY_PREREQUISITES = {
    "hands-off": ["narrowly scoped permissions", "Never make a run unattended by switching permission checks off"],
    "two-at-once": ["must never share one directory", "Isolate the run"],
    "fan-out": ["Do not turn off permission prompts"],
    "sandbox-autonomy": ["Do not turn approvals off"],
    "schedule-the-clean-up": ["do not reach for permission bypass"],
    "guard-destructive": ["You never run a destructive command to try this out"],
}
DESTRUCTIVE = re.compile(r"rm -rf|reset --hard|push --force|push -f\b|dangerously-skip-permissions|--yolo|approve (?:all|everything)", re.I)


def test_autonomy_guides_keep_their_safety_prerequisites():
    for pid, phrases in SAFETY_PREREQUISITES.items():
        guide = (PATTERNS / pid / "guide.md").read_text(encoding="utf-8")
        for phrase in phrases:
            assert phrase in guide, f"{pid}: guide lost safety prerequisite {phrase!r}"


def test_guides_and_copy_offer_no_destructive_copy_paste_commands(catalogue):
    for pid in catalogue.ids:
        for name in ("guide.md", "text.yaml"):
            text = (PATTERNS / pid / name).read_text(encoding="utf-8")
            assert not DESTRUCTIVE.search(text), f"{pid}/{name}: {DESTRUCTIVE.search(text).group(0)!r}"


def test_no_copy_promises_recognition_while_detection_is_unavailable(catalogue):
    promise = re.compile(r"you will (?:be recognized|see a recognition|earn seen)|will show a recognition", re.I)
    for pid in catalogue.ids:
        guide = (PATTERNS / pid / "guide.md").read_text(encoding="utf-8")
        assert "will not show a recognition" in guide, pid
        assert not promise.search(guide.replace("will not show a recognition", "")), pid
