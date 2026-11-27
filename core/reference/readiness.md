# Readiness

One row per catalogue pattern, in group and rung order. The terms are defined in [authoring and readiness](authoring.md#readiness-vocabulary): **authored**, **structurally valid**, **evaluable**, **preview**, **stable**. Each is a separate claim. Every pattern in this delivery is **disabled**; none is preview or stable.

## Versions and evidence

| Item | Value |
| --- | --- |
| Pack | `glenngillen/core` 0.1.0, `channel: dev`, no `min_cli` (see [compatibility](compatibility.md#min_cli)) |
| Pattern versions | `version: 1` for all 41 (the Version column below) |
| CLI | Dram at `bdea6f678399b3684519d41cc65645b4a42d53ef`, built locally (`dram dev`); no tagged release contains the pack loader |
| Evaluation date | 2026-11-27 |
| Commands and results | [Compatibility: checks run](compatibility.md#checks-run). `dram pack eval core`: 0 passed, 0 failed, 0 errors, 607 unevaluable; exit 1 (red) |
| Pack-wide rejection scenarios | 8 in [verification scenarios](verification.md), all unevaluable at the pinned CLI |

"Structurally valid" means `dram pack validate` accepted the pack with the pattern in it; it is not an evaluation. "Not evaluable" means `dram pack eval` reported every case unevaluable, so the pack-level eval verdict is red by design. Each pattern's `definition.md` names why it is disabled, its missing capabilities and what must be verified before enabling it.

## Patterns

| Source ID | Pattern | Group | Rung | Version | Status |
| --- | --- | --- | --- | --- | --- |
| `brief-it` | [Brief It](../patterns/brief-it/definition.md) | Briefing | 1 | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `define-done` | [Define Done](../patterns/define-done/definition.md) | Briefing | 2 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `plan-first` | [Plan First](../patterns/plan-first/definition.md) | Briefing | 3 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `own-the-expectations` | [Set the Expectations Yourself](../patterns/own-the-expectations/definition.md) | Briefing | 4 | 1 | Authored; structurally valid; not evaluable (12 of 12 cases unevaluable); disabled |
| `give-it-instructions` | [Give It Instructions](../patterns/give-it-instructions/definition.md) | Guides | 1 | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `write-it-down` | [Write It Down](../patterns/write-it-down/definition.md) | Guides | 2 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `keep-it-lean` | [Keep It Lean](../patterns/keep-it-lean/definition.md) | Guides | 3 | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `save-it` | [Save It](../patterns/save-it/definition.md) | Guides | 4 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `script-it` | [Script It](../patterns/script-it/definition.md) | Guides | 5 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `reuse-your-harness` | [Reuse Your Harness](../patterns/reuse-your-harness/definition.md) | Guides | 6 | 1 | Authored; structurally valid; not evaluable (12 of 12 cases unevaluable); disabled |
| `fix-the-harness` | [Fix the Harness](../patterns/fix-the-harness/definition.md) | Guides | 7 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `clear-between-tasks` | [Clear Between Tasks](../patterns/clear-between-tasks/definition.md) | Context | 1 | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `hand-it-off` | [Hand It Off](../patterns/hand-it-off/definition.md) | Context | 2 | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `point-dont-paste` | [Point, Don't Paste](../patterns/point-dont-paste/definition.md) | Context | 3 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `prove-it` | [Prove It](../patterns/prove-it/definition.md) | Checking the work | 1 | 1 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `evidence-not-claims` | [Evidence, Not Claims](../patterns/evidence-not-claims/definition.md) | Checking the work | 2 | 1 | Authored; structurally valid; not evaluable (17 of 17 cases unevaluable); disabled |
| `checks-by-default` | [Checks by Default](../patterns/checks-by-default/definition.md) | Checking the work | 3 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `actionable-failures` | [Make Failures Actionable](../patterns/actionable-failures/definition.md) | Checking the work | 4 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `gate-done` | [Gate "done"](../patterns/gate-done/definition.md) | Checking the work | 5 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `gate-each-step` | [Gate Each Step](../patterns/gate-each-step/definition.md) | Checking the work | 6 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `back-it-up-in-ci` | [Back It Up in CI](../patterns/back-it-up-in-ci/definition.md) | Checking the work | 7 | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `second-opinion` | [Second Opinion](../patterns/second-opinion/definition.md) | Checking the work | 8 | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `test-behaviour` | [Test Behaviour](../patterns/test-behaviour/definition.md) | Checking the work | 9 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `schedule-the-clean-up` | [Schedule the Clean-up](../patterns/schedule-the-clean-up/definition.md) | Checking the work | 10 | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `learn-from-production` | [Learn From Production](../patterns/learn-from-production/definition.md) | Checking the work | 11 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `steer` | [Steer, Don't Stop](../patterns/steer/definition.md) | Correcting course | 1 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `set-checkpoints` | [Set Checkpoints](../patterns/set-checkpoints/definition.md) | Correcting course | 2 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `size-it` | [Size It](../patterns/size-it/definition.md) | Delegation | 1 | 1 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `split-it-up` | [Split It Up](../patterns/split-it-up/definition.md) | Delegation | 2 | 1 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `fan-out` | [Fan Out](../patterns/fan-out/definition.md) | Delegation | 3 | 1 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `hands-off` | [Hands Off](../patterns/hands-off/definition.md) | Delegation | 4 | 1 | Authored; structurally valid; not evaluable (17 of 17 cases unevaluable); disabled |
| `isolate-the-run` | [Isolate the Run](../patterns/isolate-the-run/definition.md) | Delegation | 5 | 1 | Authored; structurally valid; not evaluable (18 of 18 cases unevaluable); disabled |
| `two-at-once` | [Two at Once](../patterns/two-at-once/definition.md) | Delegation | 6 | 1 | Authored; structurally valid; not evaluable (20 of 20 cases unevaluable); disabled |
| `right-size-it` | [Right-size It](../patterns/right-size-it/definition.md) | Economics | 1 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `mind-the-cache` | [Mind the Cache](../patterns/mind-the-cache/definition.md) | Economics | 2 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `harness-carries-it` | [Let the Harness Carry It](../patterns/harness-carries-it/definition.md) | Economics | 3 | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `right-cadence` | [Check at the Right Cadence](../patterns/right-cadence/definition.md) | Economics | 4 | 1 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `keep-secrets-out` | [Keep Secrets Out](../patterns/keep-secrets-out/definition.md) | Safety | 1 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `scope-permissions` | [Scope Permissions](../patterns/scope-permissions/definition.md) | Safety | 2 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `guard-destructive` | [Guard Destructive Commands](../patterns/guard-destructive/definition.md) | Safety | 3 | 1 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `sandbox-autonomy` | [Sandbox Autonomy](../patterns/sandbox-autonomy/definition.md) | Safety | 4 | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |

## First activation candidates (future work)

The Infracost Notion page "cli-ai initial implementation" (recorded in this repository's `specs/requirements-evidence.md`) names eight code-checked patterns as the first to enable once their checks are supported. None is enabled here; each still needs the capabilities its definition lists and the evaluation bar below.

| Source ID | Still needed before Preview |
| --- | --- |
| `give-it-instructions` | Per-session instruction load evidence and provenance, per-repository session counts, file history, a confirmed non-trivial rule, and a runnable gate; [definition](../patterns/give-it-instructions/definition.md#missing-capabilities) |
| `mind-the-cache` | Gap and context facts per return (including cache lifetime), session-start provenance, return pairing, cost reuse, mechanism attribution; [definition](../patterns/mind-the-cache/definition.md#missing-capabilities) |
| `gate-done` | Hook execution records, enforcement behaviour, check classification, configuration attribution and history, repository coverage; [definition](../patterns/gate-done/definition.md#missing-capabilities) |
| `gate-each-step` | Hook and pre-commit run records with durations, blocking and feedback, bypass detection, check classification, attribution and coverage; [definition](../patterns/gate-each-step/definition.md#missing-capabilities) |
| `keep-secrets-out` | Effective settings per session, local secret-location facts, file-access records, local redaction findings, configuration history; [definition](../patterns/keep-secrets-out/definition.md#missing-capabilities) |
| `scope-permissions` | Effective settings precedence, allow-list semantics, permission mode, run-type attribution, sandbox classification, repository risk facts; [definition](../patterns/scope-permissions/definition.md#missing-capabilities) |
| `guard-destructive` | Effective enforcement per mode, destructive-command coverage, invocation and approval records, run-type attribution, configuration history; [definition](../patterns/guard-destructive/definition.md#missing-capabilities) |
| `isolate-the-run` | Historical working-copy facts per session, active-overlap detection, unattended classification, launch attribution; [definition](../patterns/isolate-the-run/definition.md#missing-capabilities) |

The second column abbreviates each definition's missing capabilities; the linked section is authoritative. Every candidate also needs mechanism evaluation, since nothing reaches the `continuous` stage in the pinned build.

## Stable-quality bars (future work)

Retained from the evaluation-readiness requirements. **None has been attempted**: no staff evaluation, field result or model run has happened for any pattern, and no metric here is measured.

| Area | Required evidence |
| --- | --- |
| Copy | Intent, report, coach and guide wording reviewed |
| Guides | Three of three staff users perform the pattern in their real work and receive recognition |
| Model evaluation | Every catalogue case plus at least ten additional staff-history cases labeled by two reviewers; all correct in three runs on the quick model |
| Recognition precision | At most one false recognition among twenty reviewed recognitions (at least 95%) |
| Recognition recall | At least seven of ten deliberately performed instances (at least 70%) |
| Opportunities | At least seventeen of twenty opportunities judged useful; noisy opportunities permit Seen only until fixed |
| Verification | Fabricated/changed quotes, inappropriate attribution and out-of-window evidence rejected |
| Cost | Pattern share of the pass fits the budget at the ninetieth percentile; measure, do not assume |
| Held cases | At least eighteen of twenty applicable held cases correct; every recurrence fixture produces not holding |
| Case advice | At least eighteen of twenty misses have case-specific next-time and preventive advice with a faithful setup prompt |
| Code fixtures | Every evaluable configuration/transcript case correct, without a passing average masking a failure |
| Real configurations | Runs without errors on staff machines; agreement on every result in a sample of twenty |

Preview needs every applicable recognition case for the pattern to run and pass on the pinned CLI first; Stable additionally needs every row above.

## Copy review

**Performed** (2026-11-27, by the building agent, not the owner):

- Automated, all 41 patterns, enforced by `tests/content/`: each guide says detection is not available and that finishing it will not show a recognition; each has a **Done:** step that needs the person's own action on real work, a **Not done yet:** branch, and a stop-when-not-applicable exit; no guide or `text.yaml` offers a destructive copy-paste command (`rm -rf`, `reset --hard`, forced push, permission-skip flags, approve-all); `text.yaml` uses no scoring, ranking, streak, productivity, time-saved or guarantee wording; runtime placeholders are only the supported ones.
- Safety prerequisites checked as required phrases: Hands off (narrowly scoped unattended permissions, never switch checks off), Two at once (separate working copy, Isolate the run first), Fan out (keep permission prompts), Sandbox autonomy (approvals stay on), Schedule the clean-up (no permission bypass), Guard destructive commands (never provoke the guard).
- Every mention of bypassing permissions in guides and copy was read in context (13 lines across 6 patterns): all are cautions or descriptions of a not-holding case, none an instruction.
- Read in full: the Save it and Guard destructive commands guides (real tasks chosen by the person, no manufactured code, explicit stop branches, no destructive testing).

**Outstanding**: owner review of all 41 patterns' intent, report, coach and guide wording, which is the Copy row of the stable bars. Drafting and automated checks are not that review. Applicable semantic decisions (see below) are part of it.

## Unresolved dependencies

- **CLI release**: no tagged Dram release contains the pack loader, so `min_cli` is absent and the pinned revision is the only compatibility evidence.
- **Pattern recognizer**: the pinned CLI runs no pack-authored judge; only `tool_call_matches` and `tool_call_sequence` run as fixed checks. Every pattern needs capabilities the CLI lacks (listed in its definition).
- **Verifier**: no recognition verifier for citations, quotes, attribution or windows (see [verification scenarios](verification.md)).
- **Attribution of held cases**: whether a held case must cite the originating configuration is undecided ([evidence](evidence.md#attribution-and-citations)).
- **Progression and outcomes**: stages, the automation gate and the five outcome measures are prose only; the CLI has milestones and no implemented outcome measures.
- **Host support**: guide launching, guided-session markers, personalised case rendering and fix-prompt wrappers are host features outside this pack.
- **Publication and signing**: the pack is not published to a registry or signed; registry installation has not been verified (see the repository README).

## Open questions

- Which per-pattern semantic decisions does the owner want settled before the first activation candidate is implemented?
  - evidence: Classification questions (non-trivial instruction files, routine work, meaningful configuration refresh, repeated-correction equivalence) are recorded as pending in `specs/requirements-evidence.md` and in each affected definition.
  - options: Settle them during owner copy review; settle them per pattern when its capability lands.
  - location: core/reference/readiness.md / Copy review
