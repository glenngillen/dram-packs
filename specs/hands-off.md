# Hands Off

## Overview

Source ID `hands-off`; Delegation, rung 4. Run a trusted owned workflow unattended and use its output. Detection combines code facts with model judgement.

## Requirements

- Applies to the person's own commands already run interactively at least three times.
- Seen requires an unattended run of an owned command/skill whose output is used. Apply the shared fifteen-minute unattended definition where relevant.
- Exclude ad-hoc headless prompts, discarded output and launches by software running an agent on its own behalf.
- Cite the first prompt and the output's actual use as completion.
- Continuous requires a person/team-configured schedule or trigger running the workflow in the window and holding.
- Suggest only after Scope permissions is at least Seen specifically for unattended work. Coach on owned commands repeated interactively across three or more sessions.
- Guide: choose a sufficiently familiar owned command, inspect scoped permissions, then let the person request a headless run and use its output.

## Acceptance Criteria

- [ ] Recognize unattended `/release-notes` whose notes are published after the applicability history; reject the same command run interactively without qualifying unattended work.
- [ ] Recognize scheduled `/triage` whose labels are applied; reject ad-hoc `claude -p "summarise this file"`.
- [ ] No output-use evidence means no completed recognition.
- [ ] Missing scoped unattended permissions suppresses the autonomy suggestion, not unrelated evidence collection.
- [ ] Guided setup without a qualifying run/use is incomplete.

## Edge Cases

- Three interactive runs establish applicability; the coach separately specifies three sessions. Preserve that distinction.
- A bare `requires` ID cannot encode the source's run-specific Seen requirement without CLI support.

## Dependencies

- [Scope permissions](scope-permissions.md), [pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Owned workflow history, launch provenance, unattended classification and output-use linkage.

