# Reuse your harness: scenarios

Every acceptance scenario for `glenngillen/reuse-your-harness`, in full. All people, repositories, commands and plugins are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no configuration identity, provenance or per-repository usage of a command, hook or rule, and the pattern names no block the pinned build runs.

Applicable work is at least two repositories worked in during the window.

## pos-1 User-level PR-description command used across three repositories

- kind: source-positive
- expect: seen
- Setup: the person keeps `pr-description` in their user configuration. In this window they invoke it in `lanternfish-api`, `quillmark` and `orchard-jobs`; none of those repositories defines its own copy.
- Why: one owned item from user configuration, used in three repositories.

## pos-2 Own maintained plugin with hooks

- kind: source-positive
- expect: seen
- Setup: the person maintains their own plugin, `cairn-hooks`, whose format-on-save hook fires in sessions in `basalt-sdk` and `fern-docs`.
- Why: the person's own plugin, actually applied in two repositories.

## pos-3 Guided relocation then use in two repositories

- kind: guided-success
- expect: seen
- Setup: following the guide, the person moves their `changelog-entry` command from two repositories into user configuration, removes the copies, and over the next days invokes it in both repositories on real work.
- Why: shared, owned and used in two repositories. Guided work earns Seen only.

## pos-4 Maintained harness covers every repository

- kind: mechanism-held
- expect: continuous
- Setup: the person works in four repositories. Their user configuration (commands, a hook and rules) was updated by them ten days before the window ends; its items are used in all four, and no repository has a diverged copy.
- Why: applies to every repository worked in, updated in the last four weeks, applied and holding.

## neg-1 Three diverging copies

- kind: source-negative
- expect: opportunity
- Setup: `pr-description` is defined separately in three repositories, each with different sections. The person invokes each copy in this window.
- Why: diverged copies are excluded and are what this pattern coaches on. Cites the person's invocations.

## neg-2 Marketplace plugin they did not write

- kind: source-negative
- expect: none
- Setup: a marketplace plugin's review command is used across all of the person's repositories. They own no shared items.
- Why: a third-party plugin does not establish ownership, and with no owned duplicate there is no opportunity either.

## neg-3 Single repository

- kind: no-applicable-work
- expect: none
- Setup: the person works only in `marlin-cli`, which has several of their commands and hooks.
- Why: fewer than two repositories: not applicable, not a miss.

## neg-4 Shared file unused in the second repository

- kind: mechanism-unused
- expect: none
- Setup: the person's user configuration has `deploy-notes`; they work in two repositories but invoke it only in one. No duplicates exist.
- Why: one repository's use cannot establish sharing; the item is untested in the second.

## neg-5 Guided relocation, used in one repository only

- kind: guided-no-action
- expect: none
- Setup: following the guide, the person moves `changelog-entry` into user configuration and uses it in one repository; the second repository has no work in the rest of the window. The old copy was removed.
- Why: guided relocation without use across two repositories does not meet Seen, and with no duplicate left there is no missed moment.

## neg-6 Matching filenames, unknown identity

- kind: missing-evidence
- expect: none
- Setup: two repositories each contain `.claude/commands/triage.md`, but their content and provenance are not available to the analysis.
- Why: sharing is never inferred from matching filenames. Insufficient evidence, not a miss.

## neg-7 Repository bypasses the shared harness with a diverged copy

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person's user-level `pr-description` is used in three repositories, but in `heron-service` they keep and invoke a separate, diverged repository copy instead.
- Why: a repository worked in ran a diverged copy instead of the shared item while it was in place: not holding. Cites the person's invocation of the copy.

## pos-5 Shared everywhere but not updated in four weeks

- kind: boundary
- expect: seen
- Setup: as pos-4, but the user configuration was last changed seven weeks before the window ends.
- Why: shared owned items used across four repositories earn Seen; Continuous needs an update in the last four weeks, so this is stale for Continuous, which is distinct from not holding and is not a miss.

## Scenarios the case format cannot label

### stage-boundary Established needs four applicable repositories

- kind: stage-boundary
- Setup A: three repositories worked in, all using the shared harness. Setup B: five repositories, three using it.
- Expected: A is not assessable under [`most`](../../../reference/parameters.md#most), not a miss. B meets Established (60%, inclusive).
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.
