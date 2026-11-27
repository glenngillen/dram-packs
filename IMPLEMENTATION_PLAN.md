## Summary

Build the declarative `glenngillen/core` Dram pack containing all 41 coaching patterns in eight ordered groups, with complete recognition definitions, evidence requirements, coaching copy, guides and synthetic evaluation scenarios. Add repository authoring and validation tooling, preserve unsupported semantics in prose, and ship an explicitly disabled content baseline with honest installation and readiness documentation. CLI implementation, detector activation, publishing and field evaluation are outside this delivery.

## Relevant Specs
- core-catalogue.md
- pack-compatibility.md
- requirements-evidence.md
- pattern-evidence.md
- pattern-progression.md
- pattern-parameters.md
- coaching-content.md
- outcome-content.md
- evaluation-readiness.md
- brief-it.md
- define-done.md
- plan-first.md
- own-the-expectations.md
- give-it-instructions.md
- write-it-down.md
- keep-it-lean.md
- save-it.md
- script-it.md
- reuse-your-harness.md
- fix-the-harness.md
- clear-between-tasks.md
- hand-it-off.md
- point-dont-paste.md
- prove-it.md
- evidence-not-claims.md
- checks-by-default.md
- actionable-failures.md
- gate-done.md
- gate-each-step.md
- back-it-up-in-ci.md
- second-opinion.md
- test-behaviour.md
- schedule-the-clean-up.md
- learn-from-production.md
- steer.md
- set-checkpoints.md
- size-it.md
- split-it-up.md
- fan-out.md
- hands-off.md
- isolate-the-run.md
- two-at-once.md
- right-size-it.md
- mind-the-cache.md
- harness-carries-it.md
- right-cadence.md
- keep-secrets-out.md
- scope-permissions.md
- guard-destructive.md
- sandbox-autonomy.md

## Tasks

### Foundation

- [x] Set up project infrastructure for declarative packs and Python authoring tools.
  - Add `pyproject.toml` and reproducible development dependency constraints for YAML parsing, JSON Schema validation and pytest; keep tooling outside the packaged `core/` tree.
  - Preserve the license and existing specs. Document local environment setup without adding a CLI application, executable detector or deployment workflow.

- [x] Configure pytest around safe local pack-content validation.
  - Provide reusable readers and synthetic temporary fixtures for YAML/JSONL diagnostics, duplicate YAML keys, contained relative references, missing files and symlink rejection.
  - Test the validator's rejection behavior; do not invent Dram schema or fixture fields. Keep structural checks separate from detector evaluations and their verdicts.
  - Support explicitly tracked incremental catalogue coverage until final acceptance requires all 41; missing or pending content must remain visible rather than silently excluded.

- [x] Create specs/README.md with the architecture overview and topic index.
  - Index all 50 existing specifications, the eight groups, shared requirements and source evidence; describe the proposed root index, `core/` pack, authoring tools and tests.
  - Distinguish pack content from external CLI capabilities. Use topic-only kebab-case spec names and omit originating tracker identifiers and checkout paths from spec content.

### Shared authoring contract and compatible baseline

- [x] Document shared evidence, progression, parameter and outcome contracts inside the pack.
  - Add linked Markdown authoring references under `core/` for attribution, opportunities, completion windows, mechanisms in place/applied/held, privacy and insufficient evidence.
  - Keep every provisional parameter and its origin in one pack reference; patterns link to it. Preserve strict cache gap/context boundaries, inclusive coverage thresholds and pattern-specific overrides.
  - Preserve stage-dependent follow-through, guided Seen-only limits, the three-Continuous/two-group automation gate, safety prerequisites and next-step ordering as prose, not runtime fields.
  - Include all five outcomes and group mappings, including fourteen-day survival and seven-day rework; retain unresolved attribution, classification, stage-engine and outcome semantics explicitly.
  - Define a per-pattern authoring/scenario checklist and readiness vocabulary that separates authored, structurally valid, evaluable, preview and stable. Check links and parameter-reference consistency locally.

