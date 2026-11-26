# Specifications: architecture overview and index

This repository holds the declarative **`glenngillen/core`** Dram pack: 41 evidence-based coaching patterns about how a person uses coding agents, in eight ordered groups. It contains pack content and local authoring tools only. The Dram CLI, its loader, detectors, evaluator, recommendation engine, signing and publishing live elsewhere and are external dependencies.

The specifications in this directory are the authoritative requirements. This page describes how the repository is laid out and links every specification.

## Pack content versus CLI capability

Keep these two things apart in every document, test and status report.

| This repository provides | The Dram CLI provides (external, not changed here) |
| --- | --- |
| Pattern definitions, exclusions, evidence requirements and mechanism prose | Loading and schema validation of packs (`internal/pack`) |
| Coaching copy (`text.yaml`), guides (`guide.md`) and model-judge authoring prompts (`judge.md`) | Executing code checks; at the inspected revision only `tool_call_matches` and `tool_call_sequence` run, and only `tool_call_matches` works as a gate |
| Synthetic evaluation scenarios (`eval/cases.jsonl`) and prose for scenarios the evaluator cannot express | Running evaluations and producing pass/fail/unevaluable verdicts |
| Disabled-by-default pattern entries with documented missing capabilities | Packet assembly, attribution, verification, stages, outcomes, recommendations |
| Local structural checks (file shape, references, catalogue coverage) | Any claim that a pattern is recognized in real work |

A pattern that is authored and structurally valid is **not** a working detector. Content lint in this repository never produces an evaluation verdict. See [pack compatibility](pack-compatibility.md) and [evaluation readiness](evaluation-readiness.md).

## Repository layout

| Path | Status | Purpose |
| --- | --- | --- |
| `specs/` | Present | Requirements (this directory). |
| `dram.yaml` | Proposed | Repository index; its ID must equal the manifest ID `glenngillen/core`. |
| `core/pack.yaml`, `core/groups.yaml` | Proposed | Pack manifest and the eight groups in catalogue order. |
| `core/patterns/<source-id>/` | Proposed | `pattern.yaml`, `text.yaml`, `guide.md`, `eval/cases.jsonl`, and `judge.md` for model-judged patterns. Pattern IDs are `glenngillen/<source-id>`. |
| `core/` reference Markdown | Proposed | Shared evidence, progression, parameter and outcome contracts that each pattern links to. |
| `tools/dram_pack_tools/` | Present | Python authoring helpers: strict YAML/JSONL readers, contained-reference and tree-hygiene checks, JSON Schema diagnostics, catalogue coverage. Never shipped inside `core/`. |
| `tools/catalogue.yaml` | Present | The 41 source IDs in group and rung order, plus the `require_complete` switch for incremental coverage. |
| `tests/unit/` | Present | Pure tests of the tools against synthetic temporary trees. |
| `tests/content/` | Present | Read-only structural checks of this repository's real content. |
| `scripts/run-tests.sh` | Present | Runs both test tiers through `uv`. |

The `core/` files follow the current Dram conventions recorded in [requirements evidence](requirements-evidence.md). Creating them is blocked until a pinned schema, block registry, loader and evaluator contract and a runnable released CLI are available inside this repository; no schema is invented in the meantime.

### Authoring tools and tests

- Readers reject duplicate YAML keys, multiple documents, unsafe tags, invalid UTF-8, blank or non-object JSONL lines, duplicate JSON keys and non-standard JSON constants, reporting file, line and column.
- References must be non-empty relative POSIX paths that stay inside the pack root, pass through no symlink and name an existing file. Packaged trees may contain no symlinks and no executable files.
- Catalogue coverage counts a pattern as authored once `core/patterns/<id>/pattern.yaml` exists. While `require_complete` is `false`, pending IDs are printed at the end of every test run; unknown pattern directories always fail. The complete-catalogue slice sets `require_complete: true`, making all 41 mandatory.
- Content tests also confirm that each catalogue ID has a matching spec with the same source ID, group and rung.

## Shared requirements

| Spec | Topic |
| --- | --- |
| [Core catalogue](core-catalogue.md) | Scope: 41 patterns, eight groups, content-only delivery, no scoring. |
| [Pack compatibility](pack-compatibility.md) | Loader conventions, `glenngillen/*` identity, disabled baseline, supported blocks and placeholders. |
| [Pattern evidence](pattern-evidence.md) | Attribution, person-authored citations, opportunities, mechanisms in place/applied/held, privacy. |
| [Pattern progression](pattern-progression.md) | Seen, Forming, Established, Continuous; stage-dependent completion; automation gate. |
| [Pattern parameters](pattern-parameters.md) | Provisional, tunable defaults that definitions depend on. |
| [Coaching content](coaching-content.md) | Copy wording and one guide per pattern. |
| [Outcome content](outcome-content.md) | The five intended quality measures and group associations. |
| [Evaluation readiness](evaluation-readiness.md) | Authored vs. evaluable vs. preview vs. stable, and the stable-quality bars. |
| [Requirements evidence](requirements-evidence.md) | Source record: production spec, user decisions, inspected CLI revision, example pack. |

