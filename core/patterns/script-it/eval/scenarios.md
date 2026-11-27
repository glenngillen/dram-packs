# Script it: scenarios

Every acceptance scenario for `glenngillen/script-it`, in full. All people, repositories, files and prompts are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape cannot link a tool execution to the edits it made or say who configured a tool, and the pattern names no block the pinned build runs.

Applicable work is a mechanical change across many files. Ten files is a coaching trigger only ([`many_files_coach`](../../../reference/parameters.md#many_files_coach)).

## pos-1 Codemod for the API rename, run on src/

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, the person writes "Write a codemod for the API rename (`fetchDoc` to `loadDocument`) and run it on src/". The agent writes the codemod, shows it, runs it; the run rewrites 37 files.
- Why: the person requested the tool and its execution made the change.

## pos-2 Scaffold script for the new endpoint

- kind: source-positive
- expect: seen
- Setup: in `orchard-jobs`, the person writes "Use the scaffold script to add the new endpoint for job retries". The agent runs the repository's scaffold script, which creates the handler, route, test and docs stub.
- Why: a person-requested tool, executed, made the boilerplate change.

## pos-3 Person-configured rename tool used by the agent

- kind: source-positive
- expect: seen
- Setup: the person configured a code-intelligence MCP server in their repository settings last month. Asked to rename `Ledger` to `Journal` across `basalt-sdk`, the agent uses that tool's rename operation, which updates 22 files.
- Why: a person-configured tool subsequently used by the agent to make the change.

## pos-4 Guided script on a real migration

- kind: guided-success
- expect: seen
- Setup: following the guide, the person asks for a script for a real logging-library migration in `tidepool-web`, reviews it, asks for one fix, then has it run; it changes 14 files.
- Why: requested, reviewed and executed on real work. Guided work earns Seen only.

## pos-5 Saved migration wrapper reused

- kind: mechanism-held
- expect: continuous
- Setup: `heron-service` has a saved `scripts/migrate-config` wrapper the person's team added. In this window two config migrations are made, both through the wrapper, which the person asks the agent to run.
- Why: a repository-saved wrapper in place, applied and holding on applicable changes.

## neg-1 Forty files edited individually

- kind: source-negative
- expect: opportunity
- Setup: the person writes "rename `userId` to `accountId` everywhere". The agent edits 40 files one at a time with identical edits.
- Why: file-by-file edits are not deterministic tooling. Forty files also crosses the ten-file coaching trigger. The opportunity cites the person's prompt.

## neg-2 Script written but never run

- kind: source-negative
- expect: opportunity
- Setup: the person asks for a codemod for an import rewrite; the agent writes it, then edits the 18 files by hand "to be safe". The codemod never runs.
- Why: a script never run does not count. Cites the person's request.

## neg-3 Unprompted throwaway script

- kind: source-negative
- expect: none
- Setup: the person writes "update the copyright year in the headers". Without being asked, the agent writes and runs a throwaway script that updates 12 files.
- Why: spontaneous agent behaviour never earns recognition, and the change was not made by hand, so there is no missed moment to report.

## neg-4 Tool discovered by the agent

- kind: source-negative
- expect: none
- Setup: asked to rename a type, the agent finds a language server on the machine that no one configured for it and uses it.
- Why: agent discovery does not establish person configuration; the change was not made by hand, so no opportunity either.

## neg-5 Guided discussion only

- kind: guided-no-action
- expect: opportunity
- Setup: the person reads the guide and says "next time I'll ask for a codemod". In the next real rename, they let the agent edit 15 files by hand.
- Why: discussion without requested execution earns nothing. Cites the rename prompt.

## neg-6 No mechanical change

- kind: no-applicable-work
- expect: none
- Setup: the window contains only feature work and bug fixes touching one or two files each.
- Why: nothing applicable; not a miss.

## neg-7 Execution records truncated

- kind: missing-evidence
- expect: none
- Setup: the person asked for a codemod and 30 files changed, but the session is truncated between the request and the edits, so whether the codemod or hand edits made them is unknown.
- Why: insufficient evidence, not a miss and not a recognition.

## neg-8 Nine files by hand

- kind: boundary
- expect: opportunity
- Setup: the person asks for a rename; the agent edits nine files by hand with identical edits.
- Why: below the ten-file coaching trigger, so the coaching message is not triggered, but the change can still be judged mechanical; the coaching trigger never decides recognition. Cites the person's prompt.

## neg-9 Saved wrapper in place, no applicable change

- kind: mechanism-unused
- expect: none
- Setup: `heron-service` has its migration wrapper, but no migration happens in the window.
- Why: in place, never applied: untested, not held.

## neg-10 Saved wrapper bypassed with hand edits

- kind: mechanism-not-holding
- expect: opportunity
- Setup: `heron-service` has its migration wrapper. The person writes "migrate the config files to the v3 format" and the agent edits 11 files by hand.
- Why: the same kind of change made by hand while the wrapper was in place: not holding. Cites the person's prompt.

## Scenarios the case format cannot label

### stage-boundary Forming needs two weeks of completed runs

- kind: stage-boundary
- Setup: pos-1 in week 1; in week 3 the person asks for a codemod for another rename, and it runs.
- Expected: Forming, credited to week 3. A request in week 3 whose script only runs in week 5 does not count in this window.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.
