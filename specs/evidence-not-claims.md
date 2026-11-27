# Evidence, Not Claims

## Overview

Source ID `evidence-not-claims`; Checking the work, rung 2. Challenge an agent's summary when the actual result contradicts it. Detection requires model judgement.

## Requirements

- Applies to claims contradicted by recorded failures, errors or skipped cases.
- Seen requires the person to identify that gap and the agent to address it. Exclude accepting the false claim and challenging an actually correct result.
- Cite the person's challenge (the source's completing event) and the underlying recorded result; retain the response showing it was addressed.
- Continuous requires an applied evidence-enforcing Stop hook or instruction rule requiring check output with completion claims.
- Coach when “all tests passed” is accepted despite recorded failures. The guide asks the person to compare the next completion summary against actual output.

## Acceptance Criteria

- [ ] Recognize “You said all pass but 3 failed above. Fix those first” when addressed; reject “Great, thanks” after that contradiction.
- [ ] Recognize a challenge to three passing cases when four were expected; reject challenging a correct complete result.
- [ ] Questions without an actual discrepancy do not earn this pattern.
- [ ] Guided output review without a warranted challenge is not a failure and does not fabricate an opportunity.

## Edge Cases

- Decided by [stage-dependent completion](pattern-progression.md#stage-dependent-completion): Seen completes on the person's challenge; Forming and Established count only challenges whose response addressed the recorded result, credited to the week the response finished.
- Truncated output may hide the missing case or a later pass. Insufficient evidence is unassessed.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md), [coaching content](coaching-content.md).
- Result/claim comparison, subsequent action recognition and evidence-enforcing configuration/run facts.

