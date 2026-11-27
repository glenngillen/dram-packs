# Sandbox autonomy

Source ID `sandbox-autonomy`; pattern `glenngillen/sandbox-autonomy`; Safety, rung 4. Contain unattended or broadly permissioned runs. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- **Permission-bypassed sessions** (approval-skipping modes) and **unattended runs** ([`unattended_gap`](../../reference/parameters.md#unattended_gap)) in the window.
- The intent is **system isolation**: a mistake or prompt injection in a broadly permissioned or unattended run cannot reach the person's credentials, production access or wider machine.
- This is **not working-copy isolation**. A separate worktree or clone on the person's own machine keeps runs from interfering with each other ([Isolate the run](../isolate-the-run/definition.md)); it does not contain them. The two are assessed separately.
- A window with no bypassed or unattended run is **no applicable work**.

## Recognition

**Seen** requires all of:

1. **A qualifying run**: permission-bypassed or unattended, attributable to the person (their launch, their script or their configuration; not software running an agent on its own behalf).
2. **An observable contained environment**: a container, devcontainer, VM or remote sandbox, shown by attributable **launch and environment facts**.
3. **Its permission mode** recorded.

Completing evidence: the launch/environment facts and the permission mode. Broad permissions are not a requirement: an unattended run in a container under scoped permissions qualifies.

**Bounded copy**: a container label alone cannot promise that nothing could reach credentials or production. The source does not define a sufficient sandbox capability contract, so none is invented here.

## Exclusions

- **Broad permissions on the person's credentialed host**.
- **Unattended host work with default credentials**.
- **An unused container definition**: a devcontainer file with no run inside it.
- **Guided discussion or configuration** without a qualifying run.

### Unassessed, never a miss

- **Unknown execution environment**: no recognition, and not assumed safe; not an opportunity either.
- **A separate OS user, or a host stated to be credential-free**: user decision. These partially serve the intent and are described as valid in the guide and copy, but they are **not recognized** until the CLI surfaces them as attributable facts. Until then such runs are unassessed: neither recognized nor counted as an opportunity. A separate OS user still shares the network and system-readable files.
- **Privileged containers or credential/network passthrough**: these may defeat the containment intent. With no defined capability contract, such a run is unassessed rather than recognized or called safe; see [open questions](#open-questions).

## Evidence

- **Cite** the attributable launch (command, script or configuration) and the environment facts, plus the permission mode. A person-authored citation can be supplied by launch or configuration attribution where the [evidence contract](../../reference/evidence.md#attribution-and-citations) allows, or by the person's first prompt in the run.
- **Historical**: environment and permission facts must be those of the run, not today's configuration.
- **Evidence the pinned CLI does not supply**: execution-environment facts per session (host, container, devcontainer, VM, remote sandbox); launch provenance and ownership; permission mode; mounted credentials, privilege and network passthrough; OS user and host credential facts.

## Progression

Uses the default [stages](../../reference/progression.md#stages) with a coverage qualification for Continuous ([pattern-specific overrides](../../reference/progression.md#pattern-specific-overrides)):

| Stage | For this pattern |
| --- | --- |
| Seen | One qualifying run inside an observable contained environment. |
| Forming | Such runs in at least two distinct weeks of the last four. |
| Established | At least 60% of applicable runs contained, with at least four applicable runs ([`most`](../../reference/parameters.md#most)). Unassessed runs are excluded from the count. |
| Continuous | **Every** bypassed or unattended run in the window sandboxed through the applicable mechanism, **and** the [mechanism](#mechanism) holding. |

A guided setup establishes Seen only once a qualifying run happens inside the environment ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the person's containment setup: a devcontainer configuration, a launch script or a remote sandbox they use to start these runs.

| Fact | For this pattern |
| --- | --- |
| In place | An attributable container, devcontainer, VM or sandbox setup existed during the window. |
| Applied | Bypassed or unattended runs were actually started inside it. |
| Held | Every bypassed or unattended run in the window ran inside it, and none ran on the credentialed host. |
| Not holding | While in place, a bypassed or unattended run ran on the credentialed host instead. |
| Untested | A definition that no run used in the window. |

## Opportunities and coaching

- **Opportunity**: permission bypass, or unattended work with default credentials, **outside a sandbox** on the person's credentialed host. It cites the person-authored moment (the attributable launch or the run's first prompt) ([opportunities](../../reference/evidence.md#opportunities)). Unknown environments, separate OS users and credential-free hosts are not opportunities.
- **Coaching**: the [guide](guide.md) has the person configure and use a supported devcontainer for their next real unattended task. Broad permissions are not a step of the guide, and permission bypass is never suggested as a shortcut.
- Sandbox autonomy is a broader-autonomy step: its [safety prerequisites](../../reference/progression.md#safety-prerequisites) are Keep secrets out, Scope permissions and Guard destructive commands. That prerequisite is prose, not a `requires` binding.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`, and its collected-history fixture shape has no execution-environment facts, launch provenance or permission mode. Nothing in a tool call shows whether a run was contained; a path or label that looks like a container is not proof of one.

## Missing capabilities

- **Execution-environment facts** per run: host, container, devcontainer, VM or remote sandbox.
- **Launch provenance and ownership**: who or what started the run, and with which configuration.
- **Permission mode** per run.
- **Containment facts**: mounted credentials, privileged mode, network passthrough; OS user and host credential facts (needed before separate users or credential-free hosts can be recognized).
- **Run-type attribution**: unattended versus interactive.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- Bypass inside a qualifying devcontainer is recognized; the same bypass on a host with cloud credentials is an opportunity.
- Headless work in a container started by the person's script is recognized; default-credential host headless work is an opportunity.
- An unused container definition is not an isolated run.
- Guided discussion or configuration without a qualifying run does not complete Seen.
- An unknown execution environment is unassessed, not assumed safe.
- A run as a separate OS user, or on a host stated to be credential-free, is unassessed: neither recognized nor an opportunity.
- A worktree on the host is not containment.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- What makes an environment count as containment when it is privileged or passes through credentials or the network?
  - evidence: The source names containers, devcontainers, VMs and remote sandboxes but defines no capability contract; privileged containers and credential or network passthrough may defeat the stated intent.
  - options: Define a containment contract (no host credential mounts, not privileged, stated network policy) before enabling; keep such runs unassessed.
  - location: core/patterns/sandbox-autonomy/definition.md / Exclusions
