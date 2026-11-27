# Clear Between Tasks

## Overview

Source ID `clear-between-tasks`; Context, rung 1. Reset working memory when changing to unrelated work. Detection requires model judgement with a genuine clear event.

## Requirements

- Applies when a session moves to unrelated work after several substantive turns.
- Seen requires `/clear` after substantial work (`substantial_work_prompts` in [pattern parameters](pattern-parameters.md): at least 6 person prompts, provisional) followed by a person prompt starting unrelated work. Cite the clear record and that next prompt as completion.
- Exclude early clears, clears followed by the same task, compaction and simply opening a new session.
- Continuous requires a command or instruction rule scoping sessions to one task, followed in the window with relevant evidence.
- Coach when an unrelated task inherits a large prior context. The guide prompts the person to clear before their next real switch of task.

## Acceptance Criteria

- [ ] Recognize eight turns on a ticket, `/clear`, then an unrelated export bug; reject a clear after two turns.
- [ ] Recognize six turns on CSS, `/clear`, then a date bug; reject a clear followed by continuation of the same ticket.
- [ ] Compaction and new-session creation cannot be counted as the Seen `/clear` act.
- [ ] A guided discussion without a clear followed by unrelated work earns nothing.

## Edge Cases

- The six/eight/two-turn source examples are retained as scenarios; the 6-prompt boundary is a tunable default, so a two-turn prior task is not substantial.
- This pattern's Continuous mechanism can start fresh tasks even though opening a new session alone is excluded from Seen; preserve that distinction.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Clear-event parsing, task-relatedness judgement and configuration-following evidence. Existing `/clear` summaries do not establish the full definition on their own.

