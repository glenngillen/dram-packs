# Scope Permissions

## Overview

Source ID `scope-permissions`; Safety, rung 2. Grant the tools/commands the work needs without broad approval. Intended detection is a code check.

## Requirements

- Applies to all sessions, especially unattended work.
- Seen requires an effective scoped person/team allowlist and a session running without bypassing permissions.
- Exclude unrestricted allowlists and unsafe permission bypass. Do not award this pattern merely because the run is sandboxed; that is separately recognized by Sandbox autonomy.
- Cite effective configuration and session permission mode as completion.
- Acceptance: a sandboxed bypassed session neither earns Seen nor counts against Continuous coverage; the same bypass on a credentialed host is an opportunity.
- Continuous requires all sessions, including unattended ones, to use scoped permissions through an applied/holding configuration in the window.
- Coach on bypassed permissions in repositories with production access or deploy scripts. The guide identifies actually needed commonly approved commands and lets the person request narrow permissions.
- Preserve run-scope evidence so Hands off suggestions can require Seen specifically for unattended work.

## Acceptance Criteria

- [ ] Recognize a narrow test/git-status allowlist in normal mode; reject `--dangerously-skip-permissions` in the main repository.
- [ ] Recognize an unattended run with a scoped allowlist; reject `Bash(*)`.
- [ ] A restrictive file that is overridden by effective broader settings is insufficient.
- [ ] Guided permission edits without an observed scoped session do not earn Seen.

## Edge Cases

- Decided: permission bypass (approval-skipping modes such as Claude Code's `bypassPermissions` / `--dangerously-skip-permissions` or Codex's approval-skipping flags) inside a qualifying sandbox is neutral here: neither credit nor a miss, and excluded from this pattern's applicable work. It is recognized only by Sandbox autonomy. Bypass outside a sandbox remains an opportunity.
- No exact universal allowlist breadth metric is specified. Avoid inventing one or inferring least privilege from a nonempty list.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [sandbox autonomy](sandbox-autonomy.md), [evaluation readiness](evaluation-readiness.md).
- Effective settings precedence, allowlist semantics, session mode and run-type attribution. Current permission block accepts deny only, not the required allow/mode contract.

