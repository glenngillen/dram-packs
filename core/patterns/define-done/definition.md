# Define done

Source ID `define-done`; pattern `glenngillen/define-done`; Briefing, rung 2. Establish how feature or bug-fix work will be judged before implementation. Intended detection: model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** The person says up front how they'll know the work is right: acceptance criteria, examples, or the tests that should pass.

**Why it matters.** This is what lets checks judge correctness: without acceptance criteria, correctness is outside anything that checks the work ([groups](../../reference/principles.md#groups)). If the agent decides what done means, it finishes when its own idea of the work is complete.

**What a recognition shows.** That on a feature or fix, the person set the criteria before implementation began, and the result was then checked against them.

**Why the rules are drawn this way.**

- **Feature and bug-fix work only.** Questions, exploration and reviews don't change behaviour, so there is no correctness to judge. A window with no feature or fix reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **Criteria the person authored.** Agent-written criteria accepted unread are the agent deciding what done means, the very thing this pattern replaces ([human intent only](../../reference/principles.md#human-intent-only)). A referenced spec counts when it is the person's; a missing file or unknown author leaves the result unassessed, not a miss ([missing is not low](../../reference/principles.md#missing-is-not-low)).
- **Before implementation.** The pattern is about saying it up front; criteria that arrive after implementation began are review, not defining done.
- **Concrete enough to check.** "Make sure it works" gives a check nothing to judge against. Behavioural criteria count, as long as they were checked.
- **A later check against them completes it.** Criteria exist so a check can judge the work; criteria never checked haven't done that job. Seen therefore already includes the check, so the act and its follow-through coincide ([follow-through](../../reference/principles.md#follow-through)).
- **Continuous needs a template, spec location or command that is used.** It supplies or asks for criteria without the person remembering ([stages](../../reference/principles.md#stages)). A folder of specs on its own is neither criteria for this work nor a mechanism in use ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. The intended model judgement is described in [judge.md](judge.md), which the pinned CLI does not execute.

## Applicable work

- **Feature and bug-fix work** in the person's main sessions.
- **Excluded**: questions, exploration, reviews and other work that does not change behaviour.
- A window with no feature or fix is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** requires, in order:

1. **Person-authored criteria before implementation**: acceptance criteria, examples, named tests or required behaviour, in the person's prompt or in an attributable spec the person authored and referenced. "Before implementation" means before the agent's first edit to the code the criteria govern.
2. **A later check against them**: a test run, a demonstration or an explicit comparison of the result with each criterion.

Completing evidence is the later check. Source positives: criteria saying expired and single-use reset links must be rejected, with the implementation then checked against both; "@specs/export.md implement this; the examples in it are the tests", where the person authored `specs/export.md` and the examples were later run.

A criterion may be **behavioural rather than executable** ("an admin sees the archived projects; a member does not"). It still needs evidence that it was checked.

## Exclusions

- Vague requests such as "make sure it works" or "make sure it's done properly".
- **Criteria supplied after completion** or after implementation began: that is review, not defining done.
- **Agent-written criteria accepted without review** (for example followed only by "ok").
- Criteria that were never checked.
- A spec location by itself: a folder of specs is not criteria for this work and not a mechanism in use.

## Evidence

- **Cite** the criteria (an exact quote from the person's prompt, or from the referenced spec with its attribution) and the later check as completion.
- **Ordering**: the criteria's timestamp must precede the first implementation edit; the check must follow implementation.
- **Attribution**: a referenced spec counts when it is attributable to the person (they wrote or substantively edited it). A **missing referenced file or unknown author leaves the result unassessed**, not a miss.
- **Evidence the pinned CLI does not supply**: task classification (feature/fix versus question); retrieval and authorship of referenced specs; ordering of criteria, first edit and check; recognition that a check addressed the criteria.

## Progression

Default [stages](../../reference/progression.md#stages), with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion). Because Seen already requires the check, the deliberate act and its follow-through coincide; Forming and Established credit each instance to the week its check finished.

| Stage | For this pattern |
| --- | --- |
| Seen | One feature or fix with person-authored criteria before implementation, checked against them inside the window. |
| Forming | Such instances in at least two distinct weeks of the last four. |
| Established | Such instances on at least [`most`](../../reference/parameters.md#most) features and fixes in the last four weeks. |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session earns Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is a **template, spec location or command the person uses** that supplies or asks for criteria before work starts.

| Fact | For this pattern |
| --- | --- |
| In place | The template, spec location or command exists in the person's or their team's configuration during the window. |
| Applied | The person actually started feature or fix work with it in the window (for example referenced a spec written there, or ran the command). |
| Held | That work had criteria before implementation and was checked against them. |
| Not holding | Work started through it went ahead without criteria or without a check, and was reopened for not matching intent. |
| Untested | It exists but was not used in the window. A spec location by itself is not a mechanism in use. |

## Opportunities and coaching

- **Opportunity**: accepted work that was **reopened because it did not match intent**. Cite the person's original request and the reopening prompt ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) asks the person to write two or three "done when" lines on their next real feature or fix before requesting code.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The definition needs a model judgement of criteria and checks, person attribution of referenced specs, and event ordering. The pinned CLI (revision `bdea6f6`) runs no pack-authored judge; only `tool_call_matches` and `tool_call_sequence` execute as fixed checks, and a matched test command proves neither that criteria existed beforehand nor that the check addressed them.

## Missing capabilities

- **Task classification**: feature or bug-fix work versus questions and exploration.
- **Pack-driven model judgement** of criteria and of whether a check addressed them, with exact quotations.
- **Referenced-spec retrieval with authorship**, at the time of the request.
- **Event ordering**: criteria, first implementation edit and check, with timestamps.
- **Reopen linkage** for opportunities.
- **Mechanism-use evidence** for templates, spec locations and commands; **guided-session markers**.

## Verify before enabling

- Expired and single-use reset-link criteria checked against the implementation are recognized; "Make sure it's done properly" is rejected.
- "@specs/export.md implement this; the examples in it are the tests" with attributable criteria and later checks is recognized; agent-written criteria followed only by "ok" are rejected.
- A guided criterion followed by its check earns Seen; coaching conversation without criteria or a check does not.
- A missing referenced file or unknown author leaves the result unassessed.
- Criteria supplied after implementation are rejected.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- What counts as "before implementation" when the agent made exploratory or scaffolding edits before the criteria arrived?
  - evidence: The source requires criteria before implementation but does not define where implementation starts; the same first-edit boundary is unresolved in Plan first.
  - options: Before the first edit to any file the criteria govern; before the first edit of any kind; leave such cases unassessed.
  - location: core/patterns/define-done/definition.md / Recognition
