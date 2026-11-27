# Save It

## Overview

Source ID `save-it`; Guides, rung 4. Turn repeated requests into the person's own reusable command or skill. Detection combines model similarity judgement with ownership/run checks.

## Requirements

- Applies to requests repeated nearly word-for-word across at least two sessions.
- Seen requires a new person-owned command or skill actually invoked by the person in the window. Cite their invocation and completed run.
- Exclude built-in/plugin commands, saved-but-unused commands and skills invoked unasked by the agent.
- Draft overrides: Forming requires another run on a different day; Established requires most repeated requests to have used saved versions. Continuous requires no request manually repeated across three or more sessions without a saved version, plus the shared mechanism application requirement.
- Coach on repeated similar requests across sessions. The guide uses real tasks to make repetition visible, prompts the person to request a saved command, then has them run it on another real case.

## Acceptance Criteria

- [ ] Recognize a new `.claude/commands/pr-description.md` followed by `/pr-description`; reject built-in `/review`.
- [ ] Recognize a hand-written skill first run in the window; reject creation without execution.
- [ ] Agent-only invocation cannot substitute for the person's choice.
- [ ] Completing the guide questions without saving and using a command earns nothing; guided completion earns Seen only.
- [ ] Repeat use on the same day does not meet the different-day override.

## Edge Cases

- Near-identical intent is a model judgement, not an arbitrary similarity score invented by the pack.
- “Most” uses the provisional `most` default in [pattern parameters](pattern-parameters.md). “New” and a reusable command's applicability need precise future semantics. Existing first-run facts may help, but a signal counting any skill cannot establish ownership or intention.

## Dependencies

- [Pattern progression](pattern-progression.md), [coaching content](coaching-content.md), [evaluation readiness](evaluation-readiness.md).
- Command/skill provenance, first-use history, cross-session grouping and person invocation attribution.

