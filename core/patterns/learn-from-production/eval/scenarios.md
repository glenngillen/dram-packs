# Learn from production: scenarios

Every acceptance scenario for `glenngillen/learn-from-production`, in full. All fixtures are synthetic: people, services, alerts, errors and tests are invented, and no production credentials or real incident content appear. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI because the collected-history fixture shape has no field for production-signal provenance, fix-to-check linkage or trigger provenance, and the pattern names no block the pinned build runs.

Applicable work is fix work on a production service.

## pos-1 Alert error supplied, reproducing test added

- kind: source-positive
- expect: seen
- Setup: on the invented `gannet-payments` service, the person writes: "Here's the error from the alert: `RefundError: amount_cents must be positive (got 0)` at `refunds/apply.py:88`. Fix it and add a test that reproduces it." The agent adds `test_zero_amount_refund_rejected`, runs it failing, fixes the handler and runs it passing. The person keeps the change.
- Why: an actual production signal supplied by the person, and a new regression check that would catch the problem next time.

## pos-2 Owned error-tracker trigger starting a headless fix

- kind: mechanism-held
- expect: continuous
- Setup: the person's team configured their (invented) error tracker to start a headless agent fix session for new error groups on `gannet-payments`. In the window it fired three times; each fix included a regression test that reproduces the error, the person reviewed and merged each, and none of the three errors recurred in later work.
- Why: an attributable trigger in place, applied and holding.

## pos-3 Single triggered fix with regression test

- kind: source-positive
- expect: seen
- Setup: as pos-2 but in an earlier window with only one trigger firing: the headless fix added `test_null_currency_defaults_to_account` reproducing the tracked error, and the person reviewed it and merged it with "Reviewed, merge it".
- Why: the trigger supplies the intentional action through team configuration; the fix includes a regression check. The citation keeps the trigger provenance (team configuration and the run carrying the tracked error) and the person-authored merge approval.

## pos-4 Guided: real redacted error, test before fix

- kind: guided-success
- expect: seen
- Setup: following the guide, the person pastes a redacted log excerpt from `petrel-queue` ("`TimeoutError: lease renewal exceeded 30s for job <id>`") and asks for a failing test first. The agent writes a test simulating a slow renewal, shows it failing, then fixes the retry logic.
- Why: the guided step was taken on real work with the signal and a preventive check. Guided work earns Seen only.

## pos-5 Regression check added, but the problem recurred

- kind: boundary
- expect: seen
- Setup: the team's error-tracker trigger on `gannet-payments` fired once in the window. The headless fix added `test_refund_currency_mismatch_rejected`, which reproduced the tracked error and passed after the fix, and the person merged it with "Looks right, merge it". Ten days later, on applicable later work, the same `CurrencyMismatchError` recurred through a second refund path the new test did not cover.
- Why: the single fix met Seen when it landed (owned trigger, signal, regression check run, person-authored merge approval). The recurrence makes the mechanism not holding, so this cannot support Continuous even though a regression check exists.

## neg-1 Fix the bug in payments, no signal

- kind: source-negative
- expect: none
- Setup: the person writes "Fix the bug in payments" in `gannet-payments`. The agent makes a change and adds a test.
- Why: a generic bug request without the production signal does not count. A test was added, so this is not the no-check opportunity either.

## neg-2 Fix with no new check

- kind: source-negative
- expect: opportunity
- Setup: the person pastes a production stack trace into `petrel-queue` and writes "fix this". The agent changes one line and reruns the existing tests; no new test or check is added. The person merges it.
- Why: a production fix without a new preventive check is the coaching trigger. The opportunity cites the person's request.

## neg-3 Guided explanation of an alert only

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person describes last week's alert to the agent in their own words and asks what it might mean. No signal is pasted, no test is written, no fix is made.
- Why: a guided explanation without supplying the signal and creating the preventive check is incomplete. No production fix started, so there is no opportunity.

## neg-4 Agent starts itself on production data

- kind: boundary
- expect: none
- Setup: during an unrelated refactor, the agent on its own initiative reads a log file it finds, fixes an error it sees and adds a test. The person made no production-signal request and owns no trigger.
- Why: an agent starting itself does not supply the intentional action; there is no person-authored moment to cite.

## neg-5 Regression test unrelated to the failure

- kind: boundary
- expect: opportunity
- Setup: the person pastes a production error about date parsing in `gannet-payments` and asks for a fix and a test. The agent fixes the parser but the only new test covers an unrelated formatting helper. The person merges.
- Why: the added check does not exercise the failure in the signal, so it is not a preventive check. The person's request is the citation.

## neg-6 No production service work

- kind: no-applicable-work
- expect: none
- Setup: in the window the person only works on an invented internal prototype that is not deployed anywhere.
- Why: no production-service work, so nothing applies. Not a miss.

## neg-7 Change and check not visible

- kind: missing-evidence
- expect: none
- Setup: the person pastes a production error into `petrel-queue` and asks for a fix with a test, but the session record is truncated after the request, and no later history shows the change.
- Why: whether a check was added is unknown, which is insufficient evidence, not a miss.

## neg-8 Trigger in place, never fired

- kind: mechanism-unused
- expect: none
- Setup: the team configured an error-tracker trigger for `petrel-queue`, but no new error group occurred in the window.
- Why: in place but not applied is untested, not held.

## neg-9 Trigger fixes ship without checks

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the `gannet-payments` trigger fired twice; both headless fixes changed code without adding a regression test, and the person merged them with "looks fine". One of the errors recurred a week later.
- Why: the mechanism was in place and applied but did not hold. The opportunity cites the person's merge-approving prompt.

## neg-10 Fix check finishes after the window

- kind: boundary
- expect: none
- Setup: the person supplies a production error on the last evening of the window; the reproducing test is written and run the next morning, after the window ends.
- Why: the completion falls outside the window, so it is not credited to this window; it may count in the next. The request alone is not a miss.

## Scenarios the case format cannot label

### stage-boundary Forming credited to the week the check finished

- kind: stage-boundary
- Setup: a signal-carrying request in week 1 whose regression test finishes in week 2, and another complete fix in week 4.
- Expected: Forming, with instances credited to weeks 2 and 4.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Established needs four production fixes

- kind: stage-boundary
- Setup A: three production fixes, all with signal and regression check. Setup B: five fixes, three with signal and check.
- Expected: A is not assessable for Established (fewer than four applicable items under `most`), not a miss. B meets Established (60%, inclusive).
- Why no case: as above.
