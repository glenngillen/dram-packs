# Split it up

Source ID `split-it-up`; pattern `glenngillen/split-it-up`; Delegation, rung 2. Delegate a side task intentionally. Intended detection: model judgement combined with agent provenance.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- Applies to **main sessions that break off to a side task and return**: work that is not the session's main goal (updating snapshots, researching a library, fixing an unrelated flaky test) after which the main work continues.
- Only the person's **main sessions** count. **Subagent histories are not independent main sessions** for applicability or progression; they are evidence attached to their parent session ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with no side task is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs one of:

1. **A person-requested subagent start**: a person prompt asks for a subagent (or "agent", "helper") to take the side task (for example "Use a subagent to update the snapshots"), **and** a subagent actually starts for it afterwards (a Task call or equivalent, linked to a child session).
2. **A person-defined subagent chosen**: the agent selects a subagent **the person (or their team) defined** (for example their own `test-writer`) for the side task, and it actually starts. The definition expresses the person's intent, so no per-request prompt is needed.

Completing evidence: the request (route 1) or the own-agent definition (route 2), and the subagent start.

## Exclusions

- **Unsolicited built-in subagents**: the agent spontaneously starting a built-in agent (for example Explore) with no person request is the model's habit, not the person's delegation.
- **Plugin agents without a delegation request**: a third-party or plugin-supplied agent is not the person's own definition, so it earns no ownership credit; it counts only through route 1.
- **Requests with no actual delegation**: "Do these in parallel" or "use a subagent" followed by the main agent doing the work itself, with no subagent start.
- **Task-call presence alone** never establishes intent or ownership.
- Main-task delegation that is really the whole job, with no main session returning, is not a side task (see [Fan out](../fan-out/definition.md) and [Hands off](../hands-off/definition.md) for other delegation).

## Evidence

- **Cite** the person's request (exact quote from a person prompt, not tool output, hook output or a compaction summary) or the own-agent definition with its attribution, and the subagent start (tool call and child-session link).
- Agent **provenance** must say whether the subagent is built-in, plugin-supplied, or person/team-defined; a name alone is not provenance (a person can define an agent called `explore`).
- **Evidence the pinned CLI does not supply**: request-to-delegation judgement; own/built-in/plugin agent provenance; parent-child session linkage; side-task classification.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One intentional delegation of a side task with an actual subagent start. |
| Forming | Delegations whose subagent finished and returned its result to the main session, in at least two distinct weeks of the last four. Each is credited to the week the result returned. |
| Established | At least 60% of applicable side tasks delegated and returned, with at least four applicable cases ([`most`](../../reference/parameters.md#most)). |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

| Fact | For this pattern |
| --- | --- |
| In place | The person's own subagents and an instruction rule saying when to use them, attributable to the person or their team, existed during the window. |
| Applied | The rule actually led the agent to invoke one of those subagents for a side task in the window. |
| Held | Side tasks the rule covers went to the person's subagents and their results returned to the main session. |
| Not holding | The rule and subagents were in place, but side tasks the rule covers were still done in the main session. |
| Untested | Configured, but no covered side task arose in the window. |

## Opportunities and coaching

- **Opportunity**: the main session took on a distracting side task itself and the main work suffered (lost track, had to be restated, or was left unfinished). It cites the person-authored prompt that introduced the side task or restated the lost main goal ([opportunities](../../reference/evidence.md#opportunities)). Agent-only evidence is not reported.
- **Coaching**: the [guide](guide.md) asks the person for an actual side task and prompts delegation.
- `automate` advice (own subagents plus an instruction rule) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement of the person's request and agent provenance (own, built-in or plugin), linked to a child-session start. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. A match on the Task call would count every spontaneous built-in or plugin subagent, which the definition excludes, so a fixed-pattern approximation must not stand in for it.

## Missing capabilities

- **Attributable request recognition**: classifying a person prompt as asking for delegation, linked to the start that followed.
- **Agent provenance**: whether a started subagent is built-in, plugin-supplied, or person/team-defined, from configuration that existed when the session ran.
- **Parent-child session linkage**, so subagent histories attach to their parent and are not counted as main sessions.
- **Side-task classification** and evidence the result returned to the main session.
- **Instruction-rule application** for the mechanism.
- **A runnable model judge**: [judge.md](judge.md) is not executed.

## Verify before enabling

- "Use a subagent to update the snapshots" followed by a Task call is recognized; a spontaneous built-in Explore is rejected.
- The agent choosing the person's own `test-writer` is recognized; "Do these in parallel" with no subagent start is rejected.
- A plugin agent without the person's delegation request earns no ownership credit.
- Guided delegation advice without actual invocation earns nothing.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
