# Two at once: scenarios

Every acceptance scenario for `glenngillen/two-at-once`, in full. All people, repositories, paths and prompts are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs paired evidence across two main sessions (environment facts, overlapping edit timestamps, turn durations, parent/subagent links) and model judgement of independent real work, and names no block the pinned build runs. The scenarios are kept in full so they can become fixtures when those capabilities exist.

Applicable work is an agent turn running at least 5 minutes while the person waits ([`long_turn`](../../../reference/parameters.md#long_turn)).

## pos-1 Interleaved refactor and fix in separate worktrees

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, the person's interactive session runs a 12-minute refactor of `store/` in the main checkout. Three minutes in, the person opens a second session in the worktree `lanternfish-api-fix` and writes "fix the nil pointer in handlers/order.go". Both sessions make edits between minutes 4 and 11.
- Why: two separate working copies, both interactive, each with a person prompt and edits in overlapping minutes.

## pos-2 Edits in two repositories during the same minutes

- kind: source-positive
- expect: seen
- Setup: while a session in `quillmark` runs an 8-minute migration, the person starts a session in `tidepool-web` with "update the cart badge colour". Both sessions edit files during the same minutes.
- Why: two different repositories are separate working copies, with paired active editing.

## pos-3 Guided pair on real tasks

- kind: guided-success
- expect: seen
- Setup: following the guide, the person in `marlin-cli` creates a worktree for a docs fix and starts it while a 7-minute parser change runs in the main checkout. Both sessions edit in overlapping minutes.
- Why: the guided step completed by actual paired active work. Guided work earns Seen only.

## pos-4 Exactly 5-minute turn

- kind: boundary
- expect: seen
- Setup: in `cobalt-infra`, an agent turn runs exactly 5 minutes. During it, the person starts a second session in a separate clone and writes "add the missing tag to the bucket module"; both sessions edit during the turn.
- Why: exactly 5 minutes meets `long_turn` (inclusive); the pair is isolated and active.

## pos-5 Owned script starts isolated pairs and holds

- kind: mechanism-held
- expect: continuous
- Setup: the person's `bin/pair-start` script creates a worktree and opens a second session in it. Across the window they use it four times in `orchard-jobs`, and each time both sessions make real edits.
- Why: in place, applied and held. No block reaches `continuous` in the pinned build.

## neg-1 One working session, one idle

- kind: source-negative
- expect: none
- Setup: in `fern-docs-api`, a session runs a 9-minute turn while a second session, in its own worktree, is open but receives no prompt and makes no edit.
- Why: idle overlap is not paired work. Not Seen; the opportunity is not inferred from an open idle window.

## neg-2 Sessions ten minutes apart

- kind: source-negative
- expect: none
- Setup: the person finishes a session in `kestrel-app`, then ten minutes later starts a session in a separate worktree.
- Why: no overlap, so not two at once.

## neg-3 Parent session plus its subagent

- kind: source-negative
- expect: none
- Setup: in `ember-ui`, the person's session starts a subagent to update snapshots while the main session keeps editing.
- Why: a parent and its own subagent are not two independent main sessions (that is Split it up or Fan out territory).

## neg-4 Shared directory, different branches

- kind: source-negative
- expect: none
- Setup: in `heather-cli`, two sessions edit during the same minutes in one directory, one on `feature/a` and one on `feature/b`.
- Why: branch-only separation in a shared directory does not qualify. It is an Isolate the run opportunity, not this pattern's.

## neg-5 Guide read, no second session

- kind: guided-no-action
- expect: none
- Setup: the person reads the guide during a long turn and creates a worktree, but starts nothing in it.
- Why: guided setup without paired active work does not earn Seen. Nothing is recorded against the person.

## neg-6 Isolation prerequisite missing

- kind: boundary
- expect: none
- Setup: in `saffron-jobs`, the person repeatedly waits through 10-minute turns. Isolate the run is not Seen for them.
- Why: the suggestion is suppressed until Isolate the run is at least Seen, so no opportunity is reported.

## neg-7 Waited through a long turn, prerequisite met

- kind: boundary
- expect: opportunity
- Setup: Isolate the run is Seen for the person. In `cormorant-api` they start a 9-minute turn with "migrate the jobs table to the new schema", wait with no other session working, then write "ok, now the API docs".
- Why: an applicable long turn waited out with the prerequisite met. The opportunity cites the person's prompt that started the long turn.

## neg-8 Four-minute turn

- kind: boundary
- expect: none
- Setup: in `orchard-jobs`, the person waits through a 4-minute turn with no other session working.
- Why: under `long_turn`, so not applicable: no opportunity.

## neg-9 No long turns

- kind: no-applicable-work
- expect: none
- Setup: every agent turn in the window finishes in under 2 minutes.
- Why: no turn of at least 5 minutes: no applicable work.

## neg-10 Second session's history excluded

- kind: missing-evidence
- expect: none
- Setup: in `lanternfish-api`, one session's edits are recorded during a 10-minute turn; the other session's history is excluded from analysis.
- Why: one side of the pair cannot complete it, and the gap is insufficient evidence, never a miss.

## neg-11 Pairing script never used

- kind: mechanism-unused
- expect: none
- Setup: the person wrote `bin/pair-start` but did not run it in the window.
- Why: in place, never applied: untested. Not a miss.

## neg-12 Pairing script reused one directory

- kind: mechanism-not-holding
- expect: none
- Setup: the person's `bin/pair-start` fails to create a worktree and opens the second session in the main checkout of `quillmark`. The person writes "update the README examples" there while the first session edits; both edit the same working copy.
- Why: in place and applied, but not holding: the pair shared a working copy, which is recorded as mechanism evidence for this pattern. It is not this pattern's opportunity: an opportunity here needs a long turn waited out with no other session working, and both sessions were working. Shared-directory editing is described separately as an Isolate the run opportunity (compare neg-4), citing "update the README examples".

## neg-13 Paired editing during only 4-minute turns

- kind: boundary
- expect: none
- Setup: Isolate the run is Seen for the person. In `tidepool-web`, the first session runs a 4-minute turn after "rename the cart helpers". During it, the person opens a second session in a separate worktree and writes "fix the footer link"; both sessions make edits in the overlapping minutes. No turn in either session reaches 5 minutes.
- Why: separate working copies and real paired edits, but no turn meets `long_turn`, so this is outside applicable work: neither Seen nor an opportunity.
