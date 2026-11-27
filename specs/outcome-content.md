# Outcome Content

## Overview

Document the five intended quality measures and their group associations without inventing unsupported measurements or formulas.

## Requirements

| Measure | Meaning from the source | Groups |
| --- | --- | --- |
| Kept | Agent changes still in the default branch after fourteen days | All; especially Delegation and Economics |
| Rework | Work redone or reverted within seven days, including whether the person asked why before redoing it | Briefing, Correcting course |
| Escapes | Problems discovered after gates passed, including fix-ups, reverts or failing CI on agent work | Checking the work |
| Corrections | Repeated corrections of the same kind | Guides, Correcting course |
| Cost for kept work | API-priced cost of kept changes against the person's own past | Economics |

- Preserve these meanings in content and readiness notes. Wire only a measure whose CLI semantics match; do not use a similarly named block as a substitute.
- Current registry declarations include `reverted_within` and `repeat_correction`. Their presence alone does not prove complete implementation or prove that they cover all the semantics above.
- No time-saved, ROI, productivity score or comparison with other people. Existing recommendation savings calculations are separate behavior and are not replaced by this task.
- Outcomes need their actual underlying cases. Insufficient git history, unknown attribution or a change not yet fourteen days old is unassessed, not a failed kept change.
- Quiet gates are neutral without evidence that they applied and guarded the relevant behavior. Do not call a larger harness successful solely because it ran more checks.
- Per-pattern guide and advice content can name relevant outcomes but must not claim a computed improvement without observed data.

## Acceptance Criteria

- [ ] All five measures and group mappings remain in the content, even where runtime binding is unavailable.
- [ ] Unsupported measures remain documented dependencies, not invented YAML blocks.
- [ ] Kept-dependent pattern acceptance includes the fourteen-day observation delay.
- [ ] Cost copy makes no invented allocation, savings or subscription-charge claim.
- [ ] Missing outcome data cannot become adverse evidence about the person.

## Edge Cases

- Reverts alone do not capture all rework; a one-day revert measure is not seven-day rework or fourteen-day survival.
- The source does not settle cost allocation across changes, a comparable cost weight for next steps, or detailed fix-up matching. These remain unresolved until their measurement contracts are supplied.
- A pattern may improve while its outcomes worsen. Future evidence surfaces must describe both facts without asserting causality from correlation.

## Dependencies

- Git survival, change attribution, gate-to-change linkage, correction matching and pricing measurement capabilities in the CLI.
- [Evaluation readiness](evaluation-readiness.md) and [pattern progression](pattern-progression.md).

