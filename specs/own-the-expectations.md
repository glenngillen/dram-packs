# Set the Expectations Yourself

## Overview

Source ID `own-the-expectations`; Briefing, rung 4. Separate the expectations from an implementation that could otherwise define its own success. Detection uses model judgement and git evidence.

## Requirements

- Applies to feature/fix work adding or changing tests.
- Seen requires tests or examples written by the person, or substantively reviewed and approved by them before implementation, then an implementation made to pass them.
- Exclude agent tests written after implementation, and unread approval such as “ok, go”.
- Cite the person's test-writing commit or review and the implementation passing those expectations as completion.
- Continuous requires a test-first instruction or command followed in the window, including person review before implementation.
- Coach when post-hoc tests mirror an implementation bug. The guide asks for a failing reproduction of the next real bug, has the person read it, then request the fix.

## Acceptance Criteria

- [ ] Recognize a person committing `export_test.go` and asking “make these pass”; reject code followed by agent-authored tests that pass immediately without prior review.
- [ ] Recognize a request for failing tests, the person adding an empty-input case, then authorizing implementation; reject “write tests and code” performed together.
- [ ] A guided test review with no subsequent passing implementation does not satisfy completion.
- [ ] A test-first rule merely present but ignored cannot establish Continuous.

## Edge Cases

- Agent authorship of a test is acceptable if the person meaningfully reviews it before implementation.
- A passing test is not itself evidence that the person supplied independent expectations.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md), [coaching content](coaching-content.md).
- Git/person attribution, ordered implementation/test events and substantive review recognition; unsupported bindings remain disabled.

