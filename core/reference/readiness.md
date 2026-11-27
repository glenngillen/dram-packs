# Readiness

One row per catalogue pattern, in group and rung order. The terms are defined in [authoring and readiness](authoring.md#readiness-vocabulary): **authored**, **structurally valid**, **evaluable**, **preview**, **stable**. Each is a separate claim. Every pattern in this delivery is **disabled**; none is preview or stable.

Status as of the checks recorded in [compatibility](compatibility.md#checks-run) (pinned CLI `bdea6f6`, 2026-11-27). "Structurally valid" means `dram pack validate` accepted the pack with the pattern in it; it is not an evaluation. "Not evaluable" means `dram pack eval` reported every case unevaluable, so the pack-level eval verdict is red by design.

The eight code-checked patterns named as the first activation candidates are Give it instructions, Mind the cache, Gate "done", Gate each step, Keep secrets out, Scope permissions, Guard destructive commands and Isolate the run. Each still needs its missing capabilities and the evaluation bar before it can be enabled.

| Source ID | Pattern | Group | Rung | Status |
| --- | --- | --- | --- | --- |
| `brief-it` | [Brief It](../patterns/brief-it/definition.md) | Briefing | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `define-done` | [Define Done](../patterns/define-done/definition.md) | Briefing | 2 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `plan-first` | [Plan First](../patterns/plan-first/definition.md) | Briefing | 3 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `own-the-expectations` | [Set the Expectations Yourself](../patterns/own-the-expectations/definition.md) | Briefing | 4 | Authored; structurally valid; not evaluable (12 of 12 cases unevaluable); disabled |
| `give-it-instructions` | [Give It Instructions](../patterns/give-it-instructions/definition.md) | Guides | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `write-it-down` | [Write It Down](../patterns/write-it-down/definition.md) | Guides | 2 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `keep-it-lean` | [Keep It Lean](../patterns/keep-it-lean/definition.md) | Guides | 3 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `save-it` | [Save It](../patterns/save-it/definition.md) | Guides | 4 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `script-it` | [Script It](../patterns/script-it/definition.md) | Guides | 5 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `reuse-your-harness` | [Reuse Your Harness](../patterns/reuse-your-harness/definition.md) | Guides | 6 | Authored; structurally valid; not evaluable (12 of 12 cases unevaluable); disabled |
| `fix-the-harness` | [Fix the Harness](../patterns/fix-the-harness/definition.md) | Guides | 7 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `clear-between-tasks` | [Clear Between Tasks](../patterns/clear-between-tasks/definition.md) | Context | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `hand-it-off` | [Hand It Off](../patterns/hand-it-off/definition.md) | Context | 2 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `point-dont-paste` | [Point, Don't Paste](../patterns/point-dont-paste/definition.md) | Context | 3 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `prove-it` | [Prove It](../patterns/prove-it/definition.md) | Checking the work | 1 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `evidence-not-claims` | [Evidence, Not Claims](../patterns/evidence-not-claims/definition.md) | Checking the work | 2 | Authored; structurally valid; not evaluable (17 of 17 cases unevaluable); disabled |
| `checks-by-default` | [Checks by Default](../patterns/checks-by-default/definition.md) | Checking the work | 3 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `actionable-failures` | [Make Failures Actionable](../patterns/actionable-failures/definition.md) | Checking the work | 4 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `gate-done` | [Gate "done"](../patterns/gate-done/definition.md) | Checking the work | 5 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `gate-each-step` | [Gate Each Step](../patterns/gate-each-step/definition.md) | Checking the work | 6 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `back-it-up-in-ci` | [Back It Up in CI](../patterns/back-it-up-in-ci/definition.md) | Checking the work | 7 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `second-opinion` | [Second Opinion](../patterns/second-opinion/definition.md) | Checking the work | 8 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `test-behaviour` | [Test Behaviour](../patterns/test-behaviour/definition.md) | Checking the work | 9 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `schedule-the-clean-up` | [Schedule the Clean-up](../patterns/schedule-the-clean-up/definition.md) | Checking the work | 10 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `learn-from-production` | [Learn From Production](../patterns/learn-from-production/definition.md) | Checking the work | 11 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `steer` | [Steer, Don't Stop](../patterns/steer/definition.md) | Correcting course | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `set-checkpoints` | [Set Checkpoints](../patterns/set-checkpoints/definition.md) | Correcting course | 2 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `size-it` | [Size It](../patterns/size-it/definition.md) | Delegation | 1 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `split-it-up` | [Split It Up](../patterns/split-it-up/definition.md) | Delegation | 2 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `fan-out` | [Fan Out](../patterns/fan-out/definition.md) | Delegation | 3 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `hands-off` | [Hands Off](../patterns/hands-off/definition.md) | Delegation | 4 | Authored; structurally valid; not evaluable (17 of 17 cases unevaluable); disabled |
| `isolate-the-run` | [Isolate the Run](../patterns/isolate-the-run/definition.md) | Delegation | 5 | Authored; structurally valid; not evaluable (18 of 18 cases unevaluable); disabled |
| `two-at-once` | [Two at Once](../patterns/two-at-once/definition.md) | Delegation | 6 | Authored; structurally valid; not evaluable (20 of 20 cases unevaluable); disabled |
| `right-size-it` | [Right-size It](../patterns/right-size-it/definition.md) | Economics | 1 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `mind-the-cache` | [Mind the Cache](../patterns/mind-the-cache/definition.md) | Economics | 2 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `harness-carries-it` | [Let the Harness Carry It](../patterns/harness-carries-it/definition.md) | Economics | 3 | Authored; structurally valid; not evaluable (14 of 14 cases unevaluable); disabled |
| `right-cadence` | [Check at the Right Cadence](../patterns/right-cadence/definition.md) | Economics | 4 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `keep-secrets-out` | [Keep Secrets Out](../patterns/keep-secrets-out/definition.md) | Safety | 1 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `scope-permissions` | [Scope Permissions](../patterns/scope-permissions/definition.md) | Safety | 2 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
| `guard-destructive` | [Guard Destructive Commands](../patterns/guard-destructive/definition.md) | Safety | 3 | Authored; structurally valid; not evaluable (13 of 13 cases unevaluable); disabled |
| `sandbox-autonomy` | [Sandbox Autonomy](../patterns/sandbox-autonomy/definition.md) | Safety | 4 | Authored; structurally valid; not evaluable (15 of 15 cases unevaluable); disabled |
