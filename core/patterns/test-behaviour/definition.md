# Test behaviour

Source ID `test-behaviour`; pattern `glenngillen/test-behaviour`; Checking the work, rung 9. Check observable behaviour that callers or users rely on. Intended detection: model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The judgement this pattern needs is described in [judge.md](judge.md), which the pinned CLI does not execute.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- **Behaviour-changing** changes in the person's main sessions to an **API, output or user flow** that callers or users rely on: an endpoint's contract, an export format, emitted messages or emails, a CLI's output, a UI flow.
- Pure refactors with no observable change, documentation and internal tooling nobody calls are not applicable.
- A window with no behaviour-changing change is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs both:

1. **The person's deliberate act**: they **requested or wrote a behaviour-level check**, or **reviewed an approval fixture or snapshot**. Behaviour-level checks include:
   - **contract tests** against what clients expect (for example, an export's columns and types);
   - **end-to-end checks** of a user flow;
   - **recorded side effects** ("Record the emails it sends in the test and show me"), read by the person.
2. **Execution**: the check was then **run**, with its output linked to the request.

Completing evidence: the attributable request or check, and its run.

Classify **what is checked, not the framework name**. A unit-test tool can implement a genuine behaviour check; a test labelled "e2e" without assertions on relevant behaviour cannot substitute for behaviour coverage.

A **failing** behaviour test still proves the checking occurred; it does not prove the change satisfies the behaviour. It earns Seen for the act, not a claim that the change is correct.

## Exclusions

- **Implementation-only tests authored after the code** by the agent, asserting what the code does rather than what callers rely on.
- **Unreviewed snapshot updates**: regenerating snapshots or approval fixtures (for example running the suite with `-u`) without the person reading the diff.
- A test whose name or label says "e2e", "contract" or "integration" but asserts nothing relevant.
- A check requested but never run.
- Guided discussion without a requested or written, and executed, behaviour check.
- Behaviour checks the agent added spontaneously, without the person's request or review.

## Evidence

- **Cite** the person's request (quoted exactly) or the check they wrote, the check's relevant assertions, and its run output. For snapshots and approval fixtures, cite the person's review of the recorded output. At least one attributable person-authored citation is required ([attribution](../../reference/evidence.md#attribution-and-citations)).
- **Behaviour linkage**: the check must exercise the behaviour the change touched.
- **Ordering**: a check the person requested before or during the change counts; a test the agent wrote after the code without that request is the excluded case.
- **Evidence the pinned CLI does not supply**: classification of what a test asserts (behaviour or implementation); the person's review of recorded output or snapshot diffs; linkage between a request, the test written and its run; automatic check runs from hooks or CI.

## Progression

No threshold override; the default [stages](../../reference/progression.md#stages) apply, with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | The person's request or review of a behaviour check, followed by its run, inside the window. |
| Forming, Established | Instances whose behaviour check ran and whose result was used (a failure fixed, or a pass accepted), each credited to the week that finished. Established needs [`most`](../../reference/parameters.md#most) behaviour-changing changes. |
| Continuous | Relevant behaviour checks running automatically, in place, applied and holding (see [mechanism](#mechanism)). |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is behaviour checks that run automatically on the person's changes through a hook or CI they or their team own.

| Fact | For this pattern |
| --- | --- |
| In place | Hook or CI configuration that runs the relevant behaviour checks existed during the window, attributable to the person or their team. |
| Applied | It actually ran those checks on the person's behaviour-changing changes. |
| Held | The checks covered the behaviour changed, and their results were used before acceptance. |
| Not holding | A behaviour-changing change was accepted without them running, or broke a caller they should have covered, while they were in place. |
| Untested | In place, with no behaviour-changing change in the window. |

## Opportunities and coaching

- **Opportunity**: a change that **passed unit checks but broke a caller**. It cites a person-authored moment, such as the prompt accepting the change or the later report of the breakage ([opportunities](../../reference/evidence.md#opportunities)).
- Breakage after checks passed relates to the **Escapes** [outcome](../../reference/outcomes.md); it is not wired.
- **Coaching**: the [guide](guide.md) asks for one caller-side check on the next actual API or flow change.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement about what a test checks and whether the person requested or reviewed it, plus execution linkage. The pinned CLI (revision `bdea6f6`) runs no pack-authored judge and no block that sees either. Matching a test command, a file name or an "e2e" label would substitute a weaker definition, which the pack must not do.

## Missing capabilities

- **Pack-authored model judgement**: [judge.md](judge.md) is not executed by the pinned CLI.
- **Behaviour and test semantics**: what a test asserts and whether it exercises the changed behaviour.
- **Person review evidence** for recorded outputs, snapshots and approval fixtures, including whether a snapshot diff was read.
- **Execution linkage** between a request, the check written and its run.
- **Automatic-check mechanism support**: hook and CI run records, and a stage engine that reaches `continuous`.
- **Guided-session markers**.

## Verify before enabling

- A requested export contract test against client expectations, when run, is recognized; agent unit tests alone after implementation are rejected.
- "Record the emails it sends in the test and show me", with review and execution, is recognized; unreviewed snapshot `-u` updates are rejected.
- A test labelled "e2e" without relevant assertions is not behaviour coverage.
- A unit-test tool implementing a genuine behaviour check is recognized.
- Guided discussion without a requested or written, executed behaviour check is not recognized.
- Unused, held and not-holding mechanism cases produce distinct results.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
