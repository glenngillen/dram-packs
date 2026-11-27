# Fix the harness

Source ID `fix-the-harness`; pattern `glenngillen/fix-the-harness`; Guides, rung 7. Recognize a recurring correction eliminated by a relevant harness change. Intended detection: model judgement combined with configuration history.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. Related: Write it down (the instruction-file step this pattern builds on).

## Intent

**What it's for.** When the person corrects the agent, they fix the guide or check that would have prevented it, and the same correction stops recurring.

**Why it matters.** This is the clearest sign of a self-improving harness. Correcting the same mistake every few sessions costs the person each time; a rule, check or gate aimed at it stops it at the source, and later work shows whether it really did. It is the wider form of [Write it down](../write-it-down/definition.md): any mechanism, not only an instruction line.

**What a recognition shows.** That a correction the person had made before led them to a relevant harness change, after which later relevant work went without it.

**Why the rules are drawn this way.**

- **Only corrections of a kind made before.** A repeat is what shows a gap in the harness; a first-time correction is not applicable. Matching corrections by kind is a model judgement citing both prompts. A window with no recurring correction reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **A relevant change the person owns.** A guide change unrelated to any correction is not this pattern, and agent rule changes the person never reviewed are not the person's act ([human intent only](../../reference/principles.md#human-intent-only)).
- **Seen already needs the correction to stop.** Prevention is the pattern's deliberate result, so a rule after which the same correction continues does not count ([follow-through](../../reference/principles.md#follow-through)). `fix_followup` tries to capture "enough later work where the mistake could have come back, close enough to the change to link them"; it comes from the recorded decision accepting the proposed default and is a [calibration point](../../reference/principles.md#thresholds-are-calibration-points).
- **Only later applicable sessions count.** Silence is credit only where the correction could have recurred, so vague rules such as "write clean code" stay untested ([prevention](../../reference/principles.md#prevention-when-success-removes-the-signal)).
- **Recurrence and too little later work are kept apart.** Recurrence is a finding that the change is not holding; too little later work is not yet assessable, not a miss ([missing is not low](../../reference/principles.md#missing-is-not-low)).
- **Continuous covers most recurring corrections.** The habit is that recurring corrections lead to fixes; `most` is a calibration point, and too few recurring corrections is not assessable.
- **The change must have been in place when the later sessions ran.** Current configuration cannot prove what an earlier session had ([evidence for everything](../../reference/principles.md#evidence-for-everything)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. [`judge.md`](judge.md) is authoring prose for the correction-matching judgement; the pinned CLI does not execute it.

## Applicable work

- A **recurring correction**: a person prompt correcting the agent on something of a kind the person **already corrected before** (in an earlier session or earlier in the window). Matching corrections by kind is a model judgement citing both prompts.
- A correction made for the first time is not applicable.
- A window with no recurring correction is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs all three, in order:

1. the person's **correction** (recurring, as above);
2. a **preventive harness change** relevant to that correction: an instruction rule, a check (lint, test) or a gate (hook), attributable to the person or their team; and
3. **follow-up**: later applicable sessions in the **same repository** where the correction **no longer recurs**, meeting [`fix_followup`](../../reference/parameters.md#fix_followup): at least 2 later applicable sessions within 14 days of the change, with no recurrence.

Completing evidence: the correction, the harness change, and the later relevant sessions. "Later applicable" means sessions doing work where the correction could have recurred (for example UI work for a component rule), not any later session.

## Exclusions

- **Unrelated guide changes**: an instruction edit about something never corrected.
- A rule after which the **same correction continues**: that is not holding.
- A harness change with **no later relevant sessions**: prevention is **untested**, not success.
- Broad rules ("write clean code") too vague to identify applicable work: untested.
- A guided harness change alone: it does not prove eventual prevention.
- Agent-initiated rule changes the person never reviewed.

## Evidence

- **Cite** the person's corrections (exact quotes, at least two occurrences), the harness change (configuration history), and the later relevant sessions with no recurrence.
- **Attribution**: the correction is a person prompt; the change is in configuration the person or their team owns, or was made by the agent at the person's request and reviewed.
- **Historical**: the harness change must have been in place when the later sessions ran; current configuration alone cannot prove it.
- **Completion window**: the change can be inside the window while the follow-up finishes later; keep both timestamps and credit completion to when follow-up was established ([completion windows](../../reference/evidence.md#completion-windows)).
- **Evidence the pinned CLI does not supply**: cross-session correction matching; configuration history (when a rule, check or gate appeared); relevance of later sessions to a given correction.

## Progression

Default [stages](../../reference/progression.md#stages), with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion). Seen already requires follow-up for this pattern, because prevention is its deliberate result; an instance counts in the week its follow-up was established.

| Stage | For this pattern |
| --- | --- |
| Continuous | [`most`](../../reference/parameters.md#most) recurring corrections in the window led to a harness fix and stopped recurring, **and** the shared [mechanism](#mechanism) rule is met. Fewer than four recurring corrections: not assessable, not a miss. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the harness change itself (rule, check or gate) aimed at a recurring correction.

| Fact | For this pattern |
| --- | --- |
| In place | The rule, check or gate existed, attributable to the person or their team, after the change. |
| Applied | Later applicable sessions ran with it in place (loaded, ran or fired). |
| Held | Within the [`fix_followup`](../../reference/parameters.md#fix_followup) period, at least two later applicable sessions had no recurrence. |
| Not holding | The correction **recurred** in a later applicable session while the change was in place. |
| Untested / insufficient | Fewer than two later applicable sessions, or none: **not yet assessable**, which is distinct from recurrence and is not a miss. |

**Recurrence** (not holding) and **insufficient later work** (untested) are different results and are never merged.

## Opportunities and coaching

- **Opportunity**: the same correction in at least three sessions without a guide change, **or** the correction recurred in a later applicable session after a relevant harness change was in place (not holding). An absent fix and a fix that did not hold are distinct findings. Insufficient later work stays insufficient (untested), not an opportunity. It cites the person's correction prompts ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) presents the person's actual repeated corrections and asks them to choose one to prevent with a rule or check.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) cannot match corrections across sessions, has no configuration history, and cannot tell whether a later session was relevant to a correction. The existing recommendation system's signal reduction is useful context but is not this recognition definition. Counting any instruction edit would accept unrelated changes and rules that did not stop the correction.

## Missing capabilities

- **Cross-session correction matching**: grouping person corrections of the same kind, with quotes.
- **Configuration history**: when instruction rules, checks and gates appeared or changed, attributable to the person or their team.
- **Relevance of later work**: deciding whether a later session was applicable to the corrected behaviour.
- **Follow-up windows**: counting later applicable sessions within 14 days, with completion credited to when follow-up finished.
- **A runnable judge and checks**: only `tool_call_matches` and `tool_call_sequence` run; neither expresses these.

## Verify before enabling

- Two Button-component corrections followed by a lint rule and relevant later UI work without recurrence are recognized; a `CLAUDE.md` rule followed by two more of the same correction is rejected (not holding).
- Repeated skipped tests prevented by a Stop gate are recognized; an instruction edit about something never corrected is rejected.
- No later relevant sessions gives untested, not success; one later applicable session is not enough.
- A guided harness change alone does not prove prevention; guided evidence earns Seen only.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- How should vague rules ("write clean code") be classified when deciding applicable later work?
  - evidence: The spec says broad rules may be too vague to identify applicability and remain untested, but gives no rule for when a rule is specific enough.
  - options: Model judgement must name the corrected behaviour the rule targets, else untested; require a rule to cite a concrete file, API or command.
  - location: core/patterns/fix-the-harness/definition.md / Exclusions
