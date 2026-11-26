# Define Done

## Overview

Source ID `define-done`; Briefing, rung 2. Establish how feature or bug-fix work will be judged before implementation. Detection requires model judgement.

## Requirements

- Applies to feature and bug-fix work, excluding questions and exploration.
- Seen requires person-authored acceptance criteria, examples, named tests or required behavior before implementation, followed by a check against them.
- Exclude “make sure it works”, criteria supplied after completion and agent criteria accepted without review.
- Cite the criteria in the prompt or an attributable referenced spec, then the later check as completion.
- Continuous requires a used template, spec location or command that supplies or asks for criteria, with evidence it applied and held.
- Coach when accepted work was reopened because it did not match intent. The guide asks the person to write two or three “done when” lines on their next real feature or fix before requesting code.

## Acceptance Criteria

- [ ] Recognize criteria for expired and single-use reset links when implementation is checked against them; reject “Make sure it's done properly”.
- [ ] Recognize “@specs/export.md implement this; the examples in it are the tests” with attributable criteria and later checks; reject an agent writing criteria followed only by “ok”.
- [ ] A guided person-written criterion followed by its check can earn Seen; coaching conversation without criteria or checking cannot.
- [ ] A missing referenced file or unknown author leaves the result unassessed.

## Edge Cases

- A spec location by itself is not a mechanism in use.
- A criterion can be behavioral rather than executable; the evidence must still show it was checked.

## Dependencies

- Shared [evidence](pattern-evidence.md), [coaching](coaching-content.md) and [evaluation](evaluation-readiness.md) requirements.
- Person-attributed spec retrieval, event ordering, task classification and model recognition are activation dependencies; detection stays disabled until supported.

