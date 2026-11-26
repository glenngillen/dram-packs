# Checks by Default

## Overview

Source ID `checks-by-default`; Checking the work, rung 3. Recognize checks that run because the person's harness asks for them. Detection combines configuration checks with model judgement.

## Requirements

- Applies to code-changing sessions in repositories with relevant checks.
- Seen requires an instruction rule or hook directing checks after changes and an actual subsequent check without a fresh person prompt.
- Exclude spontaneous model habits with no instruction, and rules never followed.
- Cite the attributable rule/hook and resulting check execution as completion.
- Continuous requires the rule or hook in every applicable repository and followed in the window, with applied/held evidence.
- Coach when code-changing sessions end without checking. The guide asks the person to add their real test/type-check commands to the instructions with an after-change requirement.

## Acceptance Criteria

- [ ] Recognize `CLAUDE.md` instructing `make test` after edits followed without prompting; reject unprompted tests when no rule exists.
- [ ] Recognize an owned PostToolUse hook running `tsc` after edits; reject configuration with no execution.
- [ ] An instruction added after the session cannot prove it caused that session's check.
- [ ] Guided rule creation without a subsequent followed session remains incomplete for Seen.

## Edge Cases

- Coverage is over applicable repositories, not every directory on the machine.
- A check failure is recorded honestly; mere execution cannot establish that an unresolved violation held.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [pattern progression](pattern-progression.md), [evaluation readiness](evaluation-readiness.md).
- Historical instruction resolution, check-kind classification, prompt/run ordering and repository coverage. Declared hook checks currently do not execute in the fixed-pattern engine.

