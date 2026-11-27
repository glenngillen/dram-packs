"""Read-only structural checks of the real index, pack and authored patterns.

These validate shape and authoring rules against the pinned schema and block
registry. They never run a detector; passing is not an evaluation verdict.
"""

from __future__ import annotations

import re

import pytest

from dram_pack_tools.cases import case_diagnostics
from dram_pack_tools.catalogue import coverage, load_catalogue
from dram_pack_tools.pack import block_refs, executable_refs, validate_index, validate_pack
from dram_pack_tools.readers import load_jsonl, load_yaml
from tests.content.paths import CATALOGUE, PACK, PATTERNS, REPO, SPECS

pytestmark = pytest.mark.content

PACK_ID = "glenngillen/core"
REQUIRED_FILES = ["pattern.yaml", "text.yaml", "guide.md", "definition.md", "eval/cases.jsonl", "eval/scenarios.md"]
DEFINITION_SECTIONS = [
    "Status",
    "Applicable work",
    "Recognition",
    "Exclusions",
    "Evidence",
    "Progression",
    "Mechanism",
    "Opportunities and coaching",
    "Why disabled",
    "Missing capabilities",
    "Verify before enabling",
]
BASE_KINDS = {"source-positive", "source-negative", "guided-success", "guided-no-action", "no-applicable-work", "missing-evidence"}
MECHANISM_KINDS = {"mechanism-unused", "mechanism-held", "mechanism-not-holding"}
PROHIBITED = re.compile(r"\b(score|scores|grade|grades|ranking|rank|streak|productivity|time saved|guarantee)\b", re.I)


@pytest.fixture(scope="module")
def catalogue():
    return load_catalogue(CATALOGUE)


@pytest.fixture(scope="module")
def authored(catalogue):
    return coverage(catalogue, PATTERNS).authored


def test_index_is_valid_against_the_pinned_schema(pinned):
    assert validate_index(REPO, pinned) == []
    index = load_yaml(REPO / "dram.yaml")
    assert [(p["id"], p["path"]) for p in index["packs"]] == [(PACK_ID, "core")]


def test_pack_is_valid_against_the_pinned_schema_and_registry(pinned):
    assert validate_pack(PACK, pinned) == []


def test_manifest_identity_and_no_unverified_release_claims():
    manifest = load_yaml(PACK / "pack.yaml")
    assert manifest["id"] == PACK_ID
    assert "min_cli" not in manifest, "no tagged release contains the pack loader; see reference/compatibility.md"
    assert "maintainers" not in manifest, "maintainer identity is unresolved"
    assert manifest.get("channel") == "dev"


def test_no_outcome_or_progress_runtime_files():
    # Outcomes and progression are documented in reference/ only.
    assert not (PACK / "outcomes.yaml").exists()
    assert not (PACK / "progress.yaml").exists()


def test_groups_follow_catalogue_order(catalogue, authored):
    groups = load_yaml(PACK / "groups.yaml")["groups"]
    assert [g["name"] for g in groups] == [g.name for g in catalogue.groups]
    for g, cg in zip(groups, catalogue.groups):
        assert g["id"] == cg.name.lower().replace(" ", "-")
        expected = [p for p in cg.patterns if p in authored]
        assert g.get("patterns", []) == expected


def test_authored_patterns_have_catalogue_identity(catalogue, authored):
    group_ids = {g.name: g.name.lower().replace(" ", "-") for g in catalogue.groups}
    for pid in authored:
        pattern = load_yaml(PATTERNS / pid / "pattern.yaml")
        group = catalogue.group_of(pid)
        rung = next(g.patterns for g in catalogue.groups if g.name == group).index(pid) + 1
        assert pattern["id"] == f"glenngillen/{pid}"
        assert pattern["group"] == group_ids[group]
        assert pattern["rung"] == rung


def test_every_authored_pattern_is_explicitly_disabled_preview_with_no_bindings(authored):
    for pid in authored:
        pattern = load_yaml(PATTERNS / pid / "pattern.yaml")
        assert pattern.get("enabled") is False, f"{pid}: enabled must be explicitly false (absent means true)"
        assert pattern.get("status") == "preview", pid
        assert block_refs(pattern) == [], f"{pid}: the disabled baseline names no runtime blocks"
        assert "outcomes" not in pattern and "requires" not in pattern, pid


