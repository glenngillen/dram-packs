"""Focused content checks for the Briefing, Guides, Context and Checking-the-work
pattern batch.

Content lint only: these confirm that each pattern's authored scenarios keep the
distinctions its specification requires. They never run a detector.
"""

from __future__ import annotations

import re

import pytest

from tests.content.paths import PATTERNS

pytestmark = pytest.mark.content

BATCH = [
    "brief-it", "define-done", "plan-first", "own-the-expectations",
    "write-it-down", "keep-it-lean",
    "save-it", "script-it", "reuse-your-harness", "fix-the-harness",
    "clear-between-tasks", "hand-it-off", "point-dont-paste",
    "prove-it", "evidence-not-claims", "checks-by-default",
    "actionable-failures", "gate-done", "gate-each-step",
    "back-it-up-in-ci", "second-opinion", "test-behaviour",
    "schedule-the-clean-up", "learn-from-production",
]

# Phrases (case-insensitive regexes) a pattern's definition or scenarios must keep.
REQUIRED = {
    "brief-it": [r"first edit", r"corroborat"],
    "define-done": [r"before (the )?implementation|before any edit|before editing"],
    "plan-first": [r"first edit", r"review"],
    "own-the-expectations": [r"mirror"],
    "write-it-down": [r"in place", r"held"],
    "keep-it-lean": [r"12%", r"instruction_cost_share", r"kept_window", r"exactly 12%"],
    "save-it": [r"built-in", r"different day|another day"],
    "script-it": [r"many_files_coach", r"coaching only|not recognition"],
    "reuse-your-harness": [r"repositor"],
    "fix-the-harness": [r"fix_followup", r"recurr", r"insufficient"],
    "clear-between-tasks": [r"substantial_work_prompts", r"compaction", r"resume"],
    "hand-it-off": [r"handoff_pairing", r"same repository", r"24 hours"],
    "point-dont-paste": [r"paste", r"actually (used|read)"],
    "prove-it": [r"truncated", r"pass"],
    "evidence-not-claims": [r"addressed", r"truncated"],
    "checks-by-default": [r"historical|when the session ran", r"order"],
    "actionable-failures": [r"formatter"],
    "gate-done": [r"bypass", r"unused"],
    "gate-each-step": [r"fast_check", r"next turn|next step"],
    "back-it-up-in-ci": [r"direct push|pushed directly", r"docs-only|documentation-only"],
    "second-opinion": [r"independen", r"ignored", r"acted on"],
    "test-behaviour": [r"snapshot"],
    "schedule-the-clean-up": [r"synthetic|invented", r"launch"],
    "learn-from-production": [r"regression", r"synthetic|invented"],
}


def _content(pid: str) -> str:
    root = PATTERNS / pid
    return "\n".join(
        (root / rel).read_text(encoding="utf-8")
        for rel in ("definition.md", "eval/scenarios.md")
    )


@pytest.mark.parametrize("pid", BATCH)
def test_batch_pattern_is_authored(pid):
    assert (PATTERNS / pid / "pattern.yaml").is_file(), f"{pid} not authored"


@pytest.mark.parametrize("pid", BATCH)
def test_batch_pattern_keeps_its_specified_distinctions(pid):
    if not (PATTERNS / pid / "definition.md").is_file():
        pytest.fail(f"{pid} not authored")
    text = _content(pid)
    for phrase in REQUIRED[pid]:
        assert re.search(phrase, text, re.I), f"{pid}: content lacks {phrase!r}"


def test_keep_it_lean_tests_the_strict_threshold_separately_from_the_illustration():
    text = (PATTERNS / "keep-it-lean" / "eval" / "scenarios.md").read_text(encoding="utf-8")
    kinds = re.findall(r"^- kind: boundary$", text, re.M)
    assert len(kinds) >= 1, "keep-it-lean needs a boundary scenario at exactly 12%"


# Stage-dependent completion: Seen is the person's deliberate act. Follow-through
# (corroboration, a kept edit, an addressed response, findings acted on) belongs
# to Forming and Established and must not appear among the Seen prerequisites.
SEEN_MUST_NOT_REQUIRE = {
    "brief-it": [r"ask or guess", r"did not (need|have) to"],
    "keep-it-lean": [r"change was made", r"was made\b"],
    "evidence-not-claims": [r"then addressed", r"agent then"],
    "second-opinion": [r"acted on", r"used\b"],
}


def _seen_when(pid: str) -> str:
    import yaml

    data = yaml.safe_load((PATTERNS / pid / "pattern.yaml").read_text(encoding="utf-8"))
    return " ".join(data["seen"]["when"].split())


