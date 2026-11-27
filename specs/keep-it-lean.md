# Keep It Lean

## Overview

Source ID `keep-it-lean`; Guides, rung 3. Suggest reviewing conflicting or measurably expensive instructions while preserving valuable rules. Detection combines model contradiction judgement with code-computed cost.

## Requirements

- Applies to repository and user instruction files.
- Flag contradictions only with both conflicting lines cited. Compute loading/context cost from actual resolved instruction sizes, usage and pricing, not model-invented amounts.
- Size findings use `instruction_cost_share` from [pattern parameters](pattern-parameters.md) (provisional default: more than 12% of initial context). Age or infrequent use alone never justifies trimming. All findings suggest review, never automatic deletion.
- Seen requires the person to request reconciliation of a flagged contradiction or trimming/splitting after crossing the threshold, followed by a kept change.
- Exclude agent-initiated rewrites and changes that only add content.
- Continuous requires a recurring contradiction check in the person's harness and consistent, below-threshold files in the window, subject to applied/held evidence.
- Cite the contradictory lines or measured cost, then the person's request and edit; kept evidence is also required.
- Guide: show the actual conflict or measured cost and ask the person to reconcile/reorganize while retaining every rule they still want.

## Acceptance Criteria

- [ ] Recognize conflicting test commands reconciled at the person's request and kept; reject an unused ninety-day-old migration rule without a flag.
- [ ] Preserve the example of 12% initial context prompting a split into on-demand rules; 12% is the provisional, tunable `instruction_cost_share` default.
- [ ] Reject an unprompted instruction rewrite and a guided review with no resolving action.
- [ ] No price or load evidence means no numeric cost claim; unused checks do not establish Continuous.

## Edge Cases

- Cached loading treatment and context accounting remain unresolved. Detection depending on them stays disabled.
- Decided by [stage-dependent completion](pattern-progression.md#stage-dependent-completion): Seen completes on the requested change; Forming and Established count only changes kept for `kept_window` (14 days), credited to the week survival is established.

## Dependencies

- [Outcome content](outcome-content.md), [pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Historical instruction resolution, contradiction judgement, token/pricing measurement, git survival and recurring-check evidence.

