# Gate Done

## Overview

Source ID `gate-done`; display name `Gate "done"`; Checking the work, rung 5. Require a final check before an agent finishes. Intended detection is a code check.

## Requirements

- Applies to repositories with checks where the person works.
- Seen requires a person/team-configured Stop hook or equivalent running tests, a build or type checking, actually fired in a session.
- Exclude formatter-only hooks and configured hooks never run. The mechanism must be a gate, not a command that silently ignores failure.
- Cite the attributable configuration and actual run as completion.
- Continuous requires coverage of every applicable repository and firing in the window, with the shared held requirement. Blocking then fixing a failure is held; unresolved bypass is not.
- Coach when sessions finish with failing checks. The guide asks the person to add a final gate using their actual test command and explains failure behavior.

## Acceptance Criteria

- [ ] Recognize a `make test` Stop hook firing and blocking once; reject a Stop hook running only `prettier`.
- [ ] Recognize a user-level Stop hook invoking the repository's test script; reject an unused hook in settings.
- [ ] An enforcement bypass or ignored failure must not be called holding.
- [ ] Guided configuration without a firing event does not complete Seen.

## Edge Cases

- A final gate catching nothing is neutral evidence of execution, not proof that no bugs escaped.
- A valid build/type check counts even when it is not called “test”.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [outcome content](outcome-content.md), [evaluation readiness](evaluation-readiness.md).
- Hook classification, enforcement behavior, execution records and repository coverage; `hook_configured` alone is declared but not implemented in this fixed-pattern baseline.

