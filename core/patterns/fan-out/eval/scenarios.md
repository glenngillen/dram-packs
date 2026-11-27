# Fan out: scenarios

Every acceptance scenario for `glenngillen/fan-out`, in full. All people, repositories, services, commands and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs model judgement of independent parts and the person's request, concurrent child-session timing and result-use linkage, and names no block the pinned build runs. The scenarios are kept in full so they can become fixtures when those capabilities exist.

Applicable work has at least [`several_parallel`](../../../reference/parameters.md#several_parallel) (three or more) independent parts.

## pos-1 One subagent per service, then summarise

- kind: source-positive
- expect: seen
- Setup: in the `gullwing-platform` monorepo, the person writes "Use a subagent per service to update the client, then summarise". Four subagents start within a second of each other and run with overlapping intervals, one each for `billing`, `search`, `notify` and `accounts`. The agent combines their results into one summary; the person replies "fix the notify failure, the rest looks good" and the work continues from it.
- Why: a person request, concurrent execution of four parts, and the combined result used.

## pos-2 Owned /audit-services workflow, used

- kind: mechanism-held
- expect: continuous
- Setup: the team's saved `/audit-services` workflow starts one subagent per service concurrently and writes a combined report. In the window the person ran it twice in `gullwing-platform`; both times the subagents overlapped and the person opened issues from the report.
- Why: the source's mechanism example: in place, applied and held. No block reaches `continuous` in the pinned build.

## pos-3 Guided fan-out on real work

- kind: guided-success
- expect: seen
- Setup: following the guide in `heronry-docs`, the person asks for one subagent per locale (`en`, `de`, `ja`) to check broken links, run together, then a combined list. Three subagents overlap; the person fixes the links from the list.
- Why: the guided step on real work with concurrency and use. Guided work earns Seen only.

## pos-4 Exactly three parallel investigations, no edits

- kind: boundary
- expect: seen
- Setup: in `kiln-ci`, the person writes "spin up three subagents, one per failing job, find the cause of each and report back together". Three subagents overlap, none edits a file, and the person acts on the combined findings.
- Why: three parts meets `several_parallel` (inclusive). Independent parts need not edit files.

## neg-1 One subagent

- kind: source-negative
- expect: opportunity
- Setup: in `gullwing-platform`, the person writes "use a subagent to update the client in all four services". One subagent updates them one after another.
- Why: a single subagent is not fan-out; four independent parts were done serially. The opportunity cites the person's request.

## neg-2 Parallel results thrown away

- kind: source-negative
- expect: none
- Setup: in `kiln-ci`, the person asks for a subagent per job to investigate failures. Three run concurrently, but the person then writes "never mind, I'll just rerun CI" and the combined result is never used.
- Why: discarded parallel results are not recognized. The parts were not done serially, so there is no missed moment of this pattern.

## neg-3 Sequential subagents

- kind: boundary
- expect: opportunity
- Setup: in `gullwing-platform`, the person writes "update each service's client with a subagent". The agent starts the four subagents one after another, each beginning when the previous finishes.
- Why: sequential subagents do not satisfy concurrency. The independent parts were done serially; the opportunity cites the person's request.

## neg-4 Two parallel subagents

- kind: boundary
- expect: none
- Setup: in `heronry-docs`, the person asks for two subagents, one per locale, run together; they overlap and the result is used.
- Why: two parts are below `several_parallel`: not applicable work, not a miss.

## neg-5 Guide read, no parallel run

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person asks their agent in `kiln-ci` "which of my tasks could run in parallel?" and reads the answer. No subagent starts in the window.
- Why: a guided discussion without parallel execution and result use earns nothing, and no multi-part work was attempted.

## neg-6 No multi-part work

- kind: no-applicable-work
- expect: none
- Setup: in the window, each piece of work in `cobble-tools` was a single change in one place.
- Why: no work with three or more independent parts: counted against nothing.

## neg-7 Child-session timing unavailable

- kind: missing-evidence
- expect: none
- Setup: in `gullwing-platform`, the person asks for a subagent per service. The record shows four Task calls, but child-session start and end times are missing.
- Why: concurrency cannot be established: insufficient, not a miss and not a recognition.

## neg-8 Workflow saved, never run

- kind: mechanism-unused
- expect: none
- Setup: the team added `/audit-services` in the window, but nobody ran it.
- Why: configured but never applied: untested.

## neg-9 Workflow used, parts run one after another

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person runs `/audit-services` in `gullwing-platform`; after an edit to the workflow it now starts each service's subagent only when the previous one finishes. The person writes "why is this taking so long?".
- Why: the mechanism was applied but the parts ran sequentially: not holding. The opportunity cites the person's prompt that ran the workflow.

## Scenarios the case format cannot label

### stage-boundary Requested in week 1, combined result used in week 2

- kind: stage-boundary
- Setup: a fan-out is requested and runs late on Sunday of week 1; the person uses the combined summary on Monday of week 2. Another fan-out completes and is used in week 3.
- Expected: Seen when the combined result is used (week 2), since use is part of Seen. For Forming, the instances are credited to weeks 2 and 3.
- Why no case: `expect` has no `forming` value.

### stage-boundary Safety prerequisites are not a stage

- kind: stage-boundary
- Setup: the person has no scoped permissions configured and asks for a fan-out that is concurrent and used.
- Expected: Seen is recognized from the evidence. Separately, coaching that suggests more fan-out keeps the Safety prerequisites explicit; no stage is withheld by an invented numeric requirement.
- Why no case: the case format cannot express suggestion prerequisites.
