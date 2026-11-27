# Second opinion

Source ID `second-opinion`; pattern `glenngillen/second-opinion`; Checking the work, rung 8. Obtain and use an independent review before accepting a change. Intended detection: model judgement plus review provenance.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The judgement this pattern needs is described in [judge.md](judge.md), which the pinned CLI does not execute.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- Agent changes from the person's main sessions that are **committed or opened as a pull request** in the window.
- Uncommitted exploration, discarded changes and other people's changes are not applicable.
- A window with no such change is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs both:

1. **An independent review requested or run by the person** on the change before they accepted it. Independent reviewers include:
   - the person's own review agent or command (for example `@agent-reviewer`);
   - a built-in review command such as `/review`;
   - a different model;
   - a fresh reviewer session that **did not write the code**.
2. **The result used**: the findings were **acted on** (fixes made, or a finding explicitly answered and dismissed with a reason), or an **evidenced clean result** was accepted (the reviewer's output exists and reports no blocking finding).

Completing evidence: the review request and its result, plus the follow-through that shows the result was used.

A **built-in** review command counts here, even though built-ins do not establish ownership for Save it. Each pattern keeps its own rule.

## Exclusions

- Asking the **implementing session** whether its own work is right ("Looks right to you?"): it is not independent.
- A review whose findings were **ignored**: the change was accepted with blocking findings neither fixed nor answered.
- A reviewer with a **different name but the same provenance**: a "reviewer" persona inside the session that wrote the change, or a subagent that wrote part of the change. A different name does not prove independence.
- Spontaneous agent self-review the person did not ask for, and reviews performed by another person outside the person's agent work (useful, but not this pattern's evidence).
- A guided review request with no independent execution, or with a result that was never used.

## Evidence

- **Cite** the person's review request (or the owned mechanism that ran the review), the reviewer's result, and the follow-through: the edits that act on findings, or the person's acceptance of a clean result. At least one attributable person-authored citation is required ([attribution](../../reference/evidence.md#attribution-and-citations)).
- **Reviewer provenance**: the reviewing session, agent or model must be shown not to have written the change. A name or persona is not provenance.
- **Change linkage**: the review must be linked to the same change (diff, branch or pull request) that was then accepted.
- **Completion window**: the review request is the initiating act; acting on findings is the follow-through and can finish in a later week ([completion windows](../../reference/evidence.md#completion-windows)).
- **Evidence the pinned CLI does not supply**: reviewer provenance across sessions, agents and models; linkage between a review and the change it reviewed; recognition that a response substantively acts on findings; automated review run records from hooks, CI or pull request mechanisms.

## Progression

No threshold override; the default [stages](../../reference/progression.md#stages) apply, with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | The review request with its result, inside the window. |
| Forming, Established | Only reviews whose findings were **acted on** (or whose clean result was accepted), each credited to the week that action finished. A review with findings still pending counts for Seen, not yet for later stages; it is not a miss. Established needs [`most`](../../reference/parameters.md#most) applicable changes. |
| Continuous | Automated independent review in place, applied and holding (see [mechanism](#mechanism)). |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is an automated independent review: a hook, CI job or pull request reviewer the person or their team owns.

| Fact | For this pattern |
| --- | --- |
| In place | The review hook, CI job or pull request reviewer existed during the window, attributable to the person's or team's configuration. |
| Applied | It actually ran on the person's changes in the window. |
| Held | Its findings were used (acted on, or a clean result accepted) before the changes were accepted. |
| Not holding | A change was accepted without the review running, or with its findings ignored, while it was in place. |
| Untested | In place, but no applicable change in the window. |

## Opportunities and coaching

- **Opportunity**: an unreviewed change that was merged and then **needed fix-ups**. It cites a person-authored moment, such as the prompt accepting or merging the change ([opportunities](../../reference/evidence.md#opportunities)).
- Fix-ups after merge relate to the **Escapes** [outcome](../../reference/outcomes.md); that measure is not wired.
- **Coaching**: the [guide](guide.md) has the person request an independent review of their next real diff and act on it.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement (is this reviewer independent, were the findings used) and provenance across sessions and models. The pinned CLI (revision `bdea6f6`) runs no pack-authored judge, supplies no reviewer provenance and runs no block that expresses either. Matching a `/review` command alone would substitute a weaker definition: running a review is not using its findings, and a reviewer's name is not independence.

## Missing capabilities

- **Pack-authored model judgement**: the active recommendation prompt and output schema are built inside the CLI; [judge.md](judge.md) is not executed.
- **Reviewer provenance**: which session, agent or model produced the review, and whether it wrote any part of the change.
- **Change linkage**: tying a review to the diff, branch or pull request that was accepted.
- **Substantive response recognition**: whether later edits act on the specific findings.
- **Automated review run evidence** from hooks, CI or pull request mechanisms, and a stage engine that reaches `continuous`.
- **Guided-session markers**.

## Verify before enabling

- `@agent-reviewer` review followed by two fixes is recognized; "Looks right to you?" in the implementing session is rejected.
- A fresh session reviewing the branch for bugs, with the result used, is recognized; ignored findings are rejected.
- A built-in review counts here, while built-ins still do not establish ownership for Save it.
- A reviewer with a different name but implementing provenance is rejected.
- Guided review requests without independent execution and result use do not count.
- Unused, held and not-holding mechanism cases produce distinct results.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- What makes a "clean result" evidenced enough to count as used?
  - evidence: The source allows "an evidenced clean result accepted" without saying what the evidence must contain.
  - options: The reviewer's output reports no blocking finding and the person accepts after it; require the review to name what it checked.
  - location: core/patterns/second-opinion/definition.md / Recognition
