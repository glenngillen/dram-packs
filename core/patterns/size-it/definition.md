# Size it

Source ID `size-it`; pattern `glenngillen/size-it`; Delegation, rung 1. Break large work into achievable tasks. Intended detection: model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Intent

**What it's for.** The person hands the agent work in pieces it can finish well: one goal per session or task, large work broken down first.

**Why it matters.** An agent given one huge goal tends to spread itself thin and finish nothing cleanly. Breaking the work into session-sized tasks, and finishing them one at a time, gives the person a checkable result at each step. It is the first rung of Delegation: handing work at the right size comes before handing it to subagents or letting it run unattended.

**What a recognition shows.** That the person deliberately broke large work down, used that breakdown, and finished the first piece on its own, not merely that a request happened to be small.

**Why the rules are drawn this way.**

- **Only substantial work applies.** Sizing only matters where the work was too big to finish and check cleanly in one go. Whether it was is a judgement about the work itself, so a model makes it ([code checks facts; a model judges the rest](../../reference/principles.md#code-checks-facts-a-model-judges-the-rest)); the source gives no size boundary, and none is invented. Windows with only small tasks report nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **A breakdown the person asked for, wrote or adopted.** Steps the agent listed on its own and the person never used are the agent's initiative, not the person's sizing ([human intent only](../../reference/principles.md#human-intent-only)).
- **The breakdown must actually be used.** Asking for steps and then doing everything together anyway leaves the work unsized; crediting the request would credit a pattern that isn't working ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **A naturally small request never counts.** Smallness alone doesn't show deliberate sizing, so it is excluded rather than guessed at.
- **Seen on the first finished sub-task; later stages need every sub-task finished.** Recorded decision (completion depends on the stage): the first finished piece credits the person promptly, while Forming and Established count only breakdowns carried through, credited to the week the last piece finished ([follow-through](../../reference/principles.md#follow-through)). Pending sub-tasks are not a miss.
- **Continuous needs a breakdown mechanism.** A planning command or sub-task template the person owns makes large work start from a breakdown without remembering; a high share of sized work alone is not enough ([stages](../../reference/principles.md#stages)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- Applies to **sessions with substantial work**: a goal too large to finish and check cleanly in one session (for example a migration across many modules, a multi-part feature, or several large goals at once).
- **"Substantial" is a grounded classification, not a threshold.** No token, line, file or prompt count defines it; the judge must justify it from the work itself (the scope the person described, the parts it touches). No such threshold is invented in [parameters](../../reference/parameters.md).
- Only the person's **main sessions** count; subagents, sidechains and Dram's own analysis sessions do not ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with only naturally small tasks (a one-line fix, a rename) is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs all of:

1. **Large work**: the request, as the person framed it, is substantial.
2. **A breakdown the person used**: the person asked for the work to be broken into smaller tasks (for example "Break the migration into steps we can do one per session"), or wrote the breakdown themselves. An agent-proposed breakdown counts only when the person's evidenced review adopts it.
3. **The first sub-task worked on its own and finished**: the next work (in this session or a later one in the same repository) takes up only that first sub-task, and it is finished.

Completing evidence for Seen: the person's breakdown request (or own breakdown) and the **first finished sub-task**. This is the source's citation ("the breakdown request and first completed task").

The source also says **each** sub-task is completed. That requirement is not dropped: under [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) it is the **follow-through** that later stages count. Evidence about subsequent sub-tasks (which started, which finished, when) is retained with the instance.

## Exclusions

- **An accidentally small request**: a naturally small one-line task does not prove deliberate sizing. Smallness alone is never recognized.
- **An unused agent breakdown**: the agent listed steps on its own and the person never adopted or used them.
- **A requested split followed by doing everything together anyway**: the person asked for steps and then said "just do it all" (or the agent did all steps in one go and the person accepted it). The breakdown was not used.
- "Do the whole migration" with no breakdown.
- A breakdown whose first sub-task was never finished in the record: not Seen yet; not a miss either while it is pending.

## Evidence

- **Cite** the person's breakdown request or their own written breakdown (exact quote from a person prompt, not tool output, hook output or a compaction summary), and the evidence that the first sub-task was finished (the session or turn where it completed).
- Keep **plan linkage**: which later sessions or turns took up which sub-task, with timestamps. Retain this for every sub-task, not only the first.
- Completion of a sub-task is judged from the record (the agent's work for that step is done and the person moved to the next step or confirmed it). It is not the agent's claim alone.
- **Evidence the pinned CLI does not supply**: classification of work as substantial; person-intent recognition of a breakdown request or adoption; linkage of later sessions to sub-tasks of one plan; sub-task completion judgement.

## Progression

Overrides of the [stages](../../reference/progression.md#stages) come from [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | A used breakdown of large work plus its **first finished sub-task**. |
| Forming | Breakdowns where **every sub-task finished**, in at least two distinct weeks of the last four. Each is credited to the week its **last** sub-task finished. |
| Established | At least 60% of applicable substantial work broken down with every sub-task finished, with at least four applicable cases ([`most`](../../reference/parameters.md#most)). |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

- A breakdown with only its first sub-task finished earns **Seen** but does not count toward Forming until every sub-task finishes. Pending sub-tasks are not a miss.
- A breakdown whose last sub-task finished outside the four-week window does not count toward Forming or Established in that window.
- A breakdown abandoned partway (remaining sub-tasks merged back into one go) keeps its Seen if the first sub-task finished, and never counts toward later stages.
- A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

| Fact | For this pattern |
| --- | --- |
| In place | A planning command or sub-task template, attributable to the person or their team, existed during the window. |
| Applied | It was actually used to begin substantial work in the window. |
| Held | The work it began then proceeded one sub-task at a time to completion. |
| Not holding | The command or template was used, but the work was still done all together, or its sub-tasks were abandoned. |
| Untested | Configured but never used to begin work in the window. |

A high share of sized work alone does not make this Continuous; the mechanism is required ([mechanisms](../../reference/evidence.md#mechanisms-in-place-applied-held)).

## Opportunities and coaching

- **Opportunity**: one session attempted **several large goals** (or one large goal) at once and none finished cleanly (abandoned, left half-done, or redone). It cites the person-authored prompt that started the combined work ([opportunities](../../reference/evidence.md#opportunities)). Agent-only evidence is not reported.
- **Coaching**: the [guide](guide.md) has the person break their largest real task into pieces that fit separate sessions and finish the first.
- `automate` advice (an owned planning command or template) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement that work was substantial and that the person deliberately broke it down and used the breakdown, plus linkage of later sessions to sub-tasks and judgement of each sub-task's completion. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`; no tool call distinguishes a deliberate breakdown from a request that happened to be small, so no fixed-pattern approximation may stand in for it.

## Missing capabilities

- **Substantial-work classification** grounded in the request and the work, without an invented size threshold.
- **Person-intent judgement** of a breakdown request, or adoption of an agent-proposed breakdown.
- **Task/plan linkage** across turns and sessions in the same repository.
- **Sub-task completion judgement**, with the week each sub-task finished.
- **Planning-command provenance** (owned command or template, and its use to begin work) for the mechanism.
- **A runnable model judge**: [judge.md](judge.md) is not executed.

## Verify before enabling

- "Break the migration into steps we can do one per session" followed by step one done is recognized; "Do the whole migration" is rejected.
- Three completed sessions following sub-tasks of one plan are recognized, and count toward Forming when the last finishes; a breakdown followed by doing it all in one go is rejected.
- A naturally small one-line task is never recognized as sizing.
- Guide discussion without using the breakdown earns nothing.
- A breakdown with only its first sub-task finished is Seen and does not count toward Forming.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
