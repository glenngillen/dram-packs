# Define done: scenarios

Every acceptance scenario for `glenngillen/define-done`, in full. All people, repositories and content are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs a model judgement of criteria and checks, attributable spec retrieval and ordering of criteria, first edit and check; the collected-history fixture shape has none of these, and the pattern names no block the pinned build runs.

Applicable work is a feature or bug fix in the person's main sessions.

## pos-1 Expired and single-use reset links

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, before any edit, the person writes "Done when: an expired reset link returns 410; a link can be used only once; a valid link sets the new password." After implementation the agent runs `TestResetExpired` and `TestResetSingleUse` and shows a manual check of the third line.
- Why: person-authored criteria before implementation, then a check against each.

## pos-2 Referenced spec whose examples are the tests

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, the person wrote `specs/export.md` two days earlier (their commit) with three input/output examples. They write "@specs/export.md implement this; the examples in it are the tests." After implementing, the agent turns the examples into tests and runs them; all pass.
- Why: attributable criteria in a referenced spec, before implementation, then checked.

## pos-3 Behavioural criterion, checked

- kind: boundary
- expect: seen
- Setup: in `tidepool-web`, the person writes "An admin sees archived projects; a member does not." After the change the agent logs in as each role in a local run and reports both views.
- Why: a behavioural criterion counts when the evidence shows it was checked.

## pos-4 Guided criteria on a real fix

- kind: guided-success
- expect: seen
- Setup: in `marlin-cli`, after reading the guide, the person writes two "done when" lines for a `--dry-run` bug before asking for code, then asks the agent to check both; it does.
- Why: the person's criteria and their check on real work. Guided work earns Seen only.

## pos-5 Owned spec command used and holding

- kind: mechanism-held
- expect: continuous
- Setup: the person's `/spec` command creates a spec with a "Done when" section they fill in. In the window they started four features with it; each was implemented after the criteria and checked against them.
- Why: an owned mechanism in place, applied and holding.
- Note: no block reaches `continuous` in the pinned build.

## neg-1 "Make sure it's done properly"

- kind: source-negative
- expect: opportunity
- Setup: in `orchard-jobs`, the person writes "Add job retries. Make sure it's done properly." They accept the result, then reopen it the next day: "this retries forever on bad input; that's not what I meant."
- Why: a vague request is not a criterion. The reopening prompt and the original request are the person-authored citations.

## neg-2 Agent criteria accepted with "ok"

- kind: source-negative
- expect: opportunity
- Setup: in `basalt-sdk`, the agent proposes five acceptance criteria; the person replies "ok". After acceptance, the person reopens the work because a required timeout was missing.
- Why: agent criteria accepted without review are not the person's. The reopen is the opportunity.

## neg-3 Criteria supplied after completion

- kind: boundary
- expect: none
- Setup: in `fern-docs`, the person writes "add search", the agent implements it, and only then the person writes "it should also match partial words" and the agent fixes it. No reopen after acceptance.
- Why: criteria after implementation are review, not defining done; no reopened accepted work means no opportunity.

## neg-4 Guide discussed, no criteria or check

- kind: guided-no-action
- expect: none
- Setup: in `kestrel-app`, the person talks through the guide's questions with the agent, then asks for the feature with no criteria, and never checks.
- Why: coaching conversation without criteria or a check earns nothing.

## neg-5 Only questions and exploration

- kind: no-applicable-work
- expect: none
- Setup: the person's sessions in the window only ask how parts of `slate-ui` work.
- Why: questions and exploration are not feature or fix work.

## neg-6 Referenced spec missing

- kind: missing-evidence
- expect: none
- Setup: in `amber-lib`, the person writes "@specs/billing.md implement this". The file is not present in the collected evidence, and its author is unknown. Tests are later run.
- Why: a missing referenced file or unknown author leaves the result unassessed: insufficient, not a miss and not a recognition.

## neg-7 Spec folder present but unused

- kind: mechanism-unused
- expect: none
- Setup: `heron-service` has a `specs/` folder and a template with "Done when". The person did not use it in the window; their only work was a documentation edit.
- Why: a spec location by itself is not a mechanism in use; untested, with nothing applicable.

## neg-8 Template used, criteria left blank, work reopened

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person runs `/spec` for a feature in `pewter-tools` but leaves "Done when" empty and asks for code. They accept, then reopen: "exports should include archived rows."
- Why: the mechanism was applied but did not hold. The reopening prompt is the person citation.

## neg-9 Criteria given but never checked

- kind: boundary
- expect: none
- Setup: in `garnet-web`, the person writes three clear criteria before any edit. The agent implements and the person merges without any test run or comparison. No reopen.
- Why: Seen requires a later check against the criteria; without one there is no recognition, and with no reopen no opportunity.

## Scenarios the case format cannot label

### stage-boundary Two weeks of checked criteria

- kind: stage-boundary
- Setup: pos-1 in week 1 and pos-2 in week 3, both checked in the same week as their criteria.
- Expected: Forming, crediting each instance to the week its check finished.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Criteria in week 2, check in week 3

- kind: stage-boundary
- Setup: criteria sent at the end of week 2; the check finishes in week 3.
- Expected: the instance is credited to week 3. If week 3 is outside the four-week window, it does not count for that window.
- Why no case: as above.
