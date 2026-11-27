# Gate "done": scenarios

Every acceptance scenario for `glenngillen/gate-done`, in full. All people, repositories, hooks and commands are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no hook execution record, no enforcement result, no configuration history or attribution and no check classification, and the pattern names no block the pinned build runs (`hook_configured` is declared but not implemented).

Applicable work is a repository with tests, a build or type checking where the person has main sessions in the window. "Fired" means the session record shows the gate ran when the agent finished.

## pos-1 make test Stop hook fires and blocks once

- kind: source-positive
- expect: seen
- Setup: `cormorant-api` has a committed Stop hook running `make test`. The person asks for a pagination fix. When the agent tries to finish, the hook runs, one test fails and the agent is blocked; it fixes the off-by-one and finishes after the hook passes.
- Why: attributable final gate running real tests, fired and enforced.

## pos-2 User-level Stop hook invoking the repository's test script

- kind: source-positive
- expect: seen
- Setup: the person's user-level settings contain a Stop hook that runs the repository's `./scripts/test.sh` when present. In `saffron-jobs` it fires at the end of a session and passes.
- Why: a user-level gate counts when it invokes the repository's own test script and actually fired. A passing run proves execution, not that nothing escaped.

## pos-3 Type check gate not called "test"

- kind: boundary
- expect: seen
- Setup: `ember-ui` has a team Stop hook running `pnpm typecheck && pnpm build`. It fires on finish in a session and blocks once on a type error the agent then fixes.
- Why: a valid build or type check counts even when it is not called "test". It takes about four minutes, slower than [`fast_check`](../../../reference/parameters.md#fast_check); speed matters for Gate each step, not for this final gate.

## pos-4 Guided gate fires on real work

- kind: guided-success
- expect: seen
- Setup: following the guide, the person in `heather-cli` has the agent propose a Stop hook running `cargo test`, reviews and commits it. The next day, on a real task, the hook fires on finish and passes.
- Why: guided configuration plus an actual firing on real work. Guided work earns Seen only.

## pos-5 Gate covers every applicable repository and holds

- kind: mechanism-held
- expect: continuous
- Setup: the person works in three repositories with tests in the window. A user-level Stop hook runs each one's test command; it fired in every repository, blocked twice, and both times the agent fixed the failure before finishing.
- Why: full coverage, applied and held; blocking then fixing is held. No block reaches `continuous` in the pinned build.

## neg-1 Stop hook running only prettier

- kind: source-negative
- expect: opportunity
- Setup: `cormorant-web` has a Stop hook running `prettier --write .` only. A session ends with the agent saying "all done"; the person's next prompt is "the tests are failing on main now".
- Why: a formatter-only hook is not a gate. The session finished with failing checks; the person's prompt is the citation.

## neg-2 Unused hook in settings

- kind: mechanism-unused
- expect: none
- Setup: the person added a Stop hook running `make test` in `saffron-jobs` settings, but had no session in that repository in the window.
- Why: configured, never fired: untested. Not Seen and not a miss.

## neg-3 Failure bypassed

- kind: mechanism-not-holding
- expect: opportunity
- Setup: in `cormorant-api` the `make test` Stop hook fails; the person writes "skip the hook, I'll fix the tests later" and the session finishes with failures.
- Why: an enforcement bypass is never holding. The person's prompt is the citation.

## neg-4 Hook ignores its own failure

- kind: source-negative
- expect: opportunity
- Setup: `ember-ui`'s Stop hook runs `pnpm test || true`. Tests fail; the agent finishes anyway. The person later asks "why did you say it passed?".
- Why: a command that silently ignores failure is not a gate. The person's question is the citation.

## neg-5 Guided configuration with no firing event

- kind: guided-no-action
- expect: none
- Setup: the person follows the guide in `heather-cli`, saves the hook, and has no further session there in the window.
- Why: guided configuration without a firing does not complete Seen; there is no applicable session after it.

## neg-6 Guide read, no gate added

- kind: guided-no-action
- expect: opportunity
- Setup: in `heather-cli` the person reads the guide, names `cargo test` as the check and stops. A later session ends with the agent reporting done; the person's next prompt is "cargo test fails, you missed the parser change".
- Why: answering the guide does not count. The session that finished with failing checks is an opportunity, cited by the person's prompt.

## neg-7 Agent runs tests on its own, no gate

- kind: source-negative
- expect: none
- Setup: in `saffron-jobs` there is no configured gate. The agent spontaneously runs `npm test` before finishing; it passes and nothing fails later.
- Why: spontaneous agent behaviour is not the person's gate, and with no failing finish there is no opportunity either. A test command in the transcript is not a gate.

## neg-8 No repository with checks

- kind: no-applicable-work
- expect: none
- Setup: the person's only work in the window is in `notes-vault`, a Markdown notes repository with no tests, build or type check.
- Why: nothing applicable. Not a miss.

## neg-9 Hook run records unavailable

- kind: missing-evidence
- expect: none
- Setup: `cormorant-api` has a Stop hook configured, but the session records were excluded from analysis by the person's privacy settings, so whether it fired is unknown.
- Why: excluded evidence is insufficient, not a miss and not a recognition.

## Scenarios the case format cannot label

### stage-boundary Forming across two weeks

- kind: stage-boundary
- Setup: the gate fires in `cormorant-api` sessions in weeks 1 and 3 of the window.
- Expected: Forming.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Coverage gap blocks Continuous

- kind: stage-boundary
- Setup: the gate fires and holds in two of three applicable repositories; the third has no gate.
- Expected: not Continuous (every applicable repository must be covered); the earned stage from firings is unaffected.
- Why no case: coverage-qualified stages are not expressible in the case format.
