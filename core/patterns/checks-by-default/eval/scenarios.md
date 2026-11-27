# Checks by default: scenarios

Every acceptance scenario for `glenngillen/checks-by-default`, in full. All people, repositories, rules, hooks and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs historical instruction and hook resolution, hook run records, prompt/edit/check ordering and causation judgement, and names no block the pinned build runs (declared hook checks do not execute in the fixed-pattern engine).

Applicable work is a person's main session that changed code in a repository with relevant checks.

## pos-1 CLAUDE.md instructs make test after edits, followed unprompted

- kind: source-positive
- expect: seen
- Setup: `lanternfish-api`'s committed `CLAUDE.md` (in place two months before the window) says "After editing Go files, run `make test` and show the result." In a session, the agent edits `handlers/order.go`, then runs `make test` with no person prompt in between.
- Why: an attributable rule loaded when the session ran caused a check after the edit without prompting.

## pos-2 Owned PostToolUse hook runs tsc after edits

- kind: source-positive
- expect: seen
- Setup: the person's project settings in `tidepool-web`, committed by them before the window, define a PostToolUse hook running `tsc --noEmit` after file edits. The session record shows the hook fired after the agent edited `src/cart.ts` and its output was shown.
- Why: an owned hook, in place and actually executing after an edit.

## pos-3 Rule-directed check fails

- kind: boundary
- expect: seen
- Setup: as pos-1, but `make test` fails with two errors and the agent reports the failure.
- Why: the rule caused the check, so Seen. The failure is recorded honestly; execution is not passing, and this case says nothing about the violation being resolved.

## pos-4 Guided rule followed in a later session

- kind: guided-success
- expect: seen
- Setup: following the guide, the person adds "after changing code run `pnpm test` and `pnpm typecheck`" to `marlin-web/AGENTS.md` and commits it. The next day, a new session edits `src/form.tsx` and the agent runs both commands without being asked.
- Why: the guided step completed by a later session following the rule. Guided work earns Seen only.

## pos-5 Every applicable repository covered and holding

- kind: mechanism-held
- expect: continuous
- Setup: the person changes code in three repositories with checks (`lanternfish-api`, `tidepool-web`, `quillmark`). Each has the person's after-change rule or hook in place for the whole window, and every code-changing session there ran the directed check after edits without prompting. A scratch directory with no checks is also used and is not counted.
- Why: in place, applied and holding in every applicable repository.
- Note: no block reaches `continuous` in the pinned build.

## neg-1 Unprompted tests with no rule

- kind: source-negative
- expect: opportunity
- Setup: `orchard-jobs` has no instruction file or hook about checks. The agent edits `jobs/retry.py`, runs `pytest` out of habit, then edits again and finishes. The person says "looks good, next task".
- Why: a spontaneous model habit is not the person's harness. The session ended with nothing run after the last edit; the opportunity cites "looks good, next task".

## neg-2 Hook configured, never executed

- kind: source-negative
- expect: none
- Setup: `basalt-sdk` has the person's PostToolUse hook configured to run `go vet`, but its matcher never matches the edit tool the agent uses, so it never fires. Records show no check ran; the person asked for nothing.
- Why: configuration with no execution is not recognized. As a mechanism it is untested on this repository's edits; whether it is an opportunity depends on a person-authored moment, which this scenario lacks (see neg-6 for the not-holding case).

## neg-3 Rule added after the session

- kind: source-negative
- expect: none
- Setup: in `heron-service`, the agent ran `make test` after an edit on Tuesday with no rule loaded. On Thursday the person adds an after-change rule to `CLAUDE.md`.
- Why: the rule did not exist when the session ran, so it cannot prove it caused Tuesday's check. Tuesday's check was a spontaneous habit.

## neg-4 Guided rule written, no later followed session

- kind: guided-no-action
- expect: opportunity
- Setup: following the guide in `kestrel-app`, the person saves an after-change rule. Their only later code-changing session runs no check after the last edit (the agent they use does not load that file); the person ends with "thanks, commit it".
- Why: guided rule creation without a subsequent followed session is incomplete for Seen. The opportunity cites "thanks, commit it".

## neg-5 Person asked for the check

- kind: boundary
- expect: none
- Setup: `slate-ui` has an after-change rule, but the agent finishes an edit without running checks; the person writes "run the tests" and the agent runs them.
- Why: the check followed a fresh person prompt, so it was not caused by the harness here (that request belongs to Prove it). Nothing ran unprompted, so this session is not Seen; because the person did get a check, it is not an opportunity for this pattern either.

## neg-6 Rule in place and loaded, not followed

- kind: mechanism-not-holding
- expect: opportunity
- Setup: in `quillmark`, the person's loaded `AGENTS.md` rule says to run `make lint test` after changes. In one session the agent edits three files and ends without running either; the person replies "ok, push it".
- Why: in place and applied but not holding. The opportunity cites "ok, push it".

## neg-7 Rule in place, no code-changing session

- kind: mechanism-unused
- expect: none
- Setup: `garnet-web` has the person's after-change rule, but in the window the person only asked questions there; no code changed.
- Why: in place but never applied: untested, not held, and no applicable work in that repository.

## neg-8 No code changed in any repository with checks

- kind: no-applicable-work
- expect: none
- Setup: the person's only code changes in the window were in a scratch directory with no tests, lint or build.
- Why: coverage is over applicable repositories, not every directory; nothing is counted against.

## neg-9 Configuration history unavailable

- kind: missing-evidence
- expect: none
- Setup: in `amber-lib`, the agent ran `make test` after an edit without prompting. A rule exists today, but no configuration history shows whether it existed when the session ran.
- Why: current configuration alone cannot prove historical loading. Insufficient evidence: neither Seen nor a miss.

## neg-10 Check before the edit

- kind: boundary
- expect: opportunity
- Setup: in `pewter-tools`, with an after-change rule loaded, the agent runs `make test` at the start of the session, then edits two files and finishes without running it again. The person says "great".
- Why: edit/check order matters; the check preceded the edit, so the rule was not followed after the change. The opportunity cites "great".

## Scenarios the case format cannot label

### stage-boundary Continuous needs every applicable repository

- kind: stage-boundary
- Setup: two of three applicable repositories have the rule and it holds there; the third has none.
- Expected: Seen, and Forming or Established as the weeks and coverage allow, but not Continuous: coverage of every applicable repository plus the mechanism requirement is needed.
- Why no case: `expect` cannot express "not continuous but forming".

### stage-boundary Forming across two weeks

- kind: stage-boundary
- Setup: rule-caused checks in sessions in weeks 1 and 3 of the last four.
- Expected: Forming.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.
