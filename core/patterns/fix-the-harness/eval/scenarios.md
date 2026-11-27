# Fix the harness: scenarios

Every acceptance scenario for `glenngillen/fix-the-harness`, in full. All people, repositories, components and prompts are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no configuration history and no way to link corrections across sessions or judge later work relevant, and the pattern names no block the pinned build runs.

Applicable work is a correction of a kind the person already made before. Follow-up uses [`fix_followup`](../../../reference/parameters.md#fix_followup).

## pos-1 Button corrections, lint rule, clean UI work

- kind: source-positive
- expect: seen
- Setup: in `tidepool-web`, the person writes "use the shared `Button` component, not a raw `<button>`" in sessions on 3 and 6 March. On 6 March they ask the agent to add a lint rule banning raw `<button>` in `src/ui`, review it and commit it. Sessions on 9 and 12 March build two new UI forms; no raw buttons appear and no correction is needed.
- Why: recurring correction, relevant preventive check, two later applicable sessions within 14 days without recurrence.

## pos-2 Skipped tests prevented by a Stop gate

- kind: source-positive
- expect: seen
- Setup: in `orchard-jobs`, the person corrects "don't mark failing tests as skipped" twice in a week. They add a Stop hook that blocks finishing when the diff adds a skip marker. In the next two sessions with test changes, the gate fires once, the agent fixes the test instead, and no correction is needed.
- Why: a gate aimed at the recurring correction, applied, with no recurrence in later applicable sessions.

## pos-3 Guided rule with follow-up

- kind: guided-success
- expect: seen
- Setup: following the guide, the person picks "use pnpm, not npm" (corrected in three sessions in `quillmark`), reviews and commits an instruction rule. Two later sessions installing dependencies use pnpm unprompted.
- Why: correction, change and relevant follow-up. Guided work earns Seen only.

## pos-4 Most recurring corrections fixed and holding

- kind: mechanism-held
- expect: continuous
- Setup: over four weeks the person has five recurring corrections in `basalt-sdk`; for four they add rules or checks, each followed by at least two applicable sessions with no recurrence.
- Why: most (four of five, at least 60% with at least four) recurring corrections fixed and holding.

## neg-1 CLAUDE.md rule, then the same correction twice more

- kind: source-negative
- expect: opportunity
- Setup: in `marlin-cli`, after correcting "return typed errors from handlers" twice, the person adds a `CLAUDE.md` rule. In the next two handler sessions they correct the same thing again.
- Why: the correction continues after the rule. Cites the person's later corrections.

## neg-2 Instruction edit about something never corrected

- kind: source-negative
- expect: none
- Setup: the person adds "prefer small functions" to `CLAUDE.md`. They never corrected the agent about function size, and no recurring correction exists in the window.
- Why: an unrelated guide change is not a fix; nothing recurring to count against.

## neg-3 Change made, no later relevant sessions

- kind: mechanism-unused
- expect: none
- Setup: after two "use the date helper" corrections, the person adds a lint rule on the last day of the window. No later session touches dates.
- Why: prevention is untested, not success. Insufficient later work, not a miss.

## neg-4 One later applicable session only

- kind: boundary
- expect: none
- Setup: as pos-1, but only one UI session follows within 14 days.
- Why: `fix_followup` needs at least two; one session is not yet assessable, distinct from recurrence.

## neg-5 Recurrence within 14 days after a lint rule

- kind: mechanism-not-holding
- expect: opportunity
- Setup: as pos-1, but on 10 March the person again writes "use the shared Button component" because the lint rule did not cover `src/forms`.
- Why: recurrence while the change was in place: not holding. Cites the 10 March correction.

## neg-6 Same correction in three sessions, no change

- kind: source-negative
- expect: opportunity
- Setup: the person writes "don't commit generated files" in three sessions in `heron-service` and changes nothing in the harness.
- Why: the coaching trigger: the same correction in at least three sessions without a guide change. Cites the corrections.

## neg-7 Guide read, no change made

- kind: guided-no-action
- expect: opportunity
- Setup: the person reads the guide, names "use pnpm" as their most frequent correction, and stops. They correct it again in a later session.
- Why: answering the guide earns nothing. Cites the later correction.

## neg-8 No recurring correction

- kind: no-applicable-work
- expect: none
- Setup: the person corrected the agent a few times, each on a different kind of thing, never repeated.
- Why: nothing applicable; not a miss.

## neg-9 Later sessions truncated

- kind: missing-evidence
- expect: none
- Setup: after a recurring correction and a rule, two later UI sessions exist but their transcripts are truncated before any UI work.
- Why: whether the correction recurred cannot be seen. Insufficient, not a miss and not a recognition.

## neg-10 Guided change alone

- kind: guided-no-action
- expect: none
- Setup: following the guide, the person adds a rule for "use pnpm" on the last day of the window. No later session follows.
- Why: a guided harness change alone does not prove prevention; untested, not a miss.

## Scenarios the case format cannot label

### stage-boundary Follow-up finishing outside the window

- kind: stage-boundary
- Setup: the correction and lint rule fall in week 4; the two clean later sessions fall in the following week.
- Expected: not credited in this window; credited to the week follow-up was established.
- Why no case: `expect` cannot express window crediting or Forming.

### stage-boundary Continuous needs four recurring corrections

- kind: stage-boundary
- Setup: three recurring corrections, all fixed and holding.
- Expected: Continuous not assessable under [`most`](../../../reference/parameters.md#most) (fewer than four), not a miss; each still earns Seen.
- Why no case: as above.
