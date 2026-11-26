# Readiness

One row per catalogue pattern, in group and rung order. The terms are defined in [authoring and readiness](authoring.md#readiness-vocabulary): **authored**, **structurally valid**, **evaluable**, **preview**, **stable**. Each is a separate claim. Every pattern in this delivery is **disabled**; none is preview or stable.

Status as of the checks recorded in [compatibility](compatibility.md#checks-run) (pinned CLI `bdea6f6`, 2026-11-27). "Structurally valid" means `dram pack validate` accepted the pack with the pattern in it; it is not an evaluation. "Not evaluable" means `dram pack eval` reported every case unevaluable, so the pack-level eval verdict is red by design.

The eight code-checked patterns named as the first activation candidates are Give it instructions, Mind the cache, Gate "done", Gate each step, Keep secrets out, Scope permissions, Guard destructive commands and Isolate the run. Each still needs its missing capabilities and the evaluation bar before it can be enabled.

| Source ID | Pattern | Group | Rung | Status |
| --- | --- | --- | --- | --- |
| `brief-it` | Brief It | Briefing | 1 | Pending: not authored |
| `define-done` | Define Done | Briefing | 2 | Pending: not authored |
| `plan-first` | Plan First | Briefing | 3 | Pending: not authored |
| `own-the-expectations` | Set the Expectations Yourself | Briefing | 4 | Pending: not authored |
| `give-it-instructions` | [Give It Instructions](../patterns/give-it-instructions/definition.md) | Guides | 1 | Authored; structurally valid; not evaluable (16 of 16 cases unevaluable); disabled |
| `write-it-down` | Write It Down | Guides | 2 | Pending: not authored |
| `keep-it-lean` | Keep It Lean | Guides | 3 | Pending: not authored |
| `save-it` | Save It | Guides | 4 | Pending: not authored |
| `script-it` | Script It | Guides | 5 | Pending: not authored |
| `reuse-your-harness` | Reuse Your Harness | Guides | 6 | Pending: not authored |
| `fix-the-harness` | Fix the Harness | Guides | 7 | Pending: not authored |
| `clear-between-tasks` | Clear Between Tasks | Context | 1 | Pending: not authored |
| `hand-it-off` | Hand It Off | Context | 2 | Pending: not authored |
| `point-dont-paste` | Point, Don't Paste | Context | 3 | Pending: not authored |
| `prove-it` | Prove It | Checking the work | 1 | Pending: not authored |
| `evidence-not-claims` | Evidence, Not Claims | Checking the work | 2 | Pending: not authored |
| `checks-by-default` | Checks by Default | Checking the work | 3 | Pending: not authored |
| `actionable-failures` | Make Failures Actionable | Checking the work | 4 | Pending: not authored |
| `gate-done` | Gate "done" | Checking the work | 5 | Pending: not authored |
| `gate-each-step` | Gate Each Step | Checking the work | 6 | Pending: not authored |
| `back-it-up-in-ci` | Back It Up in CI | Checking the work | 7 | Pending: not authored |
| `second-opinion` | Second Opinion | Checking the work | 8 | Pending: not authored |
| `test-behaviour` | Test Behaviour | Checking the work | 9 | Pending: not authored |
| `schedule-the-clean-up` | Schedule the Clean-up | Checking the work | 10 | Pending: not authored |
| `learn-from-production` | Learn From Production | Checking the work | 11 | Pending: not authored |
| `steer` | Steer, Don't Stop | Correcting course | 1 | Pending: not authored |
| `set-checkpoints` | Set Checkpoints | Correcting course | 2 | Pending: not authored |
| `size-it` | Size It | Delegation | 1 | Pending: not authored |
| `split-it-up` | Split It Up | Delegation | 2 | Pending: not authored |
| `fan-out` | Fan Out | Delegation | 3 | Pending: not authored |
| `hands-off` | Hands Off | Delegation | 4 | Pending: not authored |
| `isolate-the-run` | Isolate the Run | Delegation | 5 | Pending: not authored |
| `two-at-once` | Two at Once | Delegation | 6 | Pending: not authored |
| `right-size-it` | Right-size It | Economics | 1 | Pending: not authored |
| `mind-the-cache` | Mind the Cache | Economics | 2 | Pending: not authored |
| `harness-carries-it` | Let the Harness Carry It | Economics | 3 | Pending: not authored |
| `right-cadence` | Check at the Right Cadence | Economics | 4 | Pending: not authored |
| `keep-secrets-out` | Keep Secrets Out | Safety | 1 | Pending: not authored |
| `scope-permissions` | Scope Permissions | Safety | 2 | Pending: not authored |
| `guard-destructive` | Guard Destructive Commands | Safety | 3 | Pending: not authored |
| `sandbox-autonomy` | Sandbox Autonomy | Safety | 4 | Pending: not authored |
