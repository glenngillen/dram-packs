# Let the harness carry it

Source ID `harness-carries-it`; pattern `glenngillen/harness-carries-it`; Economics, rung 3. Establish that a lighter model's routine work passes checks and survives. Intended detection: code checks plus git evidence.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** The person's guides and gates are good enough that a cheaper model does routine work reliably: it passes the gates and the changes are kept.

**Why it matters.** The person's checks, not the model name, decide whether routine work is good enough. Where gates run on every change, lighter-model work that passes them and is still in place two weeks later is as kept as any other. In Economics, this is the harness doing the work a bigger model would; it builds on [Right-size it](../right-size-it/definition.md) and on the gates from Checking the work.

**What a recognition shows.** That routine work done on a lighter model passed the repository's checks and survived, not just that a lighter model was used.

**Why the rules are drawn this way.**

- **Routine work on a lighter model, in a repository whose checks ran on the change.** Without gates there is nothing to judge whether the lighter model carried the work, so that is a Checking the work matter first. "Lighter" uses Right-size it's reference tier; unknown tiers are unassessed ([missing is not low](../../reference/principles.md#missing-is-not-low)). No such work reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **The person's model choice or their own pinned subagent or command.** Lighter work the person didn't route there isn't their harness carrying it ([human intent only](../../reference/principles.md#human-intent-only)).
- **Gates passed and the change kept.** Passing checks and a kept change are the evidence that work held up. A gate that didn't run proves nothing, and an estimated saving is not a kept change ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **Kept means still in the default branch fourteen days later.** The window tries to capture "the change held up rather than being quietly replaced"; it is the shared [`kept_window`](../../reference/parameters.md#kept_window) and a [calibration point](../../reference/principles.md#thresholds-are-calibration-points). Younger changes are unassessed, and each instance is credited when its survival is established ([follow-through](../../reference/principles.md#follow-through)).
- **Finished on premium, or reverted, is excluded.** Then the lighter model did not carry the work. Failed lighter trials are never an opportunity for another lighter trial.
- **Coverage counts all routine work in gated repositories, premium included.** Measuring only lighter work would make coverage trivially complete, so Established and Continuous use the full set. "Most" (60%, at least four changes) tries to capture "routine work usually runs lighter"; it is a [calibration point](../../reference/principles.md#thresholds-are-calibration-points).
- **Continuous needs coverage and a holding mechanism.** The original spec's Continuous is coverage alone; the pack also requires the routing configuration with its gates, because a high rate without a mechanism is Established ([stages](../../reference/principles.md#stages)).
- **No savings or billing claims.** Outcomes are shown as facts with their cases ([outcomes keep it honest](../../reference/principles.md#outcomes-keep-it-honest)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- **Routine work** ([`routine_work`](../../reference/parameters.md#routine_work): renames, docstrings, formatting, version bumps, simple fixes) done on a **lighter model** in the person's main sessions or through an owned pinned-lighter subagent or command.
- In a repository with **checks that run on the change**: [Checks by default](../checks-by-default/definition.md), [Gate "done"](../gate-done/definition.md), [Gate each step](../gate-each-step/definition.md) or [CI](../back-it-up-in-ci/definition.md) linked to the change.
- What makes a model "lighter" uses the reference tier of [Right-size it](../right-size-it/definition.md); that reference is unresolved (see [open questions](#open-questions)). Unknown tiers are unassessed.
- A window with no lighter routine work is **no applicable work**.
- **Two different sets.** The lighter routine work above is the **recognition subset**: only it can earn Seen or Forming. The **coverage denominator** used by Established and Continuous is **all routine work** in gated repositories in the window, whatever model ran it, including deliberate escalations to premium; otherwise filtering to lighter work would make coverage trivially 100%. The same exclusions apply to both sets: immature changes (younger than `kept_window`) and changes with unavailable git history are unassessed and left out of both, and routine work whose checks did not run is not counted in either.

## Recognition

**Seen** needs all of:

1. **Routine work on a lighter model**, attributable to the person (their model choice or their own pinned subagent or command).
2. **Linked gates passed**: the repository's checks or gates actually ran on that change and passed. A gate that did not run proves nothing; a quiet gate is neutral ([outcomes](../../reference/outcomes.md#rules)).
3. **Kept**: the change is still in the default branch [`kept_window`](../../reference/parameters.md#kept_window) (fourteen days) later.

Completing evidence: the session, the relevant gate runs and the kept change.

**Survival is a fourteen-day fact.** A change younger than fourteen days, or one whose git history is unavailable, is **unassessed**: neither recognized nor failed. A one-day revert measure is not fourteen-day survival. The pattern's Seen therefore completes when the kept window has passed, which can be after the window in which the work happened; the work and the survival are recorded with their own dates ([completion windows](../../reference/evidence.md#completion-windows)).

## Exclusions

- **No checks**: routine work on a lighter model in a repository whose checks did not run on the change.
- **Reverted or replaced** within fourteen days.
- **Finished on premium**: the lighter model failed and the person (or a fallback) finished the work on a premium model. That is not the lighter model carrying the work.
- **Savings estimates** in place of evidence: an estimated saving is not a kept change and cannot substitute for fourteen-day survival.
- **Guided trials** without later passing and kept evidence.

## Evidence

- **Cite** the session (with the person prompt starting the routine work), the gate runs linked to the change and their results, and the commit or merge that was still in the default branch fourteen days later.
- **Stable attribution across model switches**: which model made the change that was kept. A change partly made on a lighter model and finished on a premium one is finished on premium.
- **Evidence the pinned CLI does not supply**: routine-work classification, model tier per change, gate-to-change linkage, git survival over fourteen days and attribution of kept changes to sessions. The pinned registry's `reverted_within` measure is declared but not implemented and is not fourteen-day survival.

## Progression

Uses the [stages](../../reference/progression.md#stages) with the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule; every instance is credited to the week its fourteen-day survival was established.

| Stage | For this pattern |
| --- | --- |
| Seen | One lighter routine change that passed its linked gates and was kept fourteen days. |
| Forming | Such kept changes established in at least two distinct weeks of the last four. |
| Established | [Most](../../reference/parameters.md#most) of all routine changes in the coverage denominator (at least 60%, with at least four applicable changes, premium escalations included) ran lighter, passed and were kept. |
| Continuous | Most of all routine changes in the coverage denominator ran lighter, passed and were kept, **and** the [mechanism](#mechanism) is in place, applied and holding. Coverage alone is not enough. |

Immature changes are unassessed and count neither for nor against a stage.

## Mechanism

A mechanism of the person's own that sends routine work to a lighter model (a lighter default, or an owned command or subagent pinned lighter; see [Right-size it](../right-size-it/definition.md#mechanism)) **together with** the gates that judge it.

| Fact | For this pattern |
| --- | --- |
| In place | The routing configuration and the repository's gates existed during the window, attributable to the person or their team. |
| Applied | Routine work ran through the routing and the gates ran on it. |
| Held | Most such work passed its gates and was kept fourteen days. |
| Not holding | Lighter routine work routinely failed its checks and was finished on premium, or was reverted or replaced within fourteen days. |
| Untested | Configured but no routine work in the window. |

## Opportunities and coaching

- **Opportunity**: routine work ran on a premium model in a repository where effective gates ran on that work and could have judged a lighter model's result. It cites the person prompt that started the work ([opportunities](../../reference/evidence.md#opportunities)). Without effective gates there is no opportunity here; that is a Checking-the-work matter first.
- **Failed lighter trials are not an opportunity.** Work that the lighter model attempted, failed and that was finished on premium (neg-2, and repeatedly under a lighter default in neg-9) is evidence that the lighter model is not carrying that work, or that the mechanism is not holding. It never supports recommending another lighter trial; only premium work never tried on the lighter model, in a gated repository, can be an opportunity.
- Copy makes no savings or billing claim ([outcomes](../../reference/outcomes.md#rules)).
- **Coaching**: the [guide](guide.md) proposes a real routine task on a lighter model and lets the actual checks assess it.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. It has no gate-to-change linkage, no model tier per change and no fourteen-day git survival. Approximating with a test command match or with the unimplemented `reverted_within` measure would count unchecked or immature work.

## Missing capabilities

- **Routine-work and tier facts** per change.
- **Gate-to-change linkage**: which gate runs covered which change, with results.
- **Git survival** over [`kept_window`](../../reference/parameters.md#kept_window), with immature changes reported unassessed.
- **Stable attribution across model switches**, including work finished on premium after a lighter failure.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- A Sonnet session passing its Stop gate and kept fourteen days is recognized; Haiku work without gates that is reverted is rejected.
- Pinned lighter-subagent work passing CI and kept is recognized; lighter failures finished by the person on Opus are rejected.
- Immature or unavailable survival evidence is unassessed, not failed.
- A guided trial without later passing and kept evidence does not complete the pattern.
- No savings estimate is shown as evidence of kept work.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- What is the reference tier for "lighter"?
  - evidence: The spec leaves the reference tier and routine work beyond the example list unresolved unless documented CLI contracts settle them; none does at `bdea6f6`.
  - options: Lighter than the person's usual model (as in Right-size it); lighter than the most capable model available to the person; leave unassessed until the CLI supplies tiers.
  - location: core/patterns/harness-carries-it/definition.md / Applicable work
