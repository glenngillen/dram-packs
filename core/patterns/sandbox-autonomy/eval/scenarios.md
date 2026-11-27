# Sandbox autonomy: scenarios

Every acceptance scenario for `glenngillen/sandbox-autonomy`, in full. All people, repositories, hosts, containers and scripts are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no execution-environment facts, no launch provenance, no permission mode and no credential, privilege or OS-user facts, and the pattern names no block the pinned build runs.

Applicable work is every permission-bypassed session and every unattended run in the window.

## pos-1 Bypass inside a qualifying devcontainer

- kind: source-positive
- expect: seen
- Setup: the person opens `tern-mobile` in the devcontainer defined by the repository's configuration, which has its own checkout and mounts no host credentials, and runs the agent there with approvals bypassed to update generated API clients.
- Why: a bypassed run inside an observable contained environment, with attributable launch and environment facts and its permission mode.

## pos-2 Headless work in a container started by the person's script

- kind: source-positive
- expect: seen
- Setup: the person's own `scripts/agent-nightly.sh` starts a container from `kite-ledger`'s image and runs a headless agent task inside it to refresh test fixtures.
- Why: an unattended run, launched by the person's script, inside a container.

## pos-3 Every unattended and bypassed run contained

- kind: mechanism-held
- expect: continuous
- Setup: across the window the person ran five unattended jobs and two bypassed interactive sessions. All seven started through their devcontainer configuration or launch script; none ran on the host.
- Why: the mechanism was in place, applied and held for every applicable run. No block reaches `continuous` in the pinned build.

## pos-4 Guided devcontainer used for a real unattended task

- kind: guided-success
- expect: seen
- Setup: following the guide, the person has the agent propose a devcontainer for `marten-api` without credential mounts, reviews it, and the next day runs a real dependency-bump task unattended inside it under their normal scoped permissions.
- Why: a qualifying unattended run inside the contained environment. Broad permissions were not needed. Guided work earns Seen only.

## neg-1 The same bypass on a host with cloud credentials

- kind: source-negative
- expect: opportunity
- Setup: the person runs the `tern-mobile` generated-client update with approvals bypassed directly on their laptop, which holds cloud credentials. First prompt: "regenerate the API clients and fix whatever breaks".
- Why: broad permissions on the credentialed host. The opportunity cites the attributable launch and the person's first prompt.

## neg-2 Default-credential headless work on the host

- kind: source-negative
- expect: opportunity
- Setup: the person runs `claude -p "update every dependency and open a PR"` in `kite-ledger` directly on their laptop, with their default cloud and git credentials available.
- Why: unattended host work with default credentials. The opportunity cites the person's headless prompt.

## neg-3 Unused container definition

- kind: mechanism-unused
- expect: none
- Setup: `saffron-jobs` has a devcontainer configuration, but no run used it in the window and the person ran nothing unattended or bypassed.
- Why: an unused container definition is not a contained run: untested, not Seen and not a miss.

## neg-4 Guided configuration without a qualifying run

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person has the agent draft a devcontainer for `marten-api` and saves it, then runs nothing unattended in the window.
- Why: configuration without a qualifying run does not complete Seen.

## neg-5 Unknown execution environment

- kind: missing-evidence
- expect: none
- Setup: an unattended run in `lark-utils` is recorded, but no environment facts are available: nothing shows whether it ran on the host or in a container.
- Why: unknown environment is unassessed, not assumed safe and not a miss.

## neg-6 Run as a separate OS user

- kind: boundary
- expect: none
- Setup: the person runs bypassed work in `osprey-sync` as a separate OS user account created for agents, on their own laptop.
- Why: user decision: a separate OS user partially serves the intent and the guide describes it as valid, but it is not recognized until the CLI surfaces it as an attributable fact. Unassessed: neither recognized nor an opportunity. It still shares the network and system-readable files.

## neg-7 Host stated to be credential-free

- kind: boundary
- expect: none
- Setup: the person runs unattended work in `finch-docs` on a spare machine they say has no credentials on it.
- Why: user decision: a credential-free host is unassessed until the CLI can surface it as an attributable fact. Neither recognized nor an opportunity.

## neg-8 One unattended run on the host while the devcontainer exists

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person usually starts unattended work through their devcontainer, but one evening runs a headless "tidy the migrations folder" task in `heron-billing` directly on their credentialed laptop.
- Why: a run on the credentialed host while the mechanism was in place: not holding. The opportunity cites the person's headless prompt.

## neg-9 Worktree on the host with bypass

- kind: boundary
- expect: opportunity
- Setup: the person creates a separate git worktree of `puffin-web` on their laptop and runs the agent there with approvals bypassed. First prompt: "migrate the forms to the new validation library".
- Why: working-copy isolation is not system containment. The run is still on the credentialed host, so it is an opportunity here (Isolate the run may separately recognize the worktree).

## neg-10 Privileged container with host credentials mounted

- kind: boundary
- expect: none
- Setup: the person runs bypassed work in `kite-ledger` inside a container started privileged, with their host cloud-configuration directory mounted.
- Why: the passthrough may defeat the containment intent, and no capability contract is defined, so the run is unassessed: not recognized and not called safe from its container label, and not counted as an opportunity.

## neg-11 No bypassed or unattended runs

- kind: no-applicable-work
- expect: none
- Setup: every session in the window was interactive in normal approval mode.
- Why: no applicable work. Nothing is reported.
