# Prove it: scenarios

Every acceptance scenario for `glenngillen/prove-it`, in full. All people, repositories, commands and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs model judgement of a person's request for proof and the ordering of edit, completion claim, request and check, and names no block the pinned build runs. The scenarios are kept in full so they can become fixtures when those capabilities exist.

Applicable work is a turn in the person's main session where the agent changed code and then reported completion.

## pos-1 "Run the tests and show me", then go test

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, the agent edits `handlers/order.go` and says "Done, the nil check is in place." The person replies "run the tests and show me". The agent runs `go test ./...` and shows the output (all packages ok).
- Why: a person's request for proof after the change and completion claim, followed by a relevant check actually running.

## pos-2 "Did you lint it?", then ruff check

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, the agent rewrites `parse.py` and reports "Refactor finished." The person asks "did you lint it?". The agent runs `ruff check .` and shows two warnings it then fixes.
- Why: the post-edit request was followed by a relevant lint check executing.

## pos-3 Request followed by a failing check

- kind: source-positive
- expect: seen
- Setup: in `tidepool-web`, the agent changes `src/cart.ts` and says "All passing now." The person writes "show me the test output". The agent runs `npm test`; two tests fail.
- Why: the request was made and a check ran, so the person asked for evidence. The failure is recorded as the result: it proves checking occurred, **not** that the change works. "A check ran" is distinct from "a check passed".

## pos-4 Guided request with execution

- kind: guided-success
- expect: seen
- Setup: following the guide during a real fix in `marlin-cli`, after the agent reports "fixed", the person asks "run the tests that cover this change and show me the output". The agent runs `cargo test parser::` and shows the passing output.
- Why: the guided step on real work, completed by execution. Guided work earns Seen only.

## pos-5 Check executed, output truncated

- kind: boundary
- expect: seen
- Setup: in `cobalt-infra`, after "Done", the person asks "run the tests". The record shows `go test ./...` executed and exited, but its output is truncated before any result line.
- Why: the request and the check's execution are recorded, so the person asked for evidence and a check ran: Seen. The result is **unknown**, not passing and not failing. Truncated output is never treated as adverse evidence or as a pass.

## neg-1 Spontaneous pytest without any instruction

- kind: source-negative
- expect: opportunity
- Setup: in `orchard-jobs`, the agent edits `jobs/retry.py`, runs `pytest` on its own, then says "Done." No instruction file or hook asks for checks, and the person never asked. The agent then edits `jobs/retry.py` again and says "Also handled the timeout case." The person replies "great, now let's do the scheduler".
- Why: the earlier `pytest` was the agent's own habit, not the person's act, so it is not recognized. It also ran before the final edit, so the last claim was accepted with nothing run after the last edit; the opportunity cites the person's "great, now let's do the scheduler".

## neg-2 Test request before any edit

- kind: source-negative
- expect: opportunity
- Setup: in `fern-docs-api`, the person opens with "make sure you run the tests" and asks for a bug fix. The agent runs `make test` first, then edits `server.go`, and says "Fixed." The person replies "thanks, commit it".
- Why: the request preceded any change and the check ran before the edit, so nothing substantiated the later claim. The opportunity cites "thanks, commit it", which accepted the claim with nothing run after the last edit.

## neg-3 Guided request with no following check

- kind: guided-no-action
- expect: opportunity
- Setup: reading the guide, the person asks in `kestrel-app` "did you run the tests?" after the agent reports a change done. The agent answers "Yes, they should pass" without running anything. The person then replies "ok, good" and ends the session.
- Why: a request with no following check is incomplete, so it is not Seen. The claim stood with nothing run after the last edit, and the person's later "ok, good" accepted the unverified answer; the opportunity cites that reply (with the question as context). Without such a later acceptance turn there would be no attributable accepting moment and no opportunity.

## neg-4 Check before the final edit

- kind: boundary
- expect: opportunity
- Setup: in `basalt-sdk`, the person asks "run the tests and show me" after a first edit; `go test ./...` passes. The agent then makes another edit to the same function and says "Done, also tidied the error message." The person says "ship it".
- Why: the check ran before the final edit, so it does not substantiate the later completion claim. The new claim was accepted with nothing run after the last edit; the opportunity cites "ship it".

## neg-5 Irrelevant command after the request

- kind: boundary
- expect: opportunity
- Setup: in `heron-service`, after "Done", the person asks "did you check it works?". The agent runs `git diff --stat` and says "Yes, the change is small and correct." The person replies "ok".
- Why: `git diff --stat` is not a test, build, lint or type check relevant to the change, so no check ran. The opportunity cites "ok".

## neg-6 Agent-only claim with no later person turn

- kind: boundary
- expect: none
- Setup: in `slate-ui`, the agent edits a component, says "All tests passing", and the session ends with no further person turn.
- Why: an opportunity must cite a person-authored moment that accepted the claim or started further work. Agent-only evidence is not reported.

## neg-7 No code changed

- kind: no-applicable-work
- expect: none
- Setup: in the window, the person only asked the agent to explain modules in `pewter-tools` and to draft a design note. No code was edited.
- Why: no turn changed code and ended in a completion claim, so the pattern is counted against nothing. Not a miss.

## neg-8 Truncated record hides the check

- kind: missing-evidence
- expect: none
- Setup: in `amber-lib`, after an edit and "Done", the person asks "run the tests and show me". The session record is truncated immediately after the request; whether a check ran cannot be seen.
- Why: missing evidence is insufficient, not a miss and not a recognition.

## Scenarios the case format cannot label

### stage-boundary Forming credited to the week the check ran

- kind: stage-boundary
- Setup: a proof request at 23:58 on Sunday of week 1 (person's local time). The agent starts executing the relevant check at 00:01 on Monday of week 2 and it completes at 00:03. Another request, with its check starting and completing, in week 3.
- Expected: Seen in week 2, anchored to the check's execution, because this pattern requires a relevant check actually executing and execution started in week 2; the request alone in week 1 earns nothing. For Forming, instances are credited to weeks 2 and 3, two distinct weeks of the last four.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Continuous comes from other patterns

- kind: stage-boundary
- Setup: the person adds a hook that runs tests after every edit; checks now run without asking.
- Expected: recognized under Checks by default (and Gate "done" if final), not as Continuous for this pattern. No stage is transferred automatically.
- Why no case: the case format cannot express cross-pattern stage separation.
