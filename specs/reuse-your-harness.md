# Reuse Your Harness

## Overview

Source ID `reuse-your-harness`; Guides, rung 6. Recognize the person's maintained harness following them across repositories. Intended detection is a code check.

## Requirements

- Applies when the person works in at least two repositories in the window.
- Seen requires the same owned command, skill, hook or rule used in at least two repositories through user configuration, their own plugin or a template.
- Exclude diverged copies and built-in/third-party plugins the person did not build.
- Continuous requires their maintained harness to apply to every repository worked in and to have been updated in the last four weeks, with actual application/holding evidence.
- Cite ownership, common configuration and usage in the relevant repositories; do not infer sharing solely from matching filenames.
- Coach on duplicate separately defined commands/hooks. The guide identifies an owned duplicate and has the person move one into user configuration.

## Acceptance Criteria

- [ ] Recognize a user-level PR-description command used across three repositories; reject three diverging copies.
- [ ] Recognize the person's own maintained plugin with hooks used across their repositories; reject a marketplace plugin they did not write.
- [ ] A single repository or an unused shared file cannot establish this pattern.
- [ ] Guided relocation without use across two repositories does not yet meet Seen.

## Edge Cases

- Team ownership and template identity require attributable facts; do not claim the person authored a third-party dependency.
- Equality/semantic equivalence of independently copied configuration and the source's meaning of “updated” need confirmation before activation.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [pattern progression](pattern-progression.md), [evaluation readiness](evaluation-readiness.md).
- Configuration identity/provenance, cross-repository usage and configuration history, absent from the current fixed-pattern check interface.

