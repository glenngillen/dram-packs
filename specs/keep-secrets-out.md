# Keep Secrets Out

## Overview

Source ID `keep-secrets-out`; Safety, rung 1. Keep secret files outside the agent's reach and credentials out of prompts. Intended detection is a local code check.

## Requirements

- Applies to repositories containing secret files or sessions touching them.
- Seen requires an effective person/team deny rule covering the repository's secret files and applying in a session.
- Exclude reliance on agent caution and partial rules that miss the actual secret locations.
- Cite the rule and applicable session as completion, never a secret value.
- Continuous requires effective coverage everywhere the person works and no locally detected secret pattern in their prompts during the window, with applied/held evidence.
- Coach on secret exposure or agent secret-file reads, saying only that it happened and its local location. Never put secret values in excerpts, copy or telemetry.
- Guide: identify actual secret-file locations without reading/exposing their contents, then let the person request appropriate deny rules.

## Acceptance Criteria

- [ ] Recognize an effective `.env*` read-deny in a qualifying repository session; reject an agent reading `.env` without protection.
- [ ] Preserve user-level `.env`/credentials coverage as positive; reject `.env`-only protection when secrets are in `config/secrets.yml`.
- [ ] A rule irrelevant to the current repository remains untested for it.
- [ ] Guided rule discussion without effective coverage/application does not complete Seen.
- [ ] All exposure fixtures use invented markers and never real credentials.

## Edge Cases

- A deny declaration may be bypassed by actual mode/tool behavior; evaluate effective coverage, not the presence of text.
- Absence of detected secret patterns cannot guarantee no secrets exist; copy must stay within what the local scanner observes.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Effective deny semantics, file-scope facts, session attribution and local redaction findings. Current `permission_rule` declaration has no fixed-pattern execution support.

