# Set the expectations yourself: scenarios

Every acceptance scenario for `glenngillen/own-the-expectations`, in full. All people, repositories and content are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs git authorship of tests, ordering of test, review and implementation events, and a judgement of substantive review; the collected-history fixture shape has none of these, and the pattern names no block the pinned build runs.

Applicable work is feature or fix work that adds or changes tests.

## pos-1 Person commits the test, asks for it to pass

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, the person commits `export_test.go` (their authorship) with three cases, then writes "make these pass." The agent implements the exporter; the run shows all three passing.
- Why: person-authored expectations before implementation, then an implementation made to pass them.

## pos-2 Failing tests requested, person adds a case, then authorizes

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, the person writes "write failing tests for the slug function first." The agent writes four tests. The person replies "add an empty-input case; it should return an empty string. Then implement." The agent adds it, implements, and all five pass.
- Why: agent-authored tests substantively reviewed by the person before implementation count.

## pos-3 Guided reproduction, read, then fixed

- kind: guided-success
- expect: seen
- Setup: in `tidepool-web`, after reading the guide, the person asks for a failing test reproducing a date-rollover bug, reads it, asks for the assertion to use local time, then asks for the fix. The test passes afterwards.
- Why: guided, but the person's review preceded the fix and the fix passed. Guided work earns Seen only.

## pos-4 Test-first rule followed with review

- kind: mechanism-held
- expect: continuous
- Setup: `marlin-cli`'s instruction file says "write failing tests and wait for review before implementing." In the window, four fixes followed it: the agent stopped, the person reviewed and changed a test each time, and the implementation then passed.
- Why: a mechanism in place, applied and holding, including person review before implementation.
- Note: no block reaches `continuous` in the pinned build.

## neg-1 Code first, then agent tests that mirror it

- kind: source-negative
- expect: opportunity
- Setup: in `orchard-jobs`, the person writes "add proration to invoices." The agent implements it, then writes tests that pass immediately. A week later the person writes "proration is off by one day; the tests didn't catch it because they assert the same wrong value."
- Why: post-hoc agent tests mirror the implementation bug. The person's request and their bug report are the citations.

## neg-2 "Write tests and code" together

- kind: source-negative
- expect: none
- Setup: in `basalt-sdk`, the person writes "write tests and code for the parser." The agent writes both in one step; all pass. No later bug is reported.
- Why: tests and code together, with no review between, are not independent expectations; no mirrored bug was found, so no opportunity.

## neg-3 Unread approval "ok, go"

- kind: source-negative
- expect: none
- Setup: in `fern-docs`, the agent writes failing tests and asks for review; the person replies "ok, go"; the implementation passes.
- Why: unread approval is not substantive review. A passing test is not evidence of independent expectations.

## neg-4 Guided test review, no passing implementation

- kind: guided-no-action
- expect: none
- Setup: in `kestrel-app`, after the guide, the person reviews and adjusts a failing reproduction, but the window ends before any fix is made.
- Why: completion needs the implementation passing the reviewed tests; a guided review alone does not satisfy it. It is pending, not a miss.

## neg-5 No work with tests in the window

- kind: no-applicable-work
- expect: none
- Setup: the person's work in the window changed only documentation and configuration.
- Why: no feature or fix added or changed tests.

## neg-6 Git history unavailable

- kind: missing-evidence
- expect: none
- Setup: in `amber-lib`, tests and code appear in one squashed commit and the session record is truncated, so who wrote the tests and in what order cannot be seen.
- Why: insufficient evidence, not a miss and not a recognition.

## neg-7 Test-first command in place, unused

- kind: mechanism-unused
- expect: none
- Setup: the person has a `/tdd` command. In the window they made no change that added or changed tests.
- Why: in place but untested; nothing applicable.

## neg-8 Test-first rule present but ignored

- kind: mechanism-not-holding
- expect: opportunity
- Setup: `heron-service`'s instructions require failing tests before implementation. The agent implemented a fix first and wrote tests after; the person later wrote "this fix is wrong and the new test asserts the wrong behaviour."
- Why: the rule was in place but did not hold; the mirrored bug the person reported is the citation. A rule merely present cannot establish Continuous.

## Scenarios the case format cannot label

### stage-boundary Review in week 1, passing implementation in week 2

- kind: stage-boundary
- Setup: the person reviews failing tests at the end of week 1; the implementation passes in week 2.
- Expected: the instance completes in week 2 and is credited there. Before the pass it is pending, not a miss.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Forming from two weeks

- kind: stage-boundary
- Setup: pos-1 in week 1 and pos-2 in week 3.
- Expected: Forming.
- Why no case: as above.
