# Fan out

Source ID `fan-out`; pattern `glenngillen/fan-out`; Delegation, rung 3. Run independent parts through parallel subagents and use their combined work. Intended detection: model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- Applies to work with **several independent parts**: [`several_parallel`](../../reference/parameters.md#several_parallel), three or more parts (inclusive) that do not depend on each other's results (for example the same client update in each of four services, or three independent investigations).
- **Two parts do not meet** `several_parallel`; such work is not applicable here.
- Independent parts **need not edit files**: parallel investigations count, unlike [Two at once](../two-at-once/definition.md)'s explicit edit requirement.
- Only the person's **main sessions** count as the place the request is made; subagent histories are evidence attached to their parent ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with no work of three or more independent parts is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs all of:

1. **A person request for parallel subagents** across the parts (for example "Use a subagent per service to update the client, then summarise"). Only person prompts count.
2. **Concurrent execution**: at least [`several_parallel`](../../reference/parameters.md#several_parallel) subagents actually running at overlapping times, from their start and end timestamps.
3. **Use of the combined result**: the subagents' results were brought together and used (summarised and acted on, merged, applied to the next step).

Completing evidence: the request and the **used combined result**, with the subagent starts and timings.

## Exclusions

- **A single subagent**, however large its task.
- **Sequential fan-out**: subagents run one after another do not satisfy concurrency, even when there are three or more.
- **Discarded parallel results**: results thrown away or never brought together and used.
- Parallel subagents the agent started without the person's request or an owned workflow (the model's own habit).
- Exactly two parallel subagents: below `several_parallel`.

## Evidence

- **Cite** the person's request (exact quote from a person prompt, not tool output, hook output or a compaction summary), each subagent start with its timestamps, and the moment the combined result was used.
- Concurrency rests on **overlapping run intervals** of the child sessions, not on the request wording or the number of Task calls.
- **Evidence the pinned CLI does not supply**: independent-part judgement; concurrent subagent timing from child sessions; result-use linkage; workflow provenance for the mechanism.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One person-requested concurrent fan-out of three or more parts whose combined result was used. |
| Forming | Such fan-outs in at least two distinct weeks of the last four, each credited to the week its combined result was used. |
| Established | At least 60% of applicable multi-part work fanned out and used, with at least four applicable cases ([`most`](../../reference/parameters.md#most)). |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

No numeric stage requirement beyond these shared rules is added for safety; safety is a prerequisite for suggestions, not a stage here. A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

| Fact | For this pattern |
| --- | --- |
| In place | A saved command or workflow that fans out (for example `/audit-services`, running one subagent per service), attributable to the person or their team, existed during the window. |
| Applied | It was actually run on applicable work in the window. |
| Held | It ran the parts concurrently and the combined result was used. |
| Not holding | It was used, but the parts ran one after another, or the combined result was discarded. |
| Untested | Saved but never run in the window. |

## Opportunities and coaching

- **Opportunity**: independent repeated work (three or more parts) was done **serially** in one session. It cites the person-authored prompt that started the work ([opportunities](../../reference/evidence.md#opportunities)). Agent-only evidence is not reported.
- **Coaching**: the [guide](guide.md) asks the person to choose suitable real parts and request one subagent per part, with results brought together.
- **Safety prerequisites**: parallel and autonomous work multiplies whatever each subagent can do. Advice to fan out keeps the [Safety prerequisites](../../reference/progression.md#safety-prerequisites) explicit: subagents work within the person's existing scoped permissions ([Scope permissions](../scope-permissions/definition.md)), secrets protection ([Keep secrets out](../keep-secrets-out/definition.md)) and guards on destructive commands ([Guard destructive commands](../guard-destructive/definition.md)). Permission bypass is never suggested as a way to make fan-out smoother. No numeric stage requirement is invented for these prerequisites; the source gives none.
- `automate` advice (an owned fan-out command or workflow) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement that the parts were independent and that the person asked for parallel subagents, plus concurrency from child-session timing and evidence the combined result was used. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`; counting Task calls cannot tell concurrent from sequential runs or used from discarded results, so a fixed-pattern approximation must not stand in for it.

## Missing capabilities

- **Independent-part judgement**, including the count of parts against `several_parallel`.
- **Concurrent subagent timing**: start and end of each child session, linked to the parent.
- **Result-use linkage**: evidence the combined output was brought together and used.
- **Workflow provenance**: whether a saved command or workflow is the person's or their team's, and that it caused the fan-out.
- **A runnable model judge**: [judge.md](judge.md) is not executed.

## Verify before enabling

- "Use a subagent per service to update the client, then summarise" with concurrent work used is recognized; one subagent is rejected.
- A used `/audit-services` workflow fanning out per service is mechanism evidence; parallel results thrown away are rejected.
- Sequential subagents do not satisfy concurrency; two parallel subagents do not meet `several_parallel`.
- Guided requests without parallel execution and result use are incomplete.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
