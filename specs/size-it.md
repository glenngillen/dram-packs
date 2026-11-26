# Size It

## Overview

Source ID `size-it`; Delegation, rung 1. Break large work into achievable tasks. Detection requires model judgement.

## Requirements

- Applies to sessions with substantial work.
- Seen requires a person-used breakdown of large work into smaller tasks, each completed, rather than an accidentally small request.
- Exclude unused agent breakdowns and a requested split followed by doing everything together anyway.
- Cite the breakdown request and first completed task, as specified by the source; retain evidence about subsequent tasks rather than dropping the source's “each finished” requirement.
- Continuous requires a planning command or sub-task template used to begin work in the window and holding.
- Coach when one session attempts several large goals without clean completion. The guide has the person break their largest real task into pieces that fit separate sessions.

## Acceptance Criteria

- [ ] Preserve “Break the migration into steps we can do one per session” with step one done as a positive source scenario; reject “Do the whole migration”.
- [ ] Recognize three completed sessions following sub-tasks of one plan; reject a breakdown followed by doing it all in one go.
- [ ] A naturally small one-line task does not prove deliberate sizing.
- [ ] Guide discussion without using the breakdown does not earn Seen.

## Edge Cases

- Decided by [stage-dependent completion](pattern-progression.md#stage-dependent-completion): Seen completes on the breakdown plus the first finished sub-task; Forming and Established count only breakdowns where every sub-task finished, credited to the week the last one finished.
- “Substantial” needs a grounded classification, not a new token/line threshold.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Task/plan linkage and task completion judgement; disabled until supported.

