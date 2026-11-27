# Scope permissions: scenarios

Every acceptance scenario for `glenngillen/scope-permissions`, in full. All people, repositories, hosts and settings are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no effective settings after precedence, no allow-list semantics, no permission mode, no run-type attribution and no sandbox classification, and the pinned permission block is declared deny-only with no fixed-pattern execution.

Applicable work is every main session in the window, interactive or unattended, except permission-bypassed sessions inside a qualifying sandbox, which are neutral.

## pos-1 Narrow test and git-status allow list in normal mode

- kind: source-positive
- expect: seen
- Setup: `heron-billing`'s committed settings allow `npm test` and `git status` and nothing broader; no other loaded setting adds anything. The person runs an interactive session in normal approval mode and fixes a rounding bug.
- Why: an effective scoped allow list and no bypass. Run scope: interactive.

## pos-2 Unattended run with a scoped allow list

- kind: source-positive
- expect: seen
- Setup: the person starts a headless run in `marten-api` to update a changelog. The effective settings allow `make test`, `git diff` and `git status` only, and the run uses the normal approval mode.
- Why: scoped permissions for an unattended run. The recognition records run scope **unattended**, which is what Hands off's prerequisite needs.

## pos-3 Every session scoped, unattended included

- kind: mechanism-held
- expect: continuous
- Setup: across the window the person's sessions in four repositories, two of them unattended, all run under an effective team allow list of specific test, build and read-only git commands. No session bypasses permissions and no broader entry takes effect. One devcontainer run with bypass is excluded as neutral.
- Why: applied and holding across all applicable sessions; the sandboxed bypass is excluded from the denominator, not counted against coverage. No block reaches `continuous` in the pinned build.

## pos-4 Guided allow list, then a real scoped session

- kind: guided-success
- expect: seen
- Setup: following the guide in `puffin-web`, the person has the agent list their most-approved commands and requests an allow list for `pnpm test` and `git status`. Next morning they fix a real form bug in normal mode under that list.
- Why: an observed scoped session after the guided edit. Guided work earns Seen only.

## neg-1 Permission bypass in the main repository

- kind: source-negative
- expect: opportunity
- Setup: on the person's laptop, which holds cloud credentials, they launch `--dangerously-skip-permissions` in their main checkout of `kite-ledger`, which has a deploy script. First prompt: "fix the failing reconciliation job".
- Why: bypass outside a sandbox in a repository with deploy scripts. Not Seen; the opportunity cites the attributable launch and the person's first prompt.

## neg-2 Unrestricted Bash(*)

- kind: source-negative
- expect: none
- Setup: `wren-tools`' settings allow `Bash(*)`. The person works interactively in normal mode.
- Why: an unrestricted allow list is not scoped, so not Seen. The coaching trigger is bypass, so no opportunity is reported from the allow list alone.

## neg-3 Restrictive file overridden by a broader setting

- kind: boundary
- expect: none
- Setup: `osprey-sync`'s project settings allow only `go test ./...`, but the person's local settings for the same repository allow every shell command, and that broader entry is what the session effectively ran under.
- Why: after settings precedence the effective approval was unrestricted. A restrictive file that is overridden is insufficient: not Seen.

## neg-4 Bypass inside a qualifying devcontainer

- kind: boundary
- expect: none
- Setup: the person runs `tern-mobile` work with permissions bypassed inside a devcontainer started from the repository's configuration, with no host credentials mounted.
- Why: user decision: sandboxed bypass is **neutral** here, excluded from applicable work, neither credit nor a miss, and not counted against Continuous coverage. Sandbox autonomy recognizes it, not this pattern.

## neg-5 The same bypass on a credentialed host

- kind: boundary
- expect: opportunity
- Setup: the same `tern-mobile` work, with permissions bypassed, runs directly on the person's laptop, which has cloud credentials and the repository's deploy script. First prompt: "bump the SDK and redeploy staging".
- Why: bypass outside a sandbox is an opportunity, cited by the person's first prompt.

## neg-6 Bypassed session in an unknown environment

- kind: boundary
- expect: none
- Setup: a bypassed session in `lark-utils` has no environment facts: nothing shows whether it ran on the host or in a container.
- Why: it cannot be classified as sandboxed or not, so it is unassessed: neither applicable work nor a miss.

## neg-7 Guided edit, no scoped session observed

- kind: guided-no-action
- expect: none
- Setup: following the guide, the person saves an allow list in `puffin-web` and has no session there afterwards in the window.
- Why: guided permission edits without an observed scoped session do not earn Seen.

## neg-8 Scoped list configured, never used

- kind: mechanism-unused
- expect: none
- Setup: `saffron-jobs` has a committed scoped allow list, but the person had no session there in the window.
- Why: in place, never applied: untested. Not Seen and not a miss.

## neg-9 One unattended run bypassed on the host

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person's sessions mostly run under a scoped team allow list, but one nightly unattended run in `kite-ledger`, launched by the person's own script, uses approval bypass on their credentialed laptop. The script's first prompt was written by the person: "tidy the migration folder".
- Why: a host bypass while the scoped configuration was in place: not holding. The opportunity cites the attributable launch and the person-authored prompt.

## neg-10 No sessions in the window

- kind: no-applicable-work
- expect: none
- Setup: the person had no agent sessions in the window.
- Why: no applicable work. Nothing is reported.

## neg-11 Permission mode and settings history unknown

- kind: missing-evidence
- expect: none
- Setup: sessions in `heron-billing` are recorded, but neither their permission mode nor the settings in force when they ran is available.
- Why: insufficient evidence: unassessed, not a miss and not a positive.
