# Set Checkpoints

## Overview

Source ID `set-checkpoints`; Correcting course, rung 2. Require a decision before a risky or hard-to-undo step. Detection uses model judgement and configuration checks.

## Requirements

- Applies to migrations, deploys, deletion, public API changes and other risky decision points.
- Seen requires the person to request a stop, the agent to stop at that point and the person to make the decision.
- Exclude spontaneous agent questions and unanswered checkpoints.
- Cite the checkpoint request and person's decision as completion.
- Continuous requires an instruction or ask-permission rule that actually stopped the agent in the window and held.
- Coach on an unapproved risky step the person undid. The guide has them specify a real checkpoint before their next risky task.

## Acceptance Criteria

- [ ] Recognize “Draft the migration and ask before running it”, actual stop, then “Run it, skip the backfill”; reject unprompted “Shall I proceed?”.
- [ ] Preserve an ask rule on `db:migrate` stopping the agent twice as mechanism evidence; reject an unanswered checkpoint.
- [ ] A requested stop bypassed by the agent is not holding.
- [ ] Guided wording without the actual stop and decision is incomplete.

## Edge Cases

- Automatic approval cannot stand in for the person's decision.
- Risk classification must be evidence-based, not every shell command classified as dangerous.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Decision-sequence recognition, historical permission mode and effective ask rules. Current `permission_rule` schema accepts deny only, so an ask binding must not be invented.

