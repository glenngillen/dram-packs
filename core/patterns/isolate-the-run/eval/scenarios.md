# Isolate the run: scenarios

Every acceptance scenario for `glenngillen/isolate-the-run`, in full. All people, repositories, paths and commands are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no historical worktree, clone, container or VM facts, no active-overlap timing between sessions and no launch attribution, and the pattern names no block the pinned build runs. The scenarios are kept in full so they can become fixtures when those capabilities exist.

Applicable work is an unattended run ([`unattended_gap`](../../../reference/parameters.md#unattended_gap)) or actively overlapping sessions in the same repository.

## pos-1 Headless work in a separate app-fix-export worktree

- kind: source-positive
- expect: seen
- Setup: in `app`, the person creates a git worktree `app-fix-export` and starts a headless run there to fix the CSV export, while their interactive session continues in the main checkout. The run's session header records the worktree path and that it is a worktree of `app`.
- Why: an unattended run in its own separate working copy, shown by the session's environment facts.

## pos-2 Parallel work in distinct devcontainers

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, the person runs two sessions with overlapping edits, each in its own devcontainer with its own checkout, started by the person's `bin/dev-up` script.
- Why: actively overlapping sessions in separate working copies, with attributable launch.

## pos-3 Same work in two separate clones

- kind: source-positive
- expect: seen
- Setup: the person has two clones of `tidepool-web` (`~/src/tidepool-web` and `~/src/tidepool-web-2`) and runs two sessions with edits in overlapping minutes, one in each clone.
- Why: separate clones are separate working copies. This is the decided contrast to branch-only separation (neg-3).

## pos-4 Guided worktree used for a real headless task

- kind: guided-success
- expect: seen
- Setup: following the guide in `marlin-cli`, the person has the agent propose and create a worktree, then starts a real headless dependency-upgrade run inside it.
- Why: the guided step completed by an actual qualifying run in the new working copy. Guided work earns Seen only.

## pos-5 Exactly 15 minutes unattended in a worktree

- kind: boundary
- expect: seen
- Setup: in `cobalt-infra`, the person starts an interactive session in a worktree and the agent works for exactly 15 minutes without a person prompt.
- Why: 15 minutes meets `unattended_gap` (inclusive), so the run is applicable, and it ran in its own working copy.

## pos-6 Owned script isolates every run

- kind: mechanism-held
- expect: continuous
- Setup: the person's `bin/agent-run` script creates a fresh worktree for each run. Every headless and parallel run in the window across `orchard-jobs` and `fern-docs-api` was started through it and ran in its own worktree.
- Why: in place, applied and held. No block reaches `continuous` in the pinned build.

## pos-7 Consistent manual separation, no mechanism

- kind: stage-boundary
- expect: seen
- Setup: in `kestrel-app`, the person manually creates a worktree for each of their unattended runs across the window. No owned command, script or devcontainer configuration sets them up.
- Why: each run is isolated, so Seen (and possibly Forming or Established, which the case format cannot express). Without a mechanism it cannot be Continuous: coincidental manual separation alone is not a mechanism.

## neg-1 Two active sessions in the same directory on main

- kind: source-negative
- expect: opportunity
- Setup: in `ember-ui`, one session is editing `src/form.tsx` while the person opens a second session in the same directory on `main` and writes "fix the header spacing". Both edit files in overlapping minutes.
- Why: shared working copy. The opportunity cites the person's "fix the header spacing" prompt that started the second session's work.

## neg-2 Unused created worktree

- kind: source-negative
- expect: none
- Setup: in `saffron-jobs`, the person creates a worktree `saffron-jobs-retry` but every session in the window runs in the main checkout, one at a time.
- Why: an unused worktree is not an isolated run, and there was no unattended or overlapping work to assess.

## neg-3 Same directory, different branches

- kind: source-negative
- expect: opportunity
- Setup: in `heather-cli`, one session works on branch `feature/a` while the person checks out `feature/b` in the same directory for a second session and writes "start the parser refactor". Both edit in overlapping minutes.
- Why: branch-only separation in a shared directory is not isolation (decided). The opportunity cites "start the parser refactor".

## neg-4 One active session, one idle

- kind: boundary
- expect: none
- Setup: in `cormorant-api`, two sessions are open in the same directory, but only one does any work in the window; the other sits idle.
- Why: idle sessions alone do not establish overlapping work, so nothing is applicable.

## neg-5 Guided worktree created, no run

- kind: guided-no-action
- expect: none
- Setup: following the guide, the person creates a worktree for an upcoming task but runs nothing in it in the window.
- Why: guided creation without a qualifying run is incomplete. Nothing is recorded against the person.

## neg-6 Only attended single sessions

- kind: no-applicable-work
- expect: none
- Setup: the person works in one interactive session at a time, prompting regularly, throughout the window.
- Why: no unattended or overlapping runs: no applicable work.

## neg-7 Environment facts missing

- kind: missing-evidence
- expect: none
- Setup: a headless run in `lanternfish-api` has no working-directory or worktree facts in its session record.
- Why: unknown environment is unassessed, never assumed isolated and never a miss.

## neg-8 Path that only looks like a worktree

- kind: boundary
- expect: none
- Setup: a headless run's working directory is `../app-worktrees/fix`, but the record has no fact showing it is a worktree, clone or container checkout.
- Why: a path string resembling a worktree is not proof: unassessed.

## neg-9 Script fell back to the main checkout

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person's `bin/agent-run` script normally creates a worktree. In one run worktree creation fails and the script falls back to the main checkout of `orchard-jobs`, where the person's interactive session is editing. The person had written "kick off the cleanup run" to start it.
- Why: the mechanism was in place and applied, but a run shared a working copy with an active session: not holding. The opportunity cites "kick off the cleanup run".

## neg-10 Devcontainer setup never used

- kind: mechanism-unused
- expect: none
- Setup: `fern-docs-api` has the person's devcontainer configuration for agent runs, but no run in the window used it, and the person had no unattended or parallel work.
- Why: in place, never applied: untested. Not a miss.

## neg-11 Fourteen minutes, single session

- kind: boundary
- expect: none
- Setup: in the main checkout of `marlin-cli`, the agent works 14 minutes without a person prompt; no other session is active.
- Why: 14 minutes is under `unattended_gap` and there is no overlap, so the run is not applicable.
