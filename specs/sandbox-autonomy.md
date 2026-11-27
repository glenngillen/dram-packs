# Sandbox Autonomy

## Overview

Source ID `sandbox-autonomy`; Safety, rung 4. Contain unattended or broadly permissioned runs. Intended detection is a code check.

## Requirements

- Applies to permission-bypassed sessions and unattended work.
- The intent is system isolation: a mistake or prompt injection in a broadly permissioned or unattended run cannot reach the person's credentials, production access or wider machine.
- Seen requires a qualifying run inside an observable contained environment: a container, devcontainer, VM or remote sandbox. Cite attributable launch/environment facts and permission mode as completion.
- Exclude broad permissions on the person's credentialed host and unattended host work with default credentials.
- Continuous requires every bypassed/unattended run in the window to be sandboxed through the applicable mechanism and holding.
- Coach on permission bypass outside a sandbox. The guide has the person configure and use a supported devcontainer for their next real unattended task; broad permissions are not a required step of the guide.
- Keep copy bounded: a container label alone cannot guarantee no access to credentials or production systems.

## Acceptance Criteria

- [ ] Preserve bypass inside a qualifying devcontainer as positive; reject the same bypass on a host with cloud credentials.
- [ ] Recognize headless work in a container started by the person's script; reject default-credential host headless work.
- [ ] An unused container definition is not an actual isolated run.
- [ ] Guided discussion or configuration without a qualifying run does not complete Seen.
- [ ] Unknown execution environment is unassessed, not assumed safe.
- [ ] A run as a separate OS user, or on a host stated to be credential-free, is unassessed: neither recognized nor counted as an opportunity.

## Edge Cases

- Decided: a credential-free host or a separate OS user partially serves the intent and is described as valid in the guide and copy, but is not recognized until the CLI surfaces it as an attributable fact. Until then such runs are unassessed, never a miss. A separate OS user still shares the network and system-readable files.
- Privileged containers and credential/network passthrough may defeat the stated containment intent. The source does not define a sufficient sandbox capability contract; do not invent one or assert safety from naming alone.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [scope permissions](scope-permissions.md), [evaluation readiness](evaluation-readiness.md).
- Historical environment/permission facts, ownership and effective containment semantics; unsupported detection remains disabled.
