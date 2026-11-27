# Set Checkpoints

Source ID `set-checkpoints`; pattern `glenngillen/set-checkpoints`; Correcting course, rung 2. Require a decision before a risky or hard-to-undo step. Intended detection: model judgement plus configuration checks.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A **risky decision point** in the person's main session: running a migration, a deploy, a deletion (of data, files or resources) or a public API change, or another step whose risk the evidence shows (hard to undo, affecting shared or production state).
- Risk classification must rest on evidence about the step. **Not every shell command is risky**: `ls`, a test run or a local build is not a decision point.
- Only the person's **main sessions** count; subagents, sidechains and Dram's own analysis sessions do not ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with no risky step is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs all of, in this order:

1. A **person-authored request to stop** before the risky step: "draft the migration and ask before running it", "show me the deploy plan and wait".
2. The agent **actually stopped** at that point: it did not run the step, and asked or waited.
3. The **person's decision**: a person prompt approving, changing or declining the step ("run it, skip the backfill").

Completing evidence: the checkpoint request and the person's decision, with the agent's stop between them. The decision is part of the deliberate act: a checkpoint nobody answered is not complete. Whether the step then succeeded is recorded separately and is not required.

**Automatic approval cannot stand in for the person's decision.** An auto-approve setting, a permission-skipping mode or a script answering "yes" is not the person deciding.

## Exclusions

- **Spontaneous agent questions**: an unprompted "Shall I proceed?" the person did not ask for. A welcome habit of the model, but not the person's checkpoint.
- **Unanswered checkpoints**: the agent stopped and asked, and the person never decided (the session ended or moved on).
- **A requested stop the agent bypassed**: it ran the step anyway. Not Seen; for a mechanism this is not holding.
- **Automatic approval** of the stop.
- **Guided wording without the actual stop and decision**: writing the checkpoint into a prompt during the guide does not complete Seen until the agent stops and the person decides.
- **Steps that are not risky**, however the request is phrased.

## Evidence

- **Cite** the person's checkpoint request and decision (exact quotes from person prompts, not tool output, hook output or a compaction summary), the risky step and the agent's stop between them, with timestamps.
- For the mechanism, cite the attributable instruction or ask-permission rule, the **historical permission mode** of the session (a rule that applies only in some modes may not have applied), and the stop it caused.
- An instruction or rule must have **existed and applied when the session ran** ([cross-session evidence](../../reference/evidence.md#cross-session-evidence)); current configuration alone cannot prove a past stop.
- Missing or **truncated** records between the stop and the decision leave the checkpoint unknown: insufficient, not a miss.
- **Evidence the pinned CLI does not supply**: classification of person prompts as checkpoint requests and decisions; the decision sequence (request, stop, decision); evidence-based risk classification of steps; historical permission mode; effective ask rules and whether they fired.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One requested stop before a risky step, the agent stopping, and the person's decision. |
| Forming | Such checkpoints in at least two distinct weeks of the last four, each credited to the week the person decided. |
| Established | At least 60% of applicable risky steps checkpointed and decided, with at least four applicable steps ([`most`](../../reference/parameters.md#most)). |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is an **instruction rule** ("stop and ask before running migrations or deploys") or an **ask-permission rule** on the commands that perform risky steps (for example an ask rule on `db:migrate`), configured by the person or their team.

| Fact | For this pattern |
| --- | --- |
| In place | The attributable instruction or ask rule existed during the window, covering the risky step. |
| Applied | It actually stopped the agent before a covered risky step in a session in the window. |
| Held | Every covered risky step in the window was stopped, and the person made the decision each time (for example an ask rule on `db:migrate` stopping the agent twice, decided both times). |
| Not holding | A covered risky step went ahead without the stop: the agent bypassed the requested stop, or the stop was skipped by automatic approval or a permission-skipping mode. |
| Untested | In place, but no covered risky step happened in the window. |

The pinned `permission_rule` block accepts **deny only**, and has no fixed-pattern execution, so an **ask rule** cannot be bound in `pattern.yaml`. Its semantics stay in this prose; no ask binding is invented.

## Opportunities and coaching

- **Opportunity**: a risky step went ahead without the person's approval and the person then **undid it** (reverted the migration, rolled back the deploy, restored the deleted files). It cites the person-authored moment: the prompt that started the work or the one that asked for the undo ([opportunities](../../reference/evidence.md#opportunities)). A risky step visible only in agent or tool output, with no person turn, is not reported.
- **Coaching**: the [guide](guide.md) has the person specify a real checkpoint before their next risky task.
- `automate` advice (an instruction or ask rule) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement of a checkpoint request and the person's decision, the ordering of request, stop and decision, and evidence-based risk classification. The mechanism needs effective ask rules, historical permission mode and evidence that a rule actually stopped the agent. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence` as fixed checks; its `permission_rule` block is deny-only with no fixed-pattern execution. Matching a migration command alone would count unchecked steps, so a fixed-pattern approximation must not stand in for it.

## Missing capabilities

- **Checkpoint judgement**: classifying a person prompt as a request to stop before a step, and a later one as the person's decision.
- **Decision-sequence recognition**: the order of request, agent stop (no step executed) and person decision.
- **Risk classification**: evidence that a step is a migration, deploy, deletion or public API change, rather than treating every shell command as dangerous.
- **Historical permission mode** per session, and whether automatic approval answered the stop.
- **Effective ask rules**: an `ask` permission contract (the pinned `permission_rule` is deny-only) with evidence that the rule fired.
- **A runnable model judge**: the active recommendation prompt is built inside the CLI; [judge.md](judge.md) is not executed.

## Verify before enabling

- "Draft the migration and ask before running it", an actual stop, then "Run it, skip the backfill" is recognized; an unprompted "Shall I proceed?" is rejected.
- An ask rule on `db:migrate` stopping the agent twice, decided both times, is mechanism evidence; an unanswered checkpoint is rejected.
- A requested stop the agent bypassed is not holding and not Seen.
- Automatic approval never counts as the person's decision.
- Guided wording without the actual stop and decision is incomplete.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
