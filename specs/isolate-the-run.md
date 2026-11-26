# Isolate the Run

## Overview

Source ID `isolate-the-run`; Delegation, rung 5. Keep unattended or parallel runs from interfering with other working copies. Intended detection is a code check.

## Requirements

- Applies to unattended runs and actively overlapping sessions.
- Seen requires an actual qualifying run in its own separate working copy: a git worktree, a separate clone, a container/devcontainer with its own checkout, or a VM/remote sandbox.
- Exclude two sessions sharing the same directory (on the same or different branches) and unused worktrees. A distinct branch alone is not isolation, because switching branches rewrites the same files.
- Cite the session header showing its environment as completion, with launch attribution where necessary.
- Continuous requires every unattended/parallel run in the window to be isolated through an actual command/script/devcontainer mechanism, not coincidental manual separation alone.
- Coach on simultaneous edits in one working copy. The guide has the person create and actually use a worktree for a real qualifying task.

## Acceptance Criteria

- [ ] Recognize headless work in a separate `app-fix-export` worktree; reject two active sessions in the same directory on `main`.
- [ ] Recognize parallel work in distinct devcontainers; reject an unused created worktree.
- [ ] Idle sessions alone do not establish overlapping work.
- [ ] Reject two active sessions in the same directory on different branches; recognize the same work in two separate clones.
- [ ] Guided worktree creation without a qualifying run is incomplete.

## Edge Cases

- Decided: the source's “distinct branch” wording is superseded. Only a separate working copy counts; branch-only separation in a shared directory is excluded.
- A path string resembling a worktree is not proof of one.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Historical worktree/container facts, active overlap and mechanism provenance; the present fixed-pattern interface does not consume these headers.

