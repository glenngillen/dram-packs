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
    "steer", "set-checkpoints",
    "keep-secrets-out", "scope-permissions", "guard-destructive", "sandbox-autonomy",
    "size-it", "split-it-up", "fan-out",
    "hands-off", "isolate-the-run", "two-at-once",
    "right-size-it", "mind-the-cache", "harness-carries-it", "right-cadence",
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
    "steer": [r"bare", r"changed course", r"fix the harness", r"three times|at least three|3 or more"],
    "set-checkpoints": [r"ask rule|ask-permission rule", r"unanswered", r"bypass", r"spontaneous|unprompted", r"deny only|deny-only"],
    "keep-secrets-out": [r"config/secrets\.yml", r"never .*secret value", r"invented", r"effective"],
    "scope-permissions": [r"sandbox", r"neutral", r"Bash\(\*\)", r"overrid|precedence", r"unattended"],
    "guard-destructive": [r"regex", r"bypass", r"(never|not|does not) (execute|run) .*destructive"],
    "sandbox-autonomy": [r"separate OS user", r"credential-free", r"unassessed", r"privileged|passthrough", r"unknown"],
    "size-it": [r"first (finished |completed )?sub-?task", r"every sub-?task", r"one go"],
    "split-it-up": [r"built-in", r"plugin", r"test-writer"],
    "fan-out": [r"several_parallel", r"sequential", r"discard|thrown away"],
    "hands-off": [r"three interactive", r"three (or more )?sessions", r"unattended_gap", r"scope permissions"],
    "isolate-the-run": [r"branch", r"working copy", r"unused"],
    "two-at-once": [r"long_turn", r"subagent", r"idle", r"isolate the run", r"five minutes|5 minutes"],
    "right-size-it": [r"fallback", r"infracost/right-size-it", r"subagent", r"routine_work"],
    "mind-the-cache": [r"cache_gap", r"large_context_tokens", r"exactly (1|one) hour", r"exactly 150,000", r"fresh start", r"resum"],
    "harness-carries-it": [r"kept_window", r"unassessed", r"premium|opus", r"savings"],
    "right-cadence": [r"final gate", r"both (observed )?(model )?paths", r"no checks"],
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
    "steer": [r"changed course", r"then (followed|changed|switched)"],
    "size-it": [r"every sub-?task", r"all (the )?sub-?tasks"],
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


# Review F1 (round 3): the packaged YAML must carry the same owned-trigger
# branch as the definition and judge (pos-3), and report.seen must not credit
# only the person with supplying the signal.
def test_learn_from_production_yaml_and_copy_cover_owned_triggers():
    import yaml

    assert "expect: seen" in _scenario("learn-from-production", "pos-3")
    pattern = yaml.safe_load((PATTERNS / "learn-from-production" / "pattern.yaml").read_text(encoding="utf-8"))
    when = " ".join(pattern["seen"]["when"].split())
    assert re.search(r"owned trigger", when, re.I)
    assert re.search(r"review|merg", when, re.I)
    assert not re.search(r"signal they supplied", when, re.I)
    seen_copy = " ".join(yaml.safe_load((PATTERNS / "learn-from-production" / "text.yaml").read_text(encoding="utf-8"))["report"]["seen"].split())
    assert re.search(r"trigger you own", seen_copy, re.I)
    assert not re.search(r"^You gave the agent", seen_copy)


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


# Review F1 (gate-done copy): in neg-3 and neg-4 the checks ran and failed, but
# enforcement was bypassed or swallowed. report.not_seen must describe finishing
# with failing checks without effective enforcement (absent, bypassed or
# non-enforcing gates), not claim that no gate ran the checks.
def test_gate_done_not_seen_covers_bypassed_and_non_enforcing_gates():
    for sid in ("neg-3", "neg-4"):
        body = _scenario("gate-done", sid)
        assert "expect: opportunity" in body
        assert re.search(r"fail", body, re.I)
    copy = _report_not_seen("gate-done")
    assert "{count}" in copy
    assert not re.search(r"without a final gate running", copy, re.I)
    assert re.search(r"fail", copy, re.I)
    for phrase in (r"no gate|absent|without a gate", r"bypass", r"ignor|swallow|did not block|didn't block"):
        assert re.search(phrase, copy, re.I), f"gate-done report.not_seen omits {phrase!r}"


