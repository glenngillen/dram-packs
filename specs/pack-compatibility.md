# Pack Compatibility

## Overview

Keep the new content consumable by the existing Dram pack loader without changing the CLI or implying that a schema-valid definition is an implemented detector.

## Requirements

- Use `dram.yaml` as the repository index and the current `pack.yaml`, `groups.yaml`, `patterns/<source-id>/pattern.yaml`, `text.yaml`, `guide.md` and `eval/cases.jsonl` conventions. A `judge.md` is authoring content for model-judged patterns; its presence alone does not mean the current CLI executes it.
- The index ID must equal the manifest ID. References must resolve inside the pack; packaged trees contain no symlinks or executable detection code.
- Use only fields and block parameters the current schema accepts. Unsupported packet descriptions, stage overrides, verify rules and capability requests remain prose, not invented executable fields.
- Unknown blocks are invalid even on disabled patterns: `checkBlocks` validates all patterns. Omit unsupported runtime bindings, preserve their full intended semantics in prose, and explicitly set `enabled: false`. An absent `enabled` means true in the current loader.
- Known but unimplemented blocks are not working detectors. In this baseline only `tool_call_matches` and `tool_call_sequence` run as fixed-pattern code checks; only `tool_call_matches` runs as an applicability gate.
- Do not enable a pattern using only one implemented fragment of a definition that also needs person intent, applicable-work semantics, historical configuration, outcomes or a mechanism firing.
- The existing recommendation system is functional. It uses history, setup, structural signals, model proposals, verification, savings and fix tracking. However, its active prompt and output schema are constructed in `internal/recommend/request.go`; the draft `propose` block is not evidence that arbitrary pack-authored recognizers run.
- Accordingly, the initial authoring baseline is disabled for all 41 named recognizers unless the building phase demonstrates complete support on its pinned CLI revision. Enabling requires the actual semantics and the evaluation bar, not a newer version number alone.
- Keep unsupported outcome measures and progression rules in documentation. Do not invent block names or mislabel a one-day revert measure as fourteen-day survival.
- Use `text.yaml`, not the production spec's illustrative `copy.yaml`. Only supported placeholders (`{cases}`, `{applicable}`, `{count}`, `{session}` for fixed-pattern copy) may be used in runtime copy.
- Record the CLI revision used for compatibility work. Select `min_cli` from a verified released version during building; `dev` currently bypasses version refusal and cannot establish a minimum release guarantee.
- Do not claim official status from an ID or maintainer string. Signing, official provenance, publishing and any change to the CLI's allow-list are outside this task.

## Acceptance Criteria

- [ ] The index and pack validate against the selected current CLI without schema or runtime edits.
- [ ] The index and manifest use `glenngillen/core`; all 41 patterns use `glenngillen/<source-id>`.
- [ ] Fully qualified IDs do not collide when loaded beside the built-in IaC and recommendation packs; `glenngillen/right-size-it` and `infracost/right-size-it` load together.
- [ ] Every disabled pattern documents why it is disabled, which capabilities are missing and which behavior must be verified before enabling.
- [ ] No unknown runtime field or block is included solely because `enabled` is false.
- [ ] Loading the pack does not alter or replace the existing recommendation pack.
- [ ] Runtime claims are limited to what was actually checked. A passing structural validation is not reported as a passing evaluation.
- [ ] Where an evaluation cannot run, its reason is retained; it is never converted to an expected `none` simply to get a pass.

## Edge Cases

- Current IDs are organization-scoped rather than fully pack-scoped: `Set.finish` uses the prefix before `/`. Thus `infracost/core` with `infracost/right-size-it` would collide with the built-in IaC pattern, which is why the `glenngillen` prefix was chosen. A three-component `infracost/core/right-size-it` ID does not match the current schema.
- Current `progress.yaml` accepts milestone blocks, not adjustable stage thresholds. Preserving the draft thresholds in prose does not implement them.
- The current model evaluator calls `recommend.Judge` on recorded answers. It is not a general evaluator for the production spec's `patterns`, `opportunities` and `held` response example.
- A pattern with only unevaluable cases makes the existing evaluation verdict red. This is an honest dependency result, not a reason to remove cases or weaken expectations.

## Dependencies

- The implementation evidence in [requirements evidence](requirements-evidence.md).
- Identity decided by the user: pack `glenngillen/core`, patterns `glenngillen/<source-id>` (for example `glenngillen/brief-it`, `glenngillen/right-size-it`). The `glenngillen` organization prefix avoids collision with the built-in `infracost/*` patterns, including `infracost/right-size-it`.
- Minimum supported released CLI version and final maintainer identity remain unresolved; do not infer signing authority from the repository owner.

