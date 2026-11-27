# Clear between tasks: scenarios

Every acceptance scenario for `glenngillen/clear-between-tasks`, in full. All people, repositories and prompts are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no clear-event record distinct from compaction and resume, no per-task person-prompt count and no task-relatedness judgement, and the pattern names no block the pinned build runs.

"Prompts" below are the person's own prompts in a main session; tool results, hook output and compaction summaries are never counted. Substantial work is [`substantial_work_prompts`](../../../reference/parameters.md#substantial_work_prompts).

## pos-1 Eight prompts on a ticket, clear, then an unrelated export bug

- kind: source-positive
- expect: seen
- Setup: in `ledgerline-app`, the person sends eight prompts working through ticket LL-214 (pagination on the invoices list). They run `/clear`. Their next prompt: "CSV export drops the last row when the file has a trailing newline; find out why."
- Why: a genuine clear after substantial work, followed by a person prompt starting unrelated work. Cites the clear record and the export-bug prompt.

## pos-2 Six prompts on CSS, clear, then a date bug

- kind: boundary
- expect: seen
- Setup: in `pinecone-site`, six person prompts adjust header CSS. `/clear`. Next prompt: "The booking page shows yesterday's date for users in UTC+13. Fix the date handling."
- Why: six prompts is the inclusive boundary of `substantial_work_prompts`; the date bug is unrelated to the CSS work. Also the source's second positive example.

## pos-3 Guided clear before a real task switch

- kind: guided-success
- expect: seen
- Setup: in `ledgerline-app`, after seven prompts on a migration, the person opens the guide, asks the agent whether anything is needed for the next task (it answers "nothing"), runs `/clear`, then asks to add rate limiting to the login endpoint.
- Why: the person's own clear on real work, followed by unrelated work. Guided work earns Seen only.

## pos-4 Owned one-task rule followed

- kind: mechanism-held
- expect: continuous
- Setup: the person's user-level instruction file (edited by them before the window) says "one task per session: when I switch to unrelated work, summarize anything needed and ask me to clear". In the window, three sessions reach a switch to unrelated work after six or more prompts; in each the agent offers the summary, the person clears or starts a fresh session, and the new task starts from a clean context.
- Why: rule in place, applied on applicable switches and holding. A fresh session counts here because the rule is being followed; it would not count as the Seen act.

## neg-1 Clear after two prompts

- kind: source-negative
- expect: none
- Setup: in `pinecone-site`, two prompts on a typo fix, `/clear`, then a prompt about a caching bug.
- Why: an early clear. Two prompts are not substantial work, so this switch is not applicable work: no recognition and no miss.

## neg-2 Clear followed by the same ticket

- kind: source-negative
- expect: none
- Setup: in `ledgerline-app`, nine prompts on LL-214, `/clear`, then "Carry on with LL-214: now the page size selector."
- Why: the next prompt continues the same ticket. There is no move to unrelated work, so nothing applies and nothing is recognized.

## neg-3 Compaction then unrelated work

- kind: source-negative
- expect: opportunity
- Setup: in `harbor-api`, ten prompts on a retry policy. The conversation is compacted automatically. The person's next prompt: "Unrelated: why does the healthcheck return 500 on cold start?"
- Why: compaction is not the Seen clear; it keeps a summary of the retry work in context. The unrelated task inherited the prior context. The opportunity cites the healthcheck prompt.

## neg-4 Resume then unrelated work

- kind: source-negative
- expect: opportunity
- Setup: the person resumes yesterday's `harbor-api` session (eight prompts on the retry policy) with continue, then writes "Different thing: rename the metrics prefix to harbor_."
- Why: resume brings the earlier context back; it is not a clear. The unrelated prompt is the person-authored citation.

## neg-5 New session is not the Seen clear

- kind: source-negative
- expect: none
- Setup: after eight prompts on LL-214, the person closes the session and opens a new one for the export bug. No `/clear` is run.
- Why: opening a new session is excluded from the Seen act, and the new task did not inherit prior context, so there is no opportunity either. (Under an owned one-task rule this could support the mechanism; see pos-4.)

## neg-6 Reads the guide but does not clear

- kind: guided-no-action
- expect: opportunity
- Setup: after seven prompts on a migration in `ledgerline-app`, the person reads the guide and replies "makes sense", then in the same session asks about an unrelated logging bug without clearing.
- Why: answering the guide does not count. The unrelated task started on top of the migration context; the logging prompt is the citation.

## neg-7 Five prompts then a clear

- kind: boundary
- expect: none
- Setup: five prompts on CSS in `pinecone-site`, `/clear`, then an unrelated date bug.
- Why: five prompts is below `substantial_work_prompts`, so the switch is not applicable work. Not a recognition and not a miss.

## neg-8 Single-task sessions only

- kind: no-applicable-work
- expect: none
- Setup: every session in the window stays on one task from start to finish.
- Why: nothing moved to unrelated work after substantial work.

## neg-9 Session record truncated around the switch

- kind: missing-evidence
- expect: none
- Setup: a `harbor-api` session has eight prompts on one task, then the record is truncated; the next visible prompt is on an unrelated bug. Whether a clear happened cannot be seen.
- Why: missing evidence is insufficient, not a miss and not a recognition.

## neg-10 One-task rule in place, no task switch

- kind: mechanism-unused
- expect: none
- Setup: the person's one-task rule is in place all window, but no session reaches six prompts before switching task.
- Why: the mechanism is untested, not held; there is no applicable work to count against.

## neg-11 One-task rule in place but not followed

- kind: mechanism-not-holding
- expect: opportunity
- Setup: with the rule from pos-4 loaded, the person sends seven prompts on a retry policy, then "Now look at the flaky upload test". The agent proceeds in the same context; no clear and no fresh session.
- Why: the rule was in place and applied, but the unrelated task still started on top of the old context. Cites the upload-test prompt.

## neg-12 Clear issued by an agent workflow

- kind: source-negative
- expect: none
- Setup: an automated script running the agent headless issues `/clear` between queued tasks; no person prompt follows.
- Why: a clear run by software acting on its own behalf is not the person's act, and no person-authored prompt exists to cite.

## Scenarios the case format cannot label

### stage-boundary Seen versus Forming follow-through

- kind: stage-boundary
- Setup: in week 1 the person clears after eight prompts and starts an unrelated bug; the new task proceeds and finishes in week 1. In week 3, the same again.
- Expected: Seen in week 1; Forming once the second qualifying instance's follow-through finishes in a distinct week (week 3).
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Clear whose new task is pulled back

- kind: stage-boundary
- Setup: the person clears after six prompts and starts an unrelated date bug, but two prompts later says "back to the CSS" and abandons it.
- Expected: Seen (the deliberate act qualifies); the follow-through did not finish on the unrelated task, so it does not count toward Forming.
- Why no case: as above.
