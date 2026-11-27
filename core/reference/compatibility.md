# Compatibility

What this pack was checked against, what those checks show, and what they do not.

## Pinned CLI

| Item | Value |
| --- | --- |
| Dram CLI revision | `bdea6f678399b3684519d41cc65645b4a42d53ef` (read-only checkout, clean) |
| Build | `go build -buildvcs=false -o .tmp/dram ./cmd/dram` from that revision; reports `dram dev` |
| Compatibility sources | `internal/pack/schema.json`, `internal/pack/blocks.json`, `registry.go`, `pack.go`, `set.go`, `schema.go`, `index.go`, `internal/eval/run.go`, `internal/blocks/checks/checks.go`, `docs/pack-schema.md`, built-in packs `packs/iac` and `packs/recommend` |
| Layout reference | The community example pack repository `owenrumney/dram-packs`: `dram.yaml` at the root, one directory per pack, `pattern.yaml` plus `text.yaml` per pattern |

## `min_cli`

**Absent, deliberately.** Tags in the checkout: `v0.0.0-pilot.20260930.2`, `v0.0.0-pilot.20261001.2`, `preview-2026-10-21`, `v0.1.0-preview-1`, `v0.1.0-preview-2`, `v0.1.0-preview.3`, `v0.1.0-preview.4` (latest, committed 2026-11-13). None contains `internal/pack/schema.json` or `internal/pack/index.go`. The pack loader and `dram.yaml` index were added on 2026-11-23, after every tag, so **no released version can load this pack**.

`min_cli` accepts only `major.minor.patch`, so it cannot name the pinned commit. Writing `0.1.0` would not help: the loader drops pre-release suffixes when comparing, so a `0.1.0-preview.N` build without a pack loader would compare as equal. A dev build (`dram dev`) skips the version check altogether. The minimum supported CLI is therefore recorded here as the pinned revision; set `min_cli` once a tagged release containing the loader exists and has been checked.

## Identity

- Pack `glenngillen/core`; patterns `glenngillen/<source-id>`; index entry `glenngillen/core` at `core`.
- The `glenngillen` organisation prefix keeps every pattern ID clear of the built-in `infracost/*` patterns. The pinned loader scopes pattern IDs by the part before `/`, so `glenngillen/right-size-it` (model selection) and the built-in `infracost/right-size-it` (infrastructure sizing) can load together. Their findings and history are unrelated.
- **No `maintainers` field.** The issue owner confirmed the maintainer identity as `glenngillen`. The schema does not require the field, and each entry must be a scoped `org/name` (for example `infracost/engineering`), which a bare account name is not, so it stays absent rather than inventing a team name. The field is contact information, never proof of origin; nothing in this pack claims official status, signing or provenance.

## What the pinned CLI runs

| Block use | Runs at `bdea6f6` |
| --- | --- |
| `detection.code` | `tool_call_matches`, `tool_call_sequence` only |
| `applies_to` gate | `tool_call_matches` only; any other gate narrows the pattern to nothing |
| `continuous.mechanisms` | Nothing reaches the `continuous` stage; such cases are reported unevaluable |
| Disabled pattern | Detection returns early; block names are still validated |
| `detection.model` (`propose`) | Not a general recognizer: the active recommendation prompt and output schema are built in the CLI, and the evaluator replays recorded answers through its own judge |
| Outcome measures | `reverted_within` and `repeat_correction` are declared but not referenced by any CLI code |

So every pattern in this pack names **no** blocks: binding an unimplemented block would be refused or would silently narrow to nothing, and binding an implemented one would substitute a command match for the pattern's meaning.

## Checks run

Run on 2026-11-27 in this repository, against the pinned build at `.tmp/dram` (`dram version` prints `dram dev`):

| Command | Result | What it shows |
| --- | --- | --- |
| `.tmp/dram pack validate .` | exit 0: `dram.yaml is valid: 1 pack offered`, `glenngillen/core 0.1.0 41 patterns` | The index and the pack it names load. Structural only. |
| `.tmp/dram pack validate core` | exit 0: `glenngillen/core 0.1.0 is valid: 41 patterns` | The pack loads as part of a set with the built-in packs, so ID scoping and collisions are checked. Structural only. |
| `.tmp/dram pack show --dir core --json` | 41 patterns, each `enabled: false`, `status: preview`, `blocks: []` | Each pattern is loadable without presenting an executable recognizer. |
| `.tmp/dram pack eval core --json` | exit 1 (red): 0 passed, 0 failed, 0 errors, 607 unevaluable; all 41 patterns listed as held to nothing | **No case was judged.** Every case carries its precise capability reason (printed under "Not judged, so not passed"). The red verdict is the expected, honest result for disabled content; it is not hidden or patched, and no case is relabelled `none`. |
| `.tmp/dram --state-dir <tmp> pack list --json` and `pack show --json --blocks`, with the pack copied to `<tmp>/packs/glenngillen/core` and recorded in `<tmp>/packs.json` | exit 0: `glenngillen/core`, `infracost/iac` and `infracost/recommend` load together; 48 pattern IDs, no duplicates; `glenngillen/right-size-it` and `infracost/right-size-it` both present; the `infracost/iac` and `infracost/recommend` views (with blocks) are identical to an empty state directory's | The pack loads beside the built-in packs as an installed pack would, without replacing or altering the recommendation pack. This simulates the installed layout the pinned `registry.Dirs` reads; it is **not** a network install. |
| Mutation: the same tree with every ID rewritten to `infracost/...` | `pack validate` refuses: `two packs define pattern infracost/right-size-it` | The collision the `glenngillen` prefix avoids is real. Not kept in the repository. |
| Pack-wide rejection scenarios ([verification scenarios](verification.md)) | 8 scenarios (fabricated citation, changed quote, agent-only recognition, agent-only opportunity, out-of-window completion, subagent as person, tool output as person, Dram analysis session), all unevaluable | The pinned evaluator has no recognition verifier and runs only per-pattern cases, so none can be expressed; each keeps its expected rejection and the reason. |
| `bash scripts/run-tests.sh` | 420 passed, 0 skipped (with the pinned checkout and `.tmp/dram` present) | Local structural checks: completeness (exactly 41 qualified IDs in catalogue order), schema and registry against the pinned files, references, placeholders, cases, declarative-only packaged files, copy-review rules, CLI integration. **Not an evaluation.** |

The content tests in `tests/content/` re-run the CLI commands above (the integration one in a temporary state directory) when `.tmp/dram` exists, and read the schema and registry from the pinned checkout (override with `DRAM_CLI_CHECKOUT`). Without them, those tests are skipped and say so.

## Open questions

- Which released Dram version should `min_cli` name?
  - evidence: No tag up to `v0.1.0-preview.4` contains the pack loader; the pinned revision is untagged.
  - options: Set `min_cli` to the first release containing the loader once it is tagged and checked; keep it absent and document the pinned revision.
  - location: core/reference/compatibility.md / min_cli
