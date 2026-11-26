# Gate Each Step

## Overview

Source ID `gate-each-step`; Checking the work, rung 6. Catch issues through fast checks after edits or before commits. Intended detection is a code check.

## Requirements

- Applies to repositories with fast type, lint or unit checks.
- Seen requires an owned PreToolUse, PostToolUse or pre-commit check that fired and blocked or fed back at least once.
- Exclude formatter-only and never-fired hooks, including configured pre-commit checks always bypassed.
- Cite configuration and the relevant run as completion.
- Continuous requires step-gate coverage of every applicable repository and actual firing/holding in the window.
- Coach when an early type/lint defect is found only at the end. The guide asks for an edit-time type check supported by the person's actual harness.

## Acceptance Criteria

- [ ] Recognize a PostToolUse `tsc --noEmit` check blocking after an edit; reject pre-commit always run with `--no-verify`.
- [ ] Recognize a pre-commit linter blocking a commit; reject formatter-only hooks.
- [ ] A configured but unused gate remains untested.
- [ ] Guided hook creation without an actual feedback/block event does not earn Seen.

## Edge Cases

- Successful quiet runs may establish execution but the Seen definition specifically requires a blocking or feedback instance.
- “Fast” uses `fast_check` in [pattern parameters](pattern-parameters.md): a per-step check usually finishing within 60 seconds (provisional). A slower check is not this pattern's fast gate, but may still count toward Gate "done".

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Check classification, hook/pre-commit run results, bypass detection and coverage aggregation.