- [x] Establish a schema-valid disabled pack using Give it instructions as the complete reference pattern.
  - **Compatibility inputs (supplied by the issue):** read them from the Dram CLI checkout at `/Volumes/Development/infracost/dram`, pinned at `bdea6f678399b3684519d41cc65645b4a42d53ef`. Use `internal/pack/schema.json`, `blocks.json`, `registry.go`, `pack.go`, `set.go`, `schema.go`, `docs/pack-schema.md` and the built-in packs under `packs/iac` and `packs/recommend` as the schema, block registry, loader contract and fixtures. Build a runnable CLI from that checkout with `mkdir -p <worktree>/.tmp/gotmp && GOTMPDIR=<worktree>/.tmp/gotmp TMPDIR=<worktree>/.tmp/gotmp go build -buildvcs=false -o <worktree>/.tmp/dram ./cmd/dram` (the default temp dir is not writable for the loop user, and git VCS stamping fails on the checkout's ownership). Treat the checkout as read-only: never edit, commit to or clean it. Use [owenrumney/dram-packs](https://github.com/owenrumney/dram-packs) as the reference pack layout (`dram.yaml`, pack dir, `pattern.yaml` + `text.yaml`).
  - Record the pinned revision. Set `min_cli` to the earliest tagged Dram version (`v0.1.0-preview.4` or earlier) whose schema supports the fields used; if no tag supports them, use the pinned revision, record why, and keep going rather than blocking. Resolve any schema-required maintainer metadata without claiming official status.
  - Create `dram.yaml`, `core/pack.yaml`, `core/groups.yaml` and the first complete `core/patterns/give-it-instructions/` tree using supported fields and references. Preserve final catalogue ordering as subsequent patterns are added.
  - Supply `pattern.yaml` with `enabled: false`, `text.yaml`, `guide.md`, recognition/mechanism prose and evaluation scenarios; omit unsupported runtime bindings. Include `judge.md` only where model judgement is part of the intended definition.
  - Preserve the three-session applicability boundary, meaningful loaded instructions, auto-memory/template exclusions, coverage overrides and refresh dependency. Do not invent a byte-count definition of non-trivial content.
  - Add pinned-schema, block/parameter, placeholder and loader checks. Prove that disabled content is loadable without presenting it as an executable recognizer; retain precise reasons for unrepresentable or unevaluable cases.

### Pattern content

Every following slice delivers complete pattern directories, their synthetic scenarios and supported `cases.jsonl` entries, catalogue/readiness entries and focused validation together. Preserve every supplied positive and negative example, both guide outcomes, no-applicable-work and missing-evidence cases; mechanism patterns also need unused, held and not-holding scenarios. Keep unrepresentable scenarios fully described in Markdown with exact capability dependencies rather than inventing executable case fields or changing positives to `none`.

- [x] Author Brief it, Define done, Plan first and Set the expectations yourself.
  - Preserve meaningful person intent/review, criteria before implementation, actual checks and plan/edit ordering. Keep the unresolved first-edit boundary explicit.
  - Distinguish the brief's Seen event from later corroboration, and independent expectations from post-hoc implementation-mirroring tests.

- [x] Author Write it down and Keep it lean alongside the instruction reference pattern.
  - Require persisted attributable rules and later relevant use; distinguish in-place from held configuration.
  - Cite both contradictory lines or measured instruction cost, preserve wanted rules, and distinguish requested lean-up at Seen from fourteen-day kept follow-through. Retain the source's 12% illustration while testing the strict greater-than threshold separately.

- [x] Author Save it, Script it, Reuse your harness and Fix the harness.
  - Preserve ownership, actual invocation, different-day reuse, cross-repository identity and historical configuration; built-ins and third-party tools do not establish ownership.
  - Keep the ten-file coaching trigger separate from recognition. Require relevant follow-up for harness fixes and distinguish recurrence from insufficient later work.

- [x] Author Clear between tasks, Hand it off and Point, don't paste.
  - Separate clear, compaction, resume and genuinely fresh sessions; preserve six-person-prompt applicability and same-repository handoff pairing within 24 hours.
  - Require relevant pointers actually used, rather than filenames or paste-length heuristics; retain attribution and delayed corroboration dependencies.

- [x] Author Prove it, Evidence, not claims and Checks by default.
  - Separate a person's proof request, a warranted challenge and checks caused by an owned harness. Preserve historical rule application and edit/check ordering.
  - Distinguish execution from passing, challenge-issued Seen from addressed follow-through, and missing/truncated output from adverse evidence.

- [x] Author Make failures actionable, Gate "done" and Gate each step.
  - Require visible actionable feedback and linked fixes, effective final enforcement, or actual per-step blocking/feedback as specified; formatter-only, bypassed and unused hooks remain distinct negatives.
  - Preserve the provisional fast-check boundary and next-step/next-turn ambiguity; never reduce these definitions to hook presence or command matches.

- [x] Author Back it up in CI, Second opinion and Test behaviour.
  - Preserve linked CI run/merge evidence, reviewer independence and used findings, and observable behavior checks with person review and execution.
  - Cover direct pushes, docs-only CI, ignored review findings and unreviewed snapshot updates; distinguish review result at Seen from later action on findings.

- [x] Author Schedule the clean-up and Learn from production.
  - Require owned launch/trigger provenance and used maintenance output, or an actual supplied production signal plus a preventive regression check.
  - Keep all fixtures synthetic; guides neither fetch production data nor configure or launch external schedules automatically.

- [x] Author Steer, don't stop and Set checkpoints.
  - Separate explained redirects from bare interruptions and Seen from changed-course follow-through.
  - Require the requested stop and person decision; represent ask-rule semantics in prose where unsupported and cover unanswered or bypassed checkpoints.

- [x] Author Keep secrets out, Scope permissions, Guard destructive commands and Sandbox autonomy.
  - Preserve effective settings precedence, actual secret-location coverage, scoped unattended permissions and applicable guard enforcement; never inspect or reproduce real secret values.
  - Treat sandboxed permission bypass as neutral for Scope permissions, separate working-copy isolation from system containment, and leave unobservable credential-free hosts/separate users unassessed.
  - Cover unsafe passthrough, unknown environments and ineffective guards without asserting universal regex protection or container safety. Guides must not execute destructive commands to manufacture evidence.

- [x] Author Size it, Split it up and Fan out.
  - Preserve breakdown-plus-first-task Seen versus all-subtasks follow-through, own-agent/person-requested delegation, and three or more concurrent independent parts with used combined output.
  - Exclude unsolicited built-in delegation, sequential fan-out and discarded results; reference already-authored Safety prerequisites.

- [x] Author Hands off, Isolate the run and Two at once.
  - Preserve three interactive runs for applicability versus three sessions for coaching, unattended classification, owned workflow provenance and output use.
  - Require separate working copies, active paired edits and the five-minute waiting boundary; exclude branch-only separation, idle overlap and parent/subagent pairs.
  - Keep scoped unattended permission and isolation suggestion prerequisites explicit; do not encode unsupported stage/run scopes as weaker runtime requirements.

- [x] Author Right-size it, Mind the cache, Let the harness carry it and Check at the right cadence.
  - Separate intentional lower-tier selection from fallback and ordinary subagents; preserve the model-selection identity without reusing IaC sizing history.
  - Include both fresh returns and cold resumes in cache applicability, exact threshold boundaries and unknown usage/pricing inputs.
  - Require passing linked gates and mature fourteen-day survival for kept work; preserve the final gate and both observed model paths for differentiated cadence. Never invent savings or billing claims.

### Integration and hand-off

- [ ] Enforce complete catalogue and CLI compatibility acceptance.
  - Require exactly 41 unique qualified IDs in the eight groups and source order, complete content/scenario coverage, explicit disabled status, valid references, supported fields/blocks/placeholders and no packaged symlinks or executable detection code.
  - Extend integration coverage to load alongside the supplied built-in IaC and recommendation packs, including both right-size-it IDs, without replacing recommendation behavior.
  - Run local tooling checks and the pinned CLI's supported validation/evaluation commands during building only. Record actual pass/fail/unevaluable counts and precise capability reasons; do not patch the evaluator or hide its expected red verdict for unsupported recognition.
  - Verify rejection of fabricated citations, changed quotes, inappropriate attribution and out-of-window evidence wherever the pinned evaluator can express them; otherwise preserve those scenarios as explicitly unevaluable.

- [ ] Publish repository installation guidance and an evidence-backed readiness inventory.
  - Write the root README and compatibility/readiness notes with verified installation commands, pack/rule versions, CLI revision/release, evaluation date, actual commands/results and one status row per pattern.
  - Explain disabled content availability, schema validation, evaluability and activation separately; document unresolved dependencies and keep all 41 recognizers disabled for this delivery.
  - Review copy against the guides' real-work, positive-completion and no-action branches, safety prerequisites and prohibited scoring/savings claims. Record the review actually performed and any outstanding owner review.
  - Preserve all stable-quality bars and the eight first activation candidates from the requirements evidence as future work. Do not claim a runnable preview, stable release, field results, official signing or publication.

## Notes

- **Owner review after delivery (not a loop task):** once all 41 patterns are authored, the issue owner reviews final coaching copy and resolves applicable semantic decisions; private staff evaluation against the recorded stable-quality bars happens only when detectors are executable. Keep personal histories outside repository artifacts and retain only non-sensitive aggregate readiness evidence.
- **Execution boundary:** all writes, tooling output, fixtures and generated artifacts must remain inside this worktree. The Dram CLI checkout at `/Volumes/Development/infracost/dram` is authorized read-only (plus a `go build` whose output goes to this worktree's `.tmp/`) as the compatibility source; no other adjacent checkout, global configuration, private histories, external infrastructure operations or source deletion is authorized. Build/test commands belong to building, not planning.
- **Compatibility source:** the loader/schema/fixture sources and buildable CLI come from the read-only Dram checkout at `/Volumes/Development/infracost/dram` (pinned `bdea6f6`), with owenrumney/dram-packs as the layout reference. Nothing needs to be supplied by a human before the compatible-baseline slice. Do not fabricate a minimum version, maintainer, schema or successful check to advance the checklist.
- **Established evidence:** `specs/requirements-evidence.md` contains the source/tool/query/date/identifier records and concrete findings. Its inspected CLI revision is `bdea6f678399b3684519d41cc65645b4a42d53ef`: only `tool_call_matches` and `tool_call_sequence` execute as fixed checks, only `tool_call_matches` gates, and disabled patterns still undergo block validation. Existing recommendations work but do not make arbitrary pack-authored judges execute. Preserve that distinction when verifying supplied compatibility inputs.
- **Authoring precedence:** recorded user decisions and explicit stage-dependent completion rules govern conflicting shorthand in pattern requirements. Preserve source examples with labels, explain boundary differences and leave unresolved semantics unassessed; do not silently strengthen or weaken a definition to obtain a pass.
- **Intermediate acceptance:** validate every delivered pattern and report pending catalogue IDs throughout construction. The complete-catalogue integration slice turns exact-41 coverage into a mandatory gate. Content lint is not recognition evaluation, and unevaluable cases are never successes.
- **Slice completion:** each checkbox includes implementation, meaningful focused tests/validation, readiness updates, plan completion and a local commit. No pushing or publishing is included. Adjacent independent content slices may share a batch only when they remain reviewable; follow the listed dependency order.
- **Budget:** 20 autonomous slices; approximately 16 execution/review batches, median 25–30 minutes per batch, approximately 7–8 agent-hours once compatibility inputs are available. Human waiting and future field evaluation are excluded. No iteration limit is specified, so sufficiency cannot be confirmed; allow at least 16 successful batch iterations plus retry/review headroom. If compatibility work expands the estimate beyond eight agent-hours, propose dependency-linked content child issues and retain integration/final acceptance in the parent before expanding scope.

### Human follow-up

- Maintainer identity confirmed by the issue owner: `glenngillen`. Use it wherever the schema needs maintainer metadata, without claiming official Infracost status.
