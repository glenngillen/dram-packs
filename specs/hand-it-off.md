# Hand It Off

## Overview

Source ID `hand-it-off`; Context, rung 2. Carry decisions from a long session into a genuinely fresh one. Detection requires paired-session judgement and mechanism checks.

## Requirements

- Applies to sessions meeting `long_session` in [pattern parameters](pattern-parameters.md): context over 150,000 tokens (provisional) or any compaction.
- Seen requires a fresh session whose first person prompt references a handoff written by the preceding session or pastes its state summary.
- Exclude resume/continue, compaction alone, unrelated named files and a handoff never used.
- Cite the prior handoff-writing event and the fresh session's first prompt as completion. Use the source's same-repository, previous-main-session pairing within twenty-four hours.
- Continuous requires an owned PreCompact/Stop hook or saved command producing a handoff actually used in the window, with applicable/held evidence.
- Coach when a long/compacted session loses an earlier decision. The guide asks for a handoff, then has the person start a fresh session from it.

## Acceptance Criteria

- [ ] Recognize earlier `NOTES.md` creation followed by fresh “Read NOTES.md and continue”; reject `claude --continue`.
- [ ] Recognize a fresh pasted state summary with its prior-session evidence; reject a new unrelated task despite an earlier NOTES.md file.
- [ ] Preserve the PreCompact-written HANDOFF.md used next session mechanism example.
- [ ] Guided handoff writing without subsequent fresh use is incomplete.

## Edge Cases

- An unconfirmed fresh/resumed flag is insufficient for recognition.
- A next-day boundary is not itself a violation of the twenty-four-hour pairing window.
- Privacy/retention may remove the prior session, leaving the relationship unassessable.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Fresh-session provenance, paired evidence, context/compaction facts and hook execution. Current recommendation context signals are related inputs, not the complete recognizer.

