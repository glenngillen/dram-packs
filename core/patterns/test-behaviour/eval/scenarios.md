# Test behaviour: scenarios

Every acceptance scenario for `glenngillen/test-behaviour`, in full. All people, repositories, APIs and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape cannot say what a test asserts, whether the person reviewed a recorded output or snapshot diff, or that a run belongs to a requested check, and the pattern names no block the pinned build runs nor a judge it executes.

Applicable work is a behaviour-changing change to an API, output or user flow in the person's main sessions.

## pos-1 Requested export contract test, run

- kind: source-positive
- expect: seen
- Setup: in `gannet-reports`, the person is changing the CSV export. They write "Before you change the exporter, write a contract test asserting the columns and types the billing client reads, then run it." The agent writes the test, runs it, and shows it passing after the change.
- Why: a person-requested behaviour check against client expectations, then executed.

## pos-2 Recorded emails reviewed and run

- kind: source-positive
- expect: seen
- Setup: in `pipit-accounts`, changing password reset, the person writes "Record the emails it sends in the test and show me." The agent records the outgoing emails in the test, runs it, and shows the recorded subject and link; the person reads them and asks for the link's expiry text to be fixed.
- Why: a recorded side effect, reviewed by the person, with execution.

## pos-3 Behaviour check in a unit-test tool

- kind: boundary
- expect: seen
- Setup: in `gannet-reports`, the person asks for a test, written with the project's unit-test framework, that calls the public `/v2/summary` handler with a real request and asserts the response fields the mobile app reads. It runs and passes.
- Why: classify what is checked, not the framework name.

## pos-4 Failing behaviour test

- kind: boundary
- expect: seen
- Setup: in `pipit-accounts`, the person asks for an end-to-end check of sign-up. It runs and fails on the confirmation page.
- Why: the failing run proves the checking occurred, which earns Seen for the act; it does not show the change satisfies the behaviour.

## pos-5 Guided caller-side check

- kind: guided-success
- expect: seen
- Setup: following the guide in `tern-api`, the person names the mobile client as the caller, asks for a contract test of the changed endpoint, reads it and has it run.
- Why: a qualifying check on real work while following the guide. Guided work earns Seen only.

## pos-6 Behaviour checks run in CI on every change

- kind: mechanism-held
- expect: continuous
- Setup: `gannet-reports` CI runs the contract suite on every pull request. All four of the person's behaviour-changing pull requests in the window ran it, and one failure was fixed before merge.
- Why: automatic behaviour checks in place, applied and holding.
- Note: no block reaches `continuous` in the pinned build, so this case would be unevaluable even with the needed evidence.

## neg-1 Agent unit tests alone after implementation

- kind: source-negative
- expect: opportunity
- Setup: in `tern-api`, the person writes "rename the `amount` field to `total` in the response". The agent changes the handler, then writes unit tests asserting the new field. The person accepts. The mobile client breaks the next day.
- Why: implementation-only tests after the code are excluded. The change passed unit checks but broke a caller; the person's accepting prompt is the citation.

## neg-2 Unreviewed snapshot update

- kind: source-negative
- expect: opportunity
- Setup: in `pipit-accounts`, snapshot tests of the rendered invoice fail after a change. The person writes "just update the snapshots"; the agent runs the suite with `-u` and the person accepts without reading the diff. A missing tax line reaches customers.
- Why: an unreviewed snapshot update does not count. The person's prompt is the citation.

## neg-3 "e2e" label without relevant assertions

- kind: source-negative
- expect: none
- Setup: in `tern-api`, the agent adds `test_e2e_checkout` that only asserts the server starts. The person did not ask for it. Nothing breaks afterwards.
- Why: an "e2e" label cannot substitute for behaviour coverage, and the agent added it on its own. With no broken caller, there is no opportunity to cite.

## neg-4 Guided discussion only

- kind: guided-no-action
- expect: none
- Setup: the person reads the guide, discusses callers of an endpoint with the agent, and stops before any check is written or run. The change is not made in the window.
- Why: discussion without a requested or written, executed behaviour check is incomplete; no behaviour-changing change was made, so there is nothing to call a miss.

## neg-5 Check requested but never run

- kind: boundary
- expect: none
- Setup: in `gannet-reports`, the person asks for a contract test; the agent writes it, but the session ends before it is run and no later session runs it. Nothing breaks.
- Why: Seen needs execution. Without a broken caller, there is no opportunity either.

## neg-6 Refactor with no behaviour change

- kind: no-applicable-work
- expect: none
- Setup: the person's only work in the window is renaming private helpers in `tern-api`; no API, output or flow changes.
- Why: no applicable work. Not a miss.

## neg-7 Run output truncated

- kind: missing-evidence
- expect: none
- Setup: in `pipit-accounts`, the person requests a recorded-emails test; the session record is truncated before the run output.
- Why: whether the check ran is unknown. Insufficient, not a miss and not a recognition.

## neg-8 CI contract suite in place, no behaviour change

- kind: mechanism-unused
- expect: none
- Setup: `gannet-reports` CI runs the contract suite, but the person made no behaviour-changing change there in the window.
- Why: in place, never applied: untested, not held.

## neg-9 CI behaviour checks in place, caller broke

- kind: mechanism-not-holding
- expect: opportunity
- Setup: `tern-api` CI runs contract tests, but the person writes "merge it, the CI skip label is fine" on a response change; the contract job is skipped and the mobile client breaks.
- Why: in place and normally applied, but not holding on this change. The person's prompt is the citation.

## Scenarios the case format cannot label

### stage-boundary Check run in a later week

- kind: stage-boundary
- Setup: the person requests a contract test in week 1; it is written and first run in week 2. Another requested recorded-output check runs and is used in week 3.
- Expected: Seen when the first check runs (week 2). Forming, with instances credited to weeks 2 and 3.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.
