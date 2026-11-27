# Learn from production

Source ID `learn-from-production`; pattern `glenngillen/learn-from-production`; Checking the work, rung 11. Turn actual production signals into agent fixes with a regression check. Intended detection: model judgement ([judge prose](judge.md), not executed).

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- The pattern applies to **work on production services**: fixing behaviour of code that runs in production, where production signals exist.
- A window with no production-service fix work is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs both:

1. **An actual production signal supplied to the agent**: the person's request carries a real alert, error, stack trace, log excerpt or SLO breach (redacted as needed), not a paraphrase such as "fix the bug in payments"; or an owned trigger (configured by the person or their team) started the fix from that signal, with the person's review or merge of the fix as the person-authored citation (scenario pos-3).
2. **A preventive check in the fix**: the change includes a new check (typically a regression test reproducing the failure) that would catch the same problem next time, and it was run.

Completing evidence: the person request carrying the signal (or, for an owned trigger, the trigger provenance plus the person's review or merge of the fix) and the new check. The fix-to-check relation is a model judgement: does the check exercise the failure the signal shows?

Completion follows the [stage-dependent rule](../../reference/progression.md#stage-dependent-completion). A request inside the window whose check lands after it is credited to the window where the check finished.

## Exclusions

- **Generic bug requests without the signal** ("Fix the bug in payments").
- **Fixes without a new preventive check**, including fixes that only rerun existing tests.
- A check that does not exercise the failure in the signal (for example an unrelated test added in the same change).
- **An agent starting itself** on production data; only the person's request or a person/team-configured trigger supplies the intentional action.
- A **guided explanation** of an alert without supplying the signal and creating the preventive check.
- Dram's own analysis sessions.

## Evidence

- **Cite**, for a person request, the person-authored request carrying the signal (quoted exactly, redacted) and the new check with its run.
- **Cite**, for an owned trigger, the trigger provenance (configuration attributable to the person or team, and the run record carrying the signal), the new check with its run, and at least one attributable person-authored moment for that fix, such as the person's review or merge approval. Without a person-authored moment a triggered fix is neither recognized nor an opportunity.
- Opportunities cite the person's request that started the production fix, or, for an owned trigger, the trigger provenance and the person-authored prompt that accepted or merged the fix ([opportunities](../../reference/evidence.md#opportunities)).
- **Attribution**: for a triggered fix, the trigger configuration must be attributable to the person or their team. A trigger supplies the intentional action through that configuration; an agent starting itself does not.
- **Privacy**: production signals stay on the person's machine as case content ([privacy](../../reference/evidence.md#privacy)). This pack never fetches production logs, connects to error services or commits production credentials or real incident content. All fixtures are synthetic.
- **Evidence the pinned CLI does not supply**: whether text in a request is an actual production signal (signal provenance); fix-to-check judgement; trigger configuration and run provenance for headless fixes; whether a service is a production service.

## Progression

Default [stages](../../reference/progression.md#stages), with stage-dependent completion:

| Stage | For this pattern |
| --- | --- |
| Seen | One production fix started from a supplied signal whose change added a preventive check. |
| Forming | Such fixes in two distinct weeks of the last four, each credited to the week its check finished and was kept. |
| Established | At least [`most`](../../reference/parameters.md#most) of production fixes over the last four weeks. Fewer than four is not assessable, which is not a miss. |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is a person- or team-configured alert or error trigger that starts agent fix work automatically.

| Fact | For this pattern |
| --- | --- |
| In place | An error-tracker or alert trigger, attributable to the person or team, configured to start agent fix work during the window. |
| Applied | It fired on a production signal and started a fix session in the window. |
| Held | The fixes it started included a regression check that would catch the problem next time, and the problem did not recur on applicable later work. |
| Not holding | It fired, but fixes shipped without a preventive check, or the same production problem recurred after a fix it started. |
| Untested | A trigger in place that never fired in the window. |

## Opportunities and coaching

- **Opportunity**: a production fix that added no regression check, citing the person-authored request that started it, or, when an owned trigger started it, the trigger provenance and the person-authored prompt that accepted or merged the fix (scenario neg-9). Truncated or missing change evidence is insufficient, not an opportunity.
- **Coaching**: the [guide](guide.md) asks the person to use a real, redacted production error from their own work and to request a reproducing test before the fix. It never fetches production data or connects to services.
- `automate` advice (a configured trigger) is offered only after the [automation gate](../../reference/progression.md#automation-gate), and after Scope permissions for the unattended run ([safety prerequisites](../../reference/progression.md#safety-prerequisites)).

## Why disabled

The pinned CLI (revision `bdea6f6`) does not run pack-authored judges: its active recommendation prompt is built inside the CLI. It also cannot tell an actual production signal from a paraphrase, cannot link a fix to a new check, and has no trigger provenance. Recognizing this pattern from keywords such as "error" or "test" would mistake words in a transcript for intent and completion.

## Missing capabilities

- **Pack-authored model judgement** run with verification, for signal and fix-to-check judgement.
- **Production-signal provenance**: whether request text is an actual alert, error, log or SLO signal.
- **Change and check linkage**: the files changed by the fix, the new check, and its execution result.
- **Trigger and run evidence**: which headless fix sessions a configured alert or error trigger started, and whose trigger it was.
- **Production-service classification** of repositories or services.
- **A runnable block**: none in the pinned registry expresses the above; only `tool_call_matches` and `tool_call_sequence` run.

## Verify before enabling

- "Here's the error from the alert … fix it and add a test that reproduces it" with the resulting check is recognized; "Fix the bug in payments" without a signal is rejected.
- An attributable error-tracker trigger starting a headless fix with a regression test is recognized; a fix with no new check is rejected.
- A guided explanation of an alert without supplying it and creating the check is incomplete.
- An agent starting itself on production data is not recognized.
- Quotes are exact, IDs exist, completion is in window, and agent-only evidence yields neither recognition nor opportunity.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- How is a "production service" identified?
  - evidence: The source applies the pattern to work on production services but gives no classification rule.
  - options: Person-declared repositories; repositories with deployment configuration; model judgement from the signal itself.
  - location: core/patterns/learn-from-production/definition.md / Applicable work
