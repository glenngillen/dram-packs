# Evidence, not claims

Source ID `evidence-not-claims`; pattern `glenngillen/evidence-not-claims`; Checking the work, rung 2. Challenge an agent's summary when the actual result contradicts it. Intended detection: model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Intent

**What it's for.** When the agent's summary and the recorded result disagree, the person believes the result and challenges the claim.

**Why it matters.** An agent's summary can say "all tests pass" while the output above it shows failures or skipped cases. The output is the evidence; the summary is a claim. A person who accepts the summary lets broken work through even though the proof that it is broken was in front of them.

**What a recognition shows.** That the person noticed a real gap between what the agent said and what was recorded, and pointed at it.

**Why the rules are drawn this way.**

- **Only real contradictions are applicable.** The pattern needs a recorded result the claim contradicts, including a shortfall against what the person asked for (three cases when four were expected). Where every claim matched its result, there is nothing to challenge and nothing is reported ([applicable work](../../reference/principles.md#applicable-work)).
- **The challenge must be the person's.** A tool, hook or reviewer agent catching it is the mechanism at work, not the person's act ([human intent only](../../reference/principles.md#human-intent-only)).
- **Challenging a correct result, or "are you sure?" with no discrepancy, is excluded.** The pattern is believing the result, not doubting everything; such questions are neither credit nor a miss.
- **Missing or truncated output is unassessed.** It may hide the missing case or a later pass, so it is never taken as a contradiction or as a correct result ([missing is not low](../../reference/principles.md#missing-is-not-low)).
- **Seen completes on the challenge; later stages need the agent to have addressed it.** The original spec required the agent to address the result for Seen; a recorded decision makes completion stage-dependent, so the first challenge is credited promptly, and Forming and Established count only challenges whose response dealt with the result, credited to the week it finished. A challenge the agent ignored never counts towards later stages ([follow-through](../../reference/principles.md#follow-through)).
- **Continuous is a Stop hook or instruction rule requiring the actual check output with every "done".** It surfaces the contradiction before the person has to spot it. Once it holds, there is nothing left to challenge, so credit moves to claims arriving with their output ([prevention](../../reference/principles.md#prevention-when-success-removes-the-signal)).
- **Guided sessions reach Seen only.** A guided review that finds no discrepancy is neither a failure nor an opportunity ([guided sessions reach Seen only](../../reference/principles.md#guided-sessions-reach-seen-only)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A moment is **applicable** when an agent's claim (a summary, "all tests pass", "done", "4 of 4 fixed") is **contradicted by a recorded result** in the same session: failures, errors or skipped cases in tool output, or fewer cases than the person specified.
- Only the person's **main sessions** count ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window where every claim matched its recorded result, or where no claim was made about recorded output, is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs:

1. A recorded result (test, build, lint or other output) and an agent claim it **contradicts**.
2. A **person-authored challenge** identifying that gap (for example "You said all pass but 3 failed above. Fix those first").

**Follow-through** (Forming and Established only): the agent's later response addresses the recorded result (fixing the failures, running the missing cases, or showing why the result was expected).

Per [stage-dependent completion](../../reference/progression.md#stage-dependent-completion): **Seen completes on the person's challenge**, which is the source's completing event. **Forming and Established** count only challenges whose response **addressed** the recorded result, each credited to the **week the response finished**. A challenge whose response is still pending counts for Seen and is not a miss; a response that ignored the challenge never counts toward later stages.

A contradiction can also be a shortfall against what the person asked for: three passing cases when four were expected is a warranted challenge even if everything that ran passed.

## Exclusions

- **Accepting the false claim** ("Great, thanks" after the contradiction): that is the opportunity, not a recognition.
- **Challenging a correct result**: questioning a summary that matches complete, passing output is not this pattern (it is not a miss either).
- **Questions without an actual discrepancy** ("are you sure?" with nothing in the output to contradict the claim).
- Challenges made by tools, hooks or a reviewer agent rather than the person; a mechanism catching it is the [mechanism](#mechanism), not Seen.
- A challenge based only on output that was **missing or truncated**: the contradiction cannot be shown.

## Evidence

- **Cite** the person's challenge (exact quote from a person prompt), the underlying recorded result (the tool-output lines showing the failure, error, skip or missing case), and the agent claim it contradicts. **Retain** the agent's later response showing whether it addressed the result.
- **Truncated or missing output** may hide the missing case or a later pass. That is insufficient evidence: unassessed, never a contradiction and never a correct result ([insufficient evidence](../../reference/evidence.md#insufficient-evidence)).
- **Evidence the pinned CLI does not supply**: claim/result comparison (model judgement); recognition of a person prompt as a challenge to a specific claim; recognition that the subsequent action addressed the result; truncation flags; evidence-enforcing configuration and its run facts.

## Progression

No threshold override of the [stages](../../reference/progression.md#stages); completion follows the stage-dependent rule above.

| Stage | For this pattern |
| --- | --- |
| Seen | One warranted challenge issued in the window. |
| Forming | Addressed challenges in at least two distinct weeks of the last four, each credited to the week its response finished. |
| Established | At least 60% of applicable contradictions challenged and addressed, with at least four applicable cases ([`most`](../../reference/parameters.md#most)). |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is an **evidence-enforcing Stop hook or instruction rule** that requires the actual check output alongside completion claims, owned by the person or their team.

| Fact | For this pattern |
| --- | --- |
| In place | The hook or rule existed, attributable to the person or team, when the session ran (current configuration alone cannot prove a past session). |
| Applied | It actually engaged on a completion claim: the hook fired, or the rule was loaded and the agent produced output alongside its claim. |
| Held | On that applicable work, claims came with the actual output, and any contradiction was surfaced before the person accepted it. |
| Not holding | While in place and applied, the agent still made a claim the recorded output contradicted, without the output alongside. |
| Untested | In place, but no completion claim about check output in the window. |

## Opportunities and coaching

- **Opportunity**: "all tests passed" (or similar) accepted by the person despite recorded failures, errors or skipped cases. It cites the person turn that accepted the claim and the recorded result ([opportunities](../../reference/evidence.md#opportunities)). A contradiction followed by no person turn is agent-only and is not reported.
- **Coaching**: the [guide](guide.md) asks the person to compare the next completion summary against the actual output. A guided output review that finds **no discrepancy** is neither a failure nor an opportunity.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement comparing an agent's claim against the recorded result, identifying a person's challenge to it and judging whether the response addressed it. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`, which match tool calls, not claims or person intent. Declared hook checks do not execute in the fixed-pattern engine, so the mechanism cannot be checked either.

## Missing capabilities

- **Claim/result comparison**: whether an agent's summary contradicts failures, errors, skipped cases or an expected case count in recorded output.
- **Challenge recognition**: a person prompt identifying that gap, distinct from tool output, hook output and compaction summaries.
- **Follow-through recognition**: whether the agent's later response addressed the recorded result, with its finish time for week crediting.
- **Truncation facts** on tool output, so hidden results stay unassessed.
- **Configuration history and run facts** for Stop hooks and instruction rules (in place, fired, held).
- **A runnable model judge**: [judge.md](judge.md) is not executed by the pinned CLI.

## Verify before enabling

- "You said all pass but 3 failed above. Fix those first" earns Seen when issued, including when the response is pending or ignored (pos-5, pos-7), and counts toward Forming only once addressed; "Great, thanks" after the contradiction is an opportunity.
- A challenge to three passing cases when four were expected is recognized; challenging a correct complete result is not.
- Questions without a discrepancy do not earn the pattern; a guided review finding none creates no opportunity.
- A challenge in week 1 with its response in week 2 counts toward Forming in week 2.
- Truncated output is unassessed.
- Unused, held and not-holding mechanism cases produce distinct results.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
