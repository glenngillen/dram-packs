# Right-size It

## Overview

Source ID `right-size-it`; Economics, rung 1. Intentionally choose a lighter model for routine work. This is model selection, not the existing IaC resource-sizing pattern. Detection combines judgement with model provenance.

## Requirements

- Applies to routine work (`routine_work` in [pattern parameters](pattern-parameters.md)): renames, docstrings, formatting, version bumps and simple fixes.
- Seen requires a person-selected tier below their usual model before real work, followed by edits on that tier.
- Exclude normal use of the usual model, automatic fallback after limits and ordinary lighter-model subagent runs.
- Cite the person's model command/launch flag/setting and first edit on the lower tier as completion.
- Continuous requires a lighter default with explicit hard-task escalation, premium planning with lighter execution, or an owned command/subagent pinned lighter, actually used and holding.
- Coach on long routine work on premium. The guide has the person select a real routine task, choose a lighter model and switch back when the difficult work needs it.

## Acceptance Criteria

- [ ] Recognize usual Opus, person `/model sonnet`, then docstring edits; reject usual Sonnet simply using Sonnet.
- [ ] Preserve an owned lighter `docs-writer` used twice as a Continuous example; reject automatic Opus fallback after a limit.
- [ ] A model switch without edits does not complete Seen.
- [ ] Guided discussion without the choice and work earns nothing.
- [ ] No fully qualified ID collision or history reuse with IaC sizing.

## Edge Cases

- Lighter subagents are excluded from ordinary Seen but explicitly allowed as configured mechanisms; keep the distinction.
- “Usual model”, routine work beyond the example list and unknown model tiers need established CLI semantics, not an invented averaging rule.

## Dependencies

- [Pack compatibility](pack-compatibility.md), [pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Pricing tiers, model-choice provenance, usual-model facts and edit linkage. Existing recommendation model/repricing signals are useful related capability, not this whole recognition contract.

