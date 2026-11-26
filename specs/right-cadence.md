# Check at the Right Cadence

## Overview

Source ID `right-cadence`; Economics, rung 4. Match check frequency to the work and model without removing the final quality gate. Intended detection is a code check.

## Requirements

- Applies to repositories with both step gates and a final gate, used across multiple model tiers.
- Seen requires person-configured step checks on lighter work and reduced/skipped step checks on premium work, with both paths actually observed as configured.
- Exclude identical heavy checks at every edit for every model and no checks at all.
- Cite the configuration and runs under both variants as completion.
- Continuous requires the configuration to apply to all work in the window, with the final gate and applicable/held evidence.
- Coach on heavy premium step checks that catch nothing, phrased neutrally alongside outcomes rather than asserting those checks are worthless.
- Guide: show actual check runs and explain the trade-off; any reduction remains the person's decision and preserves final checking.

## Acceptance Criteria

- [ ] Recognize lighter-subagent per-edit type checks with a main premium-session Stop gate; reject a full suite after every edit on every model as evidence of this differentiated pattern.
- [ ] Only one observed model path is insufficient for Seen.
- [ ] No checks cannot be praised as efficiency.
- [ ] Guided review of cadence without configured and observed differentiated runs is incomplete.

## Edge Cases

- Never infer that premium models are infallible or that quiet gates prove quality.
- The existence and exact meaning of model-specific hook settings must be confirmed; the guide cannot invent unsupported agent configuration syntax.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [outcome content](outcome-content.md), [evaluation readiness](evaluation-readiness.md).
- Effective model-conditioned configuration, check cost/kind/run facts and coverage across both tiers.

