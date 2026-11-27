# Keep it lean: scenarios

Every acceptance scenario for `glenngillen/keep-it-lean`, in full. All people, repositories, file contents and measurements are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no field for resolved instruction content, instruction token share or git survival, and the pattern names no block the pinned build runs.

The cost threshold is [`instruction_cost_share`](../../../reference/parameters.md#instruction_cost_share): strictly more than 12% of initial context. Kept means still in the default branch after [`kept_window`](../../../reference/parameters.md#kept_window) (14 days).

## pos-1 Conflicting test commands reconciled and kept

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, `CLAUDE.md` says "Run tests with `make test`" and `rules/testing.md` says "Run tests with `npm test`". The check flags both lines. The person writes: "Those disagree. `make test` is right; remove the npm line." The agent removes it. Twenty days later the change is still in the default branch.
- Why: a contradiction with both lines cited and the person's request: Seen on the request. The resolving edit, kept for `kept_window`, also counts toward later stages.

## pos-2 Source illustration: instructions around 12% of initial context, split into on-demand rules

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, measured from resolved instruction sizes, instruction files load 12.4% of the initial context (the source describes this case as "12%"). The person asks to split the database and release rules into on-demand rule files, keeping all of them. The agent does; the split is still in the default branch 15 days later.
- Why: the source's example of a split prompted by roughly 12% of initial context. The measured value is above the strict threshold, so it is a finding. The exact-boundary behaviour is tested separately in neg-7 and pos-4.

## pos-3 Guided lean-up on real work

- kind: guided-success
- expect: seen
- Setup: the person follows the guide in `tidepool-web`; the agent quotes two conflicting import-order rules. The person asks to keep one and remove the other; the edit is made. It is six days old at the end of the window.
- Why: a requested reconciliation after a cited finding earns Seen. Guided work earns Seen only, and a change younger than `kept_window` is unassessed for later stages, not failed.

## pos-4 Just above the threshold

- kind: boundary
- expect: seen
- Setup: in `orchard-jobs`, instruction files measurably load 12.1% of initial context. The person asks to move rarely needed deployment rules to an on-demand file, keeping them; the change is made.
- Why: 12.1% is strictly more than 12%, so it is a cost finding; the requested split earns Seen.

## pos-5 Recurring check held

- kind: mechanism-held
- expect: continuous
- Setup: the person's harness has an owned weekly command that reports contradictory instruction lines and loading share. It ran four times in the window across `lanternfish-api` and `quillmark`; the files stayed consistent and below the threshold.
- Why: check in place, applied (it ran) and held (consistent, below threshold).
- Note: no block reaches `continuous` in the pinned build.

## pos-6 Lean-up requested, edit still pending

- kind: boundary
- expect: seen
- Setup: on the last day of the window in `heron-service`, the check flags two conflicting branch-naming rules, quoting both lines. The person writes: "Those conflict. Keep `feat/` and drop the `feature/` line." The window ends before the edit is made; the edit is still pending.
- Why: Seen completes on the attributable request after a supported finding. The resolving edit and its fourteen-day survival are follow-through for Forming and Established; while pending they are unassessed, not a miss.

## neg-1 Unused ninety-day-old migration rule, no flag

- kind: source-negative
- expect: none
- Setup: `marlin-cli`'s `CLAUDE.md` has a migration rule added ninety days ago and not relevant to recent work. Nothing contradicts it and the files are well below the threshold.
- Why: age or infrequent use alone never justifies trimming. No finding, no applicable work.

## neg-2 Unprompted instruction rewrite

- kind: source-negative
- expect: none
- Setup: in `basalt-sdk` the agent, unasked, rewrites `AGENTS.md`, removing a duplicated rule. The person did not request it.
- Why: agent-initiated rewrites are excluded, even when they remove a real conflict.

## neg-3 Guided review with no resolving action

- kind: guided-no-action
- expect: none
- Setup: the person runs the guide; the agent quotes two conflicting lint commands. The person says "interesting" and ends the session; no change is made.
- Why: a guided review with no resolving action earns nothing; reading the guide is not a person-authored moment of applicable work, so no opportunity is reported.

## neg-4 Change that only adds content

- kind: source-negative
- expect: none
- Setup: after a flagged conflict between two formatting rules in `heron-service`, the person asks to add a third rule clarifying when each applies, leaving both conflicting lines.
- Why: changes that only add content are excluded; the contradiction is not reconciled.

## neg-5 No instruction files loaded

- kind: no-applicable-work
- expect: none
- Setup: the person's only repository in the window, `fern-docs`, has no instruction files and they use no user-level file.
- Why: nothing to keep lean.

## neg-6 No load or price evidence

- kind: missing-evidence
- expect: none
- Setup: `amber-lib` has a long `CLAUDE.md`, but the session records give no resolved instruction sizes or usage, so the share of initial context cannot be computed.
- Why: no price or load evidence means no numeric cost claim and no cost finding; insufficient, not a miss.

## neg-7 Exactly 12% of initial context

- kind: boundary
- expect: none
- Setup: in `slate-ui`, instruction files measurably load exactly 12% of the initial context. No contradiction is flagged. The person makes no change.
- Why: the threshold is strictly more than 12%; exactly 12% is not a finding, so there is no applicable work and no opportunity.

## neg-8 Check configured but never ran

- kind: mechanism-unused
- expect: none
- Setup: the person's harness has the contradiction check configured, but it did not run in the window. The files happen to be consistent and small.
- Why: an unused check is untested and does not establish Continuous; with no finding there is nothing else to report.

## neg-9 Check running, conflict remains and bites

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person's weekly check runs in `kestrel-app` but misses two conflicting test commands in nested rule files. The agent runs the wrong one and the person asks "why did you run `npm test`? We use `make test`."
- Why: the check was in place and applied, but a contradiction it should have caught remained: not holding. The opportunity cites the person's prompt hitting the conflict.

## neg-10 Flagged conflict worked around without reconciling

- kind: source-negative
- expect: opportunity
- Setup: in `garnet-web`, two lines disagree on the package manager and are flagged with both lines cited. Later the person writes "ignore the npm line, use pnpm" and continues without changing the files.
- Why: a finding the person worked against without reconciling; the opportunity cites their prompt.

## Scenarios the case format cannot label

### stage-boundary Seen now, Forming only after kept_window

- kind: stage-boundary
- Setup: a requested reconciliation in week 1 and another in week 3, each still in the default branch 14 days after it was made.
- Expected: Seen in week 1. The week-1 change counts toward Forming in week 3, when its 14-day survival is established; the week-3 change counts only once its own survival is established (week 5), so Forming is not reached inside this four-week window from these two alone.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Reverted lean-up

- kind: stage-boundary
- Setup: a requested trim is reverted two days later.
- Expected: Seen (the request qualified); never counts toward Forming or Established. A one-day or two-day revert measure is not fourteen-day survival.
- Why no case: as above.
