# glenngillen/core

Evidence-based coaching about how a person works with coding agents: 41 patterns in eight groups (Briefing, Guides, Context, Checking the work, Correcting course, Delegation, Economics, Safety). Findings describe work, never the person. There is no grade, score, ranking, streak or productivity measure.

**This version is content only.** Every pattern is disabled (`enabled: false`) because the detection it needs is not yet in the Dram CLI. Installing the pack makes the definitions, copy and guides available; it does not make Dram recognize any pattern. See [readiness](reference/readiness.md) for each pattern's status and [compatibility](reference/compatibility.md) for the CLI revision it was checked against.

## Why it works this way

Start with [principles](reference/principles.md): what the pack is for, and the reasoning behind every rule (human intent only, false positives are worse than misses, evidence for everything, applicable work, stages and mechanisms, prevention, outcomes, safety before autonomy, and why every threshold is a calibration point). Each pattern's `definition.md` opens with an **Intent** section that applies that reasoning to the pattern.

## Shared references

| Reference | What it settles |
| --- | --- |
| [Principles](reference/principles.md) | The over-arching reasoning for the framework, and what each group is for. |
| [Evidence](reference/evidence.md) | Attribution, person-authored citations, opportunities, completion windows, mechanisms in place/applied/held, privacy, insufficient evidence. |
| [Parameters](reference/parameters.md) | Every provisional threshold, with its origin and boundary. |
| [Progression](reference/progression.md) | Stages, stage-dependent completion, guided Seen-only, the automation gate, safety prerequisites, next-step ordering. |
| [Outcomes](reference/outcomes.md) | The five intended quality measures and their groups. |
| [Authoring and readiness](reference/authoring.md) | The pattern directory, the per-pattern checklist and the readiness vocabulary. |
| [Verification scenarios](reference/verification.md) | Pack-wide rejections a recognizer must make (fabricated citations, changed quotes, agent-only attribution, out-of-window completion), all unevaluable at the pinned CLI. |
| [Compatibility](reference/compatibility.md) | Pinned CLI revision, `min_cli`, identity, what runs and the checks performed. |
| [Readiness](reference/readiness.md) | One status row per pattern. |

## Patterns

Each pattern's `definition.md` starts with its intent: the problem it solves, why it matters and why its rules are drawn as they are. Each pattern directory holds `pattern.yaml`, `text.yaml`, `guide.md`, `definition.md` and `eval/` (cases plus full scenarios). [Give it instructions](patterns/give-it-instructions/definition.md) is the complete reference pattern.