## Pattern catalogue

Source IDs equal spec file names. Order within a group is the rung order.

### Briefing

| Rung | Source ID | Spec |
| --- | --- | --- |
| 1 | `brief-it` | [Brief It](brief-it.md) |
| 2 | `define-done` | [Define Done](define-done.md) |
| 3 | `plan-first` | [Plan First](plan-first.md) |
| 4 | `own-the-expectations` | [Set the Expectations Yourself](own-the-expectations.md) |

### Guides

| Rung | Source ID | Spec |
| --- | --- | --- |
| 1 | `give-it-instructions` | [Give It Instructions](give-it-instructions.md) |
| 2 | `write-it-down` | [Write It Down](write-it-down.md) |
| 3 | `keep-it-lean` | [Keep It Lean](keep-it-lean.md) |
| 4 | `save-it` | [Save It](save-it.md) |
| 5 | `script-it` | [Script It](script-it.md) |
| 6 | `reuse-your-harness` | [Reuse Your Harness](reuse-your-harness.md) |
| 7 | `fix-the-harness` | [Fix the Harness](fix-the-harness.md) |

### Context

| Rung | Source ID | Spec |
| --- | --- | --- |
| 1 | `clear-between-tasks` | [Clear Between Tasks](clear-between-tasks.md) |
| 2 | `hand-it-off` | [Hand It Off](hand-it-off.md) |
| 3 | `point-dont-paste` | [Point, Don't Paste](point-dont-paste.md) |

### Checking the work

| Rung | Source ID | Spec |
| --- | --- | --- |
| 1 | `prove-it` | [Prove It](prove-it.md) |
| 2 | `evidence-not-claims` | [Evidence, Not Claims](evidence-not-claims.md) |
| 3 | `checks-by-default` | [Checks by Default](checks-by-default.md) |
| 4 | `actionable-failures` | [Make Failures Actionable](actionable-failures.md) |
| 5 | `gate-done` | [Gate "done"](gate-done.md) |
| 6 | `gate-each-step` | [Gate Each Step](gate-each-step.md) |
| 7 | `back-it-up-in-ci` | [Back It Up in CI](back-it-up-in-ci.md) |
| 8 | `second-opinion` | [Second Opinion](second-opinion.md) |
| 9 | `test-behaviour` | [Test Behaviour](test-behaviour.md) |
| 10 | `schedule-the-clean-up` | [Schedule the Clean-up](schedule-the-clean-up.md) |
| 11 | `learn-from-production` | [Learn From Production](learn-from-production.md) |

### Correcting course

| Rung | Source ID | Spec |
| --- | --- | --- |
| 1 | `steer` | [Steer, Don't Stop](steer.md) |
| 2 | `set-checkpoints` | [Set Checkpoints](set-checkpoints.md) |

### Delegation

| Rung | Source ID | Spec |
| --- | --- | --- |
| 1 | `size-it` | [Size It](size-it.md) |
| 2 | `split-it-up` | [Split It Up](split-it-up.md) |
| 3 | `fan-out` | [Fan Out](fan-out.md) |
| 4 | `hands-off` | [Hands Off](hands-off.md) |
| 5 | `isolate-the-run` | [Isolate the Run](isolate-the-run.md) |
| 6 | `two-at-once` | [Two at Once](two-at-once.md) |

### Economics

| Rung | Source ID | Spec |
| --- | --- | --- |
| 1 | `right-size-it` | [Right-size It](right-size-it.md) |
| 2 | `mind-the-cache` | [Mind the Cache](mind-the-cache.md) |
| 3 | `harness-carries-it` | [Let the Harness Carry It](harness-carries-it.md) |
| 4 | `right-cadence` | [Check at the Right Cadence](right-cadence.md) |

### Safety

| Rung | Source ID | Spec |
| --- | --- | --- |
| 1 | `keep-secrets-out` | [Keep Secrets Out](keep-secrets-out.md) |
| 2 | `scope-permissions` | [Scope Permissions](scope-permissions.md) |
| 3 | `guard-destructive` | [Guard Destructive Commands](guard-destructive.md) |
| 4 | `sandbox-autonomy` | [Sandbox Autonomy](sandbox-autonomy.md) |

## Source evidence

[Requirements evidence](requirements-evidence.md) records every source relied on: the user-supplied production specification, the pack-content-only scope decision and later user decisions, the inspected Dram CLI revision and what it supports, the example community pack layout and the internal implementation note naming the eight first activation candidates. Treat that record as the basis for compatibility claims and recheck it against the pinned CLI before enabling any detector.

## Open questions

- Which released Dram CLI version should be the pack's `min_cli`, and which revision is pinned for compatibility?
  - evidence: The inspected CLI revision is recorded in requirements evidence, but no released version or runnable CLI is available in this repository; a `dev` build bypasses version refusal.
  - options: Supply a pinned schema/loader/evaluator bundle and a verified release; keep the compatible-baseline slice blocked until then.
  - location: specs/README.md / Repository layout
