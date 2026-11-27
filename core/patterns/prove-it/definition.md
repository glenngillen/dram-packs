# Prove it

Source ID `prove-it`; pattern `glenngillen/prove-it`; Checking the work, rung 1. Ask for evidence after an agent reports a code change done. Intended detection: model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Intent

**What it's for.** The person doesn't accept "done" without proof: tests, a build, the output.

**Why it matters.** "Done" from an agent is a claim, not a result. Asking it to run the relevant check after its last edit turns the claim into evidence the person can read, and a check that ran and failed is still useful: it shows the change is not finished yet. It is the first rung of Checking the work: the person checking, before checks are made automatic.

**What a recognition shows.** That after the agent changed code and called it done, the person asked for proof and a relevant check actually ran.

**Why the rules are drawn this way.**

- **Only code changes the agent reported done.** That is where a claim needs proving; discussion, reading code and documentation-only questions are not, and a window without such turns reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **The order is edit, claim, request, check.** A check before the final edit says nothing about the change that followed it, and a request before any change is not asking for proof of that change.
- **The request must be the person's.** Checks the agent ran unprompted are its own habit, not the person's ([human intent only](../../reference/principles.md#human-intent-only)). Checks a person-owned rule or hook caused are [Checks by default](../checks-by-default/definition.md), so the two habits are credited separately.
- **A relevant check must actually run.** "Yes, they pass" with nothing run, or an unrelated command such as `git status`, is not proof ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **Ran, not passed.** The pattern is about asking for evidence, so a check that ran and failed still completes the request; it is never taken as evidence the change works. Truncated or missing output leaves the result unknown rather than assumed ([missing is not low](../../reference/principles.md#missing-is-not-low)).
- **No Continuous of its own.** The original spec points to [Checks by default](../checks-by-default/definition.md) and [Gate "done"](../gate-done/definition.md) as the mechanisms that make proof automatic, so a hook running checks is recognized there. Why their stages are not carried over to this pattern: reason not recorded.
- **Guided sessions reach Seen only,** on the person's next real change ([guided sessions reach Seen only](../../reference/principles.md#guided-sessions-reach-seen-only)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A **turn is applicable** when the agent **changed code** in it (an edit or write to a source file in the person's main session) **and** then **reported completion** ("done", "fixed", "all passing", "that should work").
- Only the person's **main sessions** count; subagents, sidechains and Dram's own analysis sessions do not ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with no code-changing turn that ended in a completion claim is **no applicable work**: nothing is reported, not a miss. Pure discussion, reading code or documentation-only questions are not applicable.

## Recognition

**Seen** needs all of, in this order:

1. The agent's **last code edit** in the turn.
2. The agent's **completion claim** about that change.
3. A **person-authored request for proof** after the claim: asking for a test, build, lint, type check or other relevant check to be run and shown (for example "run the tests and show me", "did you lint it?").
4. A **relevant check actually executing** after that request (for example `go test ./...`, `ruff check .`, `npm run build`), in the same session.

Completing evidence: the person's request and the check execution. **"A check ran" is distinct from "a check passed".** The pattern is about asking for evidence, so a check that ran and **failed** still completes the request; it never becomes evidence that the change works. The outcome is recorded separately.

Order matters: a check that ran **before the final edit** does not substantiate a later completion claim, and a request made **before any change** is not a request for proof of that change.

## Exclusions

- **Unprompted checks** the agent ran on its own with no person request and no person-owned instruction: spontaneous model habit is not the person's act (a rule or hook that causes checks is [Checks by default](../checks-by-default/definition.md), not this pattern).
- A request for tests **before any edit** (for example at the start of a task): there was no change to prove yet.
- A request with **no following check**: the agent replied "yes, they pass" without running anything, or the session ended.
- A check that ran before the final edit, offered as proof of the later claim.
- An irrelevant command after the request (for example `git status` or `ls`): only a test, build, lint, type check or other check relevant to the changed code counts.
- A single tool call alone, without the person's request, never establishes intent.

## Evidence

- **Cite** the person's prompt requesting proof (exact quote, from a person prompt, not tool output, hook output or a compaction summary) and the check's tool call and its output.
- Keep the edit, claim, request and check timestamps; the ordering is part of the evidence.
- **Pass/fail**: record what the output shows. Missing or **truncated** output means the result is unknown. The request is still recognized when the check's execution is recorded, but nothing is claimed about passing.
- **Evidence the pinned CLI does not supply**: classification of person prompts as proof requests (model judgement); recognition of agent completion claims; per-turn ordering of edits, claims, requests and checks; classification of a command as a check relevant to the change.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One proof request after a completion claim, followed by a relevant check executing. |
| Forming | Such requests in at least two distinct weeks of the last four. Each is credited to the week its check ran. |
| Established | At least 60% of applicable completion claims followed by a proof request and a check, with at least four applicable cases ([`most`](../../reference/parameters.md#most)). |
| Continuous | Not defined for this pattern (see [mechanism](#mechanism)). |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

This pattern has **no mechanism of its own**. The source points to [Checks by default](../checks-by-default/definition.md) and Gate "done" for automation ([pattern-specific overrides](../../reference/progression.md#pattern-specific-overrides)). Their stages are not transferred here automatically: a hook that runs checks is recognized by those patterns, and does not make this pattern Continuous. `pattern.yaml` therefore declares no `continuous` block.

## Opportunities and coaching

- **Opportunity**: the agent reported a code change done (or passing) with **nothing run after the last edit**, and the person accepted it and moved on. It cites the person-authored moment that accepted the claim or started the next task ([opportunities](../../reference/evidence.md#opportunities)). A claim followed only by agent or tool output, with no later person turn, is not reported.
- **Coaching**: the [guide](guide.md) has the person request proof after their next actual change.
- `automate` advice (pointing to Checks by default and Gate "done") is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement of person intent (a request for proof) plus the ordering of edits, completion claims, requests and checks within a turn. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence` as fixed checks. Matching a test command alone would count spontaneous agent checks and checks before the final edit, which the definition excludes, so a fixed-pattern approximation must not stand in for it.

## Missing capabilities

- **Person-request judgement**: classifying a person prompt as a request for evidence about a change, distinct from tool results, hook output and compaction summaries.
- **Completion-claim recognition**: identifying the agent's "done"/"passing" claim about a code change.
- **Edit/claim/check ordering** per turn, including "last edit" and whether a check ran after it.
- **Check classification**: whether a command is a test, build, lint, type check or other check relevant to the changed files.
- **Result capture**: pass/fail from the check output, with truncation flagged.
- **A runnable model judge**: the active recommendation prompt is built inside the CLI; [judge.md](judge.md) is not executed.

## Verify before enabling

- Post-edit "run the tests and show me" followed by `go test ./...` is recognized; spontaneous `pytest` with no instruction is rejected.
- Post-edit "did you lint it?" followed by `ruff check .` is recognized; a test request before any edit is rejected.
- A guided request not followed by execution is incomplete.
- A failed check completes the request without being reported as the change working.
- A check before the final edit does not substantiate a later claim.
- Truncated output yields an unknown result, never a pass.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
