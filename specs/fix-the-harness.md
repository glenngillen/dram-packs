# Fix the Harness

## Overview

Source ID `fix-the-harness`; Guides, rung 7. Recognize a recurring correction eliminated by a relevant harness change. Detection combines model judgement with configuration history.

## Requirements

- Applies to corrections of a kind that already occurred before.
- Seen requires the person's correction, a preventive guide/check/gate change and later applicable sessions in the same repository where that correction no longer recurs.
- Exclude unrelated guide changes and rules after which the same correction continues.
- Cite the correction, harness change and subsequent relevant sessions as completion evidence.
- Preserve the draft Continuous definition: most recurring corrections in the window lead to a harness fix and stop recurring, while satisfying the shared mechanism rule.
- Coach after the same correction in at least three sessions without a guide change. The guide presents actual repeated corrections and asks the person to select one to prevent with a rule or check.

## Acceptance Criteria

- [ ] Recognize two Button-component corrections followed by a lint rule and relevant later UI work without recurrence; reject a CLAUDE.md rule followed by two more of the same correction.
- [ ] Recognize repeated skipped tests prevented by a Stop gate; reject an instruction edit about something never corrected.
- [ ] No later relevant sessions means prevention is untested, not success.
- [ ] A guided harness change alone does not prove the eventual prevention; preserve Seen-only limits for guided evidence.

## Edge Cases

- Follow-up uses `fix_followup` in [pattern parameters](pattern-parameters.md) (at least 2 later applicable sessions within 14 days, no recurrence) and “most” uses `most`. Both are provisional. Too few later applicable sessions means not yet assessable, not a miss.
- Broad “write clean code” rules may be too vague to identify applicability and remain untested.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [pattern progression](pattern-progression.md), [write it down](write-it-down.md).
- Cross-session correction matching, historical mechanism changes and later relevant-work evidence; current recommendation signal reduction is useful context but is not automatically this recognition definition.

