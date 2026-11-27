# Guard Destructive Commands

## Overview

Source ID `guard-destructive`; Safety, rung 3. Require effective protection around hard-to-undo commands. Intended detection is a code check.

## Requirements

- Applies to repositories with deploy/migration/infrastructure commands and all unattended runs.
- Seen requires a person/team deny or ask rule, or PreToolUse guard, actually applicable to destructive commands in a session.
- Exclude trusting the agent to ask and guards the session's bypass mode skips.
- Cite effective configuration and the relevant session as completion.
- Continuous requires effective guards wherever unattended/parallel work runs and evidence they held in the window, such as an actual block.
- Coach on destructive commands run without approval. The guide helps the person guard their most dangerous relevant command; it does not execute that command to manufacture evidence.

## Acceptance Criteria

- [ ] Recognize an effective PreToolUse guard for force pushes and recursive removal; reject an unguarded agent force push.
- [ ] Recognize an effective ask rule on `terraform apply`; reject a guard skipped by permission bypass.
- [ ] Guard text unrelated to the actual command or repository does not prove coverage.
- [ ] Guided setup with no applicable session stays incomplete/untested rather than prompting a destructive trial.

## Edge Cases

- Ask-rule protection depends on actual session mode. Configuration presence alone cannot establish “whatever mode”.
- Shell spelling, aliases, wrappers and compound commands can affect coverage; never promise universal blocking from a simple regex.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Effective deny/ask/hook enforcement, command coverage and invocation/approval evidence. The current registry's deny-only permission definition cannot express this full contract.

