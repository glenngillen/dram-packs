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
- **No `maintainers` field.** The schema does not require it, and the final maintainer identity is unresolved. The field is contact information, never proof of origin; nothing in this pack claims official status, signing or provenance.

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

Run on 2026-11-27 in this repository, against the pinned build at `.tmp/dram`:

| Command | Result | What it shows |
| --- | --- | --- |
| `.tmp/dram pack validate .` | exit 0: `dram.yaml is valid: 1 pack offered`, `glenngillen/core 0.1.0 1 pattern` | The index and pack load beside the built-in packs, with no ID collision. Structural only. |
| `.tmp/dram pack validate core` | exit 0: `glenngillen/core 0.1.0 is valid: 1 pattern` | As above. |
| `.tmp/dram pack eval core` | exit 1 (red): 0 passed, 0 failed, 16 unevaluable, 0 errors; `glenngillen/give-it-instructions` held to nothing | **No case was judged.** The red verdict is the expected, honest result for disabled content; it is not hidden or patched. |
| `.tmp/dram pack show --dir core --json` | `glenngillen/give-it-instructions`: `enabled: false`, `status: preview`, `blocks: []` | The pattern is loadable without presenting an executable recognizer. |
| `bash scripts/run-tests.sh` | 184 passed, 0 skipped (with the pinned checkout and `.tmp/dram` present) | Local structural checks: schema and registry against the pinned files, references, placeholders, cases, links, parameters, catalogue order. **Not an evaluation.** |

The content tests in `tests/content/` re-run the CLI commands above when `.tmp/dram` exists and read the schema and registry from the pinned checkout (override with `DRAM_CLI_CHECKOUT`). Without them, those tests are skipped and say so.

## Open questions

- Which released Dram version should `min_cli` name?
  - evidence: No tag up to `v0.1.0-preview.4` contains the pack loader; the pinned revision is untagged.
  - options: Set `min_cli` to the first release containing the loader once it is tagged and checked; keep it absent and document the pinned revision.
  - location: core/reference/compatibility.md / min_cli
- Who is the maintainer of `glenngillen/core`?
  - evidence: The schema does not require `maintainers`, and no maintainer identity was supplied.
  - options: Add a `maintainers` entry once confirmed; leave it absent.
  - location: core/reference/compatibility.md / Identity
