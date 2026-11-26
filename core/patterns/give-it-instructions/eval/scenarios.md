# Give it instructions: scenarios

Every acceptance scenario for `glenngillen/give-it-instructions`, in full. All people, repositories and file contents are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI because the collected-history fixture shape has no field for which instruction files a session loaded or their content, and the pattern names no block the pinned build runs. The scenarios are kept in full so that the cases can be turned into fixtures when those capabilities exist.

Applicable work is a repository with at least three of the person's main sessions in the window. "Loaded" means the session's own record shows the agent read the file at the time.

## pos-1 Loaded CLAUDE.md with build commands and conventions

- kind: source-positive
- expect: seen
- Setup: repository `lanternfish-api` has four of the person's main sessions in the window. Its committed `CLAUDE.md` says how to build (`make build`), how to run tests (`make test`) and two conventions ("handlers return typed errors", "no new dependencies without asking"). Each session's record shows the agent loaded it.
- Why: a non-trivial instruction file, actually loaded, in an applicable repository.

## pos-2 Loaded root AGENTS.md plus rules

- kind: source-positive
- expect: seen
- Setup: repository `quillmark` has three main sessions. Its root `AGENTS.md` gives the test command and points at a rules directory with a formatting rule and a migration rule; the agent loaded `AGENTS.md` and both rules in two of the sessions.
- Why: `AGENTS.md` plus rules counts as instructions when loaded. Three sessions is the inclusive applicability boundary.

## pos-3 Guided file, reviewed and loaded later

- kind: guided-success
- expect: seen
- Setup: in `tidepool-web` (five main sessions), the person follows the guide: generates a draft with `/init`, corrects the test command, adds "use the shared date helper, never raw Date parsing", saves and commits it. The next day, a new session in the repository loads the file and the agent answers "how do I run the tests?" from it.
- Why: the person's deliberate, reviewed file, loaded in a later session. A guided session earns Seen only; later stages need independent work.

## pos-4 Maintained user-level file covers every applicable repository

- kind: mechanism-held
- expect: continuous
- Setup: the person works in three applicable repositories. A user-level instruction file with their cross-project conventions was edited by the person nine days before the window ends, adding a rule. Every session in all three repositories loaded it, and two repositories also loaded their own files.
- Why: coverage of every applicable repository through a maintained user-level file, in place, applied and holding.
- Note: no block reaches `continuous` in the pinned build, so this case would be unevaluable even with load evidence.

## pos-5 User-level file loaded everywhere but not refreshed

- kind: boundary
- expect: seen
- Setup: as pos-4, but the user-level file was last changed seven weeks before the window ends.
- Why: loaded meaningful instructions earn Seen; Continuous needs an update in the last four weeks, so this is stale for Continuous, which is distinct from not holding.

## neg-1 Heading-only file

- kind: source-negative
- expect: opportunity
- Setup: `marlin-cli` has six main sessions. Its `CLAUDE.md` contains only `# Project`. The agent loaded it each time. The person's prompts in three sessions repeat "run tests with `just test`".
- Why: `# Project` alone is not instructions. The repository is applicable and frequently used, so it is a coaching opportunity, citing a person prompt that repeats the test command.

## neg-2 Conventions repeated in prompts, no instruction file

- kind: source-negative
- expect: opportunity
- Setup: `orchard-jobs` has four main sessions and no instruction file of any kind. In three of them the person writes "remember we use pnpm, not npm".
- Why: repeating a convention in prompts is not an instruction file. The repeated prompt is the person-authored citation for the opportunity.

## neg-3 Two sessions do not make a repository applicable

- kind: no-applicable-work
- expect: none
- Setup: the only repository the person used in the window, `fern-docs`, has two main sessions and no instruction file.
- Why: two sessions are below the applicability boundary, so the pattern is counted against nothing. This is not a miss.

## neg-4 Third session is a subagent or a Dram analysis session

- kind: boundary
- expect: none
- Setup: `basalt-sdk` has two of the person's main sessions, one subagent session spawned from them, and one Dram analysis session. No instruction file.
- Why: only the person's main sessions count toward the three, so the repository is not applicable.

## neg-5 Guided file generated but never reviewed or loaded

- kind: source-negative
- expect: opportunity
- Setup: in `kestrel-app` (four main sessions), the person runs `/init` while reading the guide; the agent writes a generated `CLAUDE.md` and the person ends the session without reading it. No later session in the window loads it.
- Why: guided file creation without meaningful review or later loading does not prove the pattern. The repository still lacks loaded, reviewed instructions; the opportunity cites the person's prompt starting work in a later session.

## neg-6 Reads the guide but takes no step

- kind: guided-no-action
- expect: opportunity
- Setup: `kestrel-app` again. The person opens the guide, answers its questions in conversation ("the convention I correct most is import order") and stops. No file is created.
- Why: answering coaching questions does not count. The repository remains an applicable opportunity.

## neg-7 Only Claude Code auto-memory

- kind: source-negative
- expect: opportunity
- Setup: `slate-ui` has three main sessions. The only instruction-like content loaded is Claude Code auto-memory the agent wrote for itself; no repository or user-level instruction file exists.
- Why: auto-memory is excluded; it is not instructions the person gave.

## neg-8 Unfilled template

- kind: source-negative
- expect: opportunity
- Setup: `heron-service` has five main sessions. Its `AGENTS.md` is a copied template whose sections read "Build: TODO", "Test: TODO", "Conventions: TODO". It is loaded every session.
- Why: template-only content is excluded, so the repository has no meaningful loaded instructions. Exactly where "template-only" ends needs the unresolved non-trivial rule.

## neg-9 User-level file in place, no applicable session

- kind: mechanism-unused
- expect: none
- Setup: the person maintains a user-level instruction file, updated last week, but in this window they had one session in each of two repositories.
- Why: a mechanism in place but never applied to applicable work is untested, not held, and there is no applicable repository to count against.

## neg-10 Instructions in place but not loaded in one repository

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person's user-level file is current and loaded by their main agent in `cobalt-infra` and `garnet-web`. In `pewter-tools` (three main sessions) they use a different agent that does not read that file, and the repository has no file of its own.
- Why: instructions were in place but did not reach every applicable repository, so the mechanism is not holding; `pewter-tools` is an opportunity, citing the person's prompt starting work there.

## neg-11 Load evidence unavailable

- kind: missing-evidence
- expect: none
- Setup: `amber-lib` has four main sessions and a committed `CLAUDE.md` with build commands. The session records are truncated before the start of each session, so whether the agent loaded the file cannot be seen.
- Why: missing load evidence is insufficient, not a miss and not a recognition. File existence alone does not prove loading.

## Scenarios the case format cannot label

### stage-boundary Forming: two applicable repositories

- kind: stage-boundary
- Setup: `lanternfish-api` and `quillmark` (pos-1, pos-2) both qualify in the same four weeks.
- Expected: Forming for this pattern (presence in two or more applicable repositories, an override of the default two-weeks rule).
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Established needs four applicable repositories

- kind: stage-boundary
- Setup A: three applicable repositories, all three with loaded instructions. Setup B: five applicable repositories, three with loaded instructions.
- Expected: A is not assessable for Established (fewer than four applicable items under `most`), which is not a miss. B meets Established (3 of 5 is 60%, inclusive).
- Why no case: as above.
