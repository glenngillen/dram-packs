# Split it up: scenarios

Every acceptance scenario for `glenngillen/split-it-up`, in full. All people, repositories, agents, commands and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs model judgement of a person's delegation request, agent provenance (built-in, plugin or person-defined) and parent-child session linkage, and names no block the pinned build runs. The scenarios are kept in full so they can become fixtures when those capabilities exist.

Applicable work is a main session that breaks off to a side task and returns.

## pos-1 "Use a subagent to update the snapshots"

- kind: source-positive
- expect: seen
- Setup: in `meadowlark-ui`, mid-way through a form refactor, the person writes "Use a subagent to update the snapshots". The agent makes a Task call; a child session updates `__snapshots__/` and returns "12 snapshots updated". The main session continues the refactor.
- Why: a person-requested subagent start for a side task. Citation: the request and the Task call with its child-session link.

## pos-2 Agent chooses the person's own test-writer

- kind: source-positive
- expect: seen
- Setup: the person defined a `test-writer` agent in their user-level agent configuration. In `ridgeback-api`, while adding an endpoint, the agent says "I'll ask test-writer to cover the new handler" and starts it; it returns two new test files.
- Why: the agent chose a subagent the person defined; the definition expresses the person's intent. Provenance (person-defined) and the start complete it.

## pos-3 Guided delegation of a real side task

- kind: guided-success
- expect: seen
- Setup: following the guide in `quokka-sync`, a flaky test interrupts the main task. The person writes "use a subagent to find out why test_retry is flaky and report back in two lines". A subagent starts and reports.
- Why: the guided step on real work, with an actual start. Guided work earns Seen only.

## pos-4 Own subagents invoked by an instruction rule, held

- kind: mechanism-held
- expect: continuous
- Setup: the person's `CLAUDE.md` says "send snapshot updates to snapshot-updater and dependency research to lib-scout", both person-defined agents. In the window, four side tasks the rule covers arose in two repositories; each went to the named agent and its result returned to the main session.
- Why: in place, applied and held. No block reaches `continuous` in the pinned build.

## pos-5 Plugin agent started at the person's request

- kind: boundary
- expect: seen
- Setup: in `meadowlark-ui`, the person writes "get the doc-search plugin agent to find how the router handles redirects". The plugin-supplied agent starts and returns a summary.
- Why: the plugin definition gives no ownership credit, but the person's request makes it a person-requested start (route 1).

## neg-1 Spontaneous built-in Explore

- kind: source-negative
- expect: none
- Setup: in `ridgeback-api`, the person asks "add pagination to /orders". The agent on its own starts the built-in Explore agent to scan the codebase, then implements the change. No side task was raised by the person and the main work finished.
- Why: an unsolicited built-in subagent is the model's habit, not the person's delegation. There is no missed side-task moment either.

## neg-2 "Do these in parallel" with no subagent start

- kind: source-negative
- expect: opportunity
- Setup: in `quokka-sync`, the person writes "Do these in parallel: fix the lint warnings and update the changelog" during a sync-engine change. The agent does both itself in the main session; afterwards the person has to write "where were we with the sync engine? you dropped the retry logic".
- Why: a request with no actual delegation is not Seen. The side tasks pulled the main session off track; the opportunity cites the person's restatement of the lost main goal.

## neg-3 Plugin agent without a delegation request

- kind: boundary
- expect: none
- Setup: in `meadowlark-ui`, the agent on its own starts a plugin-supplied `ui-reviewer` agent; the person never asked for it and has no own agent of that name.
- Why: a plugin agent without the person's request earns no ownership credit and is not intentional delegation.

## neg-4 Guide read, no subagent started

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person asks their agent in `ridgeback-api` "when would a subagent help me?" and reads the answer. No side task is delegated in the window.
- Why: guided delegation advice without actual invocation earns nothing.

## neg-5 No side task in the window

- kind: no-applicable-work
- expect: none
- Setup: in the window, each session in `cobble-tools` stayed on one task from start to finish.
- Why: no side task: the pattern is counted against nothing.

## neg-6 Child session link missing

- kind: missing-evidence
- expect: none
- Setup: in `quokka-sync`, the person writes "use a subagent for the changelog". The record shows a Task call, but the child session and the agent's provenance are unavailable.
- Why: whether a subagent actually started for the side task, and what it was, cannot be established: insufficient, not a miss and not a recognition.

## neg-7 Own agents and rule, no covered side task

- kind: mechanism-unused
- expect: none
- Setup: the person's rule sends snapshot updates to their `snapshot-updater`, but no snapshot update arose in the window.
- Why: configured but never applied: untested. Not a miss.

## neg-8 Rule in place, side task done in the main session

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the same rule is in place. In `meadowlark-ui` the person writes "and update the snapshots while you're there"; the agent updates them in the main session, filling the context, and the person later writes "you've lost the thread on the form validation, start again from the spec".
- Why: the mechanism was in place but a covered side task stayed in the main session: not holding. The opportunity cites the person's restatement.

## Scenarios the case format cannot label

### stage-boundary Delegated in week 1, result returned in week 2

- kind: stage-boundary
- Setup: a person-requested subagent starts late on Sunday of week 1 and returns its result on Monday of week 2. Another delegation starts and returns in week 4.
- Expected: Seen in week 1 on the start. For Forming, the instances are credited to weeks 2 and 4.
- Why no case: `expect` has no `forming` value.

### stage-boundary Subagent history is not a main session

- kind: stage-boundary
- Setup: a delegated subagent's child session itself contains several turns that look like a side task.
- Expected: the child session is evidence attached to its parent, not a separate main session; it adds no applicable work and no recognition of its own.
- Why no case: the case format cannot express session roles.
