# Plan first

Source ID `plan-first`; pattern `glenngillen/plan-first`; Briefing, rung 3. Recognize the person's review of a plan before a multi-file change. Intended detection: model judgement, plus configuration checks for its mechanism.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** On a change across several files, a plan is agreed before edits start, however it was proposed. The person's act is reviewing it.

**Why it matters.** Once an agent has edited several files, changing direction means undoing work; a plan is cheap to correct. Reading it before edits begin is the person's chance to catch the wrong approach, a missed constraint or a file that should not change. In Briefing, it is how the person guides the way the work gets done ([groups](../../reference/principles.md#groups)).

**What a recognition shows.** That the person engaged with a plan before a change that then went on to edit two or more files.

**Why the rules are drawn this way.**

- **Changes that edit at least two files.** That is where changing direction means undoing work, so a reviewed plan for a one-file change is excluded. The two-file boundary tries to capture "a change across several files" and is a [calibration point](../../reference/principles.md#thresholds-are-calibration-points). A window with no such change reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **Who proposed the plan doesn't matter; the person's review does.** The value is in the person's response, so an agent-originated plan counts through that review ([human intent only](../../reference/principles.md#human-intent-only)).
- **No person turn, no review.** Plans approved automatically in headless or permission-bypass runs, and plans nobody answered, were never checked by anyone.
- **Before the multi-file edits began.** A plan asked for after the second file was edited can no longer prevent the undoing. A plan after a single initial edit is left unassessed rather than settled by a convenient ordering rule ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **The second file's edit completes it.** It ties the review to a change that really did span several files, so act and follow-through belong to the same Seen event.
- **Whether an unread "ok" or "go" counts is not yet settled.** It is the substantive-review judgement shared across Briefing, recorded as an open question.
- **Continuous needs a rule or default setting that held.** A planning rule or default plan mode makes the plan happen without remembering ([stages](../../reference/principles.md#stages)); it must have been in place at the time, and a setting with no multi-file change to apply to is untested ([prevention](../../reference/principles.md#prevention-when-success-removes-the-signal)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. The intended model judgement is described in [judge.md](judge.md), which the pinned CLI does not execute.

## Applicable work

- A change in a main session that **edits at least two files**.
- One-file changes are not applicable.
- A window with no multi-file change is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** requires, in order:

1. **A proposed plan** before multi-file edits began. The plan may originate with the person (they asked for one, or entered plan mode) or with the agent (for example the agent called `EnterPlanMode`).
2. **The person's review**: an approval, adjustment or question that engages with the plan. The review is the intentional act; an agent-originated plan counts only through it.
3. **Subsequent edits to at least two files**. The edit to the second file is the completing evidence.

Source positives: the person enters plan mode, reviews with "keep the old API", then four files are edited; "propose an approach, don't change anything yet", an approval, then two files edited; the agent's `EnterPlanMode`, then the person's "split the migration into its own step", then three files edited.

### The first-edit boundary

The source does not settle where "before multi-file edits" begins when the agent has already edited **one** file before the plan is proposed. A plan requested after two files were edited is clearly too late. A plan proposed after a single initial edit (for example a scaffolding file) is **unresolved**: such boundary cases stay pending and unassessed rather than being decided by a convenient ordering rule (see [open questions](#open-questions)).

## Exclusions

- **Automatic approval** in unattended or permission-bypass runs, including headless runs where the plan was approved with no person turn.
- **Unanswered plans**, or exiting plan mode with no person review.
- **One-file changes**, even with a reviewed plan.
- **Plans requested after multi-file edits began** (after the second file was edited).
- Unread approval ("ok", "go") is a weak review; whether it counts is the same substantive-review judgement used across Briefing (see [open questions](#open-questions)).

## Evidence

- **Cite** the plan request or plan-mode event, the person's review prompt (quoted exactly) and the second file's edit as completion.
- **Ordering**: plan before the second edited file; review before the edits it governs.
- **Attribution**: the review is a person prompt in a main session; tool-approval output and hook output are not reviews.
- **Unattended** runs follow [completion windows](../../reference/evidence.md#completion-windows): with no person turn there is no review.
- **Evidence the pinned CLI does not supply**: plan-mode provenance (who entered it, and how it was exited); recognition that a person prompt reviewed the plan; per-file edit ordering; default plan mode or plan-then-execute settings and their history. A tool-call sequence alone cannot establish these.

## Progression

Default [stages](../../reference/progression.md#stages). The person's review and the second file's edit both belong to the Seen event; Forming and Established credit each instance to the week its second-file edit finished.

| Stage | For this pattern |
| --- | --- |
| Seen | One reviewed plan before a change that then edited at least two files. |
| Forming | Such instances in at least two distinct weeks of the last four. |
| Established | Such instances on at least [`most`](../../reference/parameters.md#most) multi-file changes in the last four weeks. |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session earns Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is a **relevant instruction rule, default plan mode or plan-then-execute setting** in the person's or their team's configuration.

| Fact | For this pattern |
| --- | --- |
| In place | The rule or setting existed, attributable, during the window (historical configuration, not today's). |
| Applied | It engaged on multi-file work in the window: sessions started in plan mode, or the rule produced a plan. |
| Held | Those multi-file changes began with plans the person reviewed. Source example: default plan mode followed by reviewed plans in three sessions. |
| Not holding | Multi-file edits began before a plan, or plans were approved without review, while it was in place. |
| Untested | The setting existed but no multi-file change happened in the window. |

## Opportunities and coaching

- **Opportunity**: a multi-file change followed by **corrections that planning could have prevented**. Cite the person's request starting the change and their correcting prompt ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) has the person choose an upcoming multi-file change and agree a plan before edits.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

`tool_call_sequence` could match a plan-mode call followed by edits, but that would accept automatic headless approval and miss the person's review, which is the intentional act. The pinned CLI (revision `bdea6f6`) runs no pack-authored judge for review recognition and supplies no plan-mode provenance or settings history. Enabling from the sequence alone would weaken the definition.

## Missing capabilities

- **Plan-mode provenance**: whether the person or the agent entered plan mode, and how it was exited.
- **Pack-driven model judgement** that a person prompt reviewed the plan, with exact quotation.
- **Per-file edit ordering** relative to the plan and the review, counting distinct files.
- **Unattended/bypass classification** of the run.
- **Historical configuration**: default plan mode, plan-then-execute settings and instruction rules, with attribution.
- **Correction linkage** for opportunities; **guided-session markers**.

## Verify before enabling

- Person-entered plan mode, "keep the old API" review and four edited files are recognized; automatic headless approval is rejected.
- "Propose an approach, don't change anything yet", approval and two edited files are recognized; a one-file plan is rejected.
- Agent `EnterPlanMode`, "split the migration into its own step" and three edited files are recognized; exit without review is rejected.
- Default plan mode with reviewed plans in three sessions establishes held; a plan requested after two files were edited is rejected.
- Guided planning without review and subsequent applicable work does not count.
- First-edit boundary cases stay unassessed until the boundary is decided.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- Does a plan proposed after one initial file edit still count as "before multi-file edits"?
  - evidence: The source requires a plan before multi-file edits and rejects a plan after two files, but does not settle a plan after exactly one edit; the requirements say to keep such cases pending.
  - options: Count it if the plan precedes the second file's edit; require the plan before the first edit; treat the case as unassessed permanently.
  - location: core/patterns/plan-first/definition.md / Recognition
- Is a bare "ok" or "go" on a plan a review?
  - evidence: The source requires approval, adjustment or questions; elsewhere in Briefing "ok" on agent-written content is unread approval.
  - options: Count any explicit approval; require the review to reference the plan's content; count it only for short plans.
  - location: core/patterns/plan-first/definition.md / Exclusions
