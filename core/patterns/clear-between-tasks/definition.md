# Clear between tasks

Source ID `clear-between-tasks`; pattern `glenngillen/clear-between-tasks`; Context, rung 1. Reset working memory when changing to unrelated work. Intended detection: model judgement anchored on a genuine clear event.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. A [judge prompt](judge.md) is authored but not executed.

## Applicable work

- A **main session that moves to unrelated work after substantial work** on an earlier task. Substantial work is [`substantial_work_prompts`](../../reference/parameters.md#substantial_work_prompts): at least six of the person's prompts on the prior task (inclusive). Five prompts are not substantial; six are.
- Person prompts exclude tool results, hook output, command output and compaction summaries ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)). Subagent turns never count.
- A session that stays on one task, or a switch after fewer than six prompts, is **no applicable work** for this pattern: nothing is reported, not a miss.

## Recognition

**Seen**: in one main session, after at least six person prompts on a task,

1. the person ran **`/clear`** (a genuine clear event in the session record), and
2. the person's **next prompt started unrelated work**: a different problem, not a continuation, sub-step or follow-up of the prior task.

Completing evidence: the clear record and the next person prompt, both inside the window. Relatedness is a model judgement ([judge](judge.md)); it must cite the prompts it relies on.

Four different events are kept apart:

| Event | Counts as the Seen clear? |
| --- | --- |
| `/clear` run by the person | Yes, when the other conditions hold. |
| **Compaction** (manual or automatic) | No. It summarizes the old task into the context rather than removing it. |
| **Resume** or continue of an earlier session | No. It brings the earlier context back. |
| **Opening a genuinely fresh session** | No for Seen: it is not a clear inside a session. It is relevant only to the [mechanism](#mechanism), where an owned rule may start new tasks in fresh sessions. |

## Exclusions

- **Early clears**: `/clear` after fewer than six person prompts on the prior task (for example after two).
- **Clear followed by the same task**: the next prompt continues the same ticket, file or bug.
- **Compaction**, **resume/continue**, and simply **opening a new session**, as above.
- A clear run by the agent or by software acting on its own behalf, not by the person.
- A guided discussion about clearing with no clear followed by unrelated work.

## Evidence

- **Cite** the `/clear` record and the person's next prompt (exact quotation). Cite at least one prior-task prompt to show the earlier task and its length.
- **Attribution**: the clear and the next prompt are the person's. For Continuous, the scoping rule or command must be the person's or their team's, and must have existed when the session ran.
- **Evidence the pinned CLI does not supply**: clear-event records distinguished from compaction and resume; person-prompt counts per task segment; a task-relatedness judgement over the prompts on either side of the clear; historical instruction or command configuration and evidence that sessions followed it. Existing `/clear` summaries alone do not establish the definition.

## Progression

Default [stages](../../reference/progression.md#stages) apply, with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | One qualifying clear followed by an unrelated person prompt. |
| Forming, Established | Qualifying clears whose follow-through finished: the unrelated task actually proceeded from the cleared context (the agent worked on it without being steered back to the old task). Credited to the week that follow-through finished. Established uses [`most`](../../reference/parameters.md#most) of applicable task switches. |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is a **command or instruction rule the person owns that scopes each session to one task** (for example an instruction to start unrelated work from a clean context, or a saved command that writes a short summary and asks the person to clear).

| Fact | For this pattern |
| --- | --- |
| In place | The rule or command existed, attributable to the person or their team, during the window. |
| Applied | A session reached an unrelated task switch after substantial work while the rule was loaded or the command was run. |
| Held | That switch started from a cleared or genuinely fresh context, as the rule asks. Here a fresh session **does** count, because it is the rule being followed, not the Seen act. |
| Not holding | With the rule in place and applied, an unrelated task still started on top of the earlier task's context. |
| Untested | The rule in place with no applicable task switch in the window. |

## Opportunities and coaching

- **Opportunity**: an unrelated task that inherited a large prior context: at least six person prompts on one task, then a person prompt starting unrelated work without a clear. It cites that person prompt ([opportunities](../../reference/evidence.md#opportunities)), with the problem where recorded (for example, the agent applied the old task's decision to the new one).
- **Coaching**: the [guide](guide.md) asks the person to clear before their next real switch of task.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The intended recognizer needs clear-event parsing, per-task person-prompt counts and a task-relatedness judgement. The pinned CLI (revision `bdea6f6`) supplies none of these as facts, does not execute pack-authored judges, and has no block that expresses them. Matching the text `/clear` would substitute a weaker definition (it cannot tell early clears, same-task continuation or compaction apart), which the pack must not do.

## Missing capabilities

- **Clear-event records** distinct from compaction, resume/continue and new-session creation, attributed to the person.
- **Person-prompt counting per task segment**, excluding tool results, hook output and compaction summaries.
- **Task-relatedness judgement** across the clear, with cited prompts, executed by the CLI's verifier.
- **Historical configuration** of instruction rules and commands, and evidence that a session followed them.
- **A runnable block**: only `tool_call_matches` and `tool_call_sequence` run in the pinned build; neither sees slash-command clears or relatedness.

## Verify before enabling

- Eight prompts on a ticket, `/clear`, then an unrelated export bug is recognized; a clear after two prompts is rejected.
- Six prompts on CSS, `/clear`, then a date bug is recognized; five prompts then a clear is not applicable.
- A clear followed by the same ticket is rejected.
- Compaction, resume and new-session creation are never counted as the Seen clear.
- A guided discussion without a clear and unrelated work earns nothing.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- How broad must "unrelated" be: is a different bug in the same file unrelated work?
  - evidence: The source examples (ticket to export bug, CSS to date bug) are clearly different problems; the spec gives no rule for near-neighbours.
  - options: Treat a different problem statement as unrelated regardless of files; require a different area of the codebase; leave it to the judge with cited prompts.
  - location: core/patterns/clear-between-tasks/definition.md / Recognition
