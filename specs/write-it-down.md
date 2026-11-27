# Write It Down

## Overview

Source ID `write-it-down`; Guides, rung 2. Turn a corrected convention into instructions instead of repeating it. Detection requires model judgement.

## Requirements

- Applies to corrections of conventions or preferences, not one-off defects.
- Seen requires the person's request to record a rule, a person `#` memory entry or `/init`, followed by a substantive instruction-file addition.
- Exclude unprompted agent instruction edits, typo-only edits and “remember this” without a persisted change.
- Cite the person's request/command and the instruction edit as completion.
- Continuous requires the specific rule to apply in later sessions and hold without renewed correction. Mere absence of later activity is not proof.
- Coach when the same convention is corrected in two sessions. The guide asks what the person keeps correcting and has them request a persistent instruction.

## Acceptance Criteria

- [ ] Recognize “We use tabs. Add that to CLAUDE.md” followed by the added rule; reject an unprompted instruction rewrite during refactoring.
- [ ] Recognize `# never run migrations locally` when persisted; reject “Remember to use tabs” without an edit.
- [ ] A guided answer describing a convention without requesting/persisting it earns nothing.
- [ ] A rule followed in relevant later work can support held evidence; a repeated violation becomes not holding.

## Edge Cases

- An unused rule remains in place but untested.
- Fix the harness is broader: it requires prior recurring correction and demonstrated prevention, and can use checks or gates as well as instructions.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md), [fix the harness](fix-the-harness.md).
- Person command provenance, instruction diffs, correction recognition and later applicable-work evidence; current tool matches cannot establish these.

