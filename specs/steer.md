# Steer, Don't Stop

## Overview

Source ID `steer`; Correcting course, rung 1. Diagnose and redirect a wrong approach rather than merely stopping it. Detection requires model judgement.

## Requirements

- Applies to moments the agent went wrong, including interrupts, failed/repeated attempts and wrong approaches.
- Seen requires a person correction explaining what was wrong or why, followed by changed course. Cite the person's redirect as the source's completing event, with the subsequent response as corroboration.
- Exclude bare “no”, “stop”, “try again”, “still failing”, and taste-only changes with no error.
- Automation points to Fix the harness; do not invent a separate Continuous mechanism or transfer its stage automatically.
- Coach when the same failing approach was retried at least three times before intervention. The guide asks the person to notice a real wrong turn and explain the reason when redirecting.

## Acceptance Criteria

- [ ] Recognize “the limit belongs in Options because callers set it per request” after an interrupt and changed approach; reject interrupt then “continue”.
- [ ] Recognize “Don't change the schema; the slow part is the query” when followed; reject “Still failing”.
- [ ] An explained correction ignored by the agent does not satisfy the complete definition.
- [ ] A guided question about what might go wrong without an actual redirect earns nothing.

## Edge Cases

- Interrupts alone do not prove meaningful steering.
- Decided by [stage-dependent completion](pattern-progression.md#stage-dependent-completion): Seen completes on the explained redirect; Forming and Established count only redirects followed by changed course, credited to the week the change finished. An ignored correction never counts toward later stages.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [fix the harness](fix-the-harness.md), [evaluation readiness](evaluation-readiness.md).
- Interrupt attribution, diagnosis judgement and changed-course evidence.

