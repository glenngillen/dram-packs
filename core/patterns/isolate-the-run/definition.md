# Isolate the run

Source ID `isolate-the-run`; pattern `glenngillen/isolate-the-run`; Delegation, rung 5. Keep unattended or parallel runs from interfering with other working copies. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. Named as one of the first activation candidates; it still needs the capabilities below.

## Applicable work

- **Unattended runs**: headless, or interactive with at least 15 minutes (inclusive) of continued agent work without a person prompt ([`unattended_gap`](../../reference/parameters.md#unattended_gap)).
- **Actively overlapping sessions**: two or more of the person's main sessions in the same repository with agent work (edits or tool activity) in overlapping minutes. **Idle sessions alone do not establish overlap**: a session open but doing nothing is not active.
- Subagents of a session are not separate sessions here ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with neither is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs an applicable run that **actually ran in its own separate working copy**, one of:

- a **git worktree** separate from the other active session's directory;
- a **separate clone** of the repository;
- a **container or devcontainer with its own checkout**;
- a **VM or remote sandbox** with its own checkout.

Completing evidence: the **session header showing its environment** (working directory, worktree or container facts) for the run, with **launch attribution** where necessary (for example that a container was started by the person's script).

**Decided**: only a separate working copy counts. The source's "distinct branch" wording is superseded: two sessions on different branches in one shared directory are **not** isolated, because switching branches rewrites the same files.

## Exclusions

- **Two sessions sharing the same directory**, on the same branch or on different branches.
- **Unused worktrees**: a worktree or clone that was created but no applicable run used it.
- **A path string that resembles a worktree** (for example `../app-worktrees/fix`) without an environment fact that it is a separate working copy: not proof.
- **Idle overlap**: an open but inactive session does not make the other run "parallel".
- **Guided worktree creation** without a qualifying run in it.

## Evidence

- **Cite** the session header (environment facts) of the isolated run and, for overlapping work, the other active session's header and an overlapping action in each. Where launch attribution matters (a container or script), cite the attributable launch.
- **Historical**: the environment facts must be those recorded when the session ran, not today's directory layout.
- Unknown environment (no working-directory or worktree facts recorded) is [insufficient](../../reference/evidence.md#insufficient-evidence): unassessed, never a miss and never assumed isolated.
- **Evidence the pinned CLI does not supply**: historical worktree, clone, container and VM facts per session; active-overlap timing across sessions; unattended classification; launch attribution for scripts and containers.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One applicable run in its own separate working copy. |
| Forming | Isolated applicable runs in at least two distinct weeks of the last four. |
| Established | At least 60% of applicable runs isolated, with at least four applicable runs ([`most`](../../reference/parameters.md#most)). |
| Continuous | Every unattended or parallel run isolated through an owned mechanism, in place, applied and holding (see [mechanism](#mechanism)). |

Coincidental manual separation, however consistent, reaches at most Established: Continuous needs a mechanism. A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is an **owned command, script or devcontainer configuration** that gives each unattended or parallel run its own working copy.

| Fact | For this pattern |
| --- | --- |
| In place | The attributable command, script or devcontainer configuration existed during the window. |
| Applied | Unattended or parallel runs in the window were actually started through it. |
| Held | Every unattended or parallel run in the window ran in its own working copy. |
| Not holding | While it was in place, an unattended or parallel run still shared a working copy with another active session (for example the script fell back to the main checkout). |
| Untested | Configured but no run used it in the window. |

## Opportunities and coaching

- **Opportunity**: simultaneous agent edits in one working copy: an unattended run or two active sessions sharing a directory (on any branches). It cites the person-authored prompt that started the second session's work or launched the unattended run ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) has the person create a worktree and actually use it for a real qualifying task.
- This pattern is the prerequisite for suggesting Two at once ([safety prerequisites](../../reference/progression.md#safety-prerequisites)).
- `automate` advice (an owned command or script that isolates every run) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`, and its fixed-pattern interface does not consume session environment headers. Matching `git worktree add` would accept unused worktrees and miss clones and containers; a directory name cannot prove a separate working copy; and nothing in the pinned build measures active overlap between sessions.

## Missing capabilities

- **Historical environment facts** per session: working directory, whether it is a worktree, clone, container or VM checkout, and which other sessions shared it.
- **Active-overlap detection**: overlapping minutes with agent activity in each session, distinct from idle open sessions.
- **Unattended classification** against `unattended_gap`.
- **Launch attribution** for scripts, containers and devcontainers.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- Headless work in a separate `app-fix-export` worktree is recognized; two active sessions in the same directory on `main` are rejected.
- Parallel work in distinct devcontainers is recognized; an unused created worktree is rejected.
- Two active sessions in the same directory on different branches are rejected; the same work in two separate clones is recognized.
- Idle sessions alone do not establish overlapping work.
- Guided worktree creation without a qualifying run is incomplete.
- A worktree-like path without environment facts is unassessed.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
