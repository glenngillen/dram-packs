# Prove It

## Overview

Source ID `prove-it`; Checking the work, rung 1. Ask for evidence after an agent reports a code change done. Detection requires model judgement.

## Requirements

- Applies to turns where code changed and the agent reported completion.
- Seen requires the person's request for proof after the change and a subsequent test, build, lint or other relevant check actually running.
- Exclude unprompted checks without a person-owned instruction, requests before any change and requests with no following check.
- Cite the person request and the check execution as completion. “A check ran” is distinct from “a check passed”.
- The source points to Checks by default and Gate done for automation; do not invent a separate Continuous definition or automatically transfer their stages.
- Coach on “done/passing” claims with nothing run after the last edit. The guide has the person request proof after their next actual change.

## Acceptance Criteria

- [ ] Recognize post-edit “run the tests and show me” followed by `go test ./...`; reject spontaneous `pytest` without instructions.
- [ ] Recognize post-edit “did you lint it?” followed by `ruff check .`; reject a test request before any edits.
- [ ] A guided request not followed by execution is incomplete.
- [ ] A failed check can prove that checking occurred without becoming evidence the change works.

## Edge Cases

- A check run before the final edit does not substantiate a later completion claim.
- Related automatic checks belong to their own definitions; one tool call alone does not establish person intent.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [checks by default](checks-by-default.md), [gate done](gate-done.md), [evaluation readiness](evaluation-readiness.md).
- Person-request semantics, edit/check ordering and completion-claim recognition remain external detector capabilities.

