# Verification scenarios

Pack-wide acceptance scenarios for the [evidence contract](evidence.md#attribution-and-citations): a future recognizer must **reject** each of these, whichever pattern it is judging. They are not repeated in every pattern's `eval/` because the rule is the same for all 41; each pattern's own scenarios cover what it recognizes.

All data below is invented. Evidence IDs (`p1`, `a1`, `t1`) stand for a person prompt, an agent turn and a tool result in a synthetic packet.

## Why none of these can run at the pinned CLI

Checked against Dram `bdea6f6` (`internal/eval/run.go`, `internal/eval/model.go`, `internal/recommend/recommend.go`, `internal/recommend/verify.go`) on 2026-11-27:

- `dram pack eval` reads only `patterns/<name>/eval/cases.jsonl`. A pack-wide scenario has nowhere to live as an executable case.
- A code-checked case expects a stage (`seen`, `opportunity`, `continuous`, `none`) from fixed blocks. Those findings carry no citation or quote, so there is nothing to fabricate or alter.
- A model-judged case replays a recorded answer through `recommend.Judge`. That verifies **recommendation proposals** (kind, signal, at least three cited occurrences in two sessions in the recent history) and silently drops citations that are not in the history. It is not a pattern-recognition verifier: it has no quote field, no person-authored citation rule, no attribution of agent or subagent turns, and no per-window completion check for a recognition.
- Every pattern in this pack is disabled and names no `detection.model` block, so no recorded answer would be judged anyway.

So every scenario here is kept, with its expected result, and marked unevaluable. None is relabelled `none` to make a check pass.

## ver-1 Fabricated citation

- rejects: fabricated-citation
- expect: rejected
- pattern: any (example: Prove it)
- packet: `p1` "Done? Show me the test output before I merge." `a1` agent reply with test output.
- answer: recognition of Prove it citing `p1` and `p7`.
- why: `p7` does not exist in the packet. A recognition citing a non-existent ID is rejected whole, not trimmed to its valid citations and accepted.
- unevaluable: at bdea6f6 no pack-authored recognition verifier exists; `recommend.Judge` silently drops unknown citations from recommendation proposals and has no recognition contract, and pack-wide cases are not run by `dram pack eval`.

## ver-2 Changed quote

- rejects: changed-quote
- expect: rejected
- pattern: any (example: Define done)
- packet: `p1` "Add the export. It's done when the CSV opens in a spreadsheet with dates in ISO format."
- answer: recognition quoting `p1` as "It's done when the tests pass."
- why: the quote does not match `p1` verbatim. A changed quote is rejected, not repaired to the nearest real text.
- unevaluable: at bdea6f6 neither the fixed-check findings nor `recommend.Judge` carries quotations, so no quote comparison exists to exercise; pack-wide cases are not run by `dram pack eval`.

## ver-3 Agent-only recognition

- rejects: agent-only-attribution
- expect: rejected
- pattern: any (example: Plan first)
- packet: `a1` agent writes a five-step plan and starts editing; the person's next prompt `p2` is about an unrelated file.
- answer: recognition of Plan first citing only `a1`.
- why: an agent-proposed plan counts only with the person's evidenced review. With no person-authored citation, the recognition is unattributable.
- unevaluable: at bdea6f6 no verifier requires a person-authored citation on a recognition; `recommend.Judge` counts occurrences, not authorship, and pack-wide cases are not run by `dram pack eval`.

## ver-4 Agent-only opportunity

- rejects: agent-only-opportunity
- expect: rejected
- pattern: any (example: Evidence, not claims)
- packet: `a1` agent summary "All 212 tests pass." `t1` test output showing three failures. The session ends with no later person turn.
- answer: opportunity for Evidence, not claims citing `a1` and `t1`.
- why: opportunities follow the same citation rule as recognitions (user decision). Agent and tool output alone yield no opportunity.
- unevaluable: at bdea6f6 opportunities are a fixed-check stage with no citations, and no verifier applies the person-citation rule to them; pack-wide cases are not run by `dram pack eval`.

## ver-5 Out-of-window completion

- rejects: out-of-window
- expect: rejected
- pattern: any (example: Second opinion)
- packet: analysis window 2026-11-02 to 2026-11-08, person's local time. `p1` on 2026-11-07 asks for an independent review; the findings are addressed in `p4` on 2026-11-10.
- answer: Forming-stage instance of Second opinion credited to the 2026-11-02 window.
- why: Forming and Established count only follow-through that finished, credited to the week it finished. The completion is outside this window, so it is rejected here and is not silently attributed to the earlier window.
- unevaluable: at bdea6f6 there is no per-window completion check for recognitions, and no stage-dependent completion rule; pack-wide cases are not run by `dram pack eval`.

## ver-6 Subagent turn cited as the person

- rejects: subagent-as-person
- expect: rejected
- pattern: any (example: Brief it)
- packet: a subagent sidechain whose opening prompt `s1` (written by the main agent) states the goal and constraints.
- answer: recognition of Brief it citing `s1` as the person's brief.
- why: main sessions exclude subagents and sidechains; `s1` is the agent's delegation, not a person prompt.
- unevaluable: at bdea6f6 no recognition verifier distinguishes sidechain turns from person prompts; pack-wide cases are not run by `dram pack eval`.

## ver-7 Tool or hook output with a user role

- rejects: tool-output-as-person
- expect: rejected
- pattern: any (example: Make failures actionable)
- packet: `t1` a hook result stored with a user role containing "Lint failed: line 12 unused import".
- answer: recognition citing `t1` as a person prompt.
- why: person prompts exclude tool results, hook output, command output and compaction summaries.
- unevaluable: at bdea6f6 no recognition verifier applies the person-prompt exclusions; pack-wide cases are not run by `dram pack eval`.

## ver-8 Dram's own analysis session

- rejects: analysis-session
- expect: rejected
- pattern: any (example: Right-size it)
- packet: a session started by Dram itself to analyse history, run on a lighter model.
- answer: recognition of Right-size it citing that session.
- why: Dram's own analysis sessions never earn recognition.
- unevaluable: at bdea6f6 the CLI drops its own sessions from collected history using its self-call marker (`internal/tasks/marker.go`), but no pattern-recognition verifier exists to show a recognition citing one is refused, and the collected-history fixture cannot carry a marked session for a pattern case; pack-wide cases are not run by `dram pack eval`.
