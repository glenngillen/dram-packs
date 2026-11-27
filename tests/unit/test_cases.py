"""Authoring rules for eval/cases.jsonl beyond the pinned schema.

A case on a pattern with no executable detection must say why it cannot be
judged; positives may never be relabelled ``none`` to make them pass.
"""

from __future__ import annotations

from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from dram_pack_tools.cases import NEGATIVE, POSITIVE, case_diagnostics
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


# Property tests. The eval tree is written once per test and only read, so
# reusing the function-scoped tmp_path across Hypothesis examples is safe.
_REUSE_TMP = settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
_N = st.integers(min_value=1, max_value=9999)
_BLANK = st.one_of(st.none(), st.text(alphabet=" \t\n", max_size=4))
_REASON = st.text(min_size=1, max_size=20).filter(lambda s: s.strip())


def _scenarios(ids):
    return "# Scenarios\n\n" + "".join(f"## {cid} Scenario\n\ntext\n\n" for cid in ids)


class TestProperties:
    @_REUSE_TMP
    @given(
        sign=st.sampled_from(["pos", "neg"]),
        n=_N,
        data=st.data(),
        reason=st.one_of(_BLANK, _REASON),
        executable=st.booleans(),
    )
    def test_incompatible_polarity_always_produces_a_diagnostic(self, tmp_path, sign, n, data, reason, executable):
        wrong = NEGATIVE if sign == "pos" else POSITIVE
        expect = data.draw(st.sampled_from(sorted(wrong)))
        cid = f"{sign}-{n}"
        write_tree(tmp_path, {"eval/scenarios.md": _scenarios([cid])})
        extra = {} if reason is None else {"unevaluable": reason}
        diags = case_diagnostics([case(cid, expect, **extra)], tmp_path / "eval", executable=executable, source="c")
        polarity = [d for d in diags if d.code == "case-polarity"]
        assert len(polarity) == 1 and polarity[0].line == 1 and cid in polarity[0].message

    @_REUSE_TMP
    @given(
        cases=st.lists(
            st.tuples(st.sampled_from(["pos", "neg"]), st.one_of(_BLANK, _REASON)),
            min_size=1,
            max_size=8,
        )
    )
    def test_non_executable_case_without_a_reason_is_always_rejected(self, tmp_path, cases):
        built, ids = [], []
        for i, (sign, reason) in enumerate(cases, start=1):
            cid = f"{sign}-{i}"
            ids.append(cid)
            expect = "seen" if sign == "pos" else "none"
            built.append(case(cid, expect, **({} if reason is None else {"unevaluable": reason})))
        write_tree(tmp_path, {"eval/scenarios.md": _scenarios(ids)})
        diags = case_diagnostics(built, tmp_path / "eval", executable=False, source="c")
        missing = sorted(d.line for d in diags if d.code == "case-unevaluable-missing")
        expected = sorted(i for i, (_, reason) in enumerate(cases, start=1) if reason is None or not reason.strip())
        assert missing == expected
        assert all(d.code == "case-unevaluable-missing" for d in diags)