# Review F2 (actionable-failures): neg-2 delivers actionable feedback that the
# agent ignores. The not-holding predicate and the Mechanism table must cover
# delivered feedback ignored or left unresolved in the agent's next qualifying
# response, keeping the unresolved step/turn boundary.
def test_actionable_failures_not_holding_covers_delivered_feedback_ignored():
    import yaml

    body = _scenario("actionable-failures", "neg-2")
    assert "expect: opportunity" in body
    assert re.search(r"returns .*to the agent", body)
    assert re.search(r"unrelated|ignor", body, re.I)
    data = yaml.safe_load((PATTERNS / "actionable-failures" / "pattern.yaml").read_text(encoding="utf-8"))
    not_holding = " ".join(data["continuous"]["held"]["not_holding_when"].split())
    text = (PATTERNS / "actionable-failures" / "definition.md").read_text(encoding="utf-8")
    row = next(l for l in _section(text, "Mechanism").splitlines() if l.startswith("| Not holding |"))
    for name, flat in (("pattern.yaml", not_holding), ("definition.md / Mechanism", row)):
        assert re.search(r"ignor", flat, re.I), f"{name}: ignored delivered feedback missing"
        assert re.search(r"did not resolve|does not resolve|left .*unresolved", flat, re.I), f"{name}: unresolved feedback missing"
        assert re.search(r"next qualifying response", flat, re.I), f"{name}: next-response boundary missing"
        assert re.search(r"open question|step or turn|step/turn", flat, re.I), f"{name}: boundary must stay unresolved"


# Review F1 (checks-by-default): a check that ran, failed and stayed
# unresolved must not satisfy the holding predicates. Seen still records the
# execution, and a missing check result stays unassessed.
def test_checks_by_default_holding_excludes_unresolved_failures():
    import yaml

    data = yaml.safe_load((PATTERNS / "checks-by-default" / "pattern.yaml").read_text(encoding="utf-8"))
    held = data["continuous"]["held"]
    holds = " ".join(held["holds_when"].split())
    not_holding = " ".join(held["not_holding_when"].split())
    assert re.search(r"unresolved", holds, re.I)
    assert re.search(r"failed and (was|remained) (left )?unresolved", not_holding, re.I)
    text = (PATTERNS / "checks-by-default" / "definition.md").read_text(encoding="utf-8")
    held_row = next(l for l in text.splitlines() if l.startswith("| Held |"))
    not_row = next(l for l in text.splitlines() if l.startswith("| Not holding |"))
    assert re.search(r"unresolved", held_row, re.I)
    assert re.search(r"unresolved", not_row, re.I)
    body = _scenario("checks-by-default", "stage-boundary Rule-directed check failed and was left unresolved")
    assert "- kind: stage-boundary" in body
    assert re.search(r"Seen", body) and re.search(r"not holding", body, re.I)
    missing = _scenario("checks-by-default", "stage-boundary Check result missing")
    assert re.search(r"unassessed", missing, re.I)
    # Seen for a failing but executed check is preserved.
    assert "expect: seen" in _scenario("checks-by-default", "pos-3")


# Review F2 (hand-it-off): the guide states the real long_session threshold,
# not context "fullness", and unknown size without compaction is insufficient.
def test_hand_it_off_guide_states_the_long_session_threshold():
    guide = (PATTERNS / "hand-it-off" / "guide.md").read_text(encoding="utf-8")
    step = guide.split("## 1.", 1)[1].split("## 2.", 1)[0]
    assert "very full context" not in guide
    assert "../../reference/parameters.md#long_session" in step
    assert re.search(r"more than 150,000", step)
    assert re.search(r"compact", step)
    assert re.search(r"unknown", step, re.I) and re.search(r"cannot (establish|show)", step)
    done = guide.split("**Done:**", 1)[1].split("\n\n", 1)[0]
    assert re.search(r"compacted or (went|grew|had) .*more than 150,000", done)


# Pattern-content batch 2: Correcting course, Safety, Delegation, Economics.
MECHANISM_PATTERNS = [
    "set-checkpoints", "keep-secrets-out", "scope-permissions", "guard-destructive",
    "sandbox-autonomy", "size-it", "split-it-up", "fan-out", "hands-off",
    "isolate-the-run", "two-at-once", "right-size-it", "mind-the-cache",
    "harness-carries-it", "right-cadence",
]


def test_steer_declares_no_mechanism_of_its_own():
    import yaml

    data = yaml.safe_load((PATTERNS / "steer" / "pattern.yaml").read_text(encoding="utf-8"))
    assert "continuous" not in data


@pytest.mark.parametrize("pid", MECHANISM_PATTERNS)
def test_mechanism_patterns_declare_held_prose(pid):
    import yaml

    data = yaml.safe_load((PATTERNS / pid / "pattern.yaml").read_text(encoding="utf-8"))
    held = data["continuous"]["held"]
    for key in ("applies_when", "holds_when", "not_holding_when"):
        assert held.get(key), f"{pid}: continuous.held.{key} missing"


