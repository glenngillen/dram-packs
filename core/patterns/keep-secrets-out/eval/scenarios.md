# Keep secrets out: scenarios

Every acceptance scenario for `glenngillen/keep-secrets-out`, in full. All people, repositories, paths and rules are invented. **No scenario contains a real credential**: where a secret pattern is needed it is the invented marker `FAKE-SECRET-MARKER-0000`, and no scenario quotes the contents of a secret file. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no effective settings, settings precedence, permission mode, secret-location facts, file-access mapping or local redaction findings, and `permission_rule` is declared deny-only with no fixed-pattern execution.

Applicable work is a repository containing secret files where the person had a main session in the window, or a session in which the agent touched a secret file.

## pos-1 Effective .env read-deny in a qualifying session

- kind: source-positive
- expect: seen
- Setup: `heron-billing` keeps its secrets in `.env` and `.env.local`. Its committed project settings deny the agent reading `.env*`, and nothing in the session's loaded settings removes the rule. The person works there on an invoice export fix.
- Why: an attributable rule covering the actual secret locations, effective in an applicable session.

## pos-2 User-level .env and credentials coverage

- kind: source-positive
- expect: seen
- Setup: the person's user-level settings deny reading `**/.env*` and `**/credentials*`. In `puffin-web`, whose only secret files are `.env` and `deploy/credentials.json`, they work on a form validation change.
- Why: a user-level rule counts where it covers the repository's actual secret locations.

## pos-3 Every repository covered, a read denied, no secret in prompts

- kind: mechanism-held
- expect: continuous
- Setup: the person works in three repositories with secret files in the window. Each has an effective deny rule for its real secret locations. In one session the agent tried to read `config/secrets.yml` and the rule denied it; the agent asked the person where the setting is defined instead. The local scanner detected no secret pattern in the person's prompts.
- Why: full coverage, applied and held; a denied read is held. No block reaches `continuous` in the pinned build.

## pos-4 Guided rule then a real session

- kind: guided-success
- expect: seen
- Setup: following the guide in `marten-api`, the person has the agent list likely secret paths by name only (`.env`, `config/secrets.yml`), then requests deny rules for both and reviews them. The next day they fix a real bug in `marten-api` with the rules in effect.
- Why: effective coverage of the actual locations, applied in a real session. Guided work earns Seen only.

## neg-1 Agent reads .env without protection

- kind: source-negative
- expect: opportunity
- Setup: `heron-billing` has no deny rule. The person asks "why is the webhook failing locally?"; the agent opens `.env` to check configuration.
- Why: a secret file read with no effective rule. The opportunity cites the person's prompt that started the work and reports only that `.env` was read; it shows no value.

## neg-2 .env-only protection where secrets live in config/secrets.yml

- kind: source-negative
- expect: opportunity
- Setup: `tern-mobile` denies `.env*`, but its secrets are in `config/secrets.yml`. The person asks "the API client can't authenticate, find out why"; the agent reads `config/secrets.yml`.
- Why: a partial rule that misses the actual location is not coverage, so not Seen. The read is an opportunity cited by the person's prompt, reporting the location only.

## neg-3 Rule written for another repository

- kind: boundary
- expect: none
- Setup: the person's only deny rule is in `heron-billing`'s project settings. They work in `wren-tools`, which keeps secrets in `secrets/dev.json`; the agent does not touch that file.
- Why: a rule irrelevant to the current repository leaves it untested, not Seen. Nothing was exposed, so there is no opportunity either.

## neg-4 Instruction to be careful, no rule

- kind: boundary
- expect: none
- Setup: `quail-docs` has an instruction file line "never read .env files" and no deny rule. The agent does not read `.env` in the session.
- Why: reliance on agent caution is excluded, so not Seen. With no read and no detected secret in prompts, there is no opportunity.

## neg-5 Rule in place, never applied

- kind: mechanism-unused
- expect: none
- Setup: the person added a `config/secrets.yml` deny rule to `saffron-jobs`, but had no session there in the window.
- Why: configured, never applied: untested. Not Seen and not a miss.

## neg-6 Read-deny skipped by a shell read

- kind: mechanism-not-holding
- expect: opportunity
- Setup: `osprey-sync` has a deny rule on the agent's file-read tool for `.env*`, but not for shell commands. The person asks "check what port the dev server uses"; the agent runs a shell command that prints `.env`.
- Why: a declaration bypassed by actual tool behaviour is not effective coverage, so the mechanism is not holding. The opportunity cites the person's prompt and reports only that `.env` was read via a shell command.

## neg-7 Credential-like string detected in a prompt

- kind: mechanism-not-holding
- expect: opportunity
- Setup: `heron-billing` is fully covered. The person pastes a token into a prompt; the local scanner flags the invented marker `FAKE-SECRET-MARKER-0000` in that prompt.
- Why: a locally detected secret pattern in a person prompt means the mechanism is not holding for Continuous. The opportunity cites the prompt by ID with the value redacted locally; copy says only that a credential-like string was detected and where.

## neg-8 Project rule not loaded for the session

- kind: boundary
- expect: none
- Setup: `kite-ledger` has a committed `.env*` deny rule, but the session was launched in a way that loaded only the person's user-level settings, which have no such rule. The agent does not touch `.env`.
- Why: after settings precedence the rule was not effective in that session, so it is not Seen. Nothing was exposed, so there is no opportunity.

## neg-9 Guided discussion, no rule saved

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person asks the agent in `marten-api` which files might hold secrets, reads the list, and saves no rule. No secret file is touched.
- Why: guided discussion without effective coverage and application does not complete Seen, and nothing was exposed.

## neg-10 No secret files anywhere

- kind: no-applicable-work
- expect: none
- Setup: the person's sessions in the window are in `lark-utils` and `finch-docs`, neither of which contains a secret file, and no session touches one.
- Why: no applicable work. Nothing is reported.

## neg-11 Settings history unavailable

- kind: missing-evidence
- expect: none
- Setup: in `heron-billing` the agent's session record is present, but the settings in effect when it ran are unknown: only today's configuration is available, and the local scanner did not run on that week.
- Why: current configuration cannot prove historical coverage, and an unscanned week proves nothing about prompts. Insufficient evidence: unassessed, not a miss.
