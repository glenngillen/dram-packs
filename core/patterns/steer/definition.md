# Steer, Don't Stop

Source ID `steer`; pattern `glenngillen/steer`; Correcting course, rung 1. Diagnose and redirect a wrong approach rather than merely stopping it. Intended detection: model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Intent

**What it's for.** When the agent goes the wrong way, the person diagnoses and redirects rather than just stopping it.

**Why it matters.** "No" or "try again" tells the agent only that it failed, so it often retries the same idea. A short reason gives it something to change. Stopping is fine; explaining is what turns a stop into a steer. It is the first rung of Correcting course: correcting the agent while the work is under way.

**What a recognition shows.** That at a moment the agent went wrong, the person said what was wrong or why, and (for later stages) the agent changed course because of it.

**Why the rules are drawn this way.**

- **Moments the agent went wrong.** A redirect only means something where there was a wrong turn; a window where the agent never went wrong reports nothing ([applicable work](../../reference/principles.md#applicable-work)). Only the person's main sessions count.
- **A person-authored correction that explains.** The value is the diagnosis, so bare stops ("no", "stop", "try again", "still failing") and an interrupt followed by "continue" are excluded: they tell the agent it failed, not what to change.
- **Taste-only changes and agent self-correction are excluded.** A change of preference with nothing wrong is an ordinary instruction, not a correction of a wrong turn; the agent fixing its own mistake isn't the person steering ([human intent only](../../reference/principles.md#human-intent-only)).
- **Seen completes on the explained redirect; later stages need the agent to change course.** An explanation the agent ignored has had no effect, so it never counts toward Forming or Established. This staging comes from the recorded completion decision ([follow-through](../../reference/principles.md#follow-through)). Truncated records after the correction leave follow-through unknown, not missed ([missing is not low](../../reference/principles.md#missing-is-not-low)).
- **No Continuous of its own.** Making a correction permanent is [Fix the harness](../fix-the-harness/definition.md), as the original spec says; a harness fix isn't credited here, so neither pattern borrows the other's stage.
- **The coaching trigger is the same failing approach retried three or more times.** It tries to capture "the agent was stuck on one idea and nobody told it why"; the count is a [calibration point](../../reference/principles.md#thresholds-are-calibration-points). Retries with no person turn aren't reported, because opportunities must cite a person-authored moment (recorded decision).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A **moment the agent went wrong** in the person's main session: the person interrupted it, an attempt failed or was repeated (the same failing approach tried again), or the agent took an approach that was wrong for the work (wrong file, wrong layer, wrong cause).
- Only the person's **main sessions** count; subagents, sidechains and Dram's own analysis sessions do not ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window where the agent never went wrong, or where every change of direction was a matter of taste with no error, is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs, at an applicable moment:

1. A **person-authored correction** (a person prompt, not tool output, hook output or a compaction summary), possibly after an interrupt.
2. The correction **explains what was wrong or why**, or names the actual cause, so the agent can change approach: for example "the limit belongs in Options because callers set it per request", or "Don't change the schema; the slow part is the query".

Completing evidence for Seen: the person's explained redirect, cited as an exact quote. That is the source's completing event and the person's deliberate act.

**Follow-through** is the agent's subsequent response: whether it **changed course** in line with the correction (moved the limit into `Options`, worked on the query instead of the schema). It is cited as corroboration. Under [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

- Seen completes on the explained redirect, even while the agent's next response is still pending.
- Forming and Established count only redirects followed by a changed course, credited to the week the change of course finished.
- An explained correction the agent **ignored** (it kept the same approach) earns Seen for the redirect itself but **never** counts toward later stages. It does not satisfy the complete definition, which needs both the explanation and the changed course.

## Exclusions

- **Bare** stops and retries with no reason: "no", "stop", "try again", "still failing", "that's wrong". They tell the agent it failed, not what to change.
- **Interrupt then "continue"**: an interrupt alone does not prove meaningful steering, and resuming the same approach is not a redirect.
- **Taste-only changes with no error**: "actually, call it `fetchAll`" when nothing was wrong. These are ordinary instructions, not corrections of a wrong turn.
- **Agent self-correction**: the agent noticing its own mistake and changing approach without a person correction.
- **Guided reflection without an actual redirect**: answering the guide's question about what might go wrong earns nothing.

## Evidence

- **Cite** the person's correction (exact quote from a person prompt) and the agent's subsequent response or edits showing whether it changed course. Keep the interrupt, the correction and the response timestamps.
- Cite the moment the agent went wrong (the failed attempt, the repeated approach or the interrupted tool call) so the correction is anchored to applicable work.
- Missing or **truncated** records after the correction leave follow-through **unknown**: Seen can still stand on the redirect, but nothing counts toward later stages until a changed course is visible. A record truncated before the correction is insufficient, not a miss.
- **Evidence the pinned CLI does not supply**: attribution of interrupts to the person; judgement that a prompt diagnoses the problem rather than merely stopping it; recognition that an attempt failed or repeated the same approach; judgement that the agent's later work changed course.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One explained redirect at a moment the agent went wrong. |
| Forming | Explained redirects followed by a changed course in at least two distinct weeks of the last four, each credited to the week the change of course finished. |
| Established | At least 60% of applicable moments redirected with an explanation and followed by a changed course, with at least four applicable moments ([`most`](../../reference/parameters.md#most)). |
| Continuous | Not defined for this pattern (see [mechanism](#mechanism)). |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

This pattern has **no mechanism of its own**. The source points to [Fix the harness](../fix-the-harness/definition.md) for automation: a correction that keeps recurring is best written into an instruction, command or hook ([pattern-specific overrides](../../reference/progression.md#pattern-specific-overrides)). No stage transfers automatically in either direction: a harness fix is recognized by Fix the harness and does not make this pattern Continuous. `pattern.yaml` therefore declares no `continuous` block.

## Opportunities and coaching

- **Opportunity**: the same failing approach was retried **at least three times** before the person intervened, or the person stopped the agent with a bare "no", "stop" or "try again" and the agent repeated the approach. It cites the person-authored moment: the bare stop, or the prompt that eventually intervened ([opportunities](../../reference/evidence.md#opportunities)). Retries visible only in agent and tool output, with no person turn, are not reported.
- **Coaching trigger**: the same failing approach retried three or more times before intervention. The [guide](guide.md) asks the person to notice a real wrong turn and explain the reason when redirecting.
- `automate` advice (pointing to Fix the harness) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement of whether a person's correction explains what was wrong or why, attribution of interrupts, and judgement that the agent's later work changed course. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence` as fixed checks. No command match can tell an explained redirect from a bare "stop", or a changed course from a repeated attempt, so a fixed-pattern approximation must not stand in for it.

## Missing capabilities

- **Interrupt attribution**: recording that the person interrupted a turn, and which tool call or response was interrupted.
- **Diagnosis judgement**: classifying a person prompt as an explained correction (what was wrong or why) versus a bare stop, a retry request or a taste-only change.
- **Wrong-turn recognition**: identifying failed and repeated attempts of the same approach, and counting retries before intervention.
- **Changed-course evidence**: judging whether the agent's subsequent response and edits followed the correction, with the week it finished.
- **A runnable model judge**: the active recommendation prompt is built inside the CLI; [judge.md](judge.md) is not executed.

## Verify before enabling

- "The limit belongs in Options because callers set it per request" after an interrupt, followed by a changed approach, is recognized; an interrupt followed by "continue" is rejected.
- "Don't change the schema; the slow part is the query", followed by the agent working on the query, is recognized; "Still failing" is rejected.
- An explained correction the agent ignored earns Seen for the redirect but never counts toward Forming or Established.
- A guided question about what might go wrong, with no actual redirect, earns nothing.
- Taste-only changes with no error are no applicable work.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
