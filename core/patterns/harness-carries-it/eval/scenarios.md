# Let the harness carry it: scenarios

Every acceptance scenario for `glenngillen/harness-carries-it`, in full. All people, repositories, models, gates and commits are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no model tier per change, no gate-to-change linkage and no fourteen-day git survival, and the pattern names no block the pinned build runs.

Applicable work is routine work ([`routine_work`](../../../reference/parameters.md#routine_work)) on a lighter model in a repository whose checks run on the change. Kept means still in the default branch after [`kept_window`](../../../reference/parameters.md#kept_window).

## pos-1 Sonnet session passing its Stop gate, kept fourteen days

- kind: source-positive
- expect: seen
- Setup: in `puffin-api`, which has a team Stop hook running `make test`, the person (usually on Opus) switches to Sonnet and asks "rename `OrderStore` to `OrderRepository`". The Stop hook runs and passes; the change merges and is still in `main` fourteen days later.
- Why: lighter routine work, linked gate passed, kept. Citations: the session's starting prompt, the gate run and the kept merge.

## pos-2 Pinned lighter subagent passing CI and kept

- kind: source-positive
- expect: seen
- Setup: the person's own `docs-writer` subagent, pinned to a lighter model, updates docstrings in `puffin-sdk`. CI runs the test and doc build on the pull request and passes; the change is still in `main` fourteen days later.
- Why: owned pinned-lighter work, CI linked to the change passed, kept.

## pos-3 Most routine work lighter, passing and kept

- kind: mechanism-held
- expect: continuous
- Setup: the person's lighter default with explicit escalation is in place. Over the last four weeks, five routine changes in gated repositories: four ran lighter through it, passed their gates and were kept fourteen days; one was a deliberate escalation to premium for a tricky fix.
- Why: most (four of five, at least four applicable) runs lighter, passes and is kept, through a mechanism in place, applied and holding. No block reaches `continuous` in the pinned build.

## pos-4 Guided trial, later kept

- kind: guided-success
- expect: seen
- Setup: following the guide, the person tries a version bump in `auk-cli` on a lighter model. The CI workflow runs and passes, the change merges and is still in `main` fourteen days later.
- Why: the guided step completed by passing gates and survival. Guided work earns Seen only.

## neg-1 Haiku work without gates, reverted

- kind: source-negative
- expect: none
- Setup: in `tern-scripts`, which has no tests, hook or CI, the person switches to Haiku for a formatting pass. It merges and is reverted three days later.
- Why: no checks ran on the change and it was reverted. Not this pattern. No opportunity either: without effective gates the coaching belongs to Checking the work.

## neg-2 Lighter failure finished on Opus

- kind: source-negative
- expect: none
- Setup: in `puffin-api`, the lighter model's simple fix fails the Stop gate twice; the person switches to Opus, which fixes it, and it is kept.
- Why: work finished on premium after a lighter failure is not the lighter model carrying the work. Kept, but not this pattern's evidence.

## neg-3 Change only nine days old

- kind: boundary
- expect: none
- Setup: in `auk-cli`, lighter routine work passed CI and merged nine days before the analysis date.
- Why: younger than fourteen days: unassessed, not failed and not yet recognized.

## neg-4 Guided trial with no passing and kept evidence yet

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person switches to a lighter model in `puffin-sdk` and asks for a rename, but stops before the checks run and nothing is merged.
- Why: a guided trial without later passing and kept evidence cannot complete the pattern. Nothing is recorded.

## neg-5 Routine work on premium with effective gates

- kind: source-negative
- expect: opportunity
- Setup: in `puffin-api`, where the Stop gate runs `make test` on every session, the person on Opus writes "add docstrings to the payments module" and the agent spends a long session doing only that.
- Why: routine premium work where effective gates could judge a lighter model's result. The opportunity cites the person's prompt and makes no savings claim.

## neg-6 No lighter routine work

- kind: no-applicable-work
- expect: none
- Setup: in the window, the person's routine work ran on their usual model, which is already their lightest, and all other work was design.
- Why: no lighter routine work in a gated repository. Not a miss.

## neg-7 Git history unavailable

- kind: missing-evidence
- expect: none
- Setup: lighter routine work in `auk-cli` passed its gate a month ago, but the repository's history is not available to the CLI (shallow clone).
- Why: survival cannot be established: unassessed, never failed.

## neg-8 Savings estimate offered as evidence

- kind: boundary
- expect: none
- Setup: a recommendation estimated what running routine work lighter in `tern-scripts` would have cost compared with Opus. No lighter run passed gates and was kept.
- Why: savings estimates are not kept-change evidence and cannot substitute for fourteen-day survival.

## neg-9 Mechanism in place, lighter work keeps failing

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person's lighter default is in place. In `puffin-api` three routine tasks in the window fail the Stop gate on the lighter model, and each time the person writes "switch to opus and finish it".
- Why: in place and applied, but lighter routine work routinely failed and was finished on premium: not holding. The opportunity cites the person's prompts and points at the failing gate output, not at the person.

## neg-10 Pinned subagent unused

- kind: mechanism-unused
- expect: none
- Setup: the person defined a lighter `changelog` subagent, but did no routine work in a gated repository in the window.
- Why: configured, never applied: untested.

## Scenarios the case format cannot label

### stage-boundary Credited to the week survival is established

- kind: stage-boundary
- Setup: lighter routine work passed and merged on day 3 of week 1; day 17 (week 3) marks fourteen days kept. Another such change is kept from week 4.
- Expected: Seen when survival is established in week 3, not in week 1. Forming credits weeks 3 and 4.
- Why no case: `expect` has no `forming` value, and the fixture shape has no git survival.
