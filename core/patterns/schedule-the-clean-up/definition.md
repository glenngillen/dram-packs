# Schedule the clean-up

Source ID `schedule-the-clean-up`; pattern `glenngillen/schedule-the-clean-up`; Checking the work, rung 10. Use scheduled agent maintenance whose output is acted on. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** Agents run on a schedule to catch drift nobody's looking at: outdated dependencies, dead code, flaky tests, broken docs.

**Why it matters.** Dependency updates, flaky-test sweeps and similar chores come back every week, and done by hand they wait until someone notices. A headless agent run on a schedule can do the first pass without anyone remembering. In Checking the work, it is a check that keeps running after the work ships.

**What a recognition shows.** That a schedule or trigger the person or their team owns launched a maintenance run, and someone used what it produced.

**Why the rules are drawn this way.**

- **People who maintain at least one repository.** Recurring upkeep only falls to someone who maintains something; no maintained repository reports nothing ([applicable work](../../reference/principles.md#applicable-work)). What "maintains" means is still open, so a repository visited once isn't assumed applicable.
- **Headless, maintenance, and launched by an owned schedule.** A run started by hand is the interactive chore, not the schedule; a vendor's bot or another team's job is not the person's harness ([human intent only](../../reference/principles.md#human-intent-only)). A headless invocation alone doesn't prove a configured schedule ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **Output must be used, even for Seen.** The scheduled run is only valuable if someone merges, files or fixes what it finds; a report nobody opens is excluded by the original spec. So use is part of Seen here, credited to the window the use finished in ([follow-through](../../reference/principles.md#follow-through)).
- **One-off interactive maintenance is the coaching moment, not a recognition.** Doing the chore by hand repeatedly is exactly what a schedule would replace.
- **Forming and Established count used runs across weeks and maintained repositories' chores.** "Two distinct weeks" and "fewer than four items is not assessable" try to capture a schedule that keeps producing used output, rather than one lucky run; both are [calibration points](../../reference/principles.md#thresholds-are-calibration-points).
- **Continuous is the schedule holding throughout the window.** Runs happening on schedule with output used is the mechanism; runs that stop or pile up unused while the chore is done by hand are not holding ([prevention](../../reference/principles.md#prevention-when-success-removes-the-signal)). How many missed runs are allowed is still open.
- **Unattended runs come after Scope permissions.** Automate advice for a scheduled run follows the Safety prerequisite for unattended work ([autonomy and safety advance together](../../reference/principles.md#autonomy-and-safety-advance-together)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- The pattern applies to a person who **maintains at least one repository** in the window: they did work in it whose recurring upkeep (dependency updates, flaky tests, lint debt, stale branches) falls to them or their team.
- What counts as "maintains" is **not settled** (see [open questions](#open-questions)). Until it is, a repository the person only visited once is not assumed applicable.
- A window with no maintained repository is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs all three facts:

1. **A headless maintenance session**: a non-interactive agent run (for example `claude -p "/check-deps"`) whose work is maintenance, not a feature or a one-off investigation.
2. **Owned launch provenance**: it was launched by a schedule or trigger **the person or their team owns** (a cron entry, a CI schedule, a scheduled routine they configured). Software acting on its own behalf is not person-authored work ([completion windows](../../reference/evidence.md#completion-windows)).
3. **Used output**: what the run produced was used: its pull request merged, its filed issue fixed or triaged, or its result otherwise acted on.

Completing evidence: the scheduled session and the action on its output. A headless invocation alone does not prove a configured schedule or useful output.

Completion follows the [stage-dependent rule](../../reference/progression.md#stage-dependent-completion): the action on the output is part of Seen here, because an unused scheduled run is excluded outright. A run in one window whose output is used in the next is credited to the window the use finished in.

## Exclusions

- **Scheduled reports nobody uses**: runs happen, output is produced, nothing is merged, filed or acted on.
- **One-off interactive maintenance**, even if repeated monthly by hand: that is the coaching trigger, not a recognition.
- **A headless run launched by hand** with no schedule or trigger behind it.
- **A schedule the person does not own**: a vendor's bot or another team's job whose output simply lands in the repository.
- An agent starting itself, or an automatic fallback.
- **Guided schedule setup** without a completed run and used output.
- Dram's own analysis sessions.

## Evidence

- **Cite** the scheduled session (its launch time, headless mode and maintenance prompt) and the action on its output (the merge, the filed issue and its fix, or the explicit use). Opportunities cite a person-authored moment such as the prompt doing the chore by hand ([opportunities](../../reference/evidence.md#opportunities)).
- **Attribution**: the schedule or trigger configuration must be attributable to the person or their team, and the scheduled session linked to it. Existing unattended-job signals are inputs, not full proof of ownership.
- **Permitted sources only**: schedulers are inspected only when the person has allowed that source. This pack cannot add that access, and its guide never inspects or edits a scheduler.
- **Evidence the pinned CLI does not supply**: launch provenance for headless sessions; schedule facts (configured cadence, which runs happened); maintenance classification of a session; linkage from a session's output to a merge, issue or other use; "maintains" per repository.

## Progression

Default [stages](../../reference/progression.md#stages), with stage-dependent completion:

| Stage | For this pattern |
| --- | --- |
| Seen | One scheduled maintenance run whose output was used. |
| Forming | Used scheduled runs in two distinct weeks of the last four, each credited to the week the output was used. |
| Established | At least [`most`](../../reference/parameters.md#most) of the maintained repositories' recurring chores handled by used scheduled runs over the last four weeks. Fewer than four applicable items is not assessable, which is not a miss. |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)); guided setup without a run and used output earns nothing.

## Mechanism

The mechanism is the owned schedule or trigger itself.

| Fact | For this pattern |
| --- | --- |
| In place | A schedule or trigger, attributable to the person or team, configured to launch a headless maintenance run during the window. |
| Applied | Scheduled runs actually happened according to that schedule. |
| Held | The runs occurred throughout the window and their output was used. |
| Not holding | Runs stopped or were skipped, or output piled up unused, while the chore was still being done by hand. |
| Untested | A schedule in place whose first run falls after the window. |

How many missed schedule runs are allowed before it is not holding is **unresolved** (see [open questions](#open-questions)).

## Opportunities and coaching

- **Opportunity**: a recurring maintenance chore done **repeatedly by hand** in a maintained repository (for example interactive dependency updates in each of the last three months), citing the person's prompt starting that chore.
- **Coaching**: the [guide](guide.md) picks the person's real chore and explains a scheduled headless workflow. It does not edit settings, configure a scheduler or launch anything unasked.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate), and comes after Scope permissions for the unattended run ([safety prerequisites](../../reference/progression.md#safety-prerequisites)).

## Why disabled

The pinned CLI (revision `bdea6f6`) cannot tell a scheduled launch from a hand-launched headless run, cannot see schedules, and cannot link a session's output to a merge or an issue. Recognizing this pattern from a headless invocation alone (for example a `tool_call_matches` on `claude -p`) would substitute a weaker definition that the acceptance criteria explicitly reject.

## Missing capabilities

- **Launch provenance**: which headless sessions were started by a schedule or trigger, and whose.
- **Permitted schedule facts**: configured cadence and the runs that happened, from a scheduler source the person allowed.
- **Maintenance classification** of a session's work.
- **Output-action linkage**: from a session's pull request, issue or report to the merge, fix or use that followed.
- **Repository maintenance attribution**: which repositories the person maintains.
- **A runnable check**: no block in the pinned registry expresses any of the above; only `tool_call_matches` and `tool_call_sequence` run.

## Verify before enabling

- A weekly `claude -p "/check-deps"` launched by an owned schedule whose pull request is merged is recognized; scheduled reports nobody uses are rejected.
- A nightly flaky-test run whose filed issue is fixed is recognized; interactive monthly dependency maintenance is rejected.
- A headless run without schedule provenance or used output is not recognized.
- Guided setup without a completed run and used output does not earn Seen.
- Held, not-holding and unused-schedule cases produce distinct results.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- What makes a person someone who "maintains" a repository?
  - evidence: The source applies the pattern to people maintaining at least one repository but gives no rule.
  - options: Main sessions in the repository in at least two weeks of the window; commits to its default branch; team ownership metadata.
  - location: core/patterns/schedule-the-clean-up/definition.md / Applicable work
- How many missed scheduled runs are allowed before the mechanism is not holding?
  - evidence: Continuous requires the run to occur "according to its schedule throughout the window"; tolerance for a skipped run is not given.
  - options: None missed; at most one missed per window; a fraction of expected runs.
  - location: core/patterns/schedule-the-clean-up/definition.md / Mechanism
- What is sufficient evidence that output was "filed or otherwise used"?
  - evidence: A merged pull request is clear; a filed issue with no later action, or a report read but not acted on, is not settled.
  - options: Require a merge or a fix linked to the filed issue; accept triage of the issue; accept an explicit person reference to the report.
  - location: core/patterns/schedule-the-clean-up/definition.md / Recognition
