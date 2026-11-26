"""Authoring rules for eval/cases.jsonl beyond the pinned schema.

A case on a pattern with no executable detection must say why it cannot be
judged; positives may never be relabelled ``none`` to make them pass.
"""

from __future__ import annotations

from dram_pack_tools.cases import case_diagnostics
from tests.helpers.tree import write_tree

SCENARIOS = "# Scenarios\n\n## pos-1 Loaded instructions\n\ntext\n\n## neg-1 Heading only\n\ntext\n"


def eval_dir(tmp_path):
    write_tree(tmp_path, {"eval/scenarios.md": SCENARIOS, "eval/fixtures/a.json": "{}"})
    return tmp_path / "eval"


def case(cid, expect, **extra):
    out = {"id": cid, "packet": f"scenarios.md#{cid}", "expect": expect, "why": "because"}
    out.update(extra)
    return out


def codes(diags):
    return [d.code for d in diags]


def test_unevaluable_cases_on_disabled_content_are_accepted(tmp_path):
    cases = [case("pos-1", "seen", unevaluable="needs x"), case("neg-1", "none", unevaluable="needs x")]
    assert case_diagnostics(cases, eval_dir(tmp_path), executable=False, source="c") == []


def test_non_executable_case_without_unevaluable_reason_is_rejected(tmp_path):
    cases = [case("pos-1", "seen"), case("neg-1", "none", unevaluable="  ")]
    assert codes(case_diagnostics(cases, eval_dir(tmp_path), executable=False, source="c")) == [
        "case-unevaluable-missing",
        "case-unevaluable-missing",
    ]


def test_executable_pattern_may_have_judged_cases(tmp_path):
    cases = [{"id": "pos-1", "packet": "fixtures/a.json", "expect": "seen", "why": "w"}]
    assert case_diagnostics(cases, eval_dir(tmp_path), executable=True, source="c") == []


def test_positive_relabelled_none_is_rejected(tmp_path):
    cases = [case("pos-1", "none", unevaluable="x")]
    assert codes(case_diagnostics(cases, eval_dir(tmp_path), executable=False, source="c")) == ["case-polarity"]


def test_negative_expecting_recognition_is_rejected(tmp_path):
    cases = [case("neg-1", "seen", unevaluable="x")]
    assert codes(case_diagnostics(cases, eval_dir(tmp_path), executable=False, source="c")) == ["case-polarity"]


def test_duplicate_case_ids_are_rejected(tmp_path):
    cases = [case("pos-1", "seen", unevaluable="x"), case("pos-1", "seen", unevaluable="x")]
    assert codes(case_diagnostics(cases, eval_dir(tmp_path), executable=False, source="c")) == ["case-duplicate"]


def test_missing_packet_file_is_rejected(tmp_path):
    cases = [dict(case("pos-1", "seen", unevaluable="x"), packet="fixtures/missing.json")]
    assert codes(case_diagnostics(cases, eval_dir(tmp_path), executable=False, source="c")) == ["case-packet"]


def test_packet_may_not_leave_the_eval_directory(tmp_path):
    write_tree(tmp_path, {"other.md": "# pos-1\n"})
    cases = [dict(case("pos-1", "seen", unevaluable="x"), packet="../other.md#pos-1")]
    assert codes(case_diagnostics(cases, eval_dir(tmp_path), executable=False, source="c")) == ["case-packet"]


def test_scenario_anchor_must_exist(tmp_path):
    cases = [dict(case("pos-1", "seen", unevaluable="x"), packet="scenarios.md#pos-9")]
    assert codes(case_diagnostics(cases, eval_dir(tmp_path), executable=False, source="c")) == ["case-scenario-missing"]


def test_why_is_required(tmp_path):
    cases = [dict(case("pos-1", "seen", unevaluable="x"), why="")]
    assert codes(case_diagnostics(cases, eval_dir(tmp_path), executable=False, source="c")) == ["case-why"]
