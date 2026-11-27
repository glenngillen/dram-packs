# Evidence, not claims: scenarios

Every acceptance scenario for `glenngillen/evidence-not-claims`, in full. All people, repositories, commands and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs model judgement comparing claims with recorded results, recognizing the person's challenge and the agent's addressing response, and names no block the pinned build runs.

Applicable work is an agent claim contradicted by a recorded result in the person's main session.

## pos-1 "You said all pass but 3 failed above", addressed

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, `go test ./...` output shows `FAIL` in three tests. The agent summarises "All tests pass." The person writes "You said all pass but 3 failed above. Fix those first." The agent fixes the three, reruns, and shows them passing.
- Why: a warranted challenge naming the gap, and the response addressed the recorded result.

## pos-2 Three passing cases when four were expected

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, the person asked for four parser cases. Output shows `3 passed`. The agent says "All cases handled." The person replies "I asked for four cases and only three ran. Where's the empty-input one?" The agent adds and runs the fourth.
- Why: a shortfall against the person's request is a contradiction even though everything that ran passed; the response addressed it.

## pos-3 Skipped tests reported as passing

- kind: source-positive
- expect: seen
- Setup: in `tidepool-web`, `npm test` output shows `12 passed, 5 skipped`. The agent says "Full suite green." The person asks "why are 5 skipped? Those cover checkout." The agent un-skips them; two fail and it fixes them.
- Why: skipped cases contradicting "full suite" are a recorded gap; the challenge was addressed.

## pos-4 Guided comparison finds a real gap

- kind: guided-success
- expect: seen
- Setup: following the guide on real work in `marlin-cli`, the person compares "build succeeded" against output showing a linker error, writes "the build output shows a linker error, fix it before we go on", and the agent fixes it and rebuilds.
- Why: the guided step on real work with an actual discrepancy. Guided work earns Seen only.

## pos-5 Challenge issued, response pending

- kind: boundary
- expect: seen
- Setup: in `orchard-jobs`, the person challenges "you said done but the lint step errored" on the last day of the window. The agent's fix finishes after the window ends.
- Why: Seen completes on the challenge. The response finished outside the window, so it does not count toward Forming or Established in this window; that is not a miss.

## pos-6 Evidence-enforcing rule held

- kind: mechanism-held
- expect: continuous
- Setup: the person's committed `AGENTS.md` in `basalt-sdk` and `heron-service` (present before the window) says "never claim tests pass without pasting the test summary". Across eight completion claims in the window the agent includes the summary lines each time; in one, the pasted output shows a failure and the agent reports it rather than claiming success.
- Why: an owned rule in place, applied to every completion claim and holding.
- Note: no block reaches `continuous` in the pinned build.

## pos-7 Challenge ignored by the agent

- kind: boundary
- expect: seen
- Setup: in `cobalt-infra`, the person writes "you said green but the integration test failed". The agent replies "That test is flaky, all good" and does nothing.
- Why: Seen completes on the challenge itself. The follow-through visibly failed, so it never counts toward Forming or Established.

## neg-1 "Great, thanks" after the contradiction

- kind: source-negative
- expect: opportunity
- Setup: as pos-1's output and claim, but the person replies "Great, thanks" and asks for the next feature.
- Why: accepting a claim the recorded output contradicts. The opportunity cites "Great, thanks" and the failing output lines.

## neg-2 Challenging a correct, complete result

- kind: source-negative
- expect: none
- Setup: in `slate-ui`, output shows `24 passed, 0 failed, 0 skipped`, matching the four cases the person asked for. The agent says "All pass." The person asks "are you sure? show me again."
- Why: no contradiction exists, so the moment is not applicable. Not a recognition and not a miss.

## neg-3 Question with no discrepancy

- kind: boundary
- expect: none
- Setup: in `fern-docs-api`, the person asks "did everything really pass?" while the output fully supports the claim.
- Why: a question without an actual discrepancy does not earn the pattern and is not applicable work.

## neg-4 Guided review finds nothing to challenge

- kind: guided-no-action
- expect: none
- Setup: following the guide in `kestrel-app`, the person compares the summary with the output and finds they match, so they do not challenge anything.
- Why: a guided review without a warranted challenge is not a failure and does not fabricate an opportunity.

## neg-5 Contradicted claim with no later person turn

- kind: boundary
- expect: none
- Setup: in `pewter-tools`, the agent says "all tests passed" above output showing two failures, and the session ends.
- Why: agent-only evidence; an opportunity needs a person-authored citation.

## neg-6 No claims about recorded results

- kind: no-applicable-work
- expect: none
- Setup: in the window, every agent claim matched its output, or no checks ran.
- Why: nothing contradicted, so the pattern is counted against nothing.

## neg-7 Truncated output hides the result

- kind: missing-evidence
- expect: none
- Setup: in `amber-lib`, the agent says "all tests passed"; the test output is truncated before its summary line. The person replies "thanks".
- Why: truncated output may hide failures or a later pass. Insufficient evidence is unassessed: not a contradiction, not an opportunity.

## neg-8 Rule in place, no applicable claim

- kind: mechanism-unused
- expect: none
- Setup: the person's evidence rule is committed in `garnet-web`, but in the window no completion claim about check output was made there.
- Why: in place but never applied: untested, not held.

## neg-9 Rule in place and applied, still contradicted

- kind: mechanism-not-holding
- expect: opportunity
- Setup: in `basalt-sdk`, with the pos-6 rule loaded, the agent claims "all tests pass" without pasting output, while the earlier run shows a failure. The person replies "ok, merge it".
- Why: the mechanism was in place and applied but did not hold. The opportunity cites "ok, merge it" and the failing output.

## neg-10 Challenge from a reviewer agent

- kind: boundary
- expect: opportunity
- Setup: in `heron-service`, a reviewer subagent comments "the summary says pass but one test failed". The person replies "fine, ship it".
- Why: the challenge came from an agent, not the person, so there is no recognition. The person accepted the contradicted claim; the opportunity cites "fine, ship it".

## Scenarios the case format cannot label

### stage-boundary Challenge in week 1, addressed in week 2

- kind: stage-boundary
- Setup: the person challenges a contradicted claim on Friday of week 1; the agent's addressing fix finishes on Monday of week 2. Another addressed challenge finishes in week 4.
- Expected: Seen in week 1 (the challenge). For Forming, the first instance is credited to week 2 and the second to week 4: two distinct weeks, so Forming.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Ignored challenges never reach Forming

- kind: stage-boundary
- Setup: two challenges in weeks 1 and 3, both ignored as in pos-7.
- Expected: Seen only. Neither counts toward Forming.
- Why no case: as above.
