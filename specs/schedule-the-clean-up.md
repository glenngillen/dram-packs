# Schedule the Clean-up

## Overview

Source ID `schedule-the-clean-up`; Checking the work, rung 10. Use scheduled agent maintenance whose output is acted on. Intended detection is a code check.

## Requirements

- Applies to people maintaining at least one repository.
- Seen requires a headless maintenance session launched by a person/team-owned schedule or trigger, with output merged, filed or otherwise used.
- Exclude unused scheduled reports and one-off interactive maintenance.
- Cite the scheduled session and the action on its output as completion.
- Continuous requires the scheduled run to occur according to its schedule throughout the window and its output to be used, satisfying the shared mechanism rule.
- Coach when a recurring maintenance chore is repeatedly done by hand. The guide chooses the person's real chore and explains a scheduled headless workflow without editing settings unasked.

## Acceptance Criteria

- [ ] Recognize weekly `claude -p "/check-deps"` producing a merged PR; reject scheduled reports nobody uses.
- [ ] Recognize a nightly flaky-test run whose filed issue is fixed; reject interactive monthly dependency maintenance.
- [ ] A headless invocation alone does not prove a configured schedule or useful output.
- [ ] Guided schedule setup without a completed run and used output does not earn Seen.

## Edge Cases

- Inspect schedulers only when the person has allowed that source. This pack cannot add that access.
- What counts as “maintains”, allowed missed schedule runs and sufficient evidence of “filed/used” remain unresolved detection semantics.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md), [scope permissions](scope-permissions.md).
- Launch provenance, permitted schedule facts, maintenance classification and output-action linkage. Existing unattended-job signals are inputs, not full proof.

