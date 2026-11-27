# Keep it lean

Source ID `keep-it-lean`; pattern `glenngillen/keep-it-lean`; Guides, rung 3. Suggest reviewing conflicting or measurably expensive instructions while preserving valuable rules. Intended detection: model contradiction judgement combined with code-computed cost.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The judge's authoring prompt is in [judge.md](judge.md) (not executed by the pinned CLI). Related: [Give it instructions](../give-it-instructions/definition.md), [Write it down](../write-it-down/definition.md).

## Intent

**What it's for.** The person keeps their instruction files consistent and worth what they cost: no rules that contradict each other, and a size whose cost to every session is justified.

**Why it matters.** Two instructions that disagree make the agent guess which one was meant, and instruction files that take a large share of the context leave less room for the work. Findings are always a suggestion to review, never to delete: a rule that rarely applies can still be the one that matters most. It keeps what [Give it instructions](../give-it-instructions/definition.md) and [Write it down](../write-it-down/definition.md) build useful.

**What a recognition shows.** That after a contradiction or a measured cost was found, the person asked for a change that resolved it, and, for later stages, that the change was kept.

**Why the rules are drawn this way.**

- **Only two kinds of finding make the files applicable.** A contradiction is flagged only with both lines cited ([evidence for everything](../../reference/principles.md#evidence-for-everything)), judged by a model. Cost is computed by code from real sizes, usage and pricing, never invented; with no load or price evidence there is no cost claim ([code checks facts; a model judges the rest](../../reference/principles.md#code-checks-facts-a-model-judges-the-rest), [missing is not low](../../reference/principles.md#missing-is-not-low)).
- **The cost threshold.** It tries to capture "large enough to measure", so that nothing is said about size below it. Both the share and its strict boundary are a [calibration point](../../reference/principles.md#thresholds-are-calibration-points).
- **Age or rare use never justifies trimming, and deleting a rule the person still wants is not lean-up.** A rule that rarely applies can still be the one that matters most.
- **The person's request for a resolving change.** Agent rewrites, even ones that remove a real conflict, are not the person's act ([human intent only](../../reference/principles.md#human-intent-only)). Requests that only add content neither reconcile nor trim.
- **Seen on the request; later stages need the edit kept.** A lean-up change requested is credited promptly; Forming and Established count only edits that survived `kept_window`, which tries to capture "the change stuck rather than being reverted" and is a calibration point ([follow-through](../../reference/principles.md#follow-through)). This follows the recorded decision on stage-dependent completion; the original spec required the kept change for Seen.
- **Continuous needs a recurring check that runs.** Files that happen to be consistent without a check are not kept that way by anything ([stages](../../reference/principles.md#stages)); a check configured but never run is untested ([prevention](../../reference/principles.md#prevention-when-success-removes-the-signal)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

Repository and user instruction files the agent loads. A finding makes them applicable; there are two kinds:

- **Contradiction**: two instruction lines that conflict (for example, two different test commands). Flagged **only with both conflicting lines cited**.
- **Measured cost**: instruction files loading more than [`instruction_cost_share`](../../reference/parameters.md#instruction_cost_share) of the initial context. The threshold is **strict**: exactly 12% does **not** exceed it. The source's example of instructions taking 12% of the initial context, prompting a split into on-demand rules, is kept as the source's illustration of the provisional, tunable default; the boundary itself is tested separately.

Cost is computed by code from **actual resolved instruction sizes, usage and pricing**, never from a model-invented amount. With no load or price evidence there is **no numeric cost claim** and no cost finding.

**Age or infrequent use alone never justifies trimming.** A ninety-day-old migration rule that has not been used recently is not a finding. All findings **suggest review, never automatic deletion**.

## Recognition

**Seen** needs, in order:

1. A **finding**: a flagged contradiction (both lines cited) or measured cost over the threshold.
2. The **person's attributable request**, after that finding, to reconcile the contradiction, or to trim or split the instructions, keeping the rules they still want. The request must ask for a resolving change, not only an addition.

Per [stage-dependent completion](../../reference/progression.md#stage-dependent-completion), **Seen completes on the lean-up request** (a lean-up change requested), even while the edit is still pending.

**Follow-through** for **Forming and Established**: the **resolving edit** to the instruction files, **kept for [`kept_window`](../../reference/parameters.md#kept_window)** (14 days in the default branch), credited to the week survival is established. An edit still pending, or younger than 14 days, is unassessed for later stages, not failed. An edit that only adds content, or that is reverted within `kept_window`, never counts toward later stages; Seen from the qualifying request stands.

## Exclusions

- **Agent-initiated rewrites**: an unprompted instruction rewrite, even one that removes a real conflict.
- **Requests and changes that only add content**: adding a rule does not reconcile or trim.
- **A guided review with no resolving action**: reading the conflict or the cost and doing nothing.
- **Trimming justified only by age or infrequent use.**
- **A deletion of a rule the person still wants**, presented as lean-up: the pattern preserves valuable rules.

## Evidence

- **Cite** the finding (both contradictory lines, quoted, with their files; or the measured cost with the sizes it was computed from), then the person's request (quoted): these complete Seen. **Retain** the resolving edit and **kept evidence** (the change still in the default branch after `kept_window`); both are required for Forming and Established, not for Seen.
- **Attribution**: the request must be a person prompt; the instruction files must be the person's or their team's.
- **Historical**: the instruction files must have had the conflicting lines or size **when the session ran**. Current files alone do not prove an earlier state.
- **Evidence the pinned CLI does not supply**: historical instruction resolution (which files loaded, with content); contradiction judgement; token counts of resolved instructions against initial context, with usage and pricing; git survival over `kept_window`; recurring-check run evidence.

## Progression

Default [stages](../../reference/progression.md#stages) with the stage-dependent completion above:

| Stage | For this pattern |
| --- | --- |
| Seen | A person's request for a reconciliation or trim/split after a finding, inside the window; the edit may still be pending. |
| Forming, Established | Only requests whose resolving edit was made and kept for `kept_window`, credited to the week survival was established. |
| Continuous | The [mechanism](#mechanism) in place, applied and held. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

A **recurring contradiction check in the person's harness** (for example an owned command or scheduled review that reports conflicting lines and loading cost).

| Fact | For this pattern |
| --- | --- |
| In place | The check exists in the person's or team's harness during the window. |
| Applied | It actually ran over the instruction files in the window. |
| Held | The loaded instruction files were consistent and below the cost threshold in the window. |
| Not holding | While the check ran, a contradiction it should have caught remained, or files grew past the threshold unflagged. |
| Untested | The check is configured but never ran: unused checks do **not** establish Continuous. |

Consistent files without a running check are not Continuous: coverage alone is never enough ([pattern-specific overrides](../../reference/progression.md#pattern-specific-overrides)).

## Opportunities and coaching

- **Opportunity**: a flagged contradiction or over-threshold cost that the person then worked against without reconciling, citing a person-authored moment such as the prompt that hit the conflict (for example, asking why the agent ran the wrong test command). Agent-only evidence is not reported.
- **Coaching**: the [guide](guide.md) shows the actual conflict or measured cost and asks the person to reconcile or reorganize while **retaining every rule they still want**.
- The outcome to watch is **Corrections** ([outcomes](../../reference/outcomes.md)). No cost saving is claimed.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Both halves of the definition need facts the pinned CLI (revision `bdea6f6`) does not supply: a contradiction judgement citing two lines, and a code-computed cost share from resolved instruction sizes. Cached loading treatment and context accounting are unresolved, so detection that depends on them stays disabled. Matching edits to instruction files would recognize additive or agent-initiated changes, which the definition excludes.

## Missing capabilities

- **Historical instruction resolution**: which instruction files a session loaded, with content, including nested and on-demand rules.
- **Contradiction judgement** that cites both lines; a pack-authored judge that runs (`judge.md` is not executed).
- **Token and pricing measurement**: resolved instruction tokens as a share of initial context, with usage and pricing, and a settled treatment of cached loading.
- **Git survival** of the change over `kept_window` in the default branch.
- **Recurring-check evidence**: that the person's check exists, ran, and what it reported.

## Verify before enabling

- Conflicting test commands reconciled at the person's request, and kept, are recognized; an unused ninety-day-old migration rule without a flag is rejected.
- The source example (12% of initial context prompting a split into on-demand rules) is handled under the strict threshold: exactly 12% is not a finding; above 12% is.
- An unprompted instruction rewrite and a guided review with no resolving action are rejected.
- No price or load evidence yields no numeric cost claim; unused checks do not establish Continuous.
- Seen on the request, including with the edit pending (pos-6); Forming only after the resolving edit survives `kept_window`.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- How should cached instruction loading count toward `instruction_cost_share`?
  - evidence: The requirements leave cached loading treatment and context accounting unresolved; cost depends on whether cached tokens count at full share.
  - options: Count resolved instruction tokens regardless of cache; count only uncached tokens; report both.
  - location: core/patterns/keep-it-lean/definition.md / Applicable work
- The source illustrates the threshold with "12% of initial context prompting a split", but the parameter is strictly more than 12%. Should the illustration be restated as an above-threshold figure?
  - evidence: The approved parameter boundary says exactly 12% does not exceed it; the source example uses exactly 12%.
  - options: Keep the illustration labelled as the source's (current); change the illustration to a figure above 12%; make the threshold inclusive.
  - location: core/patterns/keep-it-lean/eval/scenarios.md / pos-2
