# Second opinion

Source ID `second-opinion`; pattern `glenngillen/second-opinion`; Checking the work, rung 8. Obtain and use an independent review before accepting a change. Intended detection: model judgement plus review provenance.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The judgement this pattern needs is described in [judge.md](judge.md), which the pinned CLI does not execute.

## Intent

**What it's for.** Before accepting non-trivial work, the person has it reviewed independently: a review subagent, a review command, a different model, or a reviewer prompt that didn't write the code.

**Why it matters.** The session that wrote a change tends to agree with itself. A reviewer that didn't write it reads the diff without that history and catches what the author missed, before the change is accepted rather than after it causes a fix-up. In Checking the work, this adds an independent check on top of the checks the person and the agent already run.

**What a recognition shows.** That the person had a change they were about to accept reviewed by something that didn't write it, got a result back before accepting, and (for later stages) used what it found.

**Why the rules are drawn this way.**

- **Changes the person committed or opened a pull request for.** That is the work being accepted; uncommitted exploration and discarded changes are not. No such change reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **Independence is shown by provenance, not by name.** The value is a reader without the author's history. Asking the implementing session "is this right?", a "reviewer" persona inside that session, or a subagent that wrote part of the change all share that history, so a different name proves nothing ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **The result must return before the change was accepted.** A review that arrives afterwards could not have changed what was accepted.
- **The person asks for it.** Spontaneous agent self-review isn't the person's habit, and a review by another person outside their agent work, while useful, isn't this pattern's evidence ([human intent only](../../reference/principles.md#human-intent-only)). A built-in review command counts, because using a review is the pattern, not owning the reviewer.
- **Seen completes on the request with its result; later stages need the findings used.** A review only helps if it is acted on, so ignored findings never count toward Forming or Established. This staging comes from the recorded completion decision ([follow-through](../../reference/principles.md#follow-through)). What makes a "clean result" evidenced enough is still open.
- **Continuous needs an automated review that holds.** A hook, CI step or pull request reviewer the person or their team owns runs without them remembering; it holds only when its findings are used before acceptance ([stages](../../reference/principles.md#stages)).

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
2. **The review's result returned** before the change was accepted: findings, or an evidenced clean result (the reviewer's output exists and reports no blocking finding).

Per [stage-dependent completion](../../reference/progression.md#stage-dependent-completion), **Seen completes on the review request with its result**, the source's completing event.

**Follow-through** (Forming and Established only): the result was **used**. Findings were **acted on** (fixes made, or a finding explicitly answered and dismissed with a reason), or the evidenced clean result was accepted. Each instance is credited to the week that action finished. Follow-through still pending is unassessed, not a miss. **Ignored findings** (the change accepted with blocking findings neither fixed nor answered) are **failed follow-through**: they never count toward Forming or Established, but they do not withdraw an otherwise qualifying Seen. Under the mechanism they are **not holding**.

A **built-in** review command counts here, even though built-ins do not establish ownership for Save it. Each pattern keeps its own rule.

## Exclusions

- Asking the **implementing session** whether its own work is right ("Looks right to you?"): it is not independent.
- A review whose findings were **ignored** never counts toward later stages (failed follow-through); it still earns Seen when the person's request and its result qualify.
- A review whose result had not returned before the change was accepted: there was no result to use before acceptance.
- A reviewer with a **different name but the same provenance**: a "reviewer" persona inside the session that wrote the change, or a subagent that wrote part of the change. A different name does not prove independence.
- Spontaneous agent self-review the person did not ask for, and reviews performed by another person outside the person's agent work (useful, but not this pattern's evidence).
- A guided review request with no independent execution or no returned result.

## Evidence

- **Cite** the person's review request (or the owned mechanism that ran the review) and the reviewer's result: these complete Seen. **Retain** the follow-through for later stages: the edits that act on findings, or the person's acceptance of a clean result. At least one attributable person-authored citation is required ([attribution](../../reference/evidence.md#attribution-and-citations)).
- **Reviewer provenance**: the reviewing session, agent or model must be shown not to have written the change. A name or persona is not provenance.
- **Change linkage**: the review must be linked to the same change (diff, branch or pull request) that was then accepted.
- **Completion window**: the review request is the initiating act; acting on findings is the follow-through and can finish in a later week ([completion windows](../../reference/evidence.md#completion-windows)).
- **Evidence the pinned CLI does not supply**: reviewer provenance across sessions, agents and models; linkage between a review and the change it reviewed; recognition that a response substantively acts on findings; automated review run records from hooks, CI or pull request mechanisms.

## Progression

No threshold override; the default [stages](../../reference/progression.md#stages) apply, with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | The review request with its result, inside the window. |
| Forming, Established | Only reviews whose findings were **acted on** (or whose clean result was accepted), each credited to the week that action finished. A review with findings still pending counts for Seen, not yet for later stages; it is not a miss. Ignored findings never count here. Established needs [`most`](../../reference/parameters.md#most) applicable changes. |
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
- A fresh session reviewing the branch for bugs, with the result used, is recognized and counts toward Forming; ignored findings are rejected for Forming and Established while the request with its result keeps Seen (pos-7).
- A built-in review counts here, while built-ins still do not establish ownership for Save it.
- A reviewer with a different name but implementing provenance is rejected.
- Guided review requests without independent execution and a returned result do not count; guided use earns Seen only.
- Unused, held and not-holding mechanism cases produce distinct results.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- What makes a "clean result" evidenced enough to count as a result, and its acceptance as used?
  - evidence: The source allows "an evidenced clean result accepted" without saying what the evidence must contain.
  - options: The reviewer's output reports no blocking finding and the person accepts after it; require the review to name what it checked.
  - location: core/patterns/second-opinion/definition.md / Recognition
