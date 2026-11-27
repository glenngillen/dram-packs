# Point, don't paste: scenarios

Every acceptance scenario for `glenngillen/point-dont-paste`, in full. All people, repositories, files and logs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape cannot link a request's named files or excerpts to the agent's later reads, has no exploration measure and no relevance judgement, and the pattern names no block the pinned build runs.

## pos-1 Billing rounding file and failing test, both used

- kind: source-positive
- expect: seen
- Setup: in `tallyhouse`, the person writes "Half-cent invoices round down. The logic is in `billing/rounding.py`; `test_round_half_cent` in `tests/billing/test_rounding.py` fails." The agent reads `billing/rounding.py`, runs the named test, fixes the rounding and reruns it. No repository-wide search happens first.
- Why: relevant file and test named by the person and actually used without broad exploration. Cites the request and the agent's read of the file.

## pos-2 Five relevant log lines

- kind: source-positive
- expect: seen
- Setup: in `tallyhouse`, the person pastes the five lines of a worker log showing a `KeyError: 'currency'` with its stack frame, and asks why the nightly job fails. The agent goes from the frame to `jobs/nightly.py` and fixes the missing key.
- Why: a concise, relevant excerpt the agent worked from.

## pos-3 Necessary large trace is not penalized

- kind: boundary
- expect: seen
- Setup: in `quarry-db`, the person pastes a 400-line deadlock report (both full thread dumps are needed to see the lock order) and names `storage/locks.go`. The agent uses both dumps and the named file.
- Why: size alone is not the test. The paste was necessary and used, so it counts.

## pos-4 Guided pointers used in a real request

- kind: guided-success
- expect: seen
- Setup: following the guide, the person identifies `api/limits.py`, `test_burst_limit` and three error lines, then sends a real request with them. The agent reads the file and runs the test first.
- Why: the person's pointed request on real work, actually used. Guided work earns Seen only.

## pos-5 Codebase map in the instruction file, used

- kind: mechanism-held
- expect: continuous
- Setup: the team's committed `AGENTS.md` in `tallyhouse` (in place before the window) has a codebase map: billing in `billing/`, tests in `tests/billing/`, job definitions in `jobs/`. In the window, four requests needing context load it; in each the agent goes straight to the mapped area and its tests.
- Why: map in place, applied and holding.

## neg-1 "Find the bug somewhere in billing"

- kind: source-negative
- expect: opportunity
- Setup: the person writes "Find the bug somewhere in billing." The agent lists and reads twenty-three files across `billing/` and `tests/` before finding the rounding function.
- Why: no precise pointer; avoidable broad exploration followed. The person's request is the citation.

## neg-2 Unnecessary three-thousand-line log paste

- kind: source-negative
- expect: opportunity
- Setup: the person pastes a three-thousand-line job log and asks why the job fails. The failure is in five lines near the end; the rest is routine progress output. The agent's context fills and it later asks the person to restate the original question.
- Why: a huge paste where a small excerpt would have done, displacing useful context. Cites the person's request.

## neg-3 Named file not used by the work

- kind: source-negative
- expect: none
- Setup: the person writes "Something in `README.md` might help; fix the flaky upload test." The agent never opens `README.md`; it finds the issue from the test output alone.
- Why: a named file the work did not use cannot earn recognition. The agent did not explore broadly either, so there is no opportunity.

## neg-4 Guide answered, no request sent

- kind: guided-no-action
- expect: none
- Setup: the person reads the guide and lists `api/limits.py` and a test name in their reply, then ends the session without sending a request using them.
- Why: identifying pointers without using them in a request does not count. No applicable request followed, so there is nothing missed.

## neg-5 "Read the whole repository first"

- kind: source-negative
- expect: opportunity
- Setup: the person writes "Read the whole repository first, then add a retry to the uploader." The agent reads ninety files before touching `upload/client.py`.
- Why: an instruction to read everything is excluded; the uploader file was the relevant pointer. Cites the request.

## neg-6 Requests need no existing context

- kind: no-applicable-work
- expect: none
- Setup: every request in the window asks for new standalone scripts or general explanations.
- Why: nothing needed codebase or external context.

## neg-7 Agent actions truncated

- kind: missing-evidence
- expect: none
- Setup: the person names `billing/rounding.py` and a test, but the session record is truncated right after the request, so whether the agent used them cannot be seen.
- Why: missing use evidence is insufficient: not a recognition and not a miss.

## neg-8 Map in place, no applicable request

- kind: mechanism-unused
- expect: none
- Setup: the codebase map from pos-5 is in place, but in the window the person's only sessions in `tallyhouse` are documentation edits needing no code context.
- Why: in place but never applied: untested, not held.

## neg-9 Map loaded but sessions still explore broadly

- kind: mechanism-not-holding
- expect: opportunity
- Setup: with the map from pos-5 loaded, the person asks "Why are refunds double-counted?". The agent searches the whole repository and reads thirty files before reaching `billing/refunds.py`, which the map lists.
- Why: in place and applied, but broad exploration recurred for mapped material. Cites the person's request.

## Scenarios the case format cannot label

### stage-boundary Seen versus Forming follow-through

- kind: stage-boundary
- Setup: in week 1 the person sends a pointed request and the agent uses the file, but the fix is finished only in week 2. In week 3 another pointed request is used and finished the same week.
- Expected: Seen in week 1 on the request. Toward Forming, the first instance is credited to week 2 when its work finished, and the second to week 3: two distinct weeks.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Corroboration after the window ends

- kind: stage-boundary
- Setup: the pointed request is sent on the last day of the window; the agent's read of the named file happens after midnight, outside it.
- Expected: unresolved. Delayed corroboration handling is a CLI contract dependency (see the open question in the definition); the instance must not be silently credited to the earlier window.
- Why no case: as above.
