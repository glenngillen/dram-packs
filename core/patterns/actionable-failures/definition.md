# Make failures actionable

Source ID `actionable-failures`; pattern `glenngillen/actionable-failures`; Checking the work, rung 4. Feed failures back with enough detail for the agent to fix the problem. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A **repository with agent-run hooks or checks**: hooks, lint rules or checks that run during the agent's work in the person's sessions (for example a post-edit hook, a pre-commit check run by the agent, or a lint command the harness runs).
- Applicable moments are **failures of those checks during agent work** in the person's main sessions ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with no such repository, or no check failing during agent work, is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** requires all three, in order:

1. **An owned feedback path**: a hook or check the person or their team configured (repository or user-level settings, lint configuration or check scripts they maintain) that returns its failure output to the agent.
2. **Feedback the agent visibly received**: the failure output appears in the agent's context (for example as hook feedback or a tool result) and says what is wrong in enough detail to act on: the rule, the location, or the expected fix (for example "use the shared Button, see components/Button").
3. **A linked fix in the agent's next step**: the agent's next action changes the code to resolve the problem the failure named (for example replacing the ad hoc button with the shared `Button`).

Completing evidence: the attributable hook configuration, the fed-back failure as the agent received it, and the fixing change.

**Linking a fix** needs a reliable relationship between the named problem and the edit: the edit touches what the failure named and the re-run passes or no longer reports it. Any edit after an error is not enough. **Next step versus next turn**: the source wording alternates between "next step" and "next turn". The fix must be the agent's immediate response to that failure; no wider window is invented that would let a delayed, unrelated fix count (see [open questions](#open-questions)).

## Exclusions

- **Failure output the agent never saw**: a pre-commit failure in the person's terminal, CI output, or a hook that only writes logs elsewhere. Logs the agent does not receive cannot establish agent-visible feedback.
- **Failures fed back and ignored**: the agent continued without addressing them, or the person told it to skip them.
- **Uninformative output** the agent could only guess from ("lint failed", an exit code alone): that is the coaching trigger, not recognition.
- **Agent-initiated checks with no owned configuration**: the agent spontaneously running a linter it chose is not the person's harness.
- **Guided hook setup with no real failure and fix**: configuring the hook during the guide earns nothing until a real failure is fed back and fixed.
- **Formatter-only hooks** that silently rewrite files feed no failure back; they are not this pattern.

## Evidence

- **Cite** the hook or check configuration (attributable to the person or team), the failure output as delivered to the agent (quoted exactly), and the agent's next action that fixed it. At least one person-authored citation is required ([attribution](../../reference/evidence.md#attribution-and-citations)): the person's prompt that started the work, or their configuration where the evidence contract allows configuration to supply attribution.
- **Historical**: the configuration must have existed and applied when the session ran. Current settings alone cannot prove a past session's hook behaviour.
- **Command matching is not evidence**: a tool call named `eslint` is not proof the agent received actionable output or fixed what it named.
- **Evidence the pinned CLI does not supply**: hook execution records with status and output; whether that output was delivered into the agent's context; hook configuration history and attribution; a link between a named failure and the fixing edit.

## Progression

Uses the default [stages](../../reference/progression.md#stages) and [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | One owned hook failure fed back and fixed in the agent's next step. |
| Forming | Such instances in at least two distinct weeks of the last four, each credited to the week its fix finished. |
| Established | Fed-back, fixed failures in at least 60% of applicable failures with at least four applicable cases ([`most`](../../reference/parameters.md#most)). |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided setup establishes Seen only, and only with a real failure and fix ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is hooks or lint rules with actionable fix guidance that return failures to the agent.

| Fact | For this pattern |
| --- | --- |
| In place | The owned hook or lint configuration existed during the window and is set to return failure output to the agent. |
| Applied | A check actually failed during agent work and its output was delivered to the agent. |
| Held | The agent fixed the named problem in its next step. |
| Not holding | The check failed during agent work but the agent did not receive the output; or received output too vague to act on and repeated the failing attempt; or received actionable feedback and ignored it or did not resolve the named problem in its next qualifying response (step or turn: see [open questions](#open-questions)), as in scenario `neg-2`. |
| Untested | Configured, but no failure occurred during agent work in the window. A quiet hook proves nothing. |

## Opportunities and coaching

- **Opportunity**: in an applicable repository, the agent made repeated attempts at the same failure because the error was uninformative or never reached it, or the failure reached it with actionable detail and the agent ignored it. It cites a person-authored moment, such as the prompt that started the work or the person's message pointing out the repeated failure ([opportunities](../../reference/evidence.md#opportunities)). Repeated attempts visible only in agent output, with no person-authored moment, are not reported.
- **Coaching**: the [guide](guide.md) has the person pick a real, frequently failing check and wire actionable feedback into their harness.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The definition needs hook execution, delivery into the agent's context and a fix linked to the named problem. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. A sequence such as "lint command, then an edit" would match a failure the agent never saw, an ignored failure followed by an unrelated edit, and an agent-chosen linter run, so enabling it would replace the pattern with a command match.

## Missing capabilities

- **Hook execution records**: which hook or check ran, its status and output, per session.
- **Feedback delivery**: whether the output entered the agent's context (versus a terminal or a log file).
- **Configuration attribution and history**: the hook configuration in effect when the session ran, and whose it is.
- **Fix linkage**: a deterministic relationship between the problem a failure named and the agent's next change, including a passing re-run.
- **Next-step boundary**: a defined boundary for "next step" (see [open questions](#open-questions)).
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- A lint hook saying "use the shared Button, see components/Button" followed by the replacement is recognized; a pre-commit failure the agent never saw is rejected.
- A custom fix-guidance message acted on in the next turn is recognized; a fed-back failure ignored is rejected.
- A hook that only writes logs elsewhere does not establish agent-visible feedback.
- Guided hook setup without a real failure and fix earns nothing.
- An unrelated edit after a failure is not linked as its fix.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- Is the fix window the agent's next step (its next tool action) or its next turn?
  - evidence: The source alternates "next step" and "next turn"; both examples have the fix immediately follow the feedback, and the spec forbids a window that lets a delayed unrelated fix count.
  - options: The agent's next tool action after the feedback; the remainder of the agent's turn in which the feedback arrived; the next turn, requiring the edit to address the named problem.
  - location: core/patterns/actionable-failures/definition.md / Recognition
- What deterministic relationship proves an edit fixes the named failure?
  - evidence: The spec requires a reliable relationship, not any edit after an error; the fixture shape has no link between a failure and an edit.
  - options: Edit touches the named file or symbol and the re-run passes; re-run no longer reports the named rule; model judgement with cited failure and diff.
  - location: core/patterns/actionable-failures/definition.md / Recognition