def test_pattern_directories_are_complete(authored):
    for pid in authored:
        for rel in REQUIRED_FILES:
            assert (PATTERNS / pid / rel).is_file(), f"{pid}: missing {rel}"


def test_definition_has_required_sections_in_order(authored):
    for pid in authored:
        text = (PATTERNS / pid / "definition.md").read_text(encoding="utf-8")
        found = [h for h in re.findall(r"^## (.+)$", text, re.M) if h in DEFINITION_SECTIONS]
        assert found == DEFINITION_SECTIONS, f"{pid}: definition.md sections"
        for section in ("Why disabled", "Missing capabilities", "Verify before enabling"):
            body = text.split(f"## {section}\n", 1)[1].split("\n## ", 1)[0]
            assert len(body.strip()) > 40, f"{pid}: {section} is empty"


def test_judge_prompt_only_for_model_judged_patterns(authored):
    for pid in authored:
        overview = (SPECS / f"{pid}.md").read_text(encoding="utf-8").split("## Requirements")[0]
        model_judged = "judgement" in overview
        assert (PATTERNS / pid / "judge.md").exists() == model_judged, pid


def test_text_names_the_pattern_and_says_detection_is_unavailable(authored):
    for pid in authored:
        text = load_yaml(PATTERNS / pid / "text.yaml")
        title = re.search(r"^# (.+)$", (SPECS / f"{pid}.md").read_text(encoding="utf-8"), re.M).group(1)
        assert text["name"].casefold().replace('"', "") == title.casefold().replace('"', ""), pid
        assert "not available" in text["preview_note"], pid
        for key, value in text.items():
            for s in value.values() if isinstance(value, dict) else [value]:
                assert not PROHIBITED.search(s), f"{pid}: text.yaml {key} uses scoring or promise language"


def test_guide_has_completion_and_no_action_branches(authored):
    for pid in authored:
        guide = (PATTERNS / pid / "guide.md").read_text(encoding="utf-8")
        assert "Detection is not available yet" in guide, pid
        assert "**Done:**" in guide and "**Not done yet:**" in guide, pid
        assert "stop" in guide.lower(), f"{pid}: guide needs a no-applicable-task exit"


def _scenarios(pid):
    text = (PATTERNS / pid / "eval" / "scenarios.md").read_text(encoding="utf-8")
    ids = re.findall(r"^## ((?:pos|neg)-\d+)\b", text, re.M)
    kinds = set(re.findall(r"^- kind: ([a-z-]+)$", text, re.M))
    return ids, kinds


def test_cases_follow_authoring_rules(authored):
    for pid in authored:
        pattern = load_yaml(PATTERNS / pid / "pattern.yaml")
        cases = load_jsonl(PATTERNS / pid / "eval" / "cases.jsonl")
        diags = case_diagnostics(cases, PATTERNS / pid / "eval", executable=bool(executable_refs(pattern)), source=pid)
        assert diags == [], "\n".join(map(str, diags))


def test_every_scenario_has_a_case_and_required_kinds_are_covered(authored):
    for pid in authored:
        ids, kinds = _scenarios(pid)
        cases = [c["id"] for c in load_jsonl(PATTERNS / pid / "eval" / "cases.jsonl")]
        assert sorted(ids) == sorted(cases), f"{pid}: scenarios and cases differ"
        required = set(BASE_KINDS)
        if "held" in load_yaml(PATTERNS / pid / "pattern.yaml").get("continuous", {}):
            required |= MECHANISM_KINDS
        assert required <= kinds, f"{pid}: missing scenario kinds {sorted(required - kinds)}"


def test_readiness_has_one_row_per_catalogue_pattern(catalogue, authored):
    text = (PACK / "reference" / "readiness.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\| `([a-z-]+)` \|.*\| ([^|]+) \|$", text, re.M)
    assert [r[0] for r in rows] == list(catalogue.ids)
    for pid, status in rows:
        if pid in authored:
            assert status.startswith("Authored") and "disabled" in status, pid
            count = len(load_jsonl(PATTERNS / pid / "eval" / "cases.jsonl"))
            assert f"({count} of {count} cases unevaluable)" in status, f"{pid}: readiness count differs from cases.jsonl ({count})"
        else:
            assert status.startswith("Pending"), pid
