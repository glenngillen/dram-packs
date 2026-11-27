# Second opinion: scenarios

Every acceptance scenario for `glenngillen/second-opinion`, in full. All people, repositories, agents and findings are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no reviewer provenance, no link between a review and the change it reviewed, and no automated review run records, and the pattern names no block the pinned build runs nor a judge it executes.

Applicable work is an agent change from the person's main sessions committed or opened as a pull request in the window.

## pos-1 Own review agent, two fixes

- kind: source-positive
- expect: seen
- Setup: in `heathrow-ledger`, the person writes "@agent-reviewer review this diff before I commit". The reviewer, their own agent with no part in writing the change, reports three findings. The person asks the implementing session to fix two and explains why the third is intended. The change is committed.
- Why: an independent review requested by the person, with its findings acted on.

## pos-2 Fresh session reviews the branch

- kind: source-positive
- expect: seen
- Setup: in `marram-ui`, the person opens a new session that did not write the change and asks "review branch `feat/export` for bugs". It reports an off-by-one in pagination. The person has the implementing session fix it before opening the pull request.
- Why: a fresh reviewer session with no implementing provenance, and the result used.

## pos-3 Built-in review with a clean result

- kind: boundary
- expect: seen
- Setup: in `marram-ui`, the person runs `/review` on a pull request. The output lists what it checked and reports no blocking findings. The person merges.
- Why: a built-in review counts here (unlike ownership for Save it), and an evidenced clean result accepted is a used result.

## pos-4 Guided independent review used

- kind: guided-success
- expect: seen
- Setup: following the guide in `quince-api`, the person asks a different model to review their real diff and fixes the one finding before committing.
- Why: a qualifying review on real work while following the guide. Guided work earns Seen only.

## pos-5 Pull request reviewer runs and is used on every change

- kind: mechanism-held
- expect: continuous
- Setup: the team's pull request review job, configured in `heathrow-ledger`, ran on all five of the person's agent pull requests in the window. Each had its findings fixed or answered before merge.
- Why: automated independent review in place, applied and holding.
- Note: no block reaches `continuous` in the pinned build, so this case would be unevaluable even with provenance.

## pos-6 Review requested, findings pending

- kind: boundary
- expect: seen
- Setup: in the last days of the window, the person has a fresh session review a committed change in `quince-api`. The review lists two findings; the fixes are not made before the window ends.
- Why: the review request with its result earns Seen. It does not yet count toward Forming; the pending follow-through is not a miss.

## neg-1 "Looks right to you?" in the implementing session

- kind: source-negative
- expect: opportunity
- Setup: in `heathrow-ledger`, after the agent writes a migration, the person asks the same session "Looks right to you?". It answers yes; the change is merged and needs two fix-up commits the next day.
- Why: the implementing session is not independent. The unreviewed merge needing fix-ups is the opportunity, citing the person's question and merge prompt.

## neg-2 Findings ignored

- kind: source-negative
- expect: opportunity
- Setup: in `marram-ui`, a fresh session reviews the branch and reports a null-handling bug. The person writes "merge it" without fixing or answering the finding. A fix-up follows two days later.
- Why: ignored findings mean the review was not used. The person's "merge it" is the citation.

## neg-3 Reviewer persona inside the implementing session

- kind: boundary
- expect: opportunity
- Setup: in `quince-api`, the person writes "now act as a strict reviewer and check your work" to the session that wrote the change. It finds nothing; the change is merged and needs a fix-up.
- Why: a different name does not prove independence; the reviewer has implementing provenance.

## neg-4 Guided request without independent execution

- kind: guided-no-action
- expect: none
- Setup: the person reads the guide, asks the implementing session how to run a review, and stops. No review runs and the change stays uncommitted in the window.
- Why: a guided request without an independent review and its result does not count; with no change committed there is no applicable work to call a miss.

## neg-5 No committed change in the window

- kind: no-applicable-work
- expect: none
- Setup: the person's agent sessions in the window only explored code and produced no committed change or pull request.
- Why: no applicable work. Not a miss.

## neg-6 Reviewer provenance unavailable

- kind: missing-evidence
- expect: none
- Setup: in `heathrow-ledger`, a review output appears in a session, but records of which session produced the change are truncated, so whether the reviewer wrote it cannot be shown.
- Why: missing provenance is insufficient, not a miss and not a recognition.

## neg-7 Automated reviewer configured, no change in the window

- kind: mechanism-unused
- expect: none
- Setup: the pull request review job is in place in `marram-ui` but the person opened no pull request there in the window.
- Why: in place but never applied is untested, not held.

## neg-8 Automated review ran, findings ignored

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the pull request review job in `heathrow-ledger` ran on the person's pull request and flagged an unchecked error. The person wrote "approve and merge" without addressing it; a fix-up followed.
- Why: the mechanism was in place and applied but its findings were not used, so it is not holding. The person's prompt is the citation.

## neg-9 Spontaneous agent self-review, merged without fix-ups

- kind: boundary
- expect: none
- Setup: the agent decides on its own to "double-check" its change before finishing. The person commits; nothing needs fixing afterwards.
- Why: spontaneous agent behaviour is not the person's deliberate review, so it is not recognized; with no fix-up and no person-authored missed moment, there is no opportunity.

## Scenarios the case format cannot label

### stage-boundary Findings acted on in a later week

- kind: stage-boundary
- Setup: the person requests a fresh-session review in week 1 and gets findings; they act on them in week 2. Another independent review is requested and used within week 3.
- Expected: Seen in week 1 (request with result). Forming, with instances credited to weeks 2 and 3, the weeks the findings were acted on.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Follow-through outside the window

- kind: stage-boundary
- Setup: review requested and returned inside the window; findings fixed after the window ends.
- Expected: Seen in this window; the instance counts toward Forming only in the window where the fixes finished.
- Why no case: as above.
