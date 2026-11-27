# Hand it off

Source ID `hand-it-off`; pattern `glenngillen/hand-it-off`; Context, rung 2. Carry decisions from a long session into a genuinely fresh one. Intended detection: paired-session model judgement plus mechanism checks.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. A [judge prompt](judge.md) is authored but not executed.

## Applicable work

- A **long session**: [`long_session`](../../reference/parameters.md#long_session), meaning context over [`large_context_tokens`](../../reference/parameters.md#large_context_tokens) (strictly more than 150,000 tokens) **or** any compaction. Exactly 150,000 tokens with no compaction is not long.
- Only the person's **main sessions** count; subagents, sidechains and Dram's analysis sessions do not.
- Unknown context size with no compaction record is **insufficient**, not "short" and not a miss.

## Recognition

**Seen**: a cross-session pairing, per [`handoff_pairing`](../../reference/parameters.md#handoff_pairing):

1. The **previous main session in the same repository** was long, and it **wrote a handoff** (a file such as `NOTES.md` or `HANDOFF.md`, or a state summary in its output) at the person's request or through the person's owned hook or command.
2. A **genuinely fresh** main session in the same repository began **within 24 hours** after that session ended.
3. The fresh session's **first person prompt** references that handoff (for example "Read NOTES.md and continue") or pastes its state summary, and the session uses it.

Completing evidence: the prior session's handoff-writing event and the fresh session's first person prompt. The source proposes pairing the prior session's last three turns with the new session's first two as the judged evidence.

"Genuinely fresh" means a new session, confirmed by the session record. **Resume** or **continue** (for example `claude --continue`) is not fresh: it reloads the long context. An unconfirmed fresh/resumed flag is insufficient for recognition.

The 24-hour window is elapsed time from the prior session's end, not calendar days: a fresh session the next morning, 15 hours later, is inside it.

## Exclusions

- **Resume or continue** of the long session.
- **Compaction alone**: it shrinks the same session; it is not a handoff to a fresh one.
- **Unrelated named files**: a fresh session that mentions a file the prior session wrote but starts an unrelated task.
- **A handoff never used**: written but no fresh session started from it (including a guided handoff with no fresh use).
- A pairing across different repositories, or with a prior session that ended more than 24 hours before.
- A handoff written by an agent workflow nobody asked for, unless it came from the person's owned hook or command.

## Evidence

- **Cite** the handoff-writing event (the person's request or the owned hook's run, and the written content) and the fresh session's first person prompt (exact quotation).
- **Attribution**: the request or the hook/command must be the person's or their team's. The first prompt of the fresh session is the person-authored citation.
- **Cross-session**: see [cross-session evidence](../../reference/evidence.md#cross-session-evidence). If privacy or retention removed the prior session, the relationship is **unassessable**, not a miss.
- **Evidence the pinned CLI does not supply**: paired-session evidence across sessions in a repository with end and start times; fresh-versus-resumed provenance; context size and compaction records; which file a session wrote and which file a later session read; hook execution records and their configuration history. Existing recommendation context signals are related inputs, not the complete recognizer.

## Progression

Default [stages](../../reference/progression.md#stages) apply, with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | One qualifying fresh session whose first prompt used the prior session's handoff. |
| Forming, Established | Instances whose follow-through finished: the fresh session continued the work from the handoff (the agent acted on its decisions rather than re-deriving them). Credited to the week that finished. Established uses [`most`](../../reference/parameters.md#most) of applicable long sessions followed by more work in the same repository. |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

Writing a handoff is not by itself an instance: the fresh use completes it. A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is an owned **PreCompact or Stop hook, or a saved command**, that writes a handoff when a session gets long or ends.

| Fact | For this pattern |
| --- | --- |
| In place | The hook or command existed in the person's or team's configuration during the window. |
| Applied | It ran on a long session (the hook fired, or the person invoked the command) and wrote a handoff. |
| Held | The next fresh session in the same repository, within the pairing window, started from that handoff. |
| Not holding | It ran, but the next session resumed the long one or started without the handoff. |
| Untested | In place, but no long session occurred, or it never fired. |

The source's mechanism example: a PreCompact hook writes `HANDOFF.md`, and the next session's first prompt reads it.

## Opportunities and coaching

- **Opportunity**: a long or compacted session that **lost an earlier decision** (the agent contradicted or re-asked something decided before compaction), or that was resumed instead of handed off. It cites a person-authored moment, such as the prompt correcting the lost decision or the prompt resuming the session ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) asks the person to request a handoff, then start a fresh session from it.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The intended recognizer pairs two sessions, confirms the second is genuinely fresh, and judges whether its first prompt used the first session's handoff. The pinned CLI (revision `bdea6f6`) has no cross-session pairing, fresh-session provenance, context-size or compaction facts, or hook execution evidence, does not execute pack-authored judges, and has no block that expresses any of them. A filename match (for example `NOTES.md` in a prompt) would substitute a weaker definition that accepts unrelated mentions and resumed sessions.

## Missing capabilities

- **Paired-session evidence**: the previous main session in the same repository, its end time and last turns, with the next session's start time and first turns.
- **Fresh-session provenance**: whether a session was new, resumed or continued, as a confirmed fact.
- **Context and compaction facts** per session, to apply `long_session`.
- **File write/read linkage** across sessions: the handoff the first session wrote and the second session read.
- **Hook execution records** (PreCompact, Stop) and command invocations, with configuration history and attribution.
- **Judge execution and verification** of pack-authored judgement; only `tool_call_matches` and `tool_call_sequence` run in the pinned build.

## Verify before enabling

- `NOTES.md` written earlier, then a fresh "Read NOTES.md and continue", is recognized; `claude --continue` is rejected.
- A fresh pasted state summary with its prior-session evidence is recognized; a new unrelated task despite an earlier `NOTES.md` is rejected.
- The PreCompact-written `HANDOFF.md` used next session is held.
- A guided handoff written but never used in a fresh session is incomplete.
- A next-day session within 24 hours pairs; one after more than 24 hours, or in another repository, does not.
- An unconfirmed fresh/resumed flag, and a prior session removed by retention, are insufficient rather than misses.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
