# Requirements Evidence

## Overview

Source record for this requirements draft. The user's full production spec and pack-only scope decision are sufficient primary evidence; failure to retrieve its original web artifact is no longer a content gap.

## Requirements

- Use the source extracts and implementation facts below when planning. Preserve their distinction between intended behavior and observed implementation.
- Keep pending decisions explicit. A draft file is not product approval or proof of executable support.
- Recheck implementation compatibility against the chosen build revision before enabling any detector.

### Source record

| Source and retrieval | Specific evidence relied on | Conclusion |
| --- | --- | --- |
| User-provided **Infracost AI: production spec**, draft November 2026; full text supplied in conversation, received 2026-11-26/27 Australia/Melbourne. One complete document. Original identifier: [Claude artifact](https://claude.ai/artifact/7Kivvnz4VxYDVCB3tVbv8H). | Catalogue: eight groups with 4, 7, 3, 11, 2, 6, 4 and 4 patterns. Pattern sections define intent, applicability, exclusions, evidence, mechanisms, examples and guides. Rule-pack chapter says layouts and library names are illustrative. | All 41 patterns are content scope; implement against the actual current loader and retain unsupported semantics explicitly. |
| User answer **“option 1”**, received 2026-11-27; one scope decision in conversation. | The offered option was “Pack content only — specify all 41 patterns, with unsupported detection explicitly disabled and CLI dependencies documented.” | No CLI or plugin implementation belongs in this task. |
| Local Dram source via `exec_command` using `cat`, `sed` and `rg`, inspected 2026-11-26/27. Clean source checkout at commit `bdea6f678399b3684519d41cc65645b4a42d53ef`, established with `git -c safe.directory=… rev-parse HEAD` and `git status --short`. [Repository revision](https://github.com/infracost/dram/tree/bdea6f678399b3684519d41cc65645b4a42d53ef). | `internal/pack/schema.json`, `blocks.json`, `registry.go`, `pack.go`, `set.go`, `schema.go`: closed schema; `org/name` IDs; all block references validated regardless of enabled state; absent enabled defaults true; optional detection; `text.yaml`; milestone-only progress; organization prefix indexing and duplicate ID rejection. | Use valid current data shapes; omit unknown runtime bindings, explicitly disable unsupported content and avoid the existing sizing ID. |
| Same source/tool/date/revision, `internal/blocks/checks/checks.go`, `internal/detection/detection.go`, `internal/eval/run.go` and `model.go`; read the dispatch and evaluation functions. | `Implemented` accepts only `tool_call_sequence` and `tool_call_matches`; gate support only `tool_call_matches`. Detection returns early for disabled patterns. Unsupported gates yield no finding. Continuous expectations are unevaluable. No evaluable cases means red. Model replay calls `recommend.Judge`. | Limits apply to fixed-pattern recognition and its evaluator, not to the entire CLI's intelligence. A passing schema does not establish a working recognizer. |
| Same source/tool/date/revision, `docs/recommendations.md`, `internal/recommend/request.go`, `propose.go`, `verify.go`, `internal/cmds/recommendations.go`; searches for `recommend.Refresh`, `proposeInstructions`, prompt construction and verification. | Existing recommendations use 14-day history, current items and setup; model proposals are checked against at least three occurrences across two sessions and matching structural signals. `request.render` expands the Go constant `proposeInstructions`; `Proposer.call` uses `req.input()` and `proposalSchema()`. | Useful model recommendations already work. Adding new pack judge files alone does not extend that active prompt or provide the named recognition contract. Reusable facts/signals exist and should not be dismissed as absent. |
| Same source/tool/date/revision, `docs/pack-schema.md`, `docs/design-notes.md`, `packs/recommend/patterns/recommend/pattern.yaml`, `packs/iac/patterns/right-size-it/pattern.yaml`, `AGENTS.md`. | Current schema documentation; rename to Dram; code checks are a union; unrun gates narrow to nothing; recommendation extraction is a design goal; IaC owns `infracost/right-size-it` for resource sizing; public fixtures must be synthetic. | Current implementation governs compatibility. Do not confuse design goals or recommendation declarations with implemented arbitrary-pack execution. Model selection must not inherit resource-sizing identity. |
| GitHub example [owenrumney/dram-packs](https://github.com/owenrumney/dram-packs/tree/c5d28ddd3ec2b70aa741c6a7fb023055ffbdbd7f), retrieved 2026-11-26 via web `open`, then `exec_command`/`curl` against GitHub tree API (`main?recursive=1`) and raw pattern file. One repository tree and one concrete pattern inspected. | Tree contains `dram.yaml`, one tests pack and `test-before-commit`. Pattern uses a `repo_file_matches` gate for `**/*_test.go`, then `tool_call_sequence` requiring `go test` within ten turns before `git commit`, plus `text.yaml`. README still uses the older CLI name. | Follow the declarative layout, not stale command naming or an assumption that this example's gate is implemented in the local CLI. |

| Notion via `notion-search` (query “Infracost AI production spec patterns rule packs”, 5 results) then `notion-fetch` of page “cli-ai initial implementation” (ID `41d01c60-607e-80e4-85d0-d232cee41437`, last edited 2026-11-20), retrieved 2026-11-27. One page. | Phase 3 “Enough content to dogfood” names the eight code-checked release-1 patterns: Give it instructions, Mind the cache, Gate "done", Gate each step, Keep secrets out, Scope permissions, Guard destructive commands, Isolate the run. “After the dogfood target”: the pattern pass, packet building, the verify step and the model-judged patterns. Decisions taken: packs are declarative with no executable code; the core pack has all 8 groups, 41 patterns, judge prompts, copy and guides; outside patterns merge as `preview`. Also names `infracost/ai-packs` as the eventual home and lists product/CLI names as working names. | Confirms the content scope and gives a priority order for later activation: these eight are the first candidates to enable once their code checks are supported. Does not change the user's `glenngillen/core` identity decision for this repository. |

### Recorded user decisions

Answers received in conversation on 2026-11-27, in addition to the earlier “option 1” pack-only scope answer.

| Decision | Answer | Applied in |
| --- | --- | --- |
| Pack and pattern identity | Pack `glenngillen/core`; patterns `glenngillen/<source-id>` | [Pack compatibility](pack-compatibility.md), [core catalogue](core-catalogue.md) |
| Progression | Keep stages with automation gating (three Continuous patterns across two groups) | [Pattern progression](pattern-progression.md) |
| Thresholds with source examples | Use the source examples as provisional, tunable defaults | [Pattern parameters](pattern-parameters.md) |
| Thresholds without source examples | Accept proposed defaults: long session = 150k tokens or compaction; substantial work = at least 6 person prompts; harness fix follow-up = at least 2 later applicable sessions within 14 days with no recurrence | [Pattern parameters](pattern-parameters.md) |
| Mind the cache denominator | All returns to the same work after a qualifying gap, both fresh starts and cold resumes | [Mind the cache](mind-the-cache.md) |
| Isolation | Only a separate working copy counts (worktree, clone, container, VM); branch-only in a shared directory does not | [Isolate the run](isolate-the-run.md), [Two at once](two-at-once.md) |
| Sandboxed bypass | Counts for Sandbox autonomy only; neutral for Scope permissions | [Scope permissions](scope-permissions.md), [Sandbox autonomy](sandbox-autonomy.md) |
| Sandbox evidence | Intent is system isolation. Seen needs an observable container, devcontainer, VM or remote sandbox; a credential-free host or separate OS user is unassessed until the CLI exposes it as a fact | [Sandbox autonomy](sandbox-autonomy.md) |
| Completion | Depends on the stage. Seen counts on the first qualifying event; Forming and Established count only instances whose follow-through finished, credited to the week it finished; Continuous needs a holding mechanism | [Pattern progression](pattern-progression.md#stage-dependent-completion) and the six affected pattern specs |

### Searches and limitations

- Before the user supplied the spec, web `open` could not retrieve the Claude artifact. `curl` returned a JavaScript loading shell, not the catalogue. Document-control `list_document_sessions` returned no connected sessions. Local `rg` searches for the artifact ID and core-pattern references found no complete catalogue; the issue text repeated the original link. The subsequent pasted document resolves this gap.
- An earlier drafting session had no Notion, Linear, Mixpanel or Close tool. A later session had Notion and used it for the one page recorded above. Linear, Mixpanel and Close were not queried: pack content does not depend on customer usage data or CRM records. No customer-data claim appears in these specs.
- An initial unquoted GitHub query URL failed under zsh globbing and was retried with quoting. An initial Git revision query hit ownership protection; a command-local safe-directory override read the revision without changing global Git configuration. Some guessed path/glob searches found no path; later searches used the actual `internal/cmds` and `internal/recommend` paths.
- Source inspection is not execution evidence. No build, test suite, live model evaluation, `pack validate` or `pack eval` has run in requirements mode. No designated spec lint was found; none is substituted.

### Pending decisions

Identity, progression, thresholds and completion are now decided (see Recorded user decisions). These remain open. They do not block authoring definitions, examples or guides, but they do block claiming a recognizer implements a settled contract.

| Decision area | Specific unresolved behavior | Affected specification |
| --- | --- | --- |
| Attribution | Whether opportunities are exempt from the person-authored citation rule; whether held cases must cite the originating configuration | [Pattern evidence](pattern-evidence.md) |
| Classification | Non-trivial instruction files, routine work beyond the example list, meaningful configuration refresh and repeated-correction equivalence | The corresponding pattern's Edge Cases section |
| Parameters with no value | "Several" in Fan out, waiting duration in Two at once, "fast" in Gate each step | [Pattern parameters](pattern-parameters.md) |
| Outcomes | Cost allocation across changes and fix-up matching | [Outcome content](outcome-content.md) |
| Release | Minimum released CLI version and maintainer identity | [Pack compatibility](pack-compatibility.md) |


## Acceptance Criteria

- [ ] Planning can recover the exact intended catalogue and current capability limits from these specs without reopening the inaccessible artifact.
- [ ] Every consequential source-derived compatibility claim names its source, retrieval method, date and concrete supporting data.
- [ ] Unanswered questions and unrun checks are never labeled approved or passing.
- [ ] No originating tracker identifiers or local checkout paths appear in spec content.

## Edge Cases

- Current implementation can change while requirements are drafted. A new revision may unblock content, but only demonstrated semantics justify enabling it.
- A source comment describing a future design does not outweigh the observed active code path.

## Dependencies

- All other specifications in this directory; the user remains the authority for unresolved product behavior.
