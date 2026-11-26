# Let the Harness Carry It

## Overview

Source ID `harness-carries-it`; Economics, rung 3. Establish that a lighter model's routine work passes checks and survives. Detection is specified as code checks plus git evidence.

## Requirements

- Applies to routine lighter-model work, using `routine_work` in [pattern parameters](pattern-parameters.md).
- Seen requires that work in a repository with Checks by default or gates, passing those checks and remaining in the default branch fourteen days later.
- Exclude work without checks, reverted work and work finished on premium after lighter-model failure.
- Cite the session, relevant gate runs and the kept change as completion.
- Preserve draft Continuous coverage of most routine work running lighter, passing and being kept, plus the shared requirement for a mechanism.
- Coach on premium routine work where effective gates support trying lighter. The guide proposes a real routine task on a lighter model and lets actual checks assess it.

## Acceptance Criteria

- [ ] Recognize a Sonnet session passing its Stop gate and kept fourteen days; reject Haiku work without gates that is reverted.
- [ ] Recognize pinned lighter-subagent work passing CI and kept; reject lighter failures finished by the person on Opus.
- [ ] Immature or unavailable survival evidence is unassessed, not failed.
- [ ] Guided trial without later passing/kept evidence cannot prematurely complete the pattern.

## Edge Cases

- “Most” and the routine examples use [pattern parameters](pattern-parameters.md). Routine work beyond the example list and the reference tier for “lighter” remain unresolved unless existing documented CLI contracts settle them.
- Savings estimates are not kept-change evidence and cannot substitute for fourteen-day survival.

## Dependencies

- [Outcome content](outcome-content.md), [right-size it](right-size-it.md), [checks by default](checks-by-default.md), [evaluation readiness](evaluation-readiness.md).
- Routine/tier facts, gate-to-change links, git survival and stable attribution across model switches.

