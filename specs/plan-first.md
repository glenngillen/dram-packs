# Plan First

## Overview

Source ID `plan-first`; Briefing, rung 3. Recognize the person's review of a plan before a multi-file change. Detection uses model judgement, plus configuration checks for its mechanism.

## Requirements

- Applies to changes editing at least two files.
- Seen requires a proposed plan before multi-file edits, the person's approval, adjustment or questions, and subsequent edits to at least two files. A plan may originate with the person or the agent.
- Cite the plan request/mode event, person review and the second file's edit as completion.
- Exclude automatic approval in unattended/bypass runs, unanswered plans, one-file changes and plans requested after multi-file edits began.
- Continuous requires a relevant instruction rule, default plan mode or plan-then-execute setting, followed by reviewed plans in the window.
- Coach on corrections that planning could have prevented. The guide has the person choose an upcoming multi-file change and agree a plan before edits.

## Acceptance Criteria

- [ ] Recognize person-entered plan mode, “keep the old API” review and four edited files; reject automatic headless plan approval.
- [ ] Recognize “propose an approach, don't change anything yet”, approval and two edited files; reject a one-file plan.
- [ ] Recognize an agent's `EnterPlanMode` followed by “split the migration into its own step” and three edited files; reject exit without person review.
- [ ] Preserve the Continuous example of default plan mode followed by reviewed plans in three sessions; reject a plan requested after two files were edited.
- [ ] Guided planning without review and subsequent applicable work does not count.

## Edge Cases

- Agent-originated plans are allowed; the person's review is the intentional act.
- The exact boundary between an initial single-file edit and “before multi-file edits” is not fully settled by the source. Keep boundary cases pending rather than selecting a convenient ordering rule.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Plan-mode provenance, file edit ordering, person approval recognition and default-mode evidence. Tool-call sequencing alone cannot establish these.

