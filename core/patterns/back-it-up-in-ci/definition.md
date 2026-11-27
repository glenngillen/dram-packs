# Back it up in CI

Source ID `back-it-up-in-ci`; pattern `glenngillen/back-it-up-in-ci`; Checking the work, rung 7. Confirm agent changes reach the default branch through tested CI. Intended detection: configuration and git/run evidence.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A repository is applicable when it **receives commits of the person's agent work** in the window: commits produced in the person's main sessions that reach any branch of the repository.
- An agent change is counted against this pattern when it **reaches the default branch** in the window. Agent work still on an unmerged branch is not yet applicable.
- The **default branch** is the repository's actual default branch. A branch named `main` need not be it.
- A window with no agent change reaching a default branch is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs all of:

1. A **CI workflow that runs tests** (unit, integration or end-to-end), in place in the repository when the change was integrated.
2. An **agent change** from the person's work that reached the default branch **through a branch or pull request**.
3. Evidence that **CI actually ran on that branch or pull request** before the merge, linked to the change.

Completing evidence: the workflow, and the linked branch or pull request, CI run and merge into the default branch. CI that supplements local gates with integration checks is a positive example: the local gate does not make CI redundant.

A failing CI run that the person then fixed before merging still shows the change went through CI. Whether a merge made while the run was failing or still pending counts is **unresolved** (see [open questions](#open-questions)); until settled, such a case is not recognized and not reported as a miss.

## Exclusions

- **Direct pushes** to the default branch: the change never went through a branch or pull request where CI could run first, even if CI ran afterwards on the default branch.
- **CI that does not run tests**: for example **docs-only** CI (link checks, spell checks, a site build), lint-only or formatting-only workflows.
- A **workflow file alone**: its presence proves neither a run nor a merge path.
- **Git ancestry alone**: a merge commit does not prove CI ran on the branch. Without run evidence this is unassessed.
- Guided discussion of CI, or setting up a workflow, without a qualifying integrated agent change.
- Changes that are not the person's agent work (another person's commits, bots acting on their own behalf).

## Evidence

- **Cite** the test-running workflow (path and the job that runs tests, as it existed at the time), the branch or pull request, the CI run linked to the change's commit, and the merge into the default branch. At least one attributable person-authored citation is required ([attribution](../../reference/evidence.md#attribution-and-citations)): for example the session prompt that produced the change, or the person's request to open the pull request.
- **Agent provenance**: the commits must be linked to the person's agent sessions; a commit message alone is weak evidence.
- **Historical**: the workflow must have existed and run when the change was integrated. Today's workflow file cannot prove a past run.
- **Completion window**: the merge is the completing event and must fall within the window in the person's local time ([completion windows](../../reference/evidence.md#completion-windows)).
- **Evidence the pinned CLI does not supply**: CI run records linked to commits or pull requests; which jobs run tests; default-branch identity; merge linkage (branch or pull request to default branch); agent provenance of commits. This pack cannot add network reads to fetch CI runs. The declared `ci_runs` block has no implemented matching semantics.

## Progression

No pattern-specific threshold override; the default [stages](../../reference/progression.md#stages) apply, counted over agent changes that reached the default branch.

| Stage | For this pattern |
| --- | --- |
| Seen | One agent change merged through a branch or pull request with a linked test-running CI run. |
| Forming, Established | Each counted instance is a merge with a linked CI run, credited to the week the merge finished ([stage-dependent completion](../../reference/progression.md#stage-dependent-completion)). Established needs [`most`](../../reference/parameters.md#most) of the agent changes reaching the default branch. |
| Continuous | **All** agent work reaching the default branch in the window went through tested CI, **and** the [mechanism](#mechanism) applied and held. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the merge path itself: test-running CI on every branch or pull request, with agent changes integrated only through it.

| Fact | For this pattern |
| --- | --- |
| In place | A test-running CI workflow triggered on branches or pull requests, attributable to the person's or team's repository configuration, existed during the window. |
| Applied | Agent changes reached the default branch through branches or pull requests on which it ran. |
| Held | Every agent change that reached the default branch in the window had a linked test-running CI run before merging, and none reached it through a known bypass of a required check (an override, a skipped check or a merge past it). A run that happened is not enough when its required check was then bypassed. |
| Not holding | An agent change reached the default branch without a CI run while the workflow was in place: a direct push, a merge before CI finished, or a bypassed required check. Known failures and bypasses must be reported faithfully, never hidden. |
| Untested | The workflow was in place but no agent change reached the default branch in the window. |

The source does **not** require branch protection. Its presence may help hold the mechanism but is not a requirement, and its absence is not a miss.

## Opportunities and coaching

- **Opportunity**: agent work **pushed directly** to the default branch in a repository where the person's agent work lands. It cites a person-authored moment, such as the prompt asking the agent to commit and push to `main` ([opportunities](../../reference/evidence.md#opportunities)). A direct push made by an agent with no person turn that asked for it is not reported unless a person-authored moment in that work can be cited. Tests that run only after the push do not change this: the change reached the default branch before CI tested it.
- **Opportunity**: agent work merged through a branch or pull request whose CI **runs no tests** (for example docs-only or link-check workflows). It cites the person-authored moment that opened or merged the pull request. The route was right; the CI did not back the change up.
- **Coaching**: the [guide](guide.md) explains fast local checks versus slower CI checks on the person's actual workflow, and has them send the next real agent change through a branch or pull request.
- Escapes after merge (fix-ups or failing CI on agent work) relate to the **Escapes** [outcome](../../reference/outcomes.md); they are not wired.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The intended detection links configuration, git history and CI run records. The pinned CLI (revision `bdea6f6`) supplies none of the run or merge linkage and runs no block that can express it. Enabling on a workflow file or a merge commit alone would substitute a weaker definition (a file is not a run, ancestry is not CI), which the pack must not do.

## Missing capabilities

- **CI run evidence**: run records linked to a change's commit, branch or pull request, with the jobs that ran and their result. The pack cannot introduce network reads to fetch them.
- **Test classification of workflows**: whether a workflow's jobs run tests, as opposed to docs-only, lint-only or formatting-only steps, at the time of the change.
- **Default-branch identity** for each repository, independent of branch names.
- **Merge linkage**: whether a commit reached the default branch through a branch or pull request, or by direct push.
- **Agent provenance**: linking commits to the person's main sessions.
- **Historical configuration**: the workflow as it existed when the change was integrated.
- **Implemented matching semantics** for `ci_runs`; it is declared in the pinned registry but runs nothing, and nothing reaches the `continuous` stage.

## Verify before enabling

- A test workflow with an agent branch merged through a pull request with a linked CI run is recognized; a direct agent push to `main` is rejected.
- CI integration checks supplementing local gates are recognized; docs-only CI is rejected.
- A workflow file with no run or merge path is not recognized.
- A branch named `main` that is not the default branch is handled by actual default-branch identity.
- Missing run evidence leaves the case unassessed, not a miss.
- Guided discussion or workflow setup without a qualifying integrated change is not recognized.
- Unused, held and not-holding mechanism cases produce distinct results.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- Does a merge that went through a pull request whose CI was still pending or failing count for Seen?
  - evidence: The source requires CI to have "actually run" on the branch or pull request; it does not say whether the run must have passed or finished before the merge.
  - options: Require a finished, passing run before merge; accept any finished run linked to the pull request; accept a started run.
  - location: core/patterns/back-it-up-in-ci/definition.md / Recognition
