# Write it down

Source ID `write-it-down`; pattern `glenngillen/write-it-down`; Guides, rung 2. Turn a corrected convention into instructions instead of repeating it. Intended detection: model judgement, with instruction-file diffs and later-session evidence.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The judge's authoring prompt is in [judge.md](judge.md) (not executed by the pinned CLI). Related: [Give it instructions](../give-it-instructions/definition.md) (the file exists and loads) and Fix the harness (broader, below).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A **correction of a convention or preference**: the person tells the agent how this project or this person does something ("we use tabs", "never run migrations locally", "use pnpm"). It applies beyond the current change.
- **Not applicable**: a correction of a one-off defect ("that variable name is misspelled", "the test on line 40 is wrong"). Fixing a bug is not a convention.
- Corrections are person prompts in main sessions. Tool results, hook output and compaction summaries are not person prompts ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with no convention correction is **no applicable work**: nothing is reported.

## Recognition

**Seen** needs both, in order:

1. **The person's deliberate request** to persist the rule: asking the agent to record it ("We use tabs. Add that to CLAUDE.md"), a person-entered `#` memory entry (for example `# never run migrations locally`), or the person running `/init`.
2. **A substantive instruction-file addition** that followed: a rule actually written to an instruction file the agent loads (repository or user-level), stating the convention.

Completing evidence: the person's request or command, and the instruction edit (the diff adding the rule). A transcript containing the word "remember" or a `#` character is not proof; the persisted change is.

## Exclusions

- **Unprompted agent instruction edits**, for example the agent rewriting `CLAUDE.md` during a refactor without the person asking.
- **Typo-only or formatting-only edits** to an instruction file.
- **"Remember this" without a persisted change**: "Remember to use tabs" followed by no instruction-file edit.
- **One-off defect corrections**, even if written down.
- **Auto-memory the agent writes for itself** without the person's request.
- A **guided answer** that describes a convention without requesting or persisting it.

## Evidence

- **Cite** the person-authored request (quoted exactly) or the person's `#`/`/init` command, and the instruction-file edit with the added rule quoted.
- **Attribution**: the request must be a person prompt; the edit must follow it and be traceable to it. An edit with no attributable person request is not recognized.
- **Historical**: for held evidence, the rule must have existed in the instruction file and been loaded **when the later session ran**. Current configuration alone does not prove a past session had it.
- **Evidence the pinned CLI does not supply**: person command provenance (a `#` entry or `/init` typed by the person, as opposed to agent text); instruction-file diffs linked to the request; classification of a correction as convention versus defect; which instruction files later sessions loaded; later corrections of the same convention.

## Progression

Default [stages](../../reference/progression.md#stages) with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | The person's request plus the substantive addition, inside the window. |
| Forming, Established | Instances whose rule was **kept** in the instruction file (not reverted) and applied in later relevant work; credited to the week that follow-through finished. Established uses [`most`](../../reference/parameters.md#most) of convention corrections. |
| Continuous | The [mechanism](#mechanism) below in place, applied and held. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the persisted rule itself: an instruction the agent loads that carries the convention into later sessions without the person.

| Fact | For this pattern |
| --- | --- |
| In place | The rule exists in an instruction file attributable to the person (or their team), during the window. |
| Applied | A later session did work the rule covers and loaded the file containing it. |
| Held | In that later relevant work the agent followed the rule and the person did not correct the same convention again. |
| Not holding | The person corrected the same convention again in relevant work while the rule was in place and loaded. |
| Untested | The rule is in place but no later session did relevant work. An unused rule is in place but untested, not held. |

**Mere absence of later activity is not proof** that the rule held. Silence in unrelated sessions is not a before/after comparison ([mechanisms](../../reference/evidence.md#mechanisms-in-place-applied-held)).

## Opportunities and coaching

- **Opportunity**: the **same convention corrected in two sessions** with no persisted rule, **or** the same convention corrected again in relevant work while the persisted rule was in place and loaded (not holding). A missing rule and a rule that did not hold are distinct findings. Missing historical loading evidence is insufficient, not an opportunity. It cites the person's second correcting prompt ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) asks what the person keeps correcting and has them request a persistent instruction.
- The outcome to watch is **Corrections** ([outcomes](../../reference/outcomes.md)); no improvement is claimed without observed data.
- **Fix the harness is broader**: it requires a prior recurring correction and demonstrated prevention, and may use checks or gates as well as instructions. A Write it down recognition does not automatically earn Fix the harness.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs model judgement (convention versus one-off defect; deliberate request versus agent initiative) and evidence the pinned CLI (revision `bdea6f6`) does not supply. The pinned CLI runs only `tool_call_matches` and `tool_call_sequence`; matching an edit to `CLAUDE.md` would recognize unprompted agent rewrites and typo fixes, a weaker definition the pack must not substitute.

## Missing capabilities

- **Person command provenance**: whether a `#` memory entry, `/init` or request was typed by the person.
- **Instruction diffs**: the content added to an instruction file, linked to the request that caused it.
- **Correction recognition**: a judged classification of a person prompt as a convention correction, and matching of later corrections to the same convention.
- **Historical instruction loading** in later sessions, and the rule's presence at that time.
- **A pack-authored judge that runs**: the active recommendation prompt is built inside the CLI; `judge.md` is not executed.

## Verify before enabling

- "We use tabs. Add that to CLAUDE.md" followed by the added rule is recognized; an unprompted instruction rewrite during refactoring is rejected.
- `# never run migrations locally`, persisted, is recognized; "Remember to use tabs" without an edit is rejected.
- A guided answer describing a convention without persisting it earns nothing.
- A rule followed in relevant later work supports held evidence; a repeated violation is not holding; an unused rule is untested.
- A one-off defect correction is not applicable.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- How is a later correction matched to "the same convention" for not-holding and for the two-session coaching trigger?
  - evidence: The source requires the specific rule to hold without renewed correction, but defines no matching rule between differently worded corrections.
  - options: Model judgement citing both corrections and the rule; exact rule-text matching (too strict).
  - location: core/patterns/write-it-down/definition.md / Mechanism