# Safety prerequisites for autonomy suggestions stay explicit in prose and are
# never encoded as a weaker `requires` binding.
@pytest.mark.parametrize(
    "pid, prerequisite",
    [("hands-off", r"Scope permissions"), ("two-at-once", r"Isolate the run"), ("fan-out", r"Safety")],
)
def test_autonomy_suggestions_keep_safety_prerequisites(pid, prerequisite):
    text = (PATTERNS / pid / "definition.md").read_text(encoding="utf-8")
    coaching = _section(text, "Opportunities and coaching")
    assert re.search(prerequisite, coaching), f"{pid}: coaching omits {prerequisite}"


SAFETY_GUIDES = ["keep-secrets-out", "scope-permissions", "guard-destructive", "sandbox-autonomy"]
DESTRUCTIVE = re.compile(r"rm -rf|git push (-f|--force)|terraform (apply|destroy)|DROP TABLE|--dangerously-skip-permissions\b(?! )", re.I)


@pytest.mark.parametrize("pid", SAFETY_GUIDES + ["hands-off", "two-at-once", "fan-out"])
def test_guides_never_recommend_bypass_or_run_destructive_commands(pid):
    guide = (PATTERNS / pid / "guide.md").read_text(encoding="utf-8")
    for line in guide.splitlines():
        if line.startswith(">") or line.startswith("    "):
            assert not DESTRUCTIVE.search(line), f"{pid}: guide prompt includes a destructive or bypass command: {line}"
    assert not re.search(r"approve all|skip (the )?permissions", guide, re.I)


# Review findings on the second pattern-content batch.
def _read(pid: str, name: str) -> str:
    return (PATTERNS / pid / name).read_text(encoding="utf-8")


def _case(pid: str, cid: str) -> dict:
    import json

    for line in _read(pid, "eval/cases.jsonl").splitlines():
        row = json.loads(line)
        if row["id"] == cid:
            return row
    raise AssertionError(f"{pid}: no case {cid}")


def _report(pid: str, key: str) -> str:
    import yaml

    return " ".join(yaml.safe_load(_read(pid, "text.yaml"))["report"][key].split())


def test_sandbox_guide_makes_no_universal_containment_promise():
    guide = _read("sandbox-autonomy", "guide.md")
    assert "stays inside it" not in guide
    intro = guide.split("## 1.", 1)[0]
    assert re.search(r"reduces? (the )?risk", intro)
    assert re.search(r"credential|privilege|network", intro)


def test_two_at_once_requires_the_long_turn_for_recognition_and_guide():
    judge = _read("two-at-once", "judge.md")
    decide = _section(judge, "Decide")
    assert re.search(r"at least 5 minutes", decide.split("Recognize **seen**", 1)[0])
    assert "1–6" in decide
    recognition = _section(_read("two-at-once", "definition.md"), "Recognition")
    assert re.search(r"long_turn", recognition)
    guide = _read("two-at-once", "guide.md")
    assert "several minutes" not in guide
    done = guide.split("**Done:**", 1)[1].split("\n\n", 1)[0]
    assert re.search(r"at least five minutes", done)
    scenario = _scenario("two-at-once", "neg-13")
    assert "expect: none" in scenario and re.search(r"4-minute", scenario)
    assert re.search(r"second session", scenario)
    assert _case("two-at-once", "neg-13")["expect"] == "none"
    import yaml

    seen_when = " ".join(yaml.safe_load(_read("two-at-once", "pattern.yaml"))["seen"]["when"].split())
    assert re.search(r"at least five minutes", seen_when)
    assert re.search(r"long_turn", seen_when)


def test_two_at_once_shared_directory_mechanism_case_is_not_an_opportunity():
    scenario = _scenario("two-at-once", "neg-12")
    assert "expect: none" in scenario
    assert re.search(r"Isolate the run", scenario)
    assert _case("two-at-once", "neg-12")["expect"] == "none"


@pytest.mark.parametrize("pid", ["hands-off", "isolate-the-run"])
def test_unattended_guides_state_the_fifteen_minute_minimum(pid):
    guide = _read(pid, "guide.md")
    assert re.search(r"at least fifteen minutes", guide)
    assert "long stretch" not in guide
    assert not re.search(r"let it work without prompting it\)", guide)
    not_done = guide.split("**Not done yet:**", 1)[1].split("\n\n", 1)[0]
    assert re.search(r"fifteen minutes", not_done)


def test_right_size_it_compares_against_the_usual_model():
    guide = _read("right-size-it", "guide.md")
    import yaml

    fix = yaml.safe_load(_read("right-size-it", "text.yaml"))["fix_prompt"]
    for text in (guide, fix):
        assert "the one I am using now" not in text
        assert re.search(r"usual", text)
    done = guide.split("**Done:**", 1)[1].split("\n\n", 1)[0]
    assert re.search(r"below your usual", done)
    assert re.search(r"(do not|don't) know (what|which) your usual", guide)


