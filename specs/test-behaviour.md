# Test Behaviour

## Overview

Source ID `test-behaviour`; Checking the work, rung 9. Check observable behavior that callers or users rely on. Detection requires model judgement.

## Requirements

- Applies to behavior-changing APIs, outputs and user flows.
- Seen requires the person to request/write a behavior-level check, or review an approval fixture/snapshot, followed by its execution.
- Include contract tests, end-to-end checks and recorded side effects. Exclude implementation-only tests authored after the code and unreviewed snapshot updates.
- Cite the attributable request/check and its run as completion.
- Continuous requires relevant behavior checks run automatically through hooks/CI on the person's changes, applied and holding in the window.
- Coach on a change passing unit checks but breaking a caller. The guide requests one caller-side check for the next actual API/flow change.

## Acceptance Criteria

- [ ] Recognize a requested export contract test against client expectations, when run; reject agent unit tests alone after implementation.
- [ ] Recognize “Record the emails it sends in the test and show me” with review/execution; reject unreviewed snapshot `-u` updates.
- [ ] A test label containing “e2e” without relevant assertions cannot substitute for behavior coverage.
- [ ] Guided discussion without a requested/written and executed behavior check is incomplete.

## Edge Cases

- Unit-test tools can implement genuine behavior checks; classify what is checked, not the framework name.
- A failing behavior test proves checking occurred, not that the change satisfies the behavior.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md), [coaching content](coaching-content.md).
- Behavior/test semantics, person review evidence, execution linkage and automatic-check mechanism support.

