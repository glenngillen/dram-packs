# Make failures actionable: scenarios

Every acceptance scenario for `glenngillen/actionable-failures`, in full. All people, repositories, hooks and messages are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no hook execution record, no field showing whether failure output reached the agent and no link between a named failure and a fixing edit, and the pattern names no block the pinned build runs.

Applicable work is a failure, during agent work in the person's main session, of a hook or check in a repository where such checks run. "Next step" is the agent's immediate response to the delivered failure; see the definition's open question on next step versus next turn.

## pos-1 Lint hook names the shared Button and the agent replaces it

- kind: source-positive
- expect: seen
- Setup: in `wrenfield-web`, the team's committed post-edit hook runs a lint rule. The person asks for a settings page. The agent adds a raw `<button>`; the hook fails and returns to the agent: "no-raw-button: use the shared Button, see components/Button". The agent's next edit replaces the raw element with `Button` and the hook passes.
- Why: owned hook, failure delivered to the agent with fix guidance, linked fix in the next step.

## pos-2 Custom fix-guidance message acted on next turn

- kind: source-positive
- expect: seen
- Setup: in `pebble-ledger`, the person's own pre-commit check, run by the agent as part of committing, rejects money arithmetic on floats with "use Decimal from ledger/money.py; see ledger/money.py:12 for the pattern". The message appears in the agent's tool result. The agent's next turn rewrites the calculation with `Decimal` and the check passes on re-run.
- Why: a custom actionable message acted on immediately; the re-run confirms the fix is linked to the named problem.

## pos-3 Guided wiring, then a real failure fixed

- kind: guided-success
- expect: seen
- Setup: following the guide, the person in `marigold-api` asks the agent to make the import-boundary check return its message to the agent, reviews and commits the change. Two days later, on real work, the check fails with "services must not import from handlers; move shared types to types/". The agent moves the type in its next step and the check passes.
- Why: the real failure-and-fix sequence happened after guided setup. Guided work earns Seen only.

## pos-4 Feedback hook holds across the window

- kind: mechanism-held
- expect: continuous
- Setup: in `wrenfield-web` the team's lint hook with fix messages was in place all window. It failed six times during agent work across three weeks; each failure reached the agent and the agent fixed the named rule in its next step.
- Why: in place, applied (real failures delivered) and held (each fixed next). No block reaches `continuous` in the pinned build, so this is unevaluable even with the records.

## neg-1 Pre-commit failure the agent never saw

- kind: source-negative
- expect: opportunity
- Setup: in `tamarind-cli` the person commits from their own terminal after the agent's session; the pre-commit linter fails there. The agent never receives the output. The person then types "the commit failed on lint, fix it" and the agent guesses at three changes before the linter passes.
- Why: failure output the agent never saw is excluded. The repeated guessing is the coaching trigger, cited by the person's prompt.

## neg-2 Fed-back failure ignored

- kind: source-negative
- expect: opportunity
- Setup: in `pebble-ledger` the same check returns its Decimal message to the agent, which replies "this check looks unrelated" and continues with other files. The person later asks "why is the money check still failing?".
- Why: a failure the agent ignored is excluded. The person's later question is the person-authored citation.

## neg-3 Hook writes logs elsewhere

- kind: source-negative
- expect: opportunity
- Setup: in `lumen-docs`, the person's post-edit hook runs a link checker and writes failures to `.hooklogs/links.txt`; nothing returns to the agent. The person later writes "you broke three links again".
- Why: a hook merely writing logs elsewhere cannot establish agent-visible feedback.

## neg-4 Guided hook setup with no real failure

- kind: guided-no-action
- expect: none
- Setup: the person follows the guide in `marigold-api` and wires the message through, but no check fails during agent work for the rest of the window.
- Why: configuration without a real failure and fix earns nothing; the mechanism is untested, and with no failure there is no applicable moment to count against.

## neg-5 Person reads the guide and changes nothing

- kind: guided-no-action
- expect: opportunity
- Setup: in `tamarind-cli` the person reads the guide, answers "the lint check fails most" and stops. Later that week the agent again makes four attempts at the same undescribed lint failure after the person's prompt "add the export command".
- Why: answering the guide's questions does not count; the repeated attempts on uninformative output remain an opportunity, cited by the person's prompt that started the work.

## neg-6 No checks run during agent work

- kind: no-applicable-work
- expect: none
- Setup: the person's only repository in the window, `fennel-notes`, runs no hooks or checks during agent work; tests are run manually after sessions.
- Why: nothing in the window this pattern applies to. Not a miss.

## neg-7 Unrelated edit after an uninformative failure

- kind: boundary
- expect: opportunity
- Setup: in `quartz-sync` the person's hook returns "check failed (exit 1)". The agent edits a different file, then a later turn happens to fix the original problem after the person writes "the type error in sync.ts is still there".
- Why: an edit after an error is not a linked fix, and a delayed fix in a later turn after the person intervened does not fall inside the next step. The uninformative message is the coaching trigger, cited by the person's prompt.

## neg-8 Hook configured, never failed

- kind: mechanism-unused
- expect: none
- Setup: the team's lint hook with fix messages is in place in `wrenfield-web`, but every run in the window passes.
- Why: in place but never applied to a failure: untested, not held, and not a miss.

## neg-9 Feedback hook in place but not reaching the agent

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the team's lint hook in `wrenfield-web` is configured to return messages, but after an agent update the hook's output is shown only in the terminal. Twice the lint fails during agent work, the agent never receives the message, and the person writes "lint is failing, the Button rule".
- Why: in place and firing, but the feedback did not reach the agent: not holding. The person's prompt is the citation.

## neg-10 Hook output truncated in the session record

- kind: missing-evidence
- expect: none
- Setup: in `quartz-sync` a hook fails and the agent then edits a file, but the session record truncates the hook output, so neither the message nor whether it reached the agent can be seen.
- Why: truncated evidence is insufficient, not a miss and not a recognition.

## neg-11 Agent-only repeated attempts

- kind: source-negative
- expect: none
- Setup: in a headless run launched by a scheduler on its own behalf, the agent hits an uninformative lint failure and retries three times. No person prompt is part of the run.
- Why: an opportunity backed only by agent and tool output is not reported; it needs a person-authored citation.

## Scenarios the case format cannot label

### stage-boundary Forming credited to the week the fix finished

- kind: stage-boundary
- Setup: a failure delivered on the last day of week 1 is fixed in the agent's next step just after midnight in week 2 (person's local time); a second fed-back failure is fixed in week 3.
- Expected: Forming, with instances credited to weeks 2 and 3.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Established needs four applicable failures

- kind: stage-boundary
- Setup A: three applicable failures in four weeks, all fed back and fixed. Setup B: five applicable failures, three fed back and fixed.
- Expected: A is not assessable for Established (fewer than four applicable cases under `most`), which is not a miss. B meets Established (60%, inclusive).
- Why no case: as above.
