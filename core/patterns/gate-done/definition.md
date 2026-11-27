# Gate "done"

Source ID `gate-done`; pattern `glenngillen/gate-done`; Checking the work, rung 5. Require a final check before an agent finishes. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** A final gate stops the agent finishing until the checks pass. For capable models, this one gate may be all that's needed.

**Why it matters.** "Done" from an agent is a claim. A gate that runs the tests or build when the agent tries to finish turns it into a checked result, and sends failures back before the person reviews. It makes [Prove it](../prove-it/definition.md) happen without the person asking.

**What a recognition shows.** That a final gate the person or their team configured, running a real check, actually fired when the agent finished.

**Why the rules are drawn this way.**

- **The gate must be the person's or their team's.** The agent choosing to run tests at the end is not a gate, and a test command in the transcript is not evidence of one ([human intent only](../../reference/principles.md#human-intent-only)). Configuration and firing are facts, so code checks them ([code checks facts; a model judges the rest](../../reference/principles.md#code-checks-facts-a-model-judges-the-rest)).
- **It must run a real check.** Tests, a build or type checking say whether the work is correct; a formatter-only hook says nothing about that.
- **It must enforce.** The intent is to stop the agent finishing, so a command that swallows its own failure is not a gate. A bypassed or ignored failure is never called holding.
- **It must actually fire.** A hook in settings that never ran is untested, not Seen: configuration presence is never enough ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **A gate that caught nothing is neutral.** A passing run proves the gate executed, not that nothing escaped ([outcomes keep it honest](../../reference/principles.md#outcomes-keep-it-honest)).
- **Only repositories with checks where the person works.** A window with none reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **Continuous needs every applicable repository covered and the gate holding.** Coverage alone is not enough: it must fire, and failures must be fixed before finishing ([stages](../../reference/principles.md#stages)).
- **A guided setup reaches Seen only once it fires on real work** ([guided sessions reach Seen only](../../reference/principles.md#guided-sessions-reach-seen-only)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. Named as one of the first activation candidates; it still needs the capabilities below.

## Applicable work

- A **repository with checks** where the person works: one with tests, a build or type checking that could serve as a final gate, and at least one of the person's main sessions in the window.
- A window with no such repository is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** requires all of:

1. **An attributable final gate**: a Stop hook, or an equivalent mechanism that runs when the agent finishes, configured by the person or their team (repository or user-level settings).
2. **A real check**: it runs tests, a build or type checking. A valid build or type check counts even when it is not called "test". A user-level Stop hook that invokes the repository's own test script counts.
3. **A gate, not a command**: on failure it blocks the agent from finishing (or returns the failure for it to fix). A command that silently ignores its own failure (for example one that always exits successfully) is not a gate.
4. **It actually fired** in a session in the window.

Completing evidence: the attributable configuration and the actual run. A run that blocked once (for example `make test` failing and the agent fixing it before finishing) is the clearest instance; a run that passed proves execution.

A final gate that **caught nothing** is neutral evidence of execution, not proof that no bugs escaped ([outcomes](../../reference/outcomes.md#rules): quiet gates are neutral).

## Exclusions

- **Formatter-only hooks** (for example a Stop hook running only `prettier`): they check nothing about whether the work is correct.
- **Configured hooks never run**: a hook in settings that never fired in the window is untested, not Seen.
- **Non-enforcing commands**: a hook whose failure is swallowed so the agent finishes anyway.
- **The agent choosing to run tests** at the end without a configured gate: that is Prove it or Checks by default territory, not a gate. A test command appearing in the transcript is not evidence of a gate.
- **Guided configuration without a firing event**: setting the hook up during the guide does not complete Seen.

## Evidence

- **Cite** the attributable gate configuration and the run that fired (its command and result as recorded). The person-authored citation can be supplied by configuration attribution where the [evidence contract](../../reference/evidence.md#attribution-and-citations) allows, plus the person's prompt in the session where it fired.
- **Historical**: the configuration must have existed when the session ran; current settings cannot prove a past firing.
- **Enforcement**: whether a failure blocked the agent needs the hook's exit behaviour and the agent's subsequent actions, not just the configuration.
- **Evidence the pinned CLI does not supply**: hook configuration history and attribution; hook execution records with event type (stop or equivalent), command, exit status and output; enforcement behaviour; classification of a command as test, build, type check or formatter; repository coverage.

## Progression

Uses the default [stages](../../reference/progression.md#stages) with a coverage qualification for Continuous ([pattern-specific overrides](../../reference/progression.md#pattern-specific-overrides)):

| Stage | For this pattern |
| --- | --- |
| Seen | One attributable final gate running a real check that fired. |
| Forming | Firings in at least two distinct weeks of the last four. |
| Established | The gate fired in at least 60% of applicable sessions, with at least four applicable sessions ([`most`](../../reference/parameters.md#most)). |
| Continuous | **Every** applicable repository covered and the gate firing in the window, **and** the [mechanism](#mechanism) holding. Coverage alone is not enough. |

A guided setup establishes Seen only once it fires on real work ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the final gate itself.

| Fact | For this pattern |
| --- | --- |
| In place | The attributable gate configuration existed during the window, covering the repository. |
| Applied | It fired when the agent finished in an applicable session. |
| Held | Every applicable repository is covered, the gate fired, and when it failed the agent was blocked and fixed the failure before finishing. Blocking then fixing a failure is held. |
| Not holding | A session finished with the gate's failure unresolved: an enforcement bypass, an ignored failure, or the gate not firing in a covered repository. A bypass or ignored failure is never called holding. |
| Untested | Configured but never fired in the window. |

## Opportunities and coaching

- **Opportunity**: in an applicable repository, a session finished with failing checks (for example the agent reported done and the next test run, CI or the person found failures). It cites the person-authored moment, such as the prompt accepting the result or reporting the failure ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) asks the person to add a final gate using their actual test command and explains what happens on failure.
- `automate` advice (a user-level gate running each repository's own check) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. `hook_configured` is declared but not implemented, and configuration alone would accept an unused hook. Matching a test command in tool calls would accept the agent spontaneously running tests and cannot tell a gate from a formatter or a command that ignores failure. Enabling either would substitute a weaker definition.

## Missing capabilities

- **Hook execution records**: which hook fired on which event (stop or equivalent), the command, exit status and output.
- **Enforcement behaviour**: whether a failure blocked the agent from finishing, and whether it was bypassed.
- **Check classification**: test, build or type check versus formatter-only.
- **Configuration attribution and history**: the gate's settings at session time and whose they are, including user-level hooks invoking repository scripts.
- **Repository coverage**: which applicable repositories the gate covered.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- A `make test` Stop hook firing and blocking once is recognized; a Stop hook running only `prettier` is rejected.
- A user-level Stop hook invoking the repository's test script is recognized; an unused hook in settings is rejected.
- An enforcement bypass or ignored failure is never reported as holding.
- Guided configuration without a firing event does not complete Seen.
- A passing gate is reported as execution, not as proof that nothing escaped.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
