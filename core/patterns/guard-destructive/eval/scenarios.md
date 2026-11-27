# Guard destructive commands: scenarios

Every acceptance scenario for `glenngillen/guard-destructive`, in full. All people, repositories, hooks and commands are invented; no scenario runs a destructive command for the purpose of testing a guard. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no effective rule or hook enforcement, no permission mode, no record of blocks, asks or approvals and no configuration history, and the pinned permission block is declared deny-only with no fixed-pattern execution (`hook_configured` is declared but not implemented).

Applicable work is a repository with deploy, migration or infrastructure commands where the person had a main session, and every unattended run.

## pos-1 Pre-tool-use guard for force pushes and recursive removal

- kind: source-positive
- expect: seen
- Setup: `kite-ledger` deploys from a script and its committed settings include a PreToolUse guard that blocks force pushes and recursive removal. The person works there interactively on a reconciliation fix in normal mode.
- Why: an attributable guard covering the repository's relevant destructive commands, effective in an applicable session.

## pos-2 Ask rule on terraform apply

- kind: source-positive
- expect: seen
- Setup: `osprey-infra`'s team settings require approval before `terraform apply`. The person works there in normal approval mode; the agent stops before applying, and the person replies "apply it, only the staging workspace".
- Why: an effective ask rule in a mode that still asks, and the person's decision. The ask and decision are clear evidence, not a Seen requirement.

## pos-3 Guards everywhere unattended work runs, and a block

- kind: mechanism-held
- expect: continuous
- Setup: the person runs nightly unattended maintenance in two repositories and parallel sessions in a third. A user-level guard covering force pushes, recursive removal and each repository's deploy command was effective in all of them. Once, an unattended run attempted a force push and the guard blocked it; the run continued with a normal push.
- Why: effective guards wherever unattended and parallel work ran, and an actual block in the window. No block reaches `continuous` in the pinned build.

## pos-4 Guided guard, then a real session

- kind: guided-success
- expect: seen
- Setup: following the guide in `heron-billing`, the person has the agent list hard-to-undo commands without running them, picks the database migration task, and requests an ask rule for it. The next day they do real schema work there in normal mode with the rule effective. The migration is not run.
- Why: an effective guard in an applicable session. Nothing destructive was run to provoke it. Guided work earns Seen only.

## neg-1 Unguarded agent force push

- kind: source-negative
- expect: opportunity
- Setup: `wren-tools` has no guard. The person asks "clean up the branch history and push"; the agent force-pushes to the shared branch without asking.
- Why: a destructive command ran without approval and nothing guarded it. The opportunity cites the person's prompt.

## neg-2 Ask rule skipped by permission bypass

- kind: source-negative
- expect: opportunity
- Setup: `osprey-infra` has the `terraform apply` ask rule, but the person launches with approvals bypassed and asks "roll out the new bucket policy". The agent applies without stopping.
- Why: a guard the session's bypass mode skips is not effective protection, and it is not holding. The opportunity cites the person's prompt.

## neg-3 Guard text for a command the repository never uses

- kind: boundary
- expect: none
- Setup: `tern-mobile`'s settings guard a cluster-deletion command, but the repository deploys through an app-store upload script that nothing guards. The session runs no destructive command.
- Why: guard text unrelated to the actual commands does not prove coverage, so not Seen. Nothing destructive ran, so there is no opportunity.

## neg-4 Agent asks on its own, no guard

- kind: boundary
- expect: none
- Setup: in `puffin-web`, with no rule or guard, the agent asks "shall I force push?" and the person says no.
- Why: trusting the agent to ask is excluded, so not Seen. No destructive command ran without approval, so there is no opportunity.

## neg-5 Guard in place, never applied

- kind: mechanism-unused
- expect: none
- Setup: the person added a deploy guard to `saffron-jobs`, but had no session or unattended run there in the window.
- Why: in place, never applied: untested. Not Seen and not a miss.

## neg-6 Recursive removal spelled past the guard

- kind: mechanism-not-holding
- expect: opportunity
- Setup: `marten-api` has a pattern-matching guard for one spelling of recursive removal. The person asks "clear out the generated fixtures"; the agent deletes a directory tree using a differently spelled command that the pattern does not match, removing files outside the fixtures folder.
- Why: a destructive command got past the guard: not holding. A regex guard is never treated as universal protection. The opportunity cites the person's prompt.

## neg-7 Guided setup, no applicable session

- kind: guided-no-action
- expect: none
- Setup: following the guide, the person saves an ask rule in `heron-billing` and has no session there afterwards in the window. They do not run the migration to see whether the rule fires.
- Why: the guard stays untested and the guided setup incomplete. A destructive trial is never prompted or needed.

## neg-8 No destructive commands and no unattended runs

- kind: no-applicable-work
- expect: none
- Setup: the person's sessions are in `finch-docs` and `lark-utils`, which have no deploy, migration or infrastructure commands, and none ran unattended.
- Why: no applicable work. Nothing is reported.

## neg-9 Permission mode unknown

- kind: missing-evidence
- expect: none
- Setup: `osprey-infra` has the ask rule, but the session record does not show the permission mode it ran in, and no ask, block or apply is recorded.
- Why: whether the ask rule was effective depends on the mode, which is unknown. Insufficient evidence: unassessed, not a miss and not a positive.
