# Right-size it

Source ID `right-size-it`; pattern `glenngillen/right-size-it`; Economics, rung 1. Intentionally choose a lighter model for routine work. Intended detection: model judgement combined with model provenance.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

**Identity.** This pattern is **model selection**. It is not the built-in IaC pattern `infracost/right-size-it` (infrastructure resource sizing). The two load side by side because the pinned loader scopes pattern IDs by organisation ([compatibility](../../reference/compatibility.md#identity)). Findings, history and progress of `infracost/right-size-it` are **never** reused for `glenngillen/right-size-it`, and vice versa.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A session (or stretch of one) doing **routine work** as defined by [`routine_work`](../../reference/parameters.md#routine_work): renames, docstrings, formatting, version bumps and simple fixes. Work outside that list is not automatically non-routine; classifying it is a judgement the recognizer must justify with evidence.
- Only the person's **main sessions** count ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- The person's **usual model** is the reference for "lighter". How the usual model is determined is unresolved (see [open questions](#open-questions)); when it is unknown, or the tier of a model is unknown, the work is **unassessed**. No averaging rule is invented to fill the gap.
- A window with no routine work is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs all of, in this order:

1. **A person-selected lower tier**: before the routine work begins, the person chose a model below their usual tier, with a model command (for example `/model sonnet` when they usually use Opus), a launch flag or a setting they changed.
2. **Real work on that tier**: the agent then made edits for the routine work on the lighter model.

Completing evidence: the person's model command, launch flag or setting, and the **first edit** made on the lower tier. A model switch with **no edits** afterwards does not complete Seen.

## Exclusions

- **Normal use of the usual model**, even when that model is a lighter one: a person who always uses Sonnet and uses Sonnet made no choice.
- **Automatic fallback** after a usage limit or error (for example the harness falling back from one model to another): not the person's act.
- **Ordinary lighter-model subagents** chosen by the harness or a built-in agent. A lighter **owned** subagent or command pinned to a lighter model is a [mechanism](#mechanism), not ordinary Seen evidence.
- **A switch without edits**: choosing a model and doing no work on it.
- **Guided discussion** about models without the choice and the work.
- Anything learned from IaC resource sizing (`infracost/right-size-it`).

## Evidence

- **Cite** the person's model command, launch flag or setting change (exact quote, from a person prompt or attributable configuration) and the first edit on the lower tier.
- **Model provenance per turn**: which model served each turn and why (person choice, configuration, fallback, subagent).
- **Usual model**: the person's normal tier in the period, from facts the CLI supplies; never a guess.
- **Pricing tier** of each model, so "lighter" is a fact rather than a name match. Unknown tiers are unassessed.
- **Evidence the pinned CLI does not supply**: routine-work classification (model judgement), attribution of a model change to the person versus fallback, usual-model facts, pricing tiers as recognition inputs and linkage of edits to the model that made them. The recommendation system's `model` and `model-switch` signals are related inputs, not this whole recognition contract.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One deliberate lighter-tier choice followed by edits on it. |
| Forming | Such choices in at least two distinct weeks of the last four, each credited to the week its routine work finished on the lighter tier. |
| Established | At least 60% of applicable routine tasks done on a deliberately chosen lighter tier, with at least four applicable tasks ([`most`](../../reference/parameters.md#most)). |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)). Whether lighter work was kept and passed its checks is [Let the harness carry it](../harness-carries-it/definition.md), not this pattern.

## Mechanism

Any one of: a **lighter default with explicit hard-task escalation**, **premium planning with lighter execution**, or an **owned command or subagent pinned to a lighter model** (for example the person's own `docs-writer` subagent pinned to a lighter model).

| Fact | For this pattern |
| --- | --- |
| In place | The attributable configuration (default model setting, owned command or subagent definition with a pinned lighter model) existed during the window. |
| Applied | Routine work actually ran through it in the window (for example `docs-writer` invoked twice). |
| Held | That routine work ran on the lighter tier and harder work was escalated deliberately. |
| Not holding | Routine work kept running on the premium tier despite the mechanism, the pinned command or subagent was bypassed for routine work, or lighter runs were routinely finished on the premium tier after failing. |
| Untested | Configured but not used for routine work in the window. |

An ordinary lighter subagent the person did not define is excluded from Seen and is not a mechanism; an owned pinned one is explicitly allowed as a mechanism.

## Opportunities and coaching

- **Opportunity**: a long stretch of routine work ran on the person's premium usual model. It cites the person-authored prompt that started the routine work ([opportunities](../../reference/evidence.md#opportunities)). An unknown usual model or tier yields no opportunity.
- Cost copy, if any, uses only measured API-priced cost where the CLI supplies it ([outcomes](../../reference/outcomes.md#rules)); it makes no savings, allocation or subscription-billing claim.
- **Coaching**: the [guide](guide.md) has the person pick a real routine task, choose a lighter model and switch back if the work turns out to need it.
- `automate` advice (a lighter default or a pinned owned subagent) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. Neither can tell a person's choice from a fallback, know the usual model, classify routine work or link edits to the model that made them. A model-name match would count usual-model use and automatic fallbacks, which the definition excludes.

## Missing capabilities

- **Model-choice provenance**: person command, launch flag or setting versus fallback, subagent or default.
- **Usual-model facts** for the person over the period.
- **Pricing tiers** for models, as a recognition input.
- **Routine-work classification** (model judgement against [`routine_work`](../../reference/parameters.md#routine_work)).
- **Edit linkage**: which model made each edit.
- **Owned subagent/command definitions** with their pinned model, and their invocation records.
- **A runnable model judge**: [judge.md](judge.md) is not executed.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- Usual Opus, person `/model sonnet`, then docstring edits is recognized; usual Sonnet simply using Sonnet is rejected.
- An owned lighter `docs-writer` used twice is preserved as Continuous evidence; an automatic Opus fallback after a limit is rejected.
- A model switch without edits does not complete Seen.
- Guided discussion without the choice and work earns nothing.
- Loaded beside the built-in IaC pack, `glenngillen/right-size-it` and `infracost/right-size-it` do not collide and share no history.
- Unknown usual model or tier is unassessed.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- How is the person's "usual model" determined?
  - evidence: The spec says "usual model" and unknown tiers need established CLI semantics, not an invented averaging rule; no such semantics exist at `bdea6f6`.
  - options: The most-used model by turns over the previous four weeks; the configured default model at session time; leave unassessed until the CLI supplies a fact.
  - location: core/patterns/right-size-it/definition.md / Applicable work
