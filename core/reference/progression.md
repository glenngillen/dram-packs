# Progression

How a person moves through a pattern's stages, what counts as completion at each stage, and when automation advice may be offered. **This is prose, not runtime configuration.** The pinned Dram CLI defines the stage names itself and its `progress.yaml` accepts only milestone blocks (`first_seen`, `seen_again`, `step_up`, `since_enabled`). It has no field for stage thresholds, completion rules or the automation gate. This pack therefore ships **no `progress.yaml`** and no milestones: none would be backed by working detection, and milestones are not added just because the schema permits them.

Progress is **per pattern**. There is no group score, person score, total completed, streak or ranking.

## Stages

| Stage | Draft threshold |
| --- | --- |
| **Seen** | One verified instance (see the [evidence contract](evidence.md)). |
| **Forming** | Instances in at least two distinct weeks of the last four. |
| **Established** | At least 60% of applicable work, with at least four applicable cases, over the last four weeks ([`most`](parameters.md#most)). |
| **Continuous** | A mechanism in place, applied and holding ([mechanisms](evidence.md#mechanisms-in-place-applied-held)). A high success rate alone is never enough. |

- **Direct entry to Continuous** is allowed once a mechanism first demonstrably holds.
- **Removed mechanisms**, or mechanisms no longer holding, cannot be represented as Continuous.
- **Slipping** is judged over recent applicable work. Unanalysed weeks, weeks with no applicable work and absence from work are **not misses**.

### Pattern-specific overrides

Some patterns replace the draft thresholds. Each pattern's definition states its own override and links here.

| Pattern | Override |
| --- | --- |
| Give it instructions | Forming: present in two or more applicable repositories. Established: present in [`most`](parameters.md#most) applicable repositories. Continuous: every applicable repository covered, or a user-level instruction file applying everywhere, updated in the last four weeks, plus the shared mechanism requirement. |
| Save it | Forming: another run of the saved command on a different day. Established: most repeated requests used saved versions. Continuous: no request manually repeated across three or more sessions without a saved version, plus the shared mechanism requirement. |
| Patterns defining all/most coverage | Keep those coverage qualifications **and** the shared mechanism requirement. Coverage alone is never advertised as enough (for example Scope permissions). |
| Prove it, Steer, don't stop | Automation points to other patterns (Checks by default and Gate "done"; Fix the harness). Cross-reference them; do not invent a separate mechanism or transfer their stages automatically. |

## Stage-dependent completion

User decision: what counts as completion depends on the stage.

| Stage | What counts |
| --- | --- |
| Seen | The first qualifying event: the person's deliberate act inside the window (a brief sent, a breakdown with its first sub-task finished, a challenge issued, a review requested, an explained redirect, a lean-up change requested). |
| Forming, Established | Only instances whose follow-through also finished: every sub-task done, the agent's response addressed the challenge, review findings acted on, course changed after a redirect, the change kept for [`kept_window`](parameters.md#kept_window). Each instance is credited to the **week its follow-through finished**. |
| Continuous | A mechanism in place, applied and holding. Completion of individual instances is not enough. |

- A follow-through still **pending** can count for Seen but not yet toward later stages. It is not a miss.
- A follow-through that finished **outside the four-week window** does not count toward Forming or Established in that window.
- A follow-through that **visibly failed** (the agent ignored the redirect, the change was reverted) counts for Seen only if the deliberate act itself qualifies, and never toward later stages.

Worked boundaries (future acceptance scenarios):

- A breakdown with only its first sub-task finished earns Seen; it does not count toward Forming until every sub-task finishes.
- A challenge issued in week 1 whose response finishes in week 2 counts toward Forming in week 2.

## Guided sessions

A session the person runs through a pattern's guide can establish **Seen only**. Forming, Established and Continuous need independent work. Repeating a guide does not earn them. Guided work cannot inflate or penalize later stages.

## Automation gate

User decision: keep stages with automation gating.

- **Automation advice is offered only once the person has three Continuous patterns across at least two groups.**
- Before that, coaching offers the **next manual step**, not automation.
- Pattern copy explains automation as a later step, never as a shortcut that skips the stages.
- `automate` text in a pattern is therefore authored for after the gate. The pinned CLI cannot enforce the gate; a host that shows `automate` before it is met is outside this pack's contract.

## Safety prerequisites

Autonomy suggestions come after the relevant Safety mechanisms. The pinned `requires` field takes bare pattern IDs; it cannot say *which stage* is required or that the requirement applies only to a particular run. So prerequisites are stated in prose in each affected pattern, and `requires` is not used to encode a weaker version of them.

| Suggestion | Prerequisite |
| --- | --- |
| Hands off | Scoped unattended permissions (Scope permissions) for the run. |
| Two at once | A separate working copy for each session (Isolate the run). |
| Broader autonomy (Sandbox autonomy, permission bypass) | The relevant Safety mechanisms: Keep secrets out, Scope permissions, Guard destructive commands. |

Permission bypass is never recommended as a shortcut.

## Next-step ordering

When a host chooses which pattern to coach next:

1. Core foundations first: **Briefing, Checking the work, Context, Safety**.
2. Then the next rung of groups the person has already started.
3. Then evidence-based relevance (applicable work actually seen) and rotation.
4. Safety prerequisites precede any autonomy suggestion.

No cost-weighting score and no fatigue threshold are defined; none is invented here.

## Unresolved stage-engine semantics

These belong to the CLI's stage engine and are not settled by the source:

- fractional week handling;
- how inactive weeks interact with the rolling four-week window;
- stage precedence when evidence is sparse.

## Open questions

- How should fractional weeks and inactive weeks be handled in the rolling four-week window?
  - evidence: The source defines Forming and Established over "the last four weeks" without saying how partial or empty weeks count.
  - options: Calendar weeks in local time with inactive weeks skipped; a rolling 28-day window.
  - location: core/reference/progression.md / Unresolved stage-engine semantics
- Should the CLI gain a stage-scoped `requires` so Safety prerequisites can be encoded?
  - evidence: `requires` in the pinned schema is a list of bare pattern IDs; it cannot express "Continuous for this run".
  - options: Add stage/run scope to `requires` in the CLI; keep prerequisites as prose and host logic.
  - location: core/reference/progression.md / Safety prerequisites
