# Two at once

Source ID `two-at-once`; pattern `glenngillen/two-at-once`; Delegation, rung 6. Use waiting time for independent work in another isolated active session. Intended detection: model judgement combined with timing facts.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- An **agent turn running at least 5 minutes** (five minutes, inclusive) while the person waits ([`long_turn`](../../reference/parameters.md#long_turn)) in one of the person's main sessions. A 4-minute turn is not applicable; exactly 5 minutes is.
- Subagents and sidechains are not main sessions ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with no such turn is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs all of, as **paired evidence**:

1. **Two main sessions**, each in its own **separate working copy** as defined in [Isolate the run](../isolate-the-run/definition.md#recognition) (a worktree, separate clone, container or VM checkout). Two different repositories are separate working copies.
2. **At least one** of them **interactive**.
3. **Real editing in overlapping minutes**: each session has a person prompt that started its work, and **both** sessions make agent edits during the overlap. The first session's initiating prompt may come before the overlap begins (the second session usually opens while the first is already working, as in pos-1); what must fall inside the overlap is active editing in both.
4. **During an applicable turn**: the overlap falls during an agent turn of at least 5 minutes ([`long_turn`](../../reference/parameters.md#long_turn), inclusive) in one of the sessions. Paired editing during only shorter turns (for example 4 minutes) is outside applicable work: neither Seen nor a miss.

Completing evidence: **each session's initiating person prompt** (the first may precede the overlap), **an edit in each during the overlap**, and the turn duration showing the applicable long turn. One session's evidence alone does not complete the pattern ([cross-session evidence](../../reference/evidence.md#cross-session-evidence)).

Session start and end intervals alone overcount: two sessions open at the same time are not two sessions working. Edit and turn evidence is required.

## Exclusions

- **Idle overlap**: one session working while the other is open but idle.
- **Sessions sharing one directory**, whatever their branches (the isolation decision in Isolate the run: branch-only separation does not qualify).
- **A parent session plus its own subagent**: a subagent is not an independent main session.
- **Sessions that do not overlap**, for example ten minutes apart.
- **Guided setup** without actual paired active work.

## Evidence

- **Cite** each session's initiating person prompt (exact quotes; the first session's prompt may precede the overlap, as in pos-1) and an edit from each session during the overlap, with timestamps showing the overlap, plus each session's environment facts showing separate working copies.
- Missing or excluded history for either session is [insufficient](../../reference/evidence.md#insufficient-evidence): one side's evidence cannot complete the pair, and the gap is not a miss.
- **Evidence the pinned CLI does not supply**: cross-session pairing; per-turn timing and waiting classification against `long_turn`; active-edit timestamps in each session; historical environment facts; parent/subagent linkage; interactive versus headless launch facts.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One paired instance of isolated, actively overlapping editing. |
| Forming | Paired instances in at least two distinct weeks of the last four. |
| Established | At least 60% of applicable long turns used for paired isolated work, with at least four applicable turns ([`most`](../../reference/parameters.md#most)). |
| Continuous | An owned command or script starting isolated parallel sessions, in place, applied and holding (see [mechanism](#mechanism)). |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is an **owned command or script that starts isolated parallel sessions**.

| Fact | For this pattern |
| --- | --- |
| In place | The attributable command or script existed during the window. |
| Applied | It started parallel sessions in the window. |
| Held | Each pair it started did qualifying paired work: each session in its own working copy, at least one interactive, both making edits during overlapping minutes, and the overlap falling during a turn of at least five minutes (`long_turn`) in one of them. Pairs overlapping only during shorter turns, or with no interactive session, are outside applicable work: they neither show it held nor not holding. |
| Not holding | While in place, it started sessions that shared a working copy, or one of the pair sat idle while the person waited through a long turn. |
| Untested | Configured but not used in the window. |

## Opportunities and coaching

- **Prerequisite.** This suggestion is offered **only after Isolate the run is at least Seen** ([safety prerequisites](../../reference/progression.md#safety-prerequisites)). Without that, suggesting parallel sessions would invite two agents into one working copy. The pinned `requires` field takes bare pattern IDs and cannot express "at least Seen", so it is not used to encode a weaker version; the requirement stays here in prose. A missing prerequisite **suppresses the suggestion**, not evidence collection.
- **Opportunity**: with the prerequisite met, the person waited through an applicable long turn with no other session working. It cites the person-authored prompt that started the long turn or the person's next prompt after waiting ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) has the person select two independent real tasks and run them in isolated sessions.
- `automate` advice (an owned command or script starting isolated sessions) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition is a property of a pair of sessions, not one. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence` over a session's tool calls, with no environment facts, no cross-session overlap and no turn-duration facts. It cannot tell idle overlap from active editing, a subagent from an independent session or a shared directory from a separate working copy. The stage-specific Isolate the run prerequisite cannot be encoded by `requires`.

## Missing capabilities

- **Cross-session pairing** of active turns by overlapping minutes.
- **Turn duration and waiting classification** against `long_turn`.
- **Per-session edit timestamps** and person-prompt attribution during the overlap.
- **Historical environment facts** showing separate working copies.
- **Parent/subagent linkage** to exclude a session's own subagents.
- **Stage-scoped prerequisite enforcement** (Isolate the run at least Seen) before suggesting.
- **A runnable model judge** for independent, real work; [judge.md](judge.md) is not executed. Nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- Interleaved refactor and fix edits in separate worktrees are recognized; one working session with one idle is rejected.
- Edits in two repositories during the same minutes are recognized; sessions ten minutes apart without overlap are rejected.
- A parent session plus its subagent cannot count as two independent main sessions.
- Two sessions in one directory on different branches are rejected.
- Guided setup without actual paired active work does not earn Seen.
- Missing isolation prerequisite suppresses the suggestion.
- A turn of exactly 5 minutes is applicable; 4 minutes is not, including when a second isolated session edits during it.
- A pairing script that opens the second session in a shared working copy is mechanism-not-holding evidence, not an opportunity for this pattern.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
