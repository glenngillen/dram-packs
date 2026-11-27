# Plan first: scenarios

Every acceptance scenario for `glenngillen/plan-first`, in full. All people, repositories and content are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs plan-mode provenance, recognition of the person's review and per-file edit ordering; the collected-history fixture shape cannot tell a person's review from automatic approval, and the pattern names no block the pinned build runs.

Applicable work is a change in a main session that edits at least two files.

## pos-1 Person-entered plan mode, reviewed, four files

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, the person enters plan mode and asks for a pagination change. The agent proposes edits to four files. The person replies "keep the old API working alongside the new one." The agent revises, exits plan mode and edits four files.
- Why: plan before edits, the person's adjustment, then at least two files edited. The second file's edit completes it.

## pos-2 "Propose an approach, don't change anything yet"

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, the person writes "propose an approach for moving config to TOML, don't change anything yet." The agent proposes two files. The person replies "approved, go ahead." Two files are edited.
- Why: a person-requested plan, approved, then two files edited (the inclusive boundary).

## pos-3 Agent-originated plan, adjusted by the person

- kind: source-positive
- expect: seen
- Setup: in `tidepool-web`, the agent calls `EnterPlanMode` and proposes a schema change plus migration. The person writes "split the migration into its own step." Three files are edited afterwards.
- Why: agent-originated plans count through the person's review, which is the intentional act.

## pos-4 Default plan mode with reviewed plans

- kind: mechanism-held
- expect: continuous
- Setup: the person's user settings make plan mode the default. In the window, three sessions in `marlin-cli` each began with a plan the person questioned or adjusted, followed by multi-file edits.
- Why: the source's Continuous example: a setting in place, applied and holding.
- Note: no block reaches `continuous` in the pinned build.

## pos-5 Guided plan on real work

- kind: guided-success
- expect: seen
- Setup: in `orchard-jobs`, after reading the guide, the person asks for a plan for a retry refactor, asks "why change the scheduler at all?", accepts the revised plan, and three files are edited.
- Why: the person's review of a plan on real multi-file work. Guided work earns Seen only.

## neg-1 Automatic headless approval

- kind: source-negative
- expect: none
- Setup: a headless run in `basalt-sdk` enters plan mode, approves its own plan with permission bypass and edits five files. No person turn occurs.
- Why: automatic approval in unattended or bypass runs is excluded. With no person-authored moment there is no opportunity either.

## neg-2 One-file plan

- kind: source-negative
- expect: none
- Setup: in `fern-docs`, the person asks for a plan, reviews it, and the change edits one file.
- Why: one-file changes are not applicable.

## neg-3 Plan mode exited without review

- kind: source-negative
- expect: opportunity
- Setup: in `kestrel-app`, the agent enters plan mode, presents a plan and exits plan mode with no person reply, editing three files. The person then writes "no, don't touch the auth middleware, undo that."
- Why: no review, so no recognition. The person's correction, which a reviewed plan could have caught, is the citation for the opportunity.

## neg-4 Plan requested after two files were edited

- kind: source-negative
- expect: none
- Setup: in `slate-ui`, the agent edits `button.tsx` and `theme.ts`, then the person writes "stop, show me a plan first." They approve the plan and one more file is edited. No later correction.
- Why: a plan requested after multi-file edits began is too late. No correction follows, so no opportunity.

## neg-5 Guide read, plan never reviewed

- kind: guided-no-action
- expect: none
- Setup: in `heron-service`, the person reads the guide and asks for a plan; the agent proposes one; the session ends with no reply and no edits.
- Why: guided planning without review and subsequent applicable work does not count, and nothing applicable was edited.

## neg-6 Only one-file changes in the window

- kind: no-applicable-work
- expect: none
- Setup: every change the person made in the window edited a single file.
- Why: no multi-file change, so nothing is applicable.

## neg-7 Edit ordering unavailable

- kind: missing-evidence
- expect: none
- Setup: in `amber-lib`, the session record lost its edit timestamps; a plan and a person approval are visible, and four files changed at some point.
- Why: whether the plan came before the edits cannot be established: insufficient, not a miss.

## neg-8 Default plan mode set, no multi-file work

- kind: mechanism-unused
- expect: none
- Setup: default plan mode is on in the person's settings, but in the window they only made single-file fixes.
- Why: the mechanism is in place but untested; nothing applicable.

## neg-9 Plan-first rule in place, edits began anyway

- kind: mechanism-not-holding
- expect: opportunity
- Setup: `pewter-tools`'s instruction file says "propose a plan before editing more than one file." In a session the agent edited three files without a plan. The person wrote "you were supposed to plan this first; the config change was wrong."
- Why: the rule was in place and applicable but did not hold. The person's correction is the citation.

## neg-10 Plan after a single initial edit

- kind: boundary
- expect: none
- Setup: in `garnet-web`, the agent creates `migrations/0042.sql`, then proposes a plan for the remaining work; the person adjusts it; two more files are edited.
- Why: the first-edit boundary is unresolved, so the case stays pending: neither a recognition nor a miss.

## Scenarios the case format cannot label

### stage-boundary Forming across two weeks

- kind: stage-boundary
- Setup: pos-2 in week 1, pos-3 in week 3.
- Expected: Forming, each credited to the week its second-file edit finished.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Reviewed plan, edits finished next week

- kind: stage-boundary
- Setup: the person reviews a plan on the last day of week 1; the second file is edited in week 2.
- Expected: the instance completes in week 2. Until the second file is edited it is pending, not a miss.
- Why no case: as above.
