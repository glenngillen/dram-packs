# Hands off: scenarios

Every acceptance scenario for `glenngillen/hands-off`, in full. All people, repositories, commands and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs owned-command provenance, per-command interactive run history, unattended classification, launch provenance and output-use judgement, and names no block the pinned build runs. The scenarios are kept in full so they can become fixtures when those capabilities exist.

Applicable work is an owned command or skill already run interactively at least three times. "Unattended" follows [`unattended_gap`](../../../reference/parameters.md#unattended_gap): headless, or at least 15 minutes of continued agent work without a person prompt.

## pos-1 Unattended /release-notes, notes published

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api` the person's own `/release-notes` command (defined in the repository's committed commands) was run interactively in three earlier sessions. This week the person starts it headless with scoped permissions. Next morning they write in a new session "publish the draft notes from last night's run", and the notes are published.
- Why: an owned, familiar command run unattended, and its output used. Completing evidence: the headless invocation and the publish step.

## pos-2 Scheduled /triage, labels applied

- kind: source-positive
- expect: seen
- Setup: in `quillmark` the team's `/triage` skill was run interactively four times by the person. The person configures a nightly schedule that runs it unattended. After the first scheduled run, the person writes "apply the labels triage proposed" and the labels are applied.
- Why: a person-configured trigger launched an owned workflow unattended, and the output was used.

## pos-3 Guided unattended run with output used

- kind: guided-success
- expect: seen
- Setup: following the guide in `tidepool-web`, the person picks their own `/changelog` command (five earlier interactive runs), reviews a scoped permission set, starts it headless on the real release branch and commits the generated changelog.
- Why: the guided step on real work, completed by use. Guided work earns Seen only.

## pos-4 Exactly 15 minutes without a person prompt

- kind: boundary
- expect: seen
- Setup: in `marlin-cli` the person invokes their own `/dep-audit` command (three earlier interactive runs) in an interactive session and steps away. The agent works for exactly 15 minutes without a person prompt. The person returns and writes "open PRs for the two upgrades you flagged".
- Why: 15 minutes of continued agent work without a person prompt meets `unattended_gap` (inclusive), and the output was used.

## pos-5 Configured trigger held across the window

- kind: mechanism-held
- expect: continuous
- Setup: the person's team configured a weekly schedule running their own `/triage` skill in `orchard-jobs`. It ran every week of the window and each time the person applied the proposed labels.
- Why: in place, applied and held: the configured trigger ran the owned workflow and its output was used. No block reaches `continuous` in the pinned build.

## neg-1 Same command run only interactively

- kind: source-negative
- expect: opportunity
- Setup: in `lanternfish-api` the person runs their own `/release-notes` interactively in four separate sessions, watching each run. Scope permissions is already Seen for an unattended session of theirs. In the fourth session they write "/release-notes for v2.4".
- Why: no qualifying unattended work, so not Seen. The command repeated across three or more sessions with the prerequisite met makes it an opportunity, citing the person's "/release-notes for v2.4" prompt.

## neg-2 Ad-hoc headless prompt

- kind: source-negative
- expect: none
- Setup: in `fern-docs-api` the person runs `claude -p "summarise this file"` headless and reads the summary.
- Why: an ad-hoc prompt is not an owned workflow, so the pattern does not apply.

## neg-3 Output discarded

- kind: boundary
- expect: none
- Setup: in `kestrel-app` the person's own `/weekly-report` command (three earlier interactive runs) runs headless. The produced report is never opened, published or referenced afterwards.
- Why: no output-use evidence, so no completed recognition. Discarded output is not counted as a miss either.

## neg-4 Guide read, no unattended run

- kind: guided-no-action
- expect: none
- Setup: the person reads the guide and asks their agent to list the permissions their `/triage` command needs, then stops without running it unattended.
- Why: guided setup without a qualifying run and use is incomplete. Nothing is recorded against the person.

## neg-5 Scope permissions not Seen for unattended work

- kind: boundary
- expect: none
- Setup: in `cobalt-infra` the person runs their own `/drift-report` interactively in three separate sessions. Scope permissions is Seen for their interactive sessions only; they have never run an unattended session with scoped permissions.
- Why: the run-scoped prerequisite is missing, so the suggestion is suppressed and no opportunity is reported. Evidence collection for other patterns, including Scope permissions, continues.

## neg-6 No owned commands

- kind: no-applicable-work
- expect: none
- Setup: in the window the person uses only built-in commands and ad-hoc prompts.
- Why: no owned command run interactively three times: no applicable work.

## neg-7 Unattended before three interactive runs

- kind: boundary
- expect: none
- Setup: in `heather-cli` the person runs their own `/bump-deps` interactively twice, then headless, and merges the resulting branch.
- Why: two interactive runs do not meet the three-run applicability, so the run is not assessed. Not Seen and not a miss.

## neg-8 Run record truncated

- kind: missing-evidence
- expect: none
- Setup: in `saffron-jobs` the person's own `/triage` runs headless, but the run record is truncated before its output and no later session refers to it.
- Why: whether the output existed or was used is unknown: insufficient, never a miss.

## neg-9 Launched by software on its own behalf

- kind: source-negative
- expect: none
- Setup: a third-party review service installed on `ember-ui` launches an agent that runs the person's `/lint-fix` command for its own checks. The person did not configure the launch.
- Why: a launch by software acting on its own behalf is not automatically person-authored work.

## neg-10 Schedule configured, never ran

- kind: mechanism-unused
- expect: none
- Setup: the person configured a nightly schedule for their `/triage` skill in `cormorant-api`, but it did not run in the window.
- Why: in place but never applied: untested. Not Continuous and not a miss.

## neg-11 Scheduled output redone by hand

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the team's weekly schedule runs the owned `/triage` skill in `orchard-jobs` throughout the window. Its proposed labels are never applied; each week the person writes "/triage" in an interactive session and applies those results instead. Scope permissions is already Seen for an unattended session of theirs, so the prerequisite flag is true.
- Why: applied but not holding: the trigger's output went unused and the work was redone by hand. The opportunity cites the person's interactive "/triage" prompt.

## neg-12 Fourteen minutes without a person prompt

- kind: boundary
- expect: none
- Setup: in `marlin-cli` the person invokes their own `/dep-audit` interactively; the agent works for 14 minutes, then the person prompts "skip the dev dependencies", and later uses the output.
- Why: 14 minutes is under `unattended_gap`, so this is an interactive run (applicability history), not an unattended one.

## stage-boundary Output used after the window closed

- kind: stage-boundary
- Setup: the person's own `/release-notes` runs headless on the last day of the window; the notes are published two days into the next window.
- Why: the use is the completing evidence, so the instance is credited to the window and week in which the notes were published, not silently to the run's window. The case format cannot express window crediting, so this scenario has no case.
