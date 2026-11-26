"""The pack's shared authoring references: links, parameters, outcomes, topics."""

from __future__ import annotations

import re

import pytest

from dram_pack_tools.docs import check_links, parameter_links, parse_parameter_table
from tests.content.paths import PACK, SPECS

pytestmark = pytest.mark.content

REF = PACK / "reference"


def _md_files():
    return sorted(PACK.rglob("*.md"))


def test_every_markdown_link_in_the_pack_resolves_inside_it():
    problems = [d for md in _md_files() for d in check_links(md, PACK)]
    assert problems == [], "\n".join(map(str, problems))


def test_parameters_match_the_spec_and_are_all_provisional():
    ours = parse_parameter_table((REF / "parameters.md").read_text(encoding="utf-8"), "parameters.md")
    spec = parse_parameter_table((SPECS / "pattern-parameters.md").read_text(encoding="utf-8"), "spec")
    assert list(ours) == list(spec)
    for name, row in ours.items():
        assert row.default == spec[name].default, name
        assert row.origin == spec[name].origin, name
        assert row.status == "Provisional", name


def test_every_parameter_link_names_a_defined_parameter():
    names = set(parse_parameter_table((REF / "parameters.md").read_text(encoding="utf-8"), "parameters.md"))
    for md in _md_files():
        for name, anchor in parameter_links(md.read_text(encoding="utf-8")):
            assert name in names, f"{md}: unknown parameter {name}"
            assert anchor == name, f"{md}: link to {name} points at #{anchor}"


def _outcome_rows(text):
    rows = re.finditer(r"^\| \*{0,2}([A-Z][a-z]+(?: [a-z]+)*)\*{0,2} \|[^|]+\| ([^|]+) \|$", text, re.M)
    return {m.group(1): m.group(2).strip() for m in rows if m.group(1) != "Measure"}


def test_all_five_outcomes_keep_their_group_mappings():
    ours = _outcome_rows((REF / "outcomes.md").read_text(encoding="utf-8"))
    spec = _outcome_rows((SPECS / "outcome-content.md").read_text(encoding="utf-8"))
    assert list(spec) == ["Kept", "Rework", "Escapes", "Corrections", "Cost for kept work"]
    assert ours == spec


@pytest.mark.parametrize(
    "doc, headings",
    [
        ("evidence.md", ["Attribution and citations", "Opportunities", "Completion windows", "Mechanisms: in place, applied, held", "Privacy", "Insufficient evidence"]),
        ("progression.md", ["Stages", "Stage-dependent completion", "Guided sessions", "Automation gate", "Safety prerequisites", "Next-step ordering", "Unresolved stage-engine semantics"]),
        ("outcomes.md", ["Rules", "Unresolved semantics"]),
        ("authoring.md", ["Authoring checklist", "Readiness vocabulary", "Required scenarios"]),
        ("compatibility.md", ["Pinned CLI", "`min_cli`", "Identity", "Checks run"]),
    ],
)
def test_references_cover_their_contract(doc, headings):
    found = re.findall(r"^#{2,3} (.+)$", (REF / doc).read_text(encoding="utf-8"), re.M)
    for h in headings:
        assert h in found, f"{doc}: missing section {h}"


def test_readiness_vocabulary_separates_the_five_terms():
    text = (REF / "authoring.md").read_text(encoding="utf-8")
    vocab = text.split("## Readiness vocabulary", 1)[1]
    terms = re.findall(r"^\| \*\*([A-Za-z ]+)\*\* \|", vocab, re.M)
    assert terms == ["Authored", "Structurally valid", "Evaluable", "Preview", "Stable"]


def test_progression_records_the_automation_gate_and_completion_rules():
    text = (REF / "progression.md").read_text(encoding="utf-8")
    assert "three Continuous patterns across at least two groups" in text
    assert "Seen only" in text
    assert "week its follow-through finished" in text


def test_open_questions_use_the_review_shape():
    for md in _md_files():
        text = md.read_text(encoding="utf-8")
        parts = re.split(r"^## Open questions$", text, maxsplit=1, flags=re.M)
        if len(parts) == 1:
            continue
        section = parts[1].split("\n## ", 1)[0]
        items = re.split(r"^- ", section.strip(), flags=re.M)[1:]
        assert items, f"{md}: empty open questions section"
        for item in items:
            assert "\n  - evidence: " in item and "\n  - options: " in item, f"{md}: {item[:60]}"
