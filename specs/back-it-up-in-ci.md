# Back It Up in CI

## Overview

Source ID `back-it-up-in-ci`; Checking the work, rung 7. Confirm agent changes reach the default branch through tested CI. Detection uses configuration and git/run evidence.

## Requirements

- Applies to repositories receiving commits of the person's agent work.
- Seen requires a test-running CI workflow and an agent change reaching the default branch through a branch/pull request where CI actually ran.
- Exclude direct pushes to the default branch and CI that does not run tests.
- Cite the workflow and linked branch/PR/run/merge evidence as completion.
- Continuous requires all agent work reaching the default branch in the window to have gone through CI, plus applied/held evidence.
- Coach on agent work pushed directly to the default branch. The guide explains fast local checks versus slower CI checks on the person's actual workflow.

## Acceptance Criteria

- [ ] Recognize a test workflow with an agent branch merged through a PR with CI evidence; reject direct agent pushes to `main`.
- [ ] Preserve CI integration checks supplementing local gates as a positive scenario; reject docs-only CI.
- [ ] A workflow file alone does not prove a run or a merge path.
- [ ] Guided discussion or workflow setup without a qualifying integrated change is incomplete.

## Edge Cases

- Git ancestry alone may not prove CI ran. Missing run evidence leaves this unassessed; this pack cannot introduce network reads to fill it.
- A branch named `main` need not be the actual default branch.
- The Seen definition proves CI ran, while mechanism holding must faithfully reflect known failures/bypasses; do not invent a branch-protection requirement absent from the source.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [outcome content](outcome-content.md), [evaluation readiness](evaluation-readiness.md).
- CI execution attribution, default-branch/merge linkage and agent change provenance. Declared `ci_runs` is insufficient without implemented matching semantics.

