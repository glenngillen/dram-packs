# Mind the cache

Source ID `mind-the-cache`; pattern `glenngillen/mind-the-cache`; Economics, rung 2. Avoid rebuilding large cold contexts after long breaks. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. Named as one of the first activation candidates; it still needs the capabilities below.

## Applicable work

User decision: the applicable denominator is **every return to the same work** after a gap over [`cache_gap`](../../reference/parameters.md#cache_gap) from a context over [`large_context_tokens`](../../reference/parameters.md#large_context_tokens). It includes both outcomes:

- a **fresh start** from a handoff or after `/clear`: a hit;
- a **cold resume** that continues the large cold context: a miss.

The source's narrower "sessions resumed" wording is superseded: counting only resumes would leave the fresh-start choice out of the assessment.

Both thresholds are strict ([boundaries](../../reference/parameters.md)):

| Fact | Inside | Outside |
| --- | --- | --- |
| Gap | More than 1 hour (for example two hours) | Five minutes; **exactly 1 hour** |
| Prior context | More than 150,000 tokens | 40,000 tokens; **exactly 150,000** tokens |

If the CLI supplies the model's known cache lifetime as a fact, that lifetime replaces the default gap ([`cache_gap`](../../reference/parameters.md#cache_gap)). **Unknown** cache lifetime, context size or timestamps produce no recognition, no miss and no cost ([insufficient evidence](../../reference/evidence.md#insufficient-evidence)).

"Same work" means the same task continued: the cold session itself, or a new session in the same repository picking the task up. Unrelated new work after a break is not a return. A window with no qualifying return is **no applicable work**.

## Recognition

**Seen** needs all of:

1. **A qualifying break**: a gap over `cache_gap` after a context over `large_context_tokens`.
2. **A fresh start** for the same work after that break: a new session started from a handoff (for example a `NOTES.md` the person had the agent write), or `/clear` followed by the person re-pointing the agent at the work.
3. The fresh start is the **person's act** (their command or first prompt), not an automatic compaction or a harness restart.

Completing evidence: the timestamps establishing the gap, the prior context size, and the fresh start's **first prompt**.

## Exclusions

- **Short gaps** (exactly 1 hour or less) and **small contexts** (exactly 150,000 tokens or less): outside applicable work, neither hit nor miss.
- **Compaction** on resume: the harness summarising the cold context is not the person's fresh start.
- **A handoff written but not used**: creating `NOTES.md` before the break and then continuing the old session afterwards is a cold resume.
- **Guided handoff creation** without the later fresh start after a qualifying gap.
- Dram's own analysis sessions.

## Evidence

- **Cite** the gap timestamps, the prior context size, and the fresh start's first prompt (exact quote, person-authored). For a miss, cite the person prompt that continued the cold context.
- **Cost**: where the CLI has measured usage and prices, reuse the recommendation system's existing **`cache-rebuild` signal** (value `idle`: a break longer than the cache lasts) and its estimate of what the rebuild cost above reading the cache. That is an **API-priced** figure for comparison with the person's own past; it is never presented as what anyone was billed, and no extra subscription charge is inferred from it ([outcomes](../../reference/outcomes.md#rules)). Unknown usage or pricing gives no cost line.
- **Evidence the pinned CLI does not supply to a pattern**: per-turn gap and prior-context facts as recognition inputs, the model's cache lifetime, provenance of a session start (fresh, `/clear`, resume, compaction), linkage of a fresh session to the earlier work and to a handoff file actually read, and mechanism attribution.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One fresh start after a qualifying break. |
| Forming | Fresh starts in at least two distinct weeks of the last four. |
| Established | At least 60% of qualifying returns are fresh starts, with at least four qualifying returns ([`most`](../../reference/parameters.md#most)). |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session establishes Seen only, and only once the fresh start after a qualifying break happens ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

An **end-of-day command** or **Stop mechanism** of the person's own that writes a handoff.

| Fact | For this pattern |
| --- | --- |
| In place | The attributable command or hook existed during the window. |
| Applied | It produced a handoff before a qualifying break. |
| Held | After the break, the person started fresh from that handoff (for example an end-of-day handoff used the next morning). |
| Not holding | The mechanism was in place but the person continued the large cold context after a qualifying break, or the handoff it produced was not used. |
| Untested | Configured but no qualifying break in the window. |

Relationship to [Hand it off](../hand-it-off/definition.md): that pattern is about carrying decisions out of a long session; this one is about the break. One fresh start can be evidence for both, but no stage transfers automatically.

## Opportunities and coaching

- **Opportunity**: the person continued a large context (over `large_context_tokens`) after a break over `cache_gap`. It cites the person prompt that resumed the cold context ([opportunities](../../reference/evidence.md#opportunities)), with the measured API-priced rebuild cost where available and no cost otherwise.
- **Coaching**: the [guide](guide.md) has the person request a handoff before a real long break and start from it afterwards.
- `automate` advice (an end-of-day command or Stop hook writing the handoff) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. Neither sees turn gaps, prior context size, cache lifetime or how a session started. The recommendation system's `cache-rebuild` signal measures rebuilds for its own proposals and savings; it does not make a pack-authored recognizer run, and it does not see fresh starts, which are the hits in this pattern's denominator.

## Missing capabilities

- **Gap and context facts** per return: the gap length, prior context tokens and the model's cache lifetime.
- **Session-start provenance**: fresh start, `/clear`, resume, compaction.
- **Pairing** of a return with the earlier work, including a fresh session in the same repository, and with the handoff file it read.
- **Cost reuse**: the `cache-rebuild` estimate exposed to pattern copy, with unknown usage or pricing producing nothing.
- **Mechanism attribution and evaluation**: an owned command or Stop hook writing handoffs; nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- A two-hour gap then a fresh start from a `NOTES.md` handoff is recognized; a five-minute resume is outside scope.
- An end-of-day handoff used the next morning is recognized as mechanism evidence; resuming a large 150k-token-plus context after lunch is a miss, not successful cache management.
- Exactly 1 hour and exactly 150,000 tokens are outside.
- A fresh start after a qualifying gap counts in the denominator alongside cold resumes.
- Guided handoff creation without the later fresh start is incomplete.
- Unknown cache lifetime, context size, usage or pricing produces no recognition and no cost.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
