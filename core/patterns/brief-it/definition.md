# Brief it

Source ID `brief-it`; pattern `glenngillen/brief-it`; Briefing, rung 1. Help the person give the agent the goal and the constraints or context needed to avoid guessing. Intended detection: model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** The request gives the agent the goal, the constraints and the context the work needs, so it doesn't have to guess.

**Why it matters.** The person is the agent's guide for each piece of work ([groups](../../reference/principles.md#groups)). A goal alone leaves the agent to guess what the person already knows: which service to reuse, what must stay untouched, how a limit should behave. A wrong guess becomes a correction later. This is the first rung of Briefing; Define done and Plan first build on it.

**What a recognition shows.** That the person opened a piece of work with its goal and at least one constraint or fact the agent could not otherwise know, and, for later stages, that the work then used it without asking or guessing.

**Why the rules are drawn this way.**

- **Only the first request of a piece of work.** Briefing happens before the agent starts. Later prompts on the same task are steering, and questions or exploration have no work to brief. A window with no new piece of work reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **A goal plus at least one substantive constraint or relevant fact.** A goal alone is exactly what leaves the agent guessing. Length counts neither way: what matters is whether the request carries what the work needs, and background the work never used spares no guess.
- **The brief must be the person's.** An agent-written brief approved with "ok", tool output and compaction summaries are not the person telling the agent anything ([human intent only](../../reference/principles.md#human-intent-only)).
- **Constraints given only after a wrong guess are excluded.** By then the agent has already guessed; that is correcting course ([Steer, don't stop](../steer/definition.md)), not briefing.
- **Seen on the brief; later stages need corroboration.** Sending the brief is the deliberate act, so it is credited promptly. Forming and Established count only briefs the work went on to use, credited when that finished, because context the work never relied on is not a habit worth crediting ([follow-through](../../reference/principles.md#follow-through)). This follows the recorded decision on stage-dependent completion; the original spec required the agent not to have guessed for Seen itself.
- **Continuous needs a saved command, skill or template that is used.** A starting point that asks for the goal and constraints makes briefing happen without remembering ([stages](../../reference/principles.md#stages)). One that exists but was never used is untested, not held ([prevention](../../reference/principles.md#prevention-when-success-removes-the-signal)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. The intended model judgement is described in [judge.md](judge.md), which the pinned CLI does not execute.

## Applicable work

- The **first request of a piece of work**: the opening person prompt of a main session, or the first prompt of a **new task within a session** (a request unrelated to the work before it).
- Follow-up prompts on the same task are not applicable; they are steering, not briefing.
- Questions and pure exploration are not a piece of work to brief.
- A window with no new piece of work is **no applicable work**: nothing is reported, not a miss.
- Where one task ends and the next begins is a judgement the pinned CLI cannot make (see [missing capabilities](#missing-capabilities)).

## Recognition

**Seen** is the person's brief itself, the deliberate act ([stage-dependent completion](../../reference/progression.md#stage-dependent-completion)):

- the request states the **goal**, and
- at least one **substantive constraint** (what to reuse, what must not change, a limit or rule) or **relevant contextual fact** the agent could not otherwise know.

Seen completes when the qualifying brief is sent. Whether the later work used that context is **corroboration**, not a Seen prerequisite (see below).

Source positives: "Add password reset. Use the existing email service, links expire after an hour" (the source's example also shows the work using the email service and the expiry, which is corroboration); an end-date filter request that says the end date is inclusive and existing timezone handling must not change.

Length is neither positive nor negative evidence. A one-line request can be a sufficient brief, and a long one can carry only background.

### Seen versus corroboration

The brief completes Seen when it is sent. **Corroboration** is the later evidence that the context mattered: the agent's work applied the constraint (reused the named service, kept the protected behaviour) without asking or guessing. Corroboration usually finishes later than the brief, often after the **first edit** and sometimes in a later week. It is required for Forming and Established, and is credited to the week it finished. A brief whose corroboration is still pending counts for Seen, not yet for later stages, and is not a miss.

## Exclusions

- **A goal alone**, for example "Add password reset".
- **Irrelevant background**: context the requested work does not need (the source's "background the work never used"), however long. Relevance is judged from the request and the task, not from whether corroboration has arrived.
- **An agent-written brief accepted with "ok"** or similar unread approval. The agent's restatement is not the person's brief unless the person evidently reviewed and changed or confirmed it with substance.
- Constraints supplied only after the agent guessed wrong: that is a correction (Steer, don't stop), not a brief.
- Tool results, hook output, pasted command output and compaction summaries are not the person's request ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).

## Evidence

- **Cite** the person's request as the completing evidence for Seen: an exact quotation of the goal and the constraint or context.
- **Retain** the later work that shows the context was used (the agent action or edit applying it) for Forming and Established; it is not required for Seen.
- **Attribution**: the request is a person prompt in a main session. Text the agent wrote and the person accepted unread is not attributable as the person's brief.
- A truncated or excluded session start is [insufficient](../../reference/evidence.md#insufficient-evidence): unassessed, not a miss.
- Unavailable later work does not undo Seen. When the attributable brief and its task context are available, the brief is Seen; missing follow-up is insufficient only for the corroboration that Forming and Established need.
- **Evidence the pinned CLI does not supply**: task boundaries inside sessions; a judgement of goal, constraint and relevance; linkage from a request to the later work that applied it; use of a saved command, skill or issue template.

## Progression

Default [stages](../../reference/progression.md#stages), with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | One qualifying brief sent inside the window. |
| Forming | Corroborated briefs in at least two distinct weeks of the last four, each credited to the week its corroboration finished. |
| Established | Corroborated briefs on at least [`most`](../../reference/parameters.md#most) of the new pieces of work in the last four weeks. |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session earns Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is a **saved command, skill or issue template the person uses** that asks for the goal and the constraints.

| Fact | For this pattern |
| --- | --- |
| In place | The command, skill or template exists in the person's or their team's configuration during the window. |
| Applied | The person actually started work with it in the window. |
| Held | Work started through it carried the goal and a substantive constraint, and the agent did not have to guess about them. |
| Not holding | Work started through it still missed a constraint that mattered, and the person corrected a wrong assumption. |
| Untested | The template exists but was never used in the window. A template existing without use cannot establish Continuous. |

## Opportunities and coaching

- **Opportunity**: an open request (goal only) that led to a **wrong assumption the person then corrected**. Cite the person's original request and their correcting prompt ([opportunities](../../reference/evidence.md#opportunities)). A bare goal that caused no wrong assumption is not an opportunity.
- **Coaching**: the [guide](guide.md) asks what done looks like and what must not change, then has the person include both in their real request.
- `automate` advice (an owned brief template) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The definition needs a model judgement of intent and relevance plus linkage to later work. The pinned CLI (revision `bdea6f6`) runs no pack-authored judge: its recommendation prompt is built inside the CLI, and only `tool_call_matches` and `tool_call_sequence` execute as fixed checks. A keyword or length heuristic would substitute a weaker definition, which the pack must not do.

## Missing capabilities

- **Task-boundary recognition**: the first request of a piece of work, including new tasks within a session.
- **Pack-driven model judgement** of goal, substantive constraint and relevance, with exact person-authored quotations.
- **Request-to-work linkage**: evidence the later work used the constraint without asking or guessing, with its completion timestamp for week crediting.
- **Correction linkage** for opportunities: a later person prompt correcting an assumption the brief left open.
- **Template-use evidence**: attributable saved commands, skills or issue templates and their invocations.
- **Guided-session markers**, so guided briefs earn Seen only.

## Verify before enabling

- The password-reset brief with the email service and one-hour expiry earns Seen when sent, and counts toward Forming once the work used them; "Add password reset" alone is rejected.
- The inclusive end-date brief protecting timezone handling is recognized; lengthy unused background is rejected.
- An agent-written brief accepted with "ok" is rejected.
- Guide questions answered without a substantive brief earn nothing; a guided brief earns Seen only.
- A template present but unused does not establish Continuous.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- Where does a "new task within a session" begin?
  - evidence: The source applies the pattern to new tasks within a session but gives no boundary rule; the pinned CLI has no task segmentation.
  - options: A model judgement that the request is unrelated to the preceding work; an explicit marker such as `/clear` or a new issue reference; both.
  - location: core/patterns/brief-it/definition.md / Applicable work
- Does a brief still corroborate when the agent asked one clarifying question about a detail the brief did not cover?
  - evidence: Seen completes on the brief; corroboration for Forming and Established requires work that did not need to ask or guess about the brief's details. A question about a different detail is not addressed by the source.
  - options: Count it as corroborated when the question concerns details outside the brief; treat any clarifying question as failed corroboration.
  - location: core/patterns/brief-it/definition.md / Seen versus corroboration
