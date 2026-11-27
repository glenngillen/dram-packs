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