def test_mind_the_cache_separates_required_inputs_from_pricing():
    text = _read("mind-the-cache", "definition.md")
    applicable = _section(text, "Applicable work")
    assert not re.search(r"\*\*Unknown\*\* cache lifetime", applicable)
    assert re.search(r"no (cache-)?lifetime fact.*default", applicable, re.S)
    verify = _section(text, "Verify before enabling")
    assert "Unknown cache lifetime, context size, usage or pricing produces no recognition" not in verify
    assert re.search(r"[Uu]nknown usage or pricing (suppresses|produces) (only )?(the )?cost", verify)


def test_right_cadence_opportunity_copy_does_not_claim_every_model():
    assert "every model" not in _report("right-cadence", "not_seen")


def test_size_it_opportunity_copy_covers_one_large_goal():
    copy = _report("size-it", "not_seen")
    assert "several large goals at once" not in copy
    assert re.search(r"one large goal", copy)


def test_guard_destructive_opportunity_copy_covers_spelling_evasion():
    copy = _report("guard-destructive", "not_seen")
    assert re.search(r"did not (match|cover)", copy)


def test_harness_carries_it_distinguishes_recognition_subset_from_coverage_denominator():
    text = _read("harness-carries-it", "definition.md")
    applicable = _section(text, "Applicable work")
    assert re.search(r"coverage denominator", applicable)
    assert re.search(r"all routine work", applicable)
    progression = _section(text, "Progression")
    assert re.search(r"all (applicable )?routine (work|changes)", progression)


def test_set_checkpoints_unapproved_deploy_request_is_preparation_only():
    scenario = _scenario("set-checkpoints", "neg-7")
    assert "ship it" not in scenario
    assert re.search(r"do not deploy|don't deploy", scenario)


def test_harness_carries_it_failed_lighter_trials_are_not_opportunities():
    for cid in ("neg-2", "neg-9"):
        scenario = _scenario("harness-carries-it", cid)
        assert "expect: none" in scenario
        assert _case("harness-carries-it", cid)["expect"] == "none"
    assert "kind: mechanism-not-holding" in _scenario("harness-carries-it", "neg-9")
    assert re.search(r"not holding", _scenario("harness-carries-it", "neg-9"))
    opportunities = _section(_read("harness-carries-it", "definition.md"), "Opportunities and coaching")
    assert re.search(r"[Ff]ailed lighter trials are not an opportunity", opportunities)
    assert re.search(r"never tried on the lighter model", opportunities)


# Review F1 (mind-the-cache): a supplied cache lifetime replaces the one-hour
# default, so the guide's non-completion branch must not hard-code one hour.
def test_mind_the_cache_guide_uses_the_applicable_cache_lifetime():
    guide = (PATTERNS / "mind-the-cache" / "guide.md").read_text(encoding="utf-8")
    not_done = guide.split("**Not done yet:**", 1)[1].split("\n\n", 1)[0]
    assert not re.search(r"hour or less", not_done)
    assert re.search(r"no longer than the cache lasts", not_done)
    assert re.search(r"one hour (is only )?the default|default.{0,40}one hour", not_done)
    assert re.search(r"(known|supplied).{0,40}lifetime", not_done)


# Hand-off review (final batch) F1: two-at-once lets the first initiating
# prompt precede the overlap (pos-1) while requiring edits in both during it.
def test_two_at_once_initiating_prompt_may_precede_overlap():
    assert "expect: seen" in _scenario("two-at-once", "pos-1")
    for name in ("definition.md", "judge.md", "pattern.yaml"):
        flat = " ".join(_read("two-at-once", name).split())
        assert re.search(r"may (come before|precede) the overlap", flat), f"{name}: first prompt must be allowed before the overlap"
        assert not re.search(r"prompt starting work during the overlap", flat), f"{name}: still requires both prompts inside the overlap"


# F2: hands-off neg-11 expects an opportunity, so it must establish the
# Scope permissions prerequisite the judge requires.
def test_hands_off_neg_11_establishes_scope_permissions_prerequisite():
    scenario = _scenario("hands-off", "neg-11")
    assert "expect: opportunity" in scenario
    assert re.search(r"Scope permissions is already Seen for an unattended session", scenario)


# F3: mind-the-cache's short-gap exclusion follows the applicable lifetime,
# with one hour only as the default.
def test_mind_the_cache_short_gap_follows_applicable_lifetime():
    text = " ".join(_read("mind-the-cache", "definition.md").split())
    exclusion = re.search(r"\*\*Short gaps\*\*[^\n]*?outside applicable work", text).group(0)
    assert re.search(r"applicable cache lifetime", exclusion)
    assert re.search(r"by default", exclusion)
    assert re.search(r"five-minute lifetime, a twenty-minute return is applicable", text)
