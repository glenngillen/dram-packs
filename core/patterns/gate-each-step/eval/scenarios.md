# Gate each step: scenarios

Every acceptance scenario for `glenngillen/gate-each-step`, in full. All people, repositories, hooks and commands are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no hook or pre-commit run record, no bypass flag, no check duration or classification and no configuration history, and the pattern names no block the pinned build runs.

Applicable work is a repository with a fast type, lint or unit check (usually finishing within [`fast_check`](../../../reference/parameters.md#fast_check)) where the agent edits or commits in the person's main sessions.

## pos-1 PostToolUse tsc --noEmit blocks after an edit

- kind: source-positive
- expect: seen
- Setup: `osprey-dashboard` has a committed PostToolUse hook running `tsc --noEmit` (about 12 seconds). After the agent edits `chart.ts`, the hook reports "Property 'label' does not exist on type 'Series'" back to the agent, which corrects the type before its next edit.
- Why: owned per-step check, fired after an edit and fed back.

## pos-2 Pre-commit linter blocks a commit

- kind: source-positive
- expect: seen
- Setup: `juniper-sdk` has the team's pre-commit hook running `ruff check` (about 3 seconds). The agent's commit is rejected for an unused import; it removes the import and commits again.
- Why: owned pre-commit check blocked a commit.

## pos-3 Check at the fast_check boundary

- kind: boundary
- expect: seen
- Setup: `osprey-dashboard` replaces its check with `tsc --noEmit -p .` taking 55–60 seconds on every run in the window. It feeds back a type error after an edit.
- Why: a check usually finishing within 60 seconds is fast under the provisional `fast_check` default.

## pos-4 Guided edit-time type check catches a real error

- kind: guided-success
- expect: seen
- Setup: following the guide, the person in `lark-mobile` has the agent propose a PostToolUse type check, reviews and commits it. On a real task that afternoon it feeds back a type error after an edit.
- Why: guided setup followed by an actual feedback event. Guided work earns Seen only.

## pos-5 Step gate covers every repository and holds

- kind: mechanism-held
- expect: continuous
- Setup: the person works in `osprey-dashboard` and `juniper-sdk` in the window. Both have owned step gates; they fired on agent edits or commits every week, caught nine problems and each was fixed at that step. No commit bypassed them.
- Why: full coverage, applied and held. No block reaches `continuous` in the pinned build.

## neg-1 Pre-commit always run with --no-verify

- kind: source-negative
- expect: opportunity
- Setup: `juniper-sdk` has a pre-commit linter, but every agent commit in the window uses `git commit --no-verify`. CI later fails on lint; the person writes "CI is red on lint again, fix it".
- Why: a configured check always bypassed is excluded. The lint defect found only at the end is the opportunity, cited by the person's prompt.

## neg-2 Formatter-only hook

- kind: source-negative
- expect: none
- Setup: `lark-mobile`'s only PostToolUse hook runs a formatter. It rewrites files after each edit; nothing is checked and no defect surfaces later in the window.
- Why: formatter-only hooks are excluded, and with no late-found defect there is no opportunity either.

## neg-3 Configured gate never fired

- kind: mechanism-unused
- expect: none
- Setup: `kite-infra` has a PostToolUse lint hook configured, but the agent made no edits there in the window.
- Why: configured but unused: untested. Not Seen, not a miss.

## neg-4 Gate fires but only passes

- kind: boundary
- expect: none
- Setup: in `osprey-dashboard` the type-check hook fires after every agent edit in the window and passes every time.
- Why: quiet runs establish execution but not Seen, which needs a block or feedback instance. Nothing was missed, so there is no opportunity.

## neg-5 Slower check is not a fast step gate

- kind: boundary
- expect: none
- Setup: `basalt-engine`'s only per-edit hook runs the full test suite, usually taking about four minutes. It feeds back a failure once.
- Why: a check usually slower than `fast_check` is not this pattern's fast gate; it may count toward Gate "done". The repository has no fast check, so it is not applicable here.

## neg-6 Defect found only at the end, gate not firing

- kind: mechanism-not-holding
- expect: opportunity
- Setup: `osprey-dashboard`'s type-check hook is configured for edits, but the agent in use edits through a tool the hook does not cover. A type error introduced early is found only by the final gate; the person writes "why didn't the type check catch this when you edited chart.ts?".
- Why: in place, but it did not fire on the edits it should cover, and the defect surfaced only at the end: not holding.

## neg-7 Guided hook created, no feedback event

- kind: guided-no-action
- expect: none
- Setup: in `lark-mobile` the person configures the type-check hook through the guide; for the rest of the window it fires and passes, never blocking.
- Why: guided hook creation without an actual feedback or block event does not earn Seen.

## neg-8 Guide read, nothing configured

- kind: guided-no-action
- expect: opportunity
- Setup: the person reads the guide for `kite-infra`, names `golangci-lint` as the fast check and stops. Later the final CI run fails on an early lint error; the person writes "lint fails on the first file you touched".
- Why: answering the guide does not count. The late-found early defect is an opportunity, cited by the person's prompt.

## neg-9 No repository with a fast check

- kind: no-applicable-work
- expect: none
- Setup: the person's only repository in the window, `prose-site`, has no type check, linter or unit tests.
- Why: nothing applicable. Not a miss.

## neg-10 Hook records truncated

- kind: missing-evidence
- expect: none
- Setup: `juniper-sdk` sessions are recorded, but hook output is truncated and commit flags are missing, so whether the pre-commit ran or was bypassed cannot be seen.
- Why: truncated evidence is insufficient, not a miss and not a recognition.

## Scenarios the case format cannot label

### stage-boundary Forming from blocking instances in two weeks

- kind: stage-boundary
- Setup: the pre-commit linter in `juniper-sdk` blocks one agent commit in week 1 and one in week 4; weeks 2 and 3 have only passing runs.
- Expected: Forming (instances in two distinct weeks of the last four).
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Quiet runs only

- kind: stage-boundary
- Setup: across all four weeks, the owned PostToolUse type-check hook in `osprey-dashboard` fires after agent edits in eight sessions and passes every time; it never blocks or feeds back.
- Expected: not Seen, not Forming, not Established. Execution alone is not a qualifying instance, and with no defect introduced there are no applicable cases toward Established; this is not a miss.
- Why no case: the case format has no `forming` or `established` expectation (neg-4 covers the Seen-level result).

### stage-boundary Continuous needs every applicable repository

- kind: stage-boundary
- Setup: step gates hold in `osprey-dashboard`, but `juniper-sdk` (also applicable) has none.
- Expected: not Continuous; coverage of every applicable repository is required alongside the held mechanism.
- Why no case: coverage-qualified stages are not expressible in the case format.
