# Hand it off: scenarios

Every acceptance scenario for `glenngillen/hand-it-off`, in full. All people, repositories and file contents are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape is per session, with no pairing of sessions, no confirmed fresh/resumed flag, no context-size or compaction record and no hook execution record, and the pattern names no block the pinned build runs.

A long session is [`long_session`](../../../reference/parameters.md#long_session). Pairing is [`handoff_pairing`](../../../reference/parameters.md#handoff_pairing): the previous main session in the same repository ending within 24 hours before the new one began.

## pos-1 NOTES.md written, then a fresh "Read NOTES.md and continue"

- kind: source-positive
- expect: seen
- Setup: in `ridgeway-billing`, a session reaches 180,000 tokens of context. The person asks "write our decisions and next steps to NOTES.md"; the agent writes it. The session ends at 18:10. At 09:30 the next day the person starts a confirmed new session in `ridgeway-billing`; the first prompt is "Read NOTES.md and continue." The agent continues the proration work from the notes.
- Why: a long prior session wrote a handoff at the person's request; a genuinely fresh session in the same repository, 15 hours later (inside 24 hours, across a day boundary), started from it.

## pos-2 Fresh session with a pasted state summary

- kind: source-positive
- expect: seen
- Setup: in `ridgeway-billing`, a session is compacted once. Before ending it the person asks for "a state summary I can paste into a new session"; the agent produces one. Two hours later the person starts a new session in the same repository and pastes the summary as the first prompt.
- Why: pasting the prior session's state summary is a handoff, supported by the prior-session evidence that produced it.

## pos-3 Guided handoff used in a fresh session

- kind: guided-success
- expect: seen
- Setup: in `kiln-scheduler`, after a compacted session, the person follows the guide, asks for `HANDOFF.md`, corrects one decision in it, and an hour later starts a new session with "Read HANDOFF.md and continue from where it says we are."
- Why: the person's deliberate handoff on real work, used in a fresh session. Guided work earns Seen only.

## pos-4 PreCompact hook writes HANDOFF.md, used next session

- kind: mechanism-held
- expect: continuous
- Setup: the person's user-level settings (theirs, before the window) define a PreCompact hook that asks the agent to write `HANDOFF.md`. In the window, three long sessions in two repositories compact; each time the hook runs and writes the file, and the next fresh session in that repository, within 24 hours, opens with a prompt reading it.
- Why: the source's mechanism example: owned hook in place, applied and holding.

## neg-1 Resumed with continue

- kind: source-negative
- expect: opportunity
- Setup: the long `ridgeway-billing` session from pos-1 wrote no notes. The next morning the person runs `claude --continue`; the resumed session re-asks a rounding decision made before compaction, and the person writes "We already decided half-up rounding."
- Why: resume is not a fresh session. The lost decision is the problem; the person's correcting prompt is the citation.

## neg-2 Earlier NOTES.md, but a new unrelated task

- kind: source-negative
- expect: none
- Setup: a long `ridgeway-billing` session wrote `NOTES.md`. The next fresh session's first prompt: "Look at NOTES.md formatting later; for now add a dark-mode toggle."
- Why: naming the file while starting unrelated work is not using the handoff. The dark-mode work did not need the prior decisions, so there is nothing missed either.

## neg-3 Compaction alone

- kind: source-negative
- expect: none
- Setup: a `kiln-scheduler` session compacts twice and the person keeps working in it to the end of the task. No later session in the repository.
- Why: compaction alone is not a handoff. No decision was lost and no later session followed, so there is no recognition and no opportunity.

## neg-4 Guided handoff never used

- kind: guided-no-action
- expect: none
- Setup: following the guide, the person asks for `HANDOFF.md` in a long `kiln-scheduler` session and reads it, but no new session is started in that repository in the window.
- Why: a handoff never used is incomplete. With no later work, nothing was missed either.

## neg-5 Fresh session more than 24 hours later

- kind: boundary
- expect: none
- Setup: `NOTES.md` was written at the end of a long `ridgeway-billing` session at 17:00 on Monday; the next session in the repository starts at 18:00 on Tuesday (25 hours later) reading it.
- Why: the previous session ended outside the 24-hour pairing window, so the pair is not assessed under the source pairing.

## neg-6 Fresh session in a different repository

- kind: boundary
- expect: none
- Setup: after a long `ridgeway-billing` session writes `NOTES.md`, the person starts a new session in `kiln-scheduler` and pastes the notes.
- Why: pairing requires the same repository.

## neg-7 Exactly 150,000 tokens, no compaction

- kind: boundary
- expect: none
- Setup: a session ends at exactly 150,000 tokens of context and was never compacted; the next session starts without a handoff.
- Why: `large_context_tokens` is strictly more than 150,000, so the session is not long and the pattern does not apply.

## neg-8 Only short sessions

- kind: no-applicable-work
- expect: none
- Setup: every session in the window stays under 60,000 tokens and none compacts.
- Why: no long session, so no applicable work.

## neg-9 Fresh/resumed flag unconfirmed

- kind: missing-evidence
- expect: none
- Setup: after a long session writes `HANDOFF.md`, the next session's first prompt reads it, but the record does not confirm whether that session was new or resumed.
- Why: an unconfirmed fresh/resumed flag is insufficient for recognition, and it is not a miss.

## neg-10 Prior session removed by retention

- kind: missing-evidence
- expect: none
- Setup: a new session's first prompt reads `NOTES.md`, but the previous session was removed under the person's retention settings.
- Why: the pairing cannot be assessed; neither a recognition nor a miss.

## neg-11 Handoff hook in place, never fires

- kind: mechanism-unused
- expect: none
- Setup: the PreCompact hook from pos-4 is configured all window, but no session compacts or grows long.
- Why: in place but never applied: untested, not held.

## neg-12 Handoff hook runs, next session resumes instead

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the hook writes `HANDOFF.md` when a `kiln-scheduler` session compacts. The person's next step is "continue" on the same session; the agent then redoes a migration step decided earlier, and the person writes "We decided to skip that step, see the handoff."
- Why: in place and applied, but the next session did not start fresh from the handoff, so it is not holding. The person's correcting prompt is the citation.

## Scenarios the case format cannot label

### stage-boundary Seen versus Forming follow-through

- kind: stage-boundary
- Setup: in week 1 a fresh session starts from `NOTES.md` (Seen) but the person abandons the work after the first prompt. In week 2 and week 4 fresh sessions start from handoffs and the agent completes the next steps from them.
- Expected: Seen in week 1. The week 1 instance does not count toward Forming because its follow-through did not finish; weeks 2 and 4 make Forming.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Handoff written in one week, used in the next

- kind: stage-boundary
- Setup: the handoff is written on a Sunday evening (week 1) and the fresh session that uses it starts Monday morning (week 2), within 24 hours.
- Expected: the instance completes in week 2, when the fresh use happened; writing alone in week 1 is not an instance.
- Why no case: as above.
