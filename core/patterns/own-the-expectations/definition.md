# Set the expectations yourself

Source ID `own-the-expectations`; pattern `glenngillen/own-the-expectations`; Briefing, rung 4. Separate the expectations from an implementation that could otherwise define its own success. Intended detection: model judgement and git evidence.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** The expectations the work is checked against (tests, examples, fixtures) are written or approved by the person before the agent implements, not written by the same agent afterwards to match what it built.

**Why it matters.** Tests written after the code tend to describe what the code does, bugs included, so they pass straight away and prove little. Expectations the person wrote or read before the implementation are independent of it, so a pass then means something. It takes [Define done](../define-done/definition.md) to the tests themselves.

**What a recognition shows.** That on a change adding or changing tests, the expectations came from the person before implementation, and the implementation was then made to pass them.

**Why the rules are drawn this way.**

- **Only work that adds or changes tests.** That is where tests can come before or after the code; criteria in general are Define done's. A window with no such work reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **Written by the person, or reviewed by them with substance.** What matters is that the person's judgement went into the expectations before the code existed, not who typed them. An unread "ok, go" puts none in ([human intent only](../../reference/principles.md#human-intent-only)).
- **Before the first implementation edit.** Independence from the implementation is the point of the pattern, so tests and code produced in one step, with no review between, are excluded.
- **Post-hoc agent tests never count, however green.** They tend to mirror the implementation, and a passing test is not itself evidence of independent expectations ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **The implementation passing them completes it.** Expectations matter because the work is checked against them; a reviewed test with no passing implementation is incomplete ([follow-through](../../reference/principles.md#follow-through)).
- **Continuous needs a test-first rule or command that is followed.** It puts the tests first without the person remembering ([stages](../../reference/principles.md#stages)); a rule present but ignored is not holding ([prevention](../../reference/principles.md#prevention-when-success-removes-the-signal)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. The intended model judgement is described in [judge.md](judge.md), which the pinned CLI does not execute.

## Applicable work

- **Feature or fix work that adds or changes tests**, in the person's main sessions.
- Work with no test change is not applicable here (Define done covers criteria in general).
- A window with no such work is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** requires, in order:

1. **Independent expectations before implementation**: tests or examples the person wrote (for example a commit of theirs adding `export_test.go`), or agent-written tests the person **substantively reviewed and approved** before any implementation edit (for example the person added an empty-input case before authorizing implementation).
2. **An implementation made to pass them**: a later test run showing those tests passing against the new code.

Completing evidence: the person's test-writing commit or review, and the implementation passing those expectations.

Agent authorship of a test is acceptable when the person meaningfully reviewed it before implementation. **A passing test is not itself evidence** that the person supplied independent expectations.

### Independent expectations versus implementation-mirroring tests

The pattern exists to separate expectations from the code they judge. Tests written **after** the implementation, by the agent, tend to **mirror** the implementation, including its bugs, and pass immediately. Such post-hoc tests never count, however thorough they look and however green the run.

## Exclusions

- Agent-authored tests written after the implementation that pass immediately with no prior review.
- **Unread approval** such as "ok, go" on agent-written tests.
- "Write tests and code" performed together, where tests and implementation arrive in the same step with no review between them.
- A guided test review with no subsequent passing implementation (incomplete, not a recognition).
- A test-first rule merely present but ignored.

## Evidence

- **Cite** the person's test-writing commit (git authorship) or their review prompt (quoted exactly, showing substance), then the passing run against the implementation.
- **Ordering**: tests and review before the first implementation edit; passing run after it.
- **Attribution**: git authorship must be the person's, or the review must be a person prompt that engages with the test content.
- Missing git history or an unavailable test run is [insufficient](../../reference/evidence.md#insufficient-evidence), not a miss.
- **Evidence the pinned CLI does not supply**: git authorship of test files; ordering of test, review and implementation events; recognition of substantive review; linkage of a test run's results to the specific tests reviewed.

## Progression

Default [stages](../../reference/progression.md#stages), with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion). Seen requires the passing implementation as well as the expectations, so each instance completes, and is credited to its week, when the implementation passes.

| Stage | For this pattern |
| --- | --- |
| Seen | One change whose person-owned expectations preceded the implementation, which then passed them. |
| Forming | Such instances in at least two distinct weeks of the last four. |
| Established | Such instances on at least [`most`](../../reference/parameters.md#most) changes adding or changing tests in the last four weeks. |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session earns Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is a **test-first instruction or command** in the person's or their team's configuration.

| Fact | For this pattern |
| --- | --- |
| In place | The rule or command existed, attributable, during the window (historical configuration). |
| Applied | Applicable work happened with it in effect and it engaged (the command was run, or the agent cited the rule). |
| Held | Tests came first, the person reviewed them before implementation, and the implementation then passed them. |
| Not holding | With it in place, tests came after the implementation or were approved without review. |
| Untested | It existed but no applicable work happened. A rule merely present but ignored cannot establish Continuous. |

## Opportunities and coaching

- **Opportunity**: post-hoc tests that **mirrored an implementation bug** later found by the person. Cite the person's request for the work and the prompt reporting or correcting the bug ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) asks for a failing reproduction of the next real bug, has the person read it, then request the fix.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The definition needs git authorship, ordered test and implementation events, and a judgement of substantive review. The pinned CLI (revision `bdea6f6`) runs no pack-authored judge, and its fixed checks (`tool_call_matches`, `tool_call_sequence`) can see that tests ran but not who wrote them, whether they were reviewed, or whether they came first. A green run alone would reward exactly the mirroring tests this pattern rejects.

## Missing capabilities

- **Git authorship and history** for test files, attributable to the person.
- **Event ordering** of test writing, person review, first implementation edit and the passing run.
- **Pack-driven model judgement** of substantive review (as opposed to "ok, go"), with exact quotation.
- **Test-result linkage** from a run to the specific tests reviewed.
- **Historical configuration** for test-first rules and commands; **guided-session markers**; bug-report linkage for opportunities.

## Verify before enabling

- A person committing `export_test.go` and asking "make these pass" is recognized when the implementation then passes them; code followed by agent-authored tests that pass immediately without prior review is rejected.
- A request for failing tests, the person adding an empty-input case, then authorizing implementation is recognized; "write tests and code" performed together is rejected.
- A guided test review with no subsequent passing implementation does not satisfy completion.
- A test-first rule present but ignored does not establish Continuous.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- What makes a person's review of agent-written tests "substantive"?
  - evidence: The source accepts adding an empty-input case and rejects "ok, go", but gives no general rule for reviews in between (for example "looks good, but rename the test").
  - options: Require the review to change or question test content; accept any reply that references specific tests; leave intermediate cases to model judgement with cited content.
  - location: core/patterns/own-the-expectations/definition.md / Recognition
