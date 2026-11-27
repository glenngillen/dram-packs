# Right-size it: scenarios

Every acceptance scenario for `glenngillen/right-size-it`, in full. All people, repositories, models and commands are invented examples. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs routine-work judgement, model-choice provenance, usual-model facts, pricing tiers and edit-to-model linkage, none of which the collected-history fixture shape carries, and it names no block the pinned build runs.

Applicable work is routine work ([`routine_work`](../../../reference/parameters.md#routine_work)) in the person's main sessions. This is model selection; nothing here comes from `infracost/right-size-it`.

## pos-1 Usual Opus, person switches to Sonnet, then docstring edits

- kind: source-positive
- expect: seen
- Setup: the person usually works on Opus in `wren-sdk`. Before asking for docstrings on the public client, they type `/model sonnet`, then "add docstrings to every exported function in client.py". The agent edits `client.py` on Sonnet.
- Why: a person-selected lower tier before routine work, followed by edits on it. The `/model sonnet` command and the first edit are the citations.

## pos-2 Owned lighter docs-writer subagent used twice

- kind: mechanism-held
- expect: continuous
- Setup: the person defined their own `docs-writer` subagent pinned to a lighter model. In the window they ask "use docs-writer to update the README for the new flags" in `wren-sdk` and, a week later, the same for `tern-cli`. Both runs edit documentation on the lighter tier; harder work in those sessions stays on the main model by the person's choice.
- Why: an owned subagent pinned lighter, in place, applied twice to routine work and holding. Unlike an ordinary lighter subagent, an owned pinned one is a mechanism. No block reaches `continuous` in the pinned build.

## pos-3 Guided switch on a real version bump

- kind: guided-success
- expect: seen
- Setup: following the guide in `heron-api`, the person asks which models are supported, switches to the lighter one the agent names, then asks "bump the version to 2.4.1 and update the changelog". The agent edits `pyproject.toml` and `CHANGELOG.md` on the lighter model.
- Why: the guided choice on real routine work, followed by edits. Guided work earns Seen only.

## pos-4 Launch flag for a rename

- kind: boundary
- expect: seen
- Setup: the person, usually on Opus, starts a session in `gannet-web` with the harness's launch flag selecting a lighter model and asks "rename `fetchUser` to `loadUser` across the app". The agent edits nine files on the lighter model.
- Why: a launch flag is a deliberate person choice just like a model command. The flag in the launch record and the first edit complete it.

## neg-1 Usual Sonnet simply using Sonnet

- kind: source-negative
- expect: none
- Setup: the person always uses Sonnet. In `plover-jobs` they ask for docstrings and the agent writes them on Sonnet.
- Why: normal use of the usual model is not a choice of a lower tier. Not a miss either: the work did not run on a premium model.

## neg-2 Automatic Opus fallback after a limit

- kind: source-negative
- expect: none
- Setup: in `wren-sdk`, the person's Opus session hits a usage limit and the harness falls back to a lighter model on its own; the agent continues a rename on it.
- Why: automatic fallback is not the person's act and earns nothing. It is also not an opportunity: the person did not choose the premium model for this stretch.

## neg-3 Model switch without edits

- kind: boundary
- expect: none
- Setup: in `tern-cli`, the person types `/model haiku`, asks "what does this module do?", reads the answer and ends the session. No file is edited.
- Why: a switch with no work on the lighter tier does not complete Seen. No routine work ran on premium, so there is no opportunity.

## neg-4 Guided discussion without the choice

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person asks their agent which models are lighter, reads the answer and continues on their usual premium model with design discussion only.
- Why: answering the guide's questions does not count, and no routine work ran. Nothing is recorded.

## neg-5 Built-in lighter subagent

- kind: source-negative
- expect: none
- Setup: in `gannet-web`, the agent on its own launches a built-in exploration subagent that runs on a lighter model to search the codebase. The person did not define it or ask for it.
- Why: an ordinary lighter subagent is not the person's model choice and is not an owned mechanism.

## neg-6 Long routine work on premium

- kind: source-negative
- expect: opportunity
- Setup: the person usually works on Opus. In `plover-jobs` they write "reformat all the SQL files and fix the import order everywhere" and the agent spends a long session on Opus doing only formatting edits.
- Why: a long stretch of routine work on the premium usual model. The opportunity cites the person's starting prompt. Copy names no saving and no billed amount.

## neg-7 No routine work in the window

- kind: no-applicable-work
- expect: none
- Setup: in the window the person only designs a new storage layer with the agent in `heron-api`.
- Why: no routine work, so nothing is counted. Not a miss.

## neg-8 Usual model unknown

- kind: missing-evidence
- expect: none
- Setup: the person switches with `/model sonnet` and does a rename in `tern-cli`, but the history available has no earlier sessions, so the usual model and whether Sonnet is below it are unknown.
- Why: unknown usual model or tier is insufficient evidence: unassessed, neither recognized nor a miss. No averaging rule is invented.

## neg-9 Mechanism in place, routine work stays on premium

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person has an owned `docs-writer` subagent pinned lighter, but in the window writes "update all the docstrings" in the main Opus session three times without using it.
- Why: the mechanism is in place but routine work kept running on the premium tier: not holding. The opportunity cites the person's prompts.

## neg-10 Mechanism never used

- kind: mechanism-unused
- expect: none
- Setup: the person defined a lighter `changelog` command but did no routine work in the window.
- Why: configured, never applied: untested. Not Seen and not a miss.

## Scenarios the case format cannot label

### stage-boundary Seen versus Forming

- kind: stage-boundary
- Setup: in week 1 the person switches to a lighter model and the first docstring edit is made; the routine task finishes in week 2. In week 3 another deliberate switch and rename finish the same day.
- Expected: Seen in week 1 at the first edit. Forming credits weeks 2 and 3, the weeks the routine work finished on the lighter tier.
- Why no case: `expect` has no `forming` value.

### stage-boundary No history shared with IaC sizing

- kind: stage-boundary
- Setup: the person has many `infracost/right-size-it` findings about oversized cloud instances.
- Expected: none of them counts as evidence, applicability or progress for `glenngillen/right-size-it`, and no model-selection finding appears in the IaC pattern.
- Why no case: the case format evaluates one pattern's packet; cross-pack history separation needs the CLI's storage.
