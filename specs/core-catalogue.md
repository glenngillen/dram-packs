# Core Catalogue

## Overview

Provide the complete initial Dram core pack: evidence-based coaching about a person's use of coding agents, expressed as 41 patterns in eight groups. This is a requirements draft for pack content, not an implementation of the CLI or the wider product.

The user explicitly selected **pack content only**: specify all 41 patterns, disable unsupported detection, and document CLI dependencies. The original production specification was supplied in full in this conversation. Its historical `infracost-ai` name becomes `dram`, consistent with the current CLI.

## Requirements

- Deliver one core pack containing the catalogue below, preserving its local pattern IDs, names, group membership and order. These IDs are the source IDs; the pack is `glenngillen/core` and each pattern is `glenngillen/<source-id>` (see [pack compatibility](pack-compatibility.md)).
- Each pattern has its own specification, recognition definition, exclusions, applicability, evidence requirements, mechanism definition where applicable, coaching copy, guide and evaluation scenarios.
- All 41 are content scope now. The source's staged product releases govern future activation, not which patterns get documented here.
- Use the current Dram pack format rather than implementing the source's illustrative schema. Preserve behavior the format cannot express as clearly identified prose, with the required CLI capability documented.
- Keep recognition, missed opportunities and mechanisms that hold distinct. Do not replace a pattern's meaning with a loose keyword or command match merely to make it executable.
- Provide a repository index, installation instructions, compatibility notes and a per-pattern readiness inventory during the building phase. No publishing, signing service, CLI changes or plugin changes are included.
- No grade, ranking, person-level score, time-saved promise or productivity measure. Findings describe work, never the person's worth or competence.
- No real session histories, personal configuration or credentials belong in repository artifacts. Synthetic evaluation fixtures are distinct from guides: guides use only the person's real work.

| Group | Patterns in order |
| --- | --- |
| Briefing | [Brief it](brief-it.md), [Define done](define-done.md), [Plan first](plan-first.md), [Set the expectations yourself](own-the-expectations.md) |
| Guides | [Give it instructions](give-it-instructions.md), [Write it down](write-it-down.md), [Keep it lean](keep-it-lean.md), [Save it](save-it.md), [Script it](script-it.md), [Reuse your harness](reuse-your-harness.md), [Fix the harness](fix-the-harness.md) |
| Context | [Clear between tasks](clear-between-tasks.md), [Hand it off](hand-it-off.md), [Point, don't paste](point-dont-paste.md) |
| Checking the work | [Prove it](prove-it.md), [Evidence, not claims](evidence-not-claims.md), [Checks by default](checks-by-default.md), [Make failures actionable](actionable-failures.md), [Gate "done"](gate-done.md), [Gate each step](gate-each-step.md), [Back it up in CI](back-it-up-in-ci.md), [Second opinion](second-opinion.md), [Test behaviour](test-behaviour.md), [Schedule the clean-up](schedule-the-clean-up.md), [Learn from production](learn-from-production.md) |
| Correcting course | [Steer, don't stop](steer.md), [Set checkpoints](set-checkpoints.md) |
| Delegation | [Size it](size-it.md), [Split it up](split-it-up.md), [Fan out](fan-out.md), [Hands off](hands-off.md), [Isolate the run](isolate-the-run.md), [Two at once](two-at-once.md) |
| Economics | [Right-size it](right-size-it.md), [Mind the cache](mind-the-cache.md), [Let the harness carry it](harness-carries-it.md), [Check at the right cadence](right-cadence.md) |
| Safety | [Keep secrets out](keep-secrets-out.md), [Scope permissions](scope-permissions.md), [Guard destructive commands](guard-destructive.md), [Sandbox autonomy](sandbox-autonomy.md) |

## Acceptance Criteria

- [ ] The catalogue contains exactly 41 distinct source IDs in the eight groups above, with no omitted or duplicated pattern.
- [ ] Every pattern is represented by complete authoring content, including when its detection cannot run.
- [ ] Installation documentation distinguishes content availability, schema compatibility, evaluability and activation; it never promises 41 working detectors without evidence.
- [ ] Unsupported patterns are explicitly disabled, with concrete dependency reasons and no substituted weaker recognition.
- [ ] The deliverable changes only this pack repository; CLI features, release infrastructure, telemetry and plugin behavior are listed as external dependencies where needed.
- [ ] Missing evidence is described as unassessed or unsupported, never as a failure by the person.

## Edge Cases

- The production spec calls the whole catalogue first-release scope in one chapter but stages it across many releases elsewhere. The user's content-only decision resolves content coverage; it does not authorize premature activation.
- Existing infrastructure sizing has the same `right-size-it` local name as model selection. Its findings and history must not be reused for this different meaning.
- A useful existing generated recommendation may overlap a core pattern without proving that the person performed that pattern. Keep both meanings intact.

## Dependencies

- [Pack compatibility](pack-compatibility.md), [pattern parameters](pattern-parameters.md), [pattern evidence](pattern-evidence.md), [pattern progression](pattern-progression.md), [coaching content](coaching-content.md), [evaluation readiness](evaluation-readiness.md), [outcome content](outcome-content.md).
- [Requirements evidence](requirements-evidence.md) records the sources and the exact current implementation limits.

