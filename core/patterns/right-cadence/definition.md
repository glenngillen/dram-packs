# Check at the right cadence

Source ID `right-cadence`; pattern `glenngillen/right-cadence`; Economics, rung 4. Match check frequency to the work and model without removing the final quality gate. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A repository with **both** per-step checks ([Gate each step](../gate-each-step/definition.md)) **and** a final gate ([Gate "done"](../gate-done/definition.md)), where the person's work in the window used **more than one model tier** (for example a premium main session and lighter subagents).
- A repository with only one tier in use, or without both kinds of check, is **no applicable work** for this pattern.

## Recognition

**Seen** needs all of:

1. **Person-configured differentiation**: configuration attributable to the person or their team runs step checks on **lighter** work and reduced or skipped step checks on **premium** work (for example per-edit type checks in a lighter subagent's definition, and only the Stop gate in the premium main session).
2. **Both observed model paths**: the lighter path ran its step checks, and the premium path ran with its reduced cadence, each as configured, in the window. **Only one observed path is insufficient.**
3. **The final gate preserved**: the final gate stayed in place and ran on work from both tiers.

Completing evidence: the configuration and the runs under both variants.

How a harness lets checks differ by model (a subagent's own hooks, a model-conditioned setting or something else) must be confirmed from its actual supported configuration. This pattern does not assume any specific syntax.

## Exclusions

- **The same heavy checks at every edit on every model** (for example the full suite after every edit everywhere): not differentiated, so not this pattern. It is not wrong either; it is neutral here.
- **No checks at all**: never praised as efficiency. Removing checks is not a cadence.
- **Removing the final gate** to save time.
- **Configuration with only one path observed**, or configured but unused.
- **Guided review** of cadence without configured and observed differentiated runs.

## Evidence

- **Cite** the attributable configuration and at least one run under each variant (lighter path with step checks, premium path with its reduced cadence), plus the final gate's runs.
- **Historical**: the configuration must have existed and applied when the sessions ran.
- **Never infer** that premium models are infallible or that quiet gates prove quality ([outcomes](../../reference/outcomes.md#rules)). Escapes past the final gate are reported beside the pattern as outcomes, not hidden.
- **Evidence the pinned CLI does not supply**: model-conditioned configuration, hook execution records with the model they ran under, check kind and cost per run, and coverage of both tiers.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One repository with both observed model paths running as configured and the final gate kept. |
| Forming | Both paths observed in at least two distinct weeks of the last four. |
| Established | The configured cadence observed in at least 60% of applicable sessions, with at least four ([`most`](../../reference/parameters.md#most)). |
| Continuous | The [mechanism](#mechanism) applies to all applicable work, with the final gate, in place, applied and holding. |

## Mechanism

The differentiated cadence configuration together with the final gate.

| Fact | For this pattern |
| --- | --- |
| In place | The model-conditioned step checks and the final gate existed during the window, attributable to the person or their team. |
| Applied | Work on both tiers ran under it. |
| Held | All applicable work ran with its configured cadence, both paths were observed, and the final gate ran on work from both tiers. |
| Not holding | Work on one tier ran with the other tier's cadence, the final gate was removed or skipped, or problems the reduced checks would have caught escaped past the final gate. |
| Untested | Configured but only one tier used, or no applicable work. |

## Opportunities and coaching

- **Opportunity**: heavy step checks running on premium work after every edit and catching nothing in the window, in a repository with a final gate. It cites the person-authored prompt that started that work ([opportunities](../../reference/evidence.md#opportunities)). Copy is **neutral**: it reports what ran and what it caught beside the outcomes, and never says those checks are worthless or that the premium model does not need them.
- Repositories with no checks yield no opportunity here; that is Checking the work first.
- **Coaching**: the [guide](guide.md) shows the actual check runs and explains the trade-off. Any reduction is the person's decision and preserves final checking.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. It records no hook runs, no model per hook run and no configuration history, and `hook_configured` is declared but not implemented. A command match would count checks the agent chose to run and could not tell which model path they belonged to.

## Missing capabilities

- **Model-conditioned configuration** facts, including whether the harness supports it.
- **Hook execution records** with the model each ran under, the check kind and its duration or cost.
- **Coverage of both tiers** per repository, and the final gate's runs on each.
- **Configuration history and attribution**.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- Lighter-subagent per-edit type checks with a main premium-session Stop gate are recognized; a full suite after every edit on every model is rejected as evidence of this pattern.
- Only one observed model path is insufficient for Seen.
- No checks are never reported as efficiency.
- Guided review of cadence without configured and observed differentiated runs is incomplete.
- Copy never states that premium models need no checks or that quiet gates prove quality.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
