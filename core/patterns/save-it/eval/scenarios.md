# Save it: scenarios

Every acceptance scenario for `glenngillen/save-it`, in full. All people, repositories, commands and prompts are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no field for command or skill provenance, who invoked a command, or cross-session grouping of near-identical prompts, and the pattern names no block the pinned build runs.

Applicable work is a person request repeated nearly word-for-word across at least two main sessions.

## pos-1 New PR-description command, then /pr-description

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, the person wrote "Write a PR description: summary, why, how to test, risks" in sessions on Monday and Wednesday. On Thursday they ask their agent to save it as `.claude/commands/pr-description.md`, read it and approve it. On Friday they type `/pr-description` on a real branch and the run completes with a description.
- Why: a new, person-owned command capturing a repeated request, invoked by the person, run completed.

## pos-2 Hand-written skill first run in the window

- kind: source-positive
- expect: seen
- Setup: the person repeated "check this migration for locking and backfill risks" in three sessions in `orchard-jobs`. They hand-write a skill for it in their user configuration and, the next day, invoke it themselves on a new migration; the run completes with findings.
- Why: an owned skill, first run in the window, invoked by the person.

## pos-3 Guided save and use

- kind: guided-success
- expect: seen
- Setup: following the guide, the person identifies "summarize the failing CI job and propose a fix" as repeated in two sessions, asks their agent to save it as a command, reads and edits it, and the same afternoon invokes it on a real failing job; the run completes.
- Why: the person saved and ran their own command on real work. Guided work earns Seen only.

## pos-4 Saved commands cover every repeated request

- kind: mechanism-held
- expect: continuous
- Setup: over four weeks the person has five repeated requests; all five go through their saved commands, each invoked by them and completed, on at least two different days. No request is typed by hand across three or more sessions.
- Why: in place, applied and holding; no manual repetition across three sessions.

## neg-1 Built-in /review

- kind: source-negative
- expect: opportunity
- Setup: the person types "review this diff for bugs and missing tests" in two sessions, then starts using the built-in `/review` command. They have no saved command of their own. Later they retype the original request in a third session.
- Why: a built-in command is not the person's own saved request. The retyped prompt is the person-authored citation for the opportunity.

## neg-2 Command saved but never run

- kind: source-negative
- expect: opportunity
- Setup: the person saves `.claude/commands/release-notes.md` after repeating "draft release notes from merged PRs" twice, but in the rest of the window types the request by hand again and never invokes the command.
- Why: creation without execution does not count. The opportunity cites the retyped prompt.

## neg-3 Skill invoked by the agent unasked

- kind: source-negative
- expect: none
- Setup: an owned skill for changelog entries exists. The person writes "fix the date parsing bug"; while doing so the agent decides on its own to invoke the changelog skill. The person never invoked it and made no repeated request in the window.
- Why: agent-only invocation cannot substitute for the person's choice, and there is no repeated request to count against.

## neg-4 Guide questions answered, nothing saved

- kind: guided-no-action
- expect: opportunity
- Setup: the person reads the guide and replies "I keep asking for PR descriptions" but saves nothing. Next day they type the PR-description request by hand again.
- Why: answering the guide earns nothing. The opportunity cites the retyped prompt.

## neg-5 No repeated requests

- kind: no-applicable-work
- expect: none
- Setup: every request in the window is different work; no request repeats nearly word-for-word across sessions.
- Why: nothing to count against; not a miss.

## neg-6 Invocation records truncated

- kind: missing-evidence
- expect: none
- Setup: an owned command exists and the person repeated its request twice, but the session where it may have been invoked is truncated before the invocation.
- Why: whether the person ran it is unknown. Insufficient evidence, not a miss and not a recognition.

## neg-7 Same topic, different requests

- kind: boundary
- expect: none
- Setup: the person writes "fix the failing auth test" and, in another session, "fix the failing billing test". No other repetition.
- Why: shared topic with different intent is not a near-identical request, so there is no applicable work.

## neg-8 Saved commands in place, no repeated request

- kind: mechanism-unused
- expect: none
- Setup: the person has six saved commands but in this window makes no repeated request and invokes none of them.
- Why: in place but never applied: untested, not held, and nothing to count against.

## neg-9 Saved version exists but request retyped across three sessions

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person has `/pr-description` saved, yet types the full PR-description request by hand in three sessions this window.
- Why: manual repetition across three sessions with a saved version available: not holding. Cites the retyped prompts.

## neg-10 Plugin command

- kind: source-negative
- expect: opportunity
- Setup: after repeating "generate API docs for this module" twice, the person installs a marketplace plugin and runs its `/api-docs` command. They wrote nothing themselves; in a third session they retype the request for a module the plugin does not handle.
- Why: a third-party plugin command does not establish ownership. Cites the retyped prompt.

## Scenarios the case format cannot label

### stage-boundary Same-day second run does not meet Forming

- kind: stage-boundary
- Setup: pos-1's person runs `/pr-description` twice on Friday and not again in the window.
- Expected: Seen only. Forming for this pattern needs another run on a **different day**.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Different-day run meets Forming

- kind: stage-boundary
- Setup: as above, plus a completed person-invoked run the following Tuesday.
- Expected: Forming, credited to the week of the Tuesday run.
- Why no case: as above.

### stage-boundary Established needs four repeated requests

- kind: stage-boundary
- Setup A: three repeated requests, all through saved commands. Setup B: five repeated requests, three through saved commands.
- Expected: A is not assessable under [`most`](../../../reference/parameters.md#most) (fewer than four), not a miss. B meets Established (60%, inclusive).
- Why no case: as above.
