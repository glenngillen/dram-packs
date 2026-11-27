# Outcomes

The five quality measures this pack intends to report beside its patterns. They describe whether agent work held up. They are never a productivity measure, a time-saved or ROI figure, or a comparison with other people.

**None is wired at runtime.** The pinned Dram CLI's block registry (`internal/pack/blocks.json`) declares two `measure` blocks, `reverted_within` and `repeat_correction`, but no Go code at that revision references either name outside a loader test, so declaring them measures nothing. Their semantics also do not match these definitions: a revert within N days is not seven-day rework (which includes redone work and whether the person asked why) and is not fourteen-day survival in the default branch. This pack therefore ships **no `outcomes.yaml`**, and no pattern lists `outcomes`.

| Measure | Meaning | Groups |
| --- | --- | --- |
| **Kept** | Agent changes still in the default branch after fourteen days ([`kept_window`](parameters.md#kept_window)). | All; especially Delegation and Economics |
| **Rework** | Work redone or reverted within seven days, including whether the person asked why before redoing it. | Briefing, Correcting course |
| **Escapes** | Problems discovered after gates passed, including fix-ups, reverts or failing CI on agent work. | Checking the work |
| **Corrections** | Repeated corrections of the same kind. | Guides, Correcting course |
| **Cost for kept work** | API-priced cost of kept changes against the person's own past. | Economics |

## Rules

- **Wire only a measure whose CLI semantics match.** A similarly named block is not a substitute.
- **Outcomes need their actual underlying cases.** Insufficient git history, unknown attribution or a change not yet fourteen days old is **unassessed**, not a failed kept change.
- **Kept-dependent acceptance includes the fourteen-day observation delay.** A change cannot be judged kept until the window has passed.
- **Missing outcome data is never adverse evidence** about the person.
- **Quiet gates are neutral** without evidence that they applied and guarded the relevant behaviour. A larger harness is not more successful because it ran more checks.
- **Cost copy makes no allocation, savings or subscription-charge claim.** "API-priced" means priced at list API rates for comparison with the person's own past; it is not what anyone was billed.
- Guides and advice may name a relevant outcome. They never claim a computed improvement without observed data.
- A pattern may improve while its outcomes worsen. Describe both facts; do not assert causality from correlation.

## Unresolved semantics

| Area | Not settled by the source |
| --- | --- |
| Cost allocation | How cost is allocated across changes, and a comparable cost weight for next-step ordering. |
| Fix-up matching | How a later fix-up is linked to the agent change it repairs (Escapes, Rework). |
| Correction equivalence | When two corrections are "of the same kind" (Corrections). |
| Gate linkage | How a passing gate is linked to the change it covered (Escapes). |

## External dependencies

Git survival over fourteen days, change attribution, gate-to-change linkage, correction matching and pricing measurement, all in the CLI.

## Open questions

- How should cost be allocated across changes for Cost for kept work?
  - evidence: The source defines the measure but not an allocation rule; the outcome spec leaves it unresolved.
  - options: Allocate session cost by changed lines kept; report session-level cost only for sessions whose changes were all kept.
  - location: core/reference/outcomes.md / Unresolved semantics
- How is a fix-up matched to the agent change it repairs?
  - evidence: Escapes and Rework depend on it; no matching contract was supplied.
  - options: Same files within seven days; commit message or PR linkage; a model judgement with cited evidence.
  - location: core/reference/outcomes.md / Unresolved semantics
