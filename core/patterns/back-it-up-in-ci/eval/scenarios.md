# Back it up in CI: scenarios

Every acceptance scenario for `glenngillen/back-it-up-in-ci`, in full. All people, repositories, workflows and runs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no CI run records, merge linkage, default-branch identity or workflow test classification, and the pattern names no block the pinned build runs.

Applicable work is an agent change from the person's main sessions reaching the actual default branch in the window.

## pos-1 Agent branch merged through a pull request with CI

- kind: source-positive
- expect: seen
- Setup: repository `wrenfield-api` has `.ci/test.yml`, which runs `make test` on every pull request. In a main session the person asks "put this on a branch and open a PR". The agent pushes `fix-rate-limit` and opens a pull request; the linked CI run executes the test job and passes; the person merges it into the default branch inside the window.
- Why: test-running CI, an agent change integrated through a pull request, and a linked run before the merge.

## pos-2 CI integration checks supplement local gates

- kind: source-positive
- expect: seen
- Setup: in `ploverkit`, a local pre-commit hook runs formatting and fast unit tests. The CI workflow on pull requests runs the integration suite against a test database. An agent change passes local checks, goes up as a pull request, the integration run is linked to its head commit, and it is merged.
- Why: CI supplementing local gates is a positive; the local gate does not make CI redundant.

## pos-3 Failing CI fixed before merge

- kind: boundary
- expect: seen
- Setup: in `wrenfield-api`, an agent pull request's first CI run fails a test. The person asks the agent to fix it; the second run passes and the pull request is merged.
- Why: the change still went through CI before reaching the default branch; the failure shows CI did its job.

## pos-4 Guided change sent through CI

- kind: guided-success
- expect: seen
- Setup: the person follows the guide in `tansy-web`: asks the agent which workflows run tests, then has it open a pull request for a real change instead of pushing to the default branch. CI runs the tests and the person merges.
- Why: a qualifying integrated change made while following the guide. Guided work earns Seen only.

## pos-5 Every agent change in the window went through CI

- kind: mechanism-held
- expect: continuous
- Setup: in `wrenfield-api` and `ploverkit`, the team's pull request workflow runs tests. All seven agent changes reaching either default branch in the window came through pull requests with linked test runs before merge.
- Why: in place, applied to every agent change, and holding.
- Note: no block reaches `continuous` in the pinned build, so this case would be unevaluable even with run evidence.

## neg-1 Direct agent push to main

- kind: source-negative
- expect: opportunity
- Setup: in `wrenfield-api`, the person writes "commit this and push to main". The agent pushes directly to `main`, the default branch. A CI workflow later runs on `main`.
- Why: a direct push skipped the branch or pull request where CI could run first. The person's prompt is the citation for the opportunity.

## neg-2 Docs-only CI

- kind: source-negative
- expect: opportunity
- Setup: `sorrel-cli` has one workflow, which builds the documentation site and checks links on pull requests. An agent change to the parser goes through a pull request, the docs-only run passes, and the person merges.
- Why: CI that runs no tests does not back up the change. The opportunity cites the person's prompt to open the pull request.

## neg-3 Workflow file alone

- kind: source-negative
- expect: none
- Setup: `sorrel-cli` gains a test workflow during the window, but no agent change reaches the default branch afterwards.
- Why: a workflow file proves neither a run nor a merge path. With no agent change integrated after it, there is nothing to recognize or count against.

## neg-4 Guided discussion without an integrated change

- kind: guided-no-action
- expect: none
- Setup: the person opens the guide in `tansy-web`, asks the agent which workflows run tests, discusses local versus CI checks and stops. No agent change reaches the default branch in the window.
- Why: discussion without a qualifying integrated change is incomplete, and with no agent change reaching the default branch there is no applicable work to call a miss.

## neg-5 Guided workflow setup, change pushed directly

- kind: guided-no-action
- expect: opportunity
- Setup: following the guide, the person asks the agent to add a test workflow to `tansy-web`, then later writes "push it to main" for a feature change. The change goes straight to the default branch.
- Why: setting up a workflow without integrating a change through it is incomplete; the direct push, cited by the person's prompt, is the missed moment.

## neg-6 No agent change reached a default branch

- kind: no-applicable-work
- expect: none
- Setup: in the window the person's agent work stays on an unmerged branch in `cobble-ml`; nothing reaches a default branch.
- Why: no applicable work. Not a miss.

## neg-7 Merge commit but no run evidence

- kind: missing-evidence
- expect: none
- Setup: in `ploverkit`, an agent branch was merged through a pull request, but run records for that period are unavailable.
- Why: git ancestry alone does not prove CI ran. Missing run evidence is unassessed, not a miss and not a recognition.

## neg-8 Branch named main is not the default branch

- kind: boundary
- expect: none
- Setup: `fenwick-site` has default branch `trunk`. The agent pushes directly to a branch named `main` that is not the default and nothing reaches `trunk` in the window.
- Why: a branch's name does not make it the default branch; nothing reached the actual default branch, so there is no applicable work.

## neg-9 Workflow in place, no agent change integrated

- kind: mechanism-unused
- expect: none
- Setup: `wrenfield-api`'s pull request test workflow is in place all window, but the person's agent work there produced no merged change.
- Why: a mechanism in place but never applied is untested, not held.

## neg-10 Pull request CI bypassed for one change

- kind: mechanism-not-holding
- expect: opportunity
- Setup: in `wrenfield-api`, six agent changes go through pull requests with test runs. For a seventh, the person writes "skip the PR, just push the hotfix to main", and it lands on the default branch without a CI run before merge.
- Why: the mechanism was in place and applied but did not hold for every change; the bypass is reported faithfully. The person's prompt is the citation.

## neg-11 Agent pushed directly with no person turn asking

- kind: boundary
- expect: none
- Setup: in an unattended run started by a scheduler acting on its own behalf, an agent pushes a formatting change directly to the default branch. No person-authored moment is linked to the work.
- Why: an opportunity needs an attributable person-authored citation; agent-only evidence yields no opportunity.

## Scenarios the case format cannot label

### stage-boundary Forming credited to the merge week

- kind: stage-boundary
- Setup: an agent pull request is opened in week 1 and its CI runs then; the person merges it in week 2. A second agent pull request with CI is merged in week 3.
- Expected: Seen from the first qualifying merge. Forming, with instances credited to weeks 2 and 3, the weeks the merges finished.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary CI ran but its required check was bypassed

- kind: stage-boundary
- Setup: in `wrenfield-api`, every agent change in the window goes through a pull request with a linked test-running CI run. For one of them, the run reports a failing required test check, and the change is merged by overriding that required check.
- Expected: the mechanism is not holding, so the window cannot reach Continuous even though every change had a linked run. The bypass is reported faithfully. Whether that merge counts for Seen is the separately unresolved pending-or-failing question in the definition's open questions; this scenario does not decide it.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`, and cannot express "not Continuous" for a mechanism.

### stage-boundary Merge outside the window

- kind: stage-boundary
- Setup: an agent pull request with CI runs inside the window, but is merged two days after the window ends.
- Expected: not counted in this window; it counts in the window where the merge finished.
- Why no case: as above.
