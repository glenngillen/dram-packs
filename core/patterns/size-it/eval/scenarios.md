# Size it: scenarios

Every acceptance scenario for `glenngillen/size-it`, in full. All people, repositories, commands and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs model judgement of substantial work and of a deliberate, used breakdown, plus task/plan linkage and sub-task completion across sessions, and names no block the pinned build runs. The scenarios are kept in full so they can become fixtures when those capabilities exist.

Applicable work is a main session (or linked sessions) with substantial work, judged from the work itself; no size threshold is used.

## pos-1 Migration broken into one step per session

- kind: source-positive
- expect: seen
- Setup: in `ledgerline-api`, the person writes "Break the migration into steps we can do one per session". The agent proposes five steps; the person replies "good, start with step one: add the new columns". The agent adds the migration for the columns, runs it against the test database, and the person confirms "step one done".
- Why: large work, a person-requested breakdown, and the first sub-task worked on its own and finished. The remaining four steps are follow-through for later stages, not required for Seen.

## pos-2 Three sessions follow sub-tasks of one plan

- kind: source-positive
- expect: seen
- Setup: in `harbourmaster-web`, the person writes a three-item plan in `PLAN.md` for a checkout redesign and asks the agent to do item one only. Over three sessions on three days, each session takes up the next item and finishes it.
- Why: the person's own breakdown, used one sub-task at a time. Seen on the first finished item; because every sub-task finished, the instance also counts toward Forming, credited to the week the last item finished.

## pos-3 Guided breakdown, first step finished

- kind: guided-success
- expect: seen
- Setup: following the guide in `pinecone-cli`, the person asks for a breakdown of a config-format change, trims it to four steps, and finishes step one (parsing the new format) in that session.
- Why: the guided step on real work with the first sub-task finished. Guided work earns Seen only.

## pos-4 Owned planning command used and held

- kind: mechanism-held
- expect: continuous
- Setup: the person owns a `/plan-steps` command that turns a goal into session-sized steps. In the window it began three pieces of substantial work in `ledgerline-api` and `harbourmaster-web`; each proceeded one step at a time and every step finished.
- Why: an attributable mechanism in place, applied to begin substantial work and held. No block reaches `continuous` in the pinned build.

## pos-5 Agent-proposed breakdown adopted by the person

- kind: boundary
- expect: seen
- Setup: in `quarry-data`, the person asks for a reporting rewrite. The agent replies with four steps and asks which to start. The person edits the list ("merge 3 and 4, then do step 1 only") and step one is finished.
- Why: an agent proposal counts because the person's evidenced review adopted and used it.

## neg-1 "Do the whole migration"

- kind: source-negative
- expect: opportunity
- Setup: in `ledgerline-api`, the person writes "Do the whole migration". The agent edits schema, models, jobs and API handlers in one session; tests fail in three places and the person ends with "this is a mess, I'll come back to it".
- Why: large work attempted at once with no breakdown and no clean finish. The opportunity cites "Do the whole migration".

## neg-2 Breakdown followed by doing it all in one go

- kind: source-negative
- expect: opportunity
- Setup: in `harbourmaster-web`, the person asks for steps, gets six, then writes "actually just do them all now". The agent works through every step in one go; two are left half-done when the session ends.
- Why: a requested split followed by doing everything together anyway: the breakdown was not used. The opportunity cites "actually just do them all now".

## neg-3 Naturally small task

- kind: boundary
- expect: none
- Setup: in `pinecone-cli`, the person asks "fix the typo in the --help text". The agent makes a one-line change.
- Why: a naturally small one-line task does not prove deliberate sizing, and needs none: not applicable, not a miss.

## neg-4 Guide read, breakdown discussed, not used

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person asks the agent in `quarry-data` "how would you split the reporting rewrite?" and reads the answer. They start no step in the window.
- Why: discussing a breakdown without using it earns nothing, and no large work was attempted, so there is no missed moment.

## neg-5 Only small work in the window

- kind: no-applicable-work
- expect: none
- Setup: in the window the person only renamed two functions and bumped a dependency in `cobble-tools`.
- Why: no substantial work: the pattern is counted against nothing.

## neg-6 Record truncated after the first step started

- kind: missing-evidence
- expect: none
- Setup: in `ledgerline-api`, the person asks for a breakdown and says "start step one". The session record is truncated shortly afterwards; whether step one finished cannot be seen, and no later session is linked.
- Why: missing evidence is insufficient: neither Seen nor a miss.

## neg-7 Planning command never used

- kind: mechanism-unused
- expect: none
- Setup: the person added a `/plan-steps` command in their user-level commands, but began no work with it in the window.
- Why: configured but never applied: untested. Not Continuous and not a miss.

## neg-8 Planning command used, work done all together

- kind: mechanism-not-holding
- expect: opportunity
- Setup: in `harbourmaster-web`, the person runs `/plan-steps` on a search rewrite, gets five steps, then writes "skip the steps, do it all". The session ends with the rewrite half-done.
- Why: the mechanism was applied but the work was still done all together: not holding. The opportunity cites "skip the steps, do it all".

## Scenarios the case format cannot label

### stage-boundary First sub-task only finished

- kind: stage-boundary
- Setup: in week 1, the person breaks a migration into four steps and finishes step one. Steps two to four are still pending at the end of the window.
- Expected: Seen in week 1. The instance does **not** count toward Forming until every sub-task finishes. Pending steps are not a miss.
- Why no case: `expect` has no `forming` value.

### stage-boundary Credited to the week the last sub-task finished

- kind: stage-boundary
- Setup: a breakdown starts in week 1, step one finishes in week 1 and the last step finishes in week 3. A second breakdown finishes all its steps in week 4.
- Expected: Seen in week 1. For Forming, the instances are credited to weeks 3 and 4, two distinct weeks of the last four.
- Why no case: `expect` has no `forming` value.

### stage-boundary Breakdown abandoned partway

- kind: stage-boundary
- Setup: step one of a breakdown finishes; the person then merges the rest into one go and it is left unfinished.
- Expected: Seen stands from the first finished sub-task; the instance never counts toward Forming or Established.
- Why no case: the case format cannot express stage-specific credit.
