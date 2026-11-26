# Give It Instructions

## Overview

Source ID `give-it-instructions`; Guides, rung 1. Recognize useful instructions loaded in repositories the person regularly uses. Intended detection is a code check.

## Requirements

- Applicable repositories have at least three of the person's sessions in the window.
- Seen requires a non-trivial `CLAUDE.md`, `AGENTS.md` or rules file in an applicable repository, actually read by the agent in a session.
- Exclude heading-only, empty or template-only files and Claude Code auto-memory.
- Preserve the source's draft overrides: Forming means presence in two or more applicable repositories; Established means most applicable repositories. “Most” uses the provisional `most` default in [pattern parameters](pattern-parameters.md) (at least 60%, with at least 4 applicable repositories).
- Continuous requires coverage of every applicable repository or a user-level instruction file applying everywhere, updated in the last four weeks, and evidence of application/holding under the shared rule.
- Cite attributable instruction content and its use, not filename existence alone.
- Coach on a frequently used repository without instructions. The guide prompts `/init`, then has the person review the result and add the convention they most often correct.

## Acceptance Criteria

- [ ] Recognize loaded `CLAUDE.md` with build commands/conventions and loaded root `AGENTS.md` plus rules; reject `# Project` alone.
- [ ] Reject repeated conventions in prompts when no instruction file exists.
- [ ] Two sessions alone do not make a repository applicable; three qualify it for assessment.
- [ ] Guided file creation without loading or meaningful review does not prove the complete pattern.
- [ ] Unused, auto-memory and stale-for-Continuous cases remain distinct.

## Edge Cases

- “Non-trivial” beyond a heading and “template-only” need a confirmed deterministic rule before code activation. Do not replace them with an arbitrary byte count.
- File modification time alone does not prove a substantive refresh or historical loading.

## Dependencies

- [Pattern progression](pattern-progression.md), [pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Instruction resolution/provenance, repository/session aggregation, file history and load evidence. `repo_file_matches` is declared but unimplemented in the inspected CLI.

