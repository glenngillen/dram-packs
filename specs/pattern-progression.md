# Pattern Progression

## Overview

Specify the progression content: stages, the automation gate and the stage-dependent completion rule. The user decided to keep stages with automation gating. The current CLI supports milestones only, so this content is documented in prose. This file does not authorize a new stage engine or unsupported `progress.yaml` fields.

## Requirements

- Record the stages: Seen requires one verified instance; Forming requires instances in at least two distinct weeks of the last four; Established requires at least 60% of applicable work with at least four applicable cases over the last four weeks.
- Continuous always requires a mechanism in place, applied and holding; a high success rate alone is insufficient. Direct entry is allowed after a mechanism first demonstrably holds.
- Preserve pattern-specific overrides: Give it instructions uses repository coverage; Save it uses reuse on another day and repeated-request coverage; patterns defining all/most coverage retain those qualifications.
- Preserve draft slipping behavior over recent applicable work. Removed mechanisms or mechanisms no longer holding cannot be represented as continuous. Unanalysed weeks, no applicable work and absence from work do not count as misses.
- Guided sessions may establish Seen only. Later progression needs independent work; merely repeating a guide does not earn it.
- Automation advice is gated: it is offered only once the person has three Continuous patterns across at least two groups (user decision: keep stages with gating). Before that, coaching offers the next manual step, not automation. Pattern copy explains automation as a later step, never as a shortcut that skips the stages.
- Preserve the next-step content ordering: core foundations (Briefing, Checking the work, Context, Safety), then the next rung of started groups, evidence-based relevance and rotation. Safety prerequisites precede autonomy suggestions. Do not invent a cost-weighting score or fatigue threshold.
- Progress is per pattern, never a group or person score. No total completed, streak or ranking.
- Any supported milestone refers to the same records; it must not require a second model pass. Do not add milestones solely because the schema permits them.
- “Most” and other coverage thresholds use the provisional defaults in [pattern parameters](pattern-parameters.md).

### Stage-dependent completion

User decision: what counts as completion depends on the stage.

| Stage | What counts |
| --- | --- |
| Seen | The first qualifying event: the person's deliberate act inside the window (a brief sent, a breakdown with its first sub-task finished, a challenge issued, a review requested, an explained redirect, a lean-up change requested). |
| Forming, Established | Only instances whose follow-through also finished: every sub-task done, the agent's response addressed the challenge, review findings acted on, course changed after a redirect, the change kept for `kept_window`. Each instance is credited to the week its follow-through finished. |
| Continuous | A mechanism in place, applied and holding, as before. Completion of individual instances is not enough. |

- An instance whose follow-through is still pending can count for Seen but not yet toward later stages. It is not a miss.
- An instance whose follow-through finished outside the four-week window does not count toward Forming or Established in that window.
- A follow-through that visibly failed (agent ignored the redirect, change reverted) counts for Seen only if the deliberate act itself qualifies, and never toward later stages.
- “Most” and other coverage thresholds use the provisional defaults in [pattern parameters](pattern-parameters.md).

### Stage-dependent completion

User decision: what counts as completion depends on the stage.

| Stage | What counts |
| --- | --- |
| Seen | The first qualifying event: the person's deliberate act inside the window (a brief sent, a breakdown with its first sub-task finished, a challenge issued, a review requested, an explained redirect, a lean-up change requested). |
| Forming, Established | Only instances whose follow-through also finished: every sub-task done, the agent's response addressed the challenge, review findings acted on, course changed after a redirect, the change kept for `kept_window`. Each instance is credited to the week its follow-through finished. |
| Continuous | A mechanism in place, applied and holding, as before. Completion of individual instances is not enough. |

- An instance whose follow-through is still pending can count for Seen but not yet toward later stages. It is not a miss.
- An instance whose follow-through finished outside the four-week window does not count toward Forming or Established in that window.
- A follow-through that visibly failed (agent ignored the redirect, change reverted) counts for Seen only if the deliberate act itself qualifies, and never toward later stages.

## Acceptance Criteria

- [ ] Draft thresholds and each explicit pattern override are documented without masquerading as supported runtime configuration.
- [ ] Mechanism prose cannot award Continuous merely for a percentage or an unused setting.
- [ ] Guided or unanalysed work cannot inflate or penalize later stages.
- [ ] Safety prerequisites remain explicit even when the current `requires` field cannot encode the required stage or run scope.
- [ ] The stage/automation decision is recorded, and automation advice is not offered before three Continuous patterns across two groups.
- [ ] A breakdown with only its first sub-task finished earns Seen but does not count toward Forming until every sub-task finishes.
- [ ] A challenge issued in week 1 whose response finishes in week 2 counts toward Forming in week 2.

## Edge Cases

- The source does not define fractional week handling, how inactive weeks interact with the rolling window, or stage precedence when evidence is sparse. These remain unresolved external stage-engine semantics.
- Some continuous definitions describe coverage without naming an enforcing mechanism (for example Save it, Scope permissions). Preserve both the pattern definition and the global mechanism requirement; coverage alone must not be advertised as enough.
- Prove it and Steer refer to other patterns for automation. Cross-reference those patterns rather than inventing a distinct mechanism or awarding their stages automatically.

## Dependencies

- Decided: keep stages with automation gating; stage-dependent completion as above. Both recorded in [requirements evidence](requirements-evidence.md).
- CLI stage calculation, guided markers and scoped recommendation prerequisites; current progress schema supports milestones only.

