# glenngillen dram packs

Coaching packs for [Dram](https://github.com/infracost/dram), the CLI that looks at how a person works with coding agents. This repository offers one pack, **`glenngillen/core`**: 41 coaching patterns in eight groups (Briefing, Guides, Context, Checking the work, Correcting course, Delegation, Economics, Safety), from briefing the agent to running it safely unattended.

Findings describe work, never the person. There is no grade, score, ranking, streak or productivity measure, and no promise of savings.

Why the framework works the way it does, and what each group is for: [principles](core/reference/principles.md).

**This release is content only.** Every pattern is disabled because the detection it needs is not yet in the Dram CLI. See [what installing gives you](#what-installing-gives-you) before installing.

## What installing gives you

Four separate things, each with its own evidence. One never implies the next.

| State | This release | Evidence |
| --- | --- | --- |
| **Content available** | Yes. Every pattern's definition, coaching copy (`text.yaml`), guide, judge prompt where model-judged, and evaluation scenarios. | The files under [`core/patterns/`](core/patterns). |
| **Structurally valid** | Yes, against the pinned CLI revision `bdea6f6`. The pack loads beside the built-in `infracost/iac` and `infracost/recommend` packs without an ID collision, including `glenngillen/right-size-it` (model selection) beside `infracost/right-size-it` (infrastructure sizing). | `dram pack validate` and `dram pack show`; see [compatibility](core/reference/compatibility.md#checks-run). Structural only. |
| **Evaluable** | No. All 607 cases are reported unevaluable, each with the capability it is missing, so `dram pack eval core` exits 1 with a red verdict. That is the expected, honest result, not a defect to patch. | `dram pack eval core`; see [readiness](core/reference/readiness.md). |
| **Active** | No. Every pattern is `enabled: false` and names no detection block, so Dram recognizes none of them and reports no opportunity. A disabled pattern never implies you missed it. | `pattern.yaml` in each pattern; `dram pack show` lists `enabled: false`. |

The guides are still usable by hand: each works on a real task in your own project and says plainly that finishing it will not show a recognition yet.

## Requirements

- A Dram build that contains the pack loader. **No tagged Dram release does yet** (the latest checked, `v0.1.0-preview.4`, predates it), so `core/pack.yaml` sets no `min_cli`. This pack was checked against Dram revision `bdea6f678399b3684519d41cc65645b4a42d53ef` built from source; a development build reports `dram dev` and skips version checks. See [compatibility](core/reference/compatibility.md#min_cli).

## Check the pack locally (verified)

From a clone of this repository, with `dram` built at the pinned revision:

```sh
dram pack validate .              # the index (dram.yaml) and the pack it offers
dram pack validate core           # the pack, loaded beside the built-in packs
dram pack show --dir core         # its 41 patterns, all disabled, no blocks
dram pack eval core               # 607 cases, all unevaluable; exits 1 (red) by design
```

These are the commands recorded, with their results, in [compatibility](core/reference/compatibility.md#checks-run).

## Install from the registry

The pinned CLI installs packs from a GitHub repository with a `dram.yaml` at its root:

```sh
dram pack registry add glenngillen/dram-packs
dram pack install glenngillen/core
dram pack list                    # glenngillen/core beside the built-in packs
```

**This path has not been verified.** It needs network access and this repository's published default branch, neither of which was exercised. What was verified is the result: with the pack laid out as an install leaves it (`<state>/packs/glenngillen/core` plus its `packs.json` record), the pinned `dram pack list` and `dram pack show` load it beside the built-in packs and leave them unchanged. The pack is not signed and claims no official status; `glenngillen` is an organisation prefix, not a mark of origin.

## Repository layout

| Path | What it holds |
| --- | --- |
| [`dram.yaml`](dram.yaml) | The repository index: one entry, `glenngillen/core` at `core`. |
| [`core/`](core) | The pack: `pack.yaml`, `groups.yaml`, `patterns/<source-id>/`, and [`reference/`](core/reference) (evidence contract, parameters, progression, outcomes, verification scenarios, compatibility, readiness). See [core/README.md](core/README.md). |
| [`specs/`](specs) | The requirements the pack was written from. Not packaged. |
| [`tools/`](tools), [`tests/`](tests), [`scripts/`](scripts) | Local authoring checks. Not packaged; the pack itself holds only YAML, Markdown and JSON data. |

## Development

```sh
uv sync
bash scripts/run-tests.sh
```

The tests are structural content checks and unit tests of the authoring tools. They never run a detector, and passing them is not an evaluation. The CLI-backed tests need the pinned Dram checkout and a build at `.tmp/dram`; see [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md).

## Status and next steps

- Per-pattern status, the eight first activation candidates, the stable-quality bars, the copy review performed and outstanding, and unresolved dependencies: [readiness](core/reference/readiness.md).
- Nothing here is a preview-ready or stable recognizer, and no field results exist. Enabling any pattern needs the CLI capabilities its definition lists and a passing evaluation on the CLI revision it is enabled for.

## Licence

See [LICENSE](LICENSE).