def _section(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    assert match, f"missing section {heading!r}"
    return match.group(1)


def _scenario(pid: str, heading_prefix: str) -> str:
    text = (PATTERNS / pid / "eval" / "scenarios.md").read_text(encoding="utf-8")
    match = re.search(
        rf"^#+ {re.escape(heading_prefix)}\b.*?\n(.*?)(?=^#+ |\Z)", text, re.M | re.S
    )
    assert match, f"{pid}: no scenario {heading_prefix!r}"
    return match.group(1)


@pytest.mark.parametrize("pid", sorted(SEEN_MUST_NOT_REQUIRE))
def test_seen_rule_does_not_require_follow_through(pid):
    seen = _seen_when(pid)
    for phrase in SEEN_MUST_NOT_REQUIRE[pid]:
        assert not re.search(phrase, seen, re.I), f"{pid}: seen.when requires follow-through {phrase!r}"


@pytest.mark.parametrize("pid", sorted(SEEN_MUST_NOT_REQUIRE))
def test_guide_done_does_not_require_follow_through(pid):
    guide = (PATTERNS / pid / "guide.md").read_text(encoding="utf-8")
    done = re.search(r"^\*\*Done:\*\*(.*)$", guide, re.M)
    assert done, f"{pid}: guide has no Done line"
    for phrase in SEEN_MUST_NOT_REQUIRE[pid]:
        if pid == "second-opinion" and phrase == r"used\b":
            continue  # "used" may describe later stages in a separate sentence
        first = done.group(1).split(". ")[0]
        assert not re.search(phrase, first, re.I), f"{pid}: guide Done requires follow-through {phrase!r}"


def test_brief_it_recognition_list_does_not_require_corroboration():
    text = (PATTERNS / "brief-it" / "definition.md").read_text(encoding="utf-8")
    recognition = _section(text, "Recognition").split("### ")[0]
    assert not re.search(r"ask or guess", recognition, re.I)


def test_keep_it_lean_seen_on_request_with_edit_pending():
    text = (PATTERNS / "keep-it-lean" / "definition.md").read_text(encoding="utf-8")
    assert "requested and made" not in text
    judge = (PATTERNS / "keep-it-lean" / "judge.md").read_text(encoding="utf-8")
    seen_line = next(l for l in judge.splitlines() if l.startswith("- `seen`"))
    assert "edit citation" not in seen_line
    body = _scenario("keep-it-lean", "pos-6")
    assert re.search(r"expect: seen", body)
    assert re.search(r"edit (is )?(still )?pending|not yet (been )?made|before the edit", body, re.I)


def test_evidence_not_claims_recognition_list_omits_addressed_response():
    text = (PATTERNS / "evidence-not-claims" / "definition.md").read_text(encoding="utf-8")
    seen_list = _section(text, "Recognition").split("Per [stage-dependent")[0]
    assert not re.search(r"addressing|addressed", seen_list, re.I)


def test_second_opinion_recognition_list_omits_acted_on_findings():
    text = (PATTERNS / "second-opinion" / "definition.md").read_text(encoding="utf-8")
    seen_part = _section(text, "Recognition").split("Per [stage-dependent")[0]
    assert not re.search(r"acted on|result used", seen_part, re.I)
    judge = (PATTERNS / "second-opinion" / "judge.md").read_text(encoding="utf-8")
    assert re.search(r"ignored.*seen", judge, re.I | re.S)


def test_second_opinion_ignored_findings_keep_seen():
    body = _scenario("second-opinion", "pos-7")
    assert "expect: seen" in body and re.search(r"ignor", body, re.I)


def test_prove_it_neg_3_has_explicit_acceptance_after_the_answer():
    body = _scenario("prove-it", "neg-3")
    setup = next(l for l in body.splitlines() if l.startswith("- Setup:"))
    answer = setup.index("without running anything")
    assert re.search(r"person (then )?(replies|writes|says)", setup[answer:], re.I)


def test_prove_it_week_boundary_anchors_seen_to_execution():
    body = _scenario("prove-it", "stage-boundary Forming")
    assert "for the deliberate request" not in body
    assert re.search(r"Seen in week 2", body)


def test_gate_each_step_established_counts_qualifying_instances():
    text = (PATTERNS / "gate-each-step" / "definition.md").read_text(encoding="utf-8")
    row = next(l for l in text.splitlines() if l.startswith("| Established"))
    assert not re.search(r"\bran on\b", row)
    assert re.search(r"block|feed", row, re.I)
    body = _scenario("gate-each-step", "stage-boundary Quiet")
    assert re.search(r"not (Seen|Forming|Established)", body)


# F1: report.seen copy describes only the qualifying Seen event, never the
# follow-through that pending (pos-6) and ignored (pos-7) scenarios lack.
SEEN_COPY_MUST_NOT_CLAIM = {
    "brief-it": (["pos-6"], [r"relied on", r"\bthen\b", r"applied", r"used\b"]),
    "second-opinion": (["pos-6", "pos-7"], [r"used\b", r"acted on", r"\bfixed\b", r"accepted"]),
}


def _report_seen(pid: str) -> str:
    import yaml

    data = yaml.safe_load((PATTERNS / pid / "text.yaml").read_text(encoding="utf-8"))
    return " ".join(data["report"]["seen"].split())


@pytest.mark.parametrize("pid", sorted(SEEN_COPY_MUST_NOT_CLAIM))
def test_report_seen_copy_holds_for_pending_and_ignored_seen_scenarios(pid):
    scenarios, phrases = SEEN_COPY_MUST_NOT_CLAIM[pid]
    for sid in scenarios:
        assert "expect: seen" in _scenario(pid, sid), f"{pid} {sid} must earn Seen"
    seen = _report_seen(pid)
    for phrase in phrases:
        assert not re.search(phrase, seen, re.I), f"{pid}: report.seen claims follow-through {phrase!r}"


# F2: an owned, independent automated review whose findings were ignored is
# Seen with failed follow-through (judge.md), and a not-holding mechanism; it
# is not an opportunity, which requires acceptance without independent review.
def test_second_opinion_owned_automated_ignored_review_is_seen_not_opportunity():
    import json

    body = _scenario("second-opinion", "pos-8")
    assert "expect: seen" in body
    assert "- kind: mechanism-not-holding" in body
    setup = next(l for l in body.splitlines() if l.startswith("- Setup:"))
    assert re.search(r"owned|team's .*configuration|person's .*configuration", setup, re.I)
    assert re.search(r"did not write", setup, re.I)
    assert re.search(r"not holding", body, re.I)
    assert re.search(r"Forming|later stages", body)
    cases = [
        json.loads(l)
        for l in (PATTERNS / "second-opinion" / "eval" / "cases.jsonl").read_text().splitlines()
        if l.strip()
    ]
    assert next(c for c in cases if c["id"] == "pos-8")["expect"] == "seen"
    judge = (PATTERNS / "second-opinion" / "judge.md").read_text(encoding="utf-8")
    assert re.search(r"opportunity\*\*: an applicable change accepted without independent review", judge)


# F3: a CI run followed by bypassing its required check must not satisfy the
# holding predicates.
def test_back_it_up_in_ci_holding_predicates_exclude_known_bypasses():
    import yaml

    data = yaml.safe_load((PATTERNS / "back-it-up-in-ci" / "pattern.yaml").read_text(encoding="utf-8"))
    holds = " ".join(data["continuous"]["held"]["holds_when"].split())
    assert re.search(r"bypass", holds, re.I)
    text = (PATTERNS / "back-it-up-in-ci" / "definition.md").read_text(encoding="utf-8")
    held = next(l for l in text.splitlines() if l.startswith("| Held |"))
    assert re.search(r"bypass", held, re.I)
    body = _scenario("back-it-up-in-ci", "stage-boundary CI ran but its required check was bypassed")
    assert "- kind: stage-boundary" in body
    assert re.search(r"not holding", body, re.I)
    assert re.search(r"Continuous", body)
    # The unresolved Seen question for pending or failing runs is preserved.
    assert re.search(r"pending or failing count for Seen", text)


# Review v1 F1: report.not_seen copy must stay true for every opportunity
# scenario. It must not assert absent configuration, unseen feedback or a test
# classification that the scenario contradicts.
NOT_SEEN_COPY_MUST_NOT_CLAIM = {
    "save-it": (["neg-2", "neg-9"], [r"no saved", r"without a saved"]),
    "write-it-down": (["neg-7"], [r"without being written", r"never written", r"not written"]),
    "fix-the-harness": (["neg-1", "neg-5"], [r"no rule", r"with no (rule|check|gate)", r"without a (rule|check|gate)"]),
    "actionable-failures": (["neg-2"], [r"never saw", r"had to guess", r"guess"]),
    "test-behaviour": (["neg-2"], [r"implementation tests", r"only by"]),
}


def _report_not_seen(pid: str) -> str:
    import yaml

    data = yaml.safe_load((PATTERNS / pid / "text.yaml").read_text(encoding="utf-8"))
    return " ".join(data["report"]["not_seen"].split())


@pytest.mark.parametrize("pid", sorted(NOT_SEEN_COPY_MUST_NOT_CLAIM))
def test_report_not_seen_copy_holds_for_every_opportunity_scenario(pid):
    scenarios, phrases = NOT_SEEN_COPY_MUST_NOT_CLAIM[pid]
    for sid in scenarios:
        assert "expect: opportunity" in _scenario(pid, sid), f"{pid} {sid} must be an opportunity"
    copy = _report_not_seen(pid)
    assert "{count}" in copy
    for phrase in phrases:
        assert not re.search(phrase, copy, re.I), f"{pid}: report.not_seen contradicts a scenario {phrase!r}"


# Review v1 F2: the judge and definition opportunity branches must cover every
# scenario that expects an opportunity with a mechanism present (saved but
# unused command, rule loaded but correction recurring, harness change in place
# but correction recurring), while insufficient evidence stays unassessed.
OPPORTUNITY_BRANCHES = {
    "save-it": (["neg-2", "neg-9"], r"saved version existed but (was not|wasn't) (invoked|used)"),
    "write-it-down": (["neg-7"], r"corrected again .*while the (persisted )?rule was in place and loaded"),
    "fix-the-harness": (["neg-1", "neg-5"], r"recurred .*after a relevant (harness )?change was in place"),
}


def _opportunity_text(pid: str, name: str) -> str:
    text = (PATTERNS / pid / name).read_text(encoding="utf-8")
    lines = [l for l in text.splitlines() if re.search(r"opportunity", l, re.I) and re.search(r"^\s*(-|\d+\.)", l)]
    return " ".join(lines)


@pytest.mark.parametrize("pid", sorted(OPPORTUNITY_BRANCHES))
def test_opportunity_branches_cover_mechanism_present_scenarios(pid):
    scenarios, branch = OPPORTUNITY_BRANCHES[pid]
    for sid in scenarios:
        assert "expect: opportunity" in _scenario(pid, sid), f"{pid} {sid} must be an opportunity"
    for name in ("judge.md", "definition.md"):
        text = _opportunity_text(pid, name)
        assert re.search(branch, text, re.I), f"{pid} {name}: opportunity omits mechanism-present branch"
        assert re.search(r"insufficient", text, re.I), f"{pid} {name}: opportunity must keep insufficient evidence unassessed"
    # The original absent-mechanism branch is preserved alongside.
    judge = _opportunity_text(pid, "judge.md")
    assert re.search(r"no saved version|without a persisted rule|no guide change", judge, re.I)


# Review v1 (round 4) F1: schedule-the-clean-up neg-1 has an owned schedule
# whose output went unused, so the copy must not claim no run existed.
def test_schedule_the_clean_up_not_seen_covers_unused_scheduled_output():
    assert "expect: opportunity" in _scenario("schedule-the-clean-up", "neg-1")
    copy = _report_not_seen("schedule-the-clean-up")
    assert not re.search(r"with no scheduled run", copy, re.I)
    assert re.search(r"output was used", copy, re.I)


# F2: direct pushes stay opportunities even when tests run afterwards, and
# CI that runs no tests (neg-2) is its own opportunity branch.
def test_back_it_up_in_ci_covers_docs_only_ci_and_timing():
    assert "expect: opportunity" in _scenario("back-it-up-in-ci", "neg-2")
    opportunities = _opportunity_text("back-it-up-in-ci", "definition.md")
    assert re.search(r"pushed directly", opportunities, re.I)
    assert re.search(r"runs no tests", opportunities, re.I)
    assert re.search(r"after the push", opportunities, re.I)
    copy = _report_not_seen("back-it-up-in-ci")
    assert re.search(r"before any CI run had\s+tested", copy, re.I)


# F3: unavailable follow-up limits later-stage corroboration, not Seen.
def test_brief_it_unavailable_follow_up_does_not_undo_seen():
    definition = (PATTERNS / "brief-it" / "definition.md").read_text(encoding="utf-8")
    judge = (PATTERNS / "brief-it" / "judge.md").read_text(encoding="utf-8")
    assert not re.search(r"request whose later work is unavailable", definition)
    assert re.search(r"Unavailable later work does not undo Seen", definition)
    assert re.search(r"Unavailable follow-up alone is not insufficient for Seen", judge)


# F4: the guide states the 24-hour pairing window that neg-5 enforces.
def test_hand_it_off_guide_states_the_24_hour_window():
    assert "expect: none" in _scenario("hand-it-off", "neg-5")
    guide = (PATTERNS / "hand-it-off" / "guide.md").read_text(encoding="utf-8")
    assert "ideally soon" not in guide
    # handoff_pairing measures from the prior main session's end, not from when
    # the handoff was written: written Mon 09:00, session ends Mon 11:00, fresh
    # session Tue 10:00 is 23 hours and qualifies.
    assert len(re.findall(r"within 24 hours of the long session ending", guide)) == 2
    assert not re.search(r"within 24 hours of (writing|the handoff)", guide)
    params = (PATTERNS.parent / "reference" / "parameters.md").read_text(encoding="utf-8")
    assert re.search(r"ended within 24 hours", params)


# F1: the guide states the strict instruction_cost_share boundary, so a
# below-threshold (or exactly 12%) cost cannot be presented as qualifying.
def test_keep_it_lean_guide_states_the_strict_cost_threshold():
    assert "expect: none" in _scenario("keep-it-lean", "neg-7")
    guide = (PATTERNS / "keep-it-lean" / "guide.md").read_text(encoding="utf-8")
    assert "../../reference/parameters.md#instruction_cost_share" in guide
    assert re.search(r"more than 12%", guide)
    assert re.search(r"exactly 12% does not", guide, re.I)
    assert "a small share" not in guide
    done = guide.split("**Done:**", 1)[1].split("\n\n", 1)[0]
    assert re.search(r"more than 12%", done), "Done must state the strict boundary"
    assert re.search(r"exactly 12% or below does not count", done)


# Review F1 (learn-from-production): an owned trigger can supply the signal for
# recognition (pos-3) and start the fix behind an opportunity (neg-9). Both keep
# trigger provenance and an attributable person-authored citation.
def test_learn_from_production_owned_trigger_branches_in_judge_and_definition():
    assert "expect: seen" in _scenario("learn-from-production", "pos-3")
    assert "expect: opportunity" in _scenario("learn-from-production", "neg-9")
    judge = _section(
        (PATTERNS / "learn-from-production" / "judge.md").read_text(encoding="utf-8"),
        "Output expectations",
    )
    definition = (PATTERNS / "learn-from-production" / "definition.md").read_text(encoding="utf-8")
    for name, text in (
        ("judge.md", judge),
        ("definition.md / Evidence", _section(definition, "Evidence")),
        ("definition.md / Opportunities", _section(definition, "Opportunities and coaching")),
    ):
        flat = " ".join(text.split())
        assert re.search(r"owned trigger", flat, re.I), f"{name}: no owned-trigger branch"
        assert re.search(r"trigger provenance", flat, re.I), f"{name}: trigger provenance not kept"
        assert re.search(r"person-authored", flat, re.I), f"{name}: no person-authored citation"
    recognize = re.search(r"^- Recognize.*?(?=^- )", judge, re.M | re.S).group(0)
    assert re.search(r"owned trigger", recognize, re.I)
    opportunity = next(l for l in judge.splitlines() if l.startswith("- Report an opportunity"))
    assert re.search(r"owned trigger", opportunity, re.I)
    assert re.search(r"merge|accept", opportunity, re.I)


# Review F2 (learn-from-production): recurrence after a fix that did add a
# regression check is not holding and cannot support Continuous.
def test_learn_from_production_holding_requires_no_recurrence():
    import json
    import yaml

    data = yaml.safe_load((PATTERNS / "learn-from-production" / "pattern.yaml").read_text(encoding="utf-8"))
    holds = " ".join(data["continuous"]["held"]["holds_when"].split())
    assert re.search(r"did not recur|no recurrence", holds, re.I)
    not_holding = " ".join(data["continuous"]["held"]["not_holding_when"].split())
    assert re.search(r"recur", not_holding, re.I)
    body = _scenario("learn-from-production", "pos-5")
    assert "- kind: boundary" in body
    assert re.search(r"regression (test|check)", body, re.I)
    assert re.search(r"recurred", body, re.I)
    assert re.search(r"not holding", body, re.I)
    assert re.search(r"cannot support Continuous|not Continuous", body)
    cases = {
        c["id"]: c
        for c in (
            json.loads(l)
            for l in (PATTERNS / "learn-from-production" / "eval" / "cases.jsonl").read_text().splitlines()
            if l.strip()
        )
    }
    assert cases["pos-5"]["expect"] != "continuous"
