# Schedule the clean-up: scenarios

Every acceptance scenario for `glenngillen/schedule-the-clean-up`, in full. All fixtures are synthetic: people, repositories, schedules, commands and pull requests are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI because the collected-history fixture shape has no field for launch provenance, schedule facts or output-action linkage, and the pattern names no block the pinned build runs.

Applicable work is a person who maintains at least one repository in the window. "Owned" means the schedule or trigger is attributable to the person or their team.

## pos-1 Weekly check-deps run producing a merged pull request

- kind: source-positive
- expect: seen
- Setup: the person maintains `wren-billing`. A weekly CI schedule their team configured launches `claude -p "/check-deps"` headless every Monday. This week's run opened a pull request bumping two libraries; the person reviewed and merged it on Tuesday.
- Why: a headless maintenance session with owned launch provenance and used output (the merge). Completion cites the scheduled session and the merge.

## pos-2 Nightly flaky-test run whose filed issue is fixed

- kind: source-positive
- expect: seen
- Setup: in `ibis-search`, a nightly trigger the person set up runs a headless agent sweep for flaky tests. One night it filed an issue naming a timing-dependent test; two days later the person fixed the test and closed the issue.
- Why: owned trigger, maintenance work, and output acted on.

## pos-3 Guided run, then scheduled and used

- kind: guided-success
- expect: seen
- Setup: following the guide, the person writes a lint-debt prompt for `moth-ui`, runs it once headless, then sets up a team-owned weekly schedule and reviews it. The first scheduled run opens a pull request the person merges.
- Why: the guided step was completed on real work with a scheduled run and used output. Guided work earns Seen only.

## pos-4 Schedule held through the window

- kind: mechanism-held
- expect: continuous
- Setup: the `wren-billing` weekly check-deps schedule ran on all four Mondays of the window. Three runs opened pull requests that were merged; one found nothing to update and said so.
- Why: in place, applied according to its schedule throughout the window, and its output used whenever it produced something worth acting on.

## pos-5 Run in week 4, merge just inside the window

- kind: boundary
- expect: seen
- Setup: a scheduled run on the last Sunday of the window at 23:00 local time opens a pull request; the person merges it at 23:40 the same night.
- Why: launch and use both fall inside the window in the person's local time.

## neg-1 Scheduled reports nobody uses

- kind: source-negative
- expect: opportunity
- Setup: in `ibis-search`, an owned nightly schedule writes a dependency report to a file. Over four weeks nobody opens, merges or files anything from it. Meanwhile the person runs dependency updates by hand in two interactive sessions, prompting "update the dependencies".
- Why: unused scheduled output is excluded. The opportunity cites the person's hand-run maintenance prompt, not the agent's report.

## neg-2 Interactive monthly dependency maintenance

- kind: source-negative
- expect: opportunity
- Setup: in `wren-billing`, the person opens an interactive session at the start of each of three months and writes "go through outdated dependencies and update them". No schedule exists.
- Why: one-off interactive maintenance is excluded; done repeatedly by hand it is the coaching trigger. The person's monthly prompt is the citation.

## neg-3 Headless invocation without schedule provenance

- kind: source-negative
- expect: none
- Setup: the session record shows `claude -p "/check-deps"` ran headless in `moth-ui`, but nothing shows it was launched by a schedule or trigger, and its output was not used.
- Why: a headless invocation alone proves neither a configured schedule nor useful output. With no person-authored maintenance moment to cite, there is no opportunity either.

## neg-4 Guided setup with no completed run

- kind: guided-no-action
- expect: none
- Setup: the person reads the guide and asks their agent what scheduling options exist for `moth-ui`. They set up nothing, and no run happens. They do no maintenance by hand in the window.
- Why: answering the guide's questions does not count, and with no hand-done chore there is no person-authored opportunity to cite.

## neg-5 Guided schedule set up, run happened, output unused

- kind: source-negative
- expect: none
- Setup: following the guide, the person configures a weekly schedule in `tern-api`. One run happens and opens a pull request that is still open, unreviewed, when the window ends. No maintenance was done by hand.
- Why: guided setup without used output does not earn Seen. The run is recent and its output pending, which is not a miss.

## neg-6 Not a maintainer

- kind: no-applicable-work
- expect: none
- Setup: the person's only work in the window is two sessions in a colleague's repository, `kiln-docs`, fixing a typo.
- Why: no maintained repository, so nothing applies. Not a miss.

## neg-7 Schedule owned by someone else

- kind: boundary
- expect: none
- Setup: a vendor's dependency bot opens weekly pull requests in `tern-api`, which the person merges. The person owns no schedule or trigger.
- Why: the launch is not the person's or their team's, so it is not this pattern; merging the bot's pull requests is not an opportunity either.

## neg-8 Scheduler records not available

- kind: missing-evidence
- expect: none
- Setup: headless sessions appear in `wren-billing` each Monday and pull requests are merged, but the person has not allowed Dram to read their scheduler or CI configuration, so launch provenance is unknown.
- Why: unavailable provenance is insufficient, not a miss and not a recognition.

## neg-9 Schedule in place, never ran in the window

- kind: mechanism-unused
- expect: none
- Setup: the person configured a monthly maintenance schedule for `heron-cli` whose first run falls after the window ends.
- Why: in place but not applied is untested, not held.

## neg-10 Schedule in place, runs stopped while chore done by hand

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the `ibis-search` nightly flaky-test schedule stopped running after week 1 (its job was disabled). In weeks 3 and 4 the person prompts "find and fix the flaky tests" in interactive sessions.
- Why: the mechanism was in place but did not keep running, and the chore went back to hand work. The opportunity cites the person's prompt.

## neg-11 Truncated output linkage

- kind: missing-evidence
- expect: none
- Setup: a scheduled run in `moth-ui` opened a pull request, but the repository history after it is unavailable, so whether it was merged cannot be seen.
- Why: unknown use is insufficient, not an unused report and not a recognition.

## Scenarios the case format cannot label

### stage-boundary Forming credited to the week of use

- kind: stage-boundary
- Setup: a scheduled run in week 1 opens a pull request merged in week 2; another run in week 3 is merged in week 3.
- Expected: Forming, with the first instance credited to week 2 (when its output was used) and the second to week 3.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Output used after the window

- kind: stage-boundary
- Setup: a scheduled run in week 4 opens a pull request merged two days after the window ends.
- Expected: nothing in this window (the use finished outside it); it may count in the next window. Not a miss.
- Why no case: the case format has no window or follow-through timestamps.
