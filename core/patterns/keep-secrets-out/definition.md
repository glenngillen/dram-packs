# Keep secrets out

Source ID `keep-secrets-out`; pattern `glenngillen/keep-secrets-out`; Safety, rung 1. Keep secret files outside the agent's reach and credentials out of prompts. Intended detection: a local code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** Secrets stay out of prompts and the agent's reach: environment and secret files are denied, and credentials aren't pasted.

**Why it matters.** An agent that is told to be careful can still read a secret file while debugging, and what it reads can end up in its context. A deny rule that covers the real locations keeps those files out of reach. It is the first rung of Safety, which gives the agent autonomy in proportion to what it could break, and a prerequisite for broader autonomy ([autonomy and safety advance together](../../reference/principles.md#autonomy-and-safety-advance-together)).

**What a recognition shows.** That a deny rule the person or their team configured, covering the repository's actual secret locations, was in effect in a session there.

**Why the rules are drawn this way.**

- **Repositories with secret files, or sessions that touched one, apply.** Elsewhere there is nothing to protect, and nothing is reported ([applicable work](../../reference/principles.md#applicable-work)).
- **A configured rule, not the agent's caution.** An instruction to be careful, or the agent choosing not to open a file, can fail the next time; only configuration enforces it ([human intent only](../../reference/principles.md#human-intent-only)).
- **It must cover the actual secret locations.** A `.env` rule doesn't protect secrets kept in `config/secrets.yml`; crediting it would show protection that isn't there ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **Effective, not merely written.** Settings precedence, the session's mode and other tool routes (a shell read around a read-deny) decide whether the rule actually applied. These are facts, so code checks them ([code checks facts; a model judges the rest](../../reference/principles.md#code-checks-facts-a-model-judges-the-rest)). A rule for paths that don't exist in this repository is untested here, not Seen.
- **Values are never read or shown.** Secret files are identified by location and kind, and findings say only that something happened and where ([private by default](../../reference/principles.md#private-by-default)). The local scanner finding nothing does not prove there are no secrets, so copy stays within what it observed.
- **Continuous needs coverage everywhere plus no secret pattern in prompts.** The rule protects files; keeping credentials out of prompts is the other half of the intent, so both must hold ([prevention: when success removes the signal](../../reference/principles.md#prevention-when-success-removes-the-signal)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. Named as one of the first activation candidates; it still needs the capabilities below.

## Applicable work

- A **repository that contains secret files** (for example `.env`, `.env.local`, `config/secrets.yml`, a credentials file) where the person had a main session in the window, or any main session in which the agent touched a secret file.
- Secret files are identified **locally** by their location and kind. Their contents are never read, quoted or sent anywhere by this pattern.
- A window with no such repository and no session touching a secret file is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** requires all of:

1. **An attributable deny rule**: configured by the person or their team (user, project or shared settings), denying the agent read access.
2. **Actual coverage**: the rule covers the repository's **actual secret-file locations**. A `.env*` rule covers a repository whose secrets are in `.env` files; it does not cover one whose secrets are in `config/secrets.yml`.
3. **Effective in the session**: after **settings precedence** (which sources were loaded, and whether a later or higher-priority source removed or overrode the rule) and the session's **mode and tool behaviour**, the rule actually applied. A declaration that another tool route, a shell command or the session's mode would skip is not effective coverage.
4. **Applied**: a main session ran in that repository while the rule was effective.

Completing evidence: the effective rule and the applicable session. A user-level rule covering `.env*` and credential files counts for every repository where those are the actual secret locations.

## Exclusions

- **Reliance on agent caution**: an instruction such as "never read `.env`", or the agent choosing not to open a file, is not protection.
- **Partial rules** that miss the actual secret locations (`.env`-only protection where the secrets live in `config/secrets.yml`).
- **A rule irrelevant to the current repository**: a rule written for another repository's paths is **untested** for this one, not Seen.
- **A declaration bypassed** by actual mode or tool behaviour (for example a read-deny that a shell `cat` would get around): evaluate effective coverage, not the presence of rule text.
- **Guided rule discussion** without an effective rule and an applicable session.

## Evidence

- **Cite** the effective rule (its source file and scope) and the applicable session. Never a secret value: excerpts, copy and telemetry say only that something happened and its **local location**.
- A person-authored citation can be supplied by configuration attribution where the [evidence contract](../../reference/evidence.md#attribution-and-citations) allows, plus the person's prompt in the applicable session.
- **Historical**: the rule must have existed and been effective when the session ran; current settings cannot prove past coverage.
- **Local scanner bounds**: a secret pattern detected in a prompt is a local redaction finding. The absence of detected patterns does **not** prove no secrets exist; copy stays within what the local scanner observed.
- **Evidence the pinned CLI does not supply**: effective settings per session (sources, precedence, mode); deny semantics across tools; the repository's secret-file locations; agent file-access records mapped to those locations; local redaction findings in person prompts; configuration history and attribution.

## Progression

Uses the default [stages](../../reference/progression.md#stages) with a coverage qualification for Continuous ([pattern-specific overrides](../../reference/progression.md#pattern-specific-overrides)):

| Stage | For this pattern |
| --- | --- |
| Seen | One applicable session with an effective rule covering the repository's actual secret locations. |
| Forming | Such sessions in at least two distinct weeks of the last four. |
| Established | At least 60% of applicable repositories covered, with at least four applicable repositories ([`most`](../../reference/parameters.md#most)). |
| Continuous | Effective coverage **everywhere** the person works with secret files, no locally detected secret pattern in their prompts in the window, **and** the [mechanism](#mechanism) holding. |

A guided setup establishes Seen only once an applicable session runs under the effective rule ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the deny rule itself.

| Fact | For this pattern |
| --- | --- |
| In place | An attributable rule covering the actual secret locations existed during the window. |
| Applied | It was effective in a main session in the covered repository, or it denied an attempted read. |
| Held | Every applicable repository was covered, no agent read of a covered secret file got through, and the local scanner detected no secret pattern in the person's prompts. A denied read is held. |
| Not holding | While in place, the agent read a covered secret file by a route the rule did not stop, or a secret pattern was detected locally in a person prompt. |
| Untested | Configured for a repository with no session in the window, or written for paths that do not exist there. |

## Opportunities and coaching

- **Opportunity**: the agent read a secret file that no effective rule covered, or the local scanner detected a secret pattern in a person prompt. It cites the person-authored moment (the prompt that started the work in which the read happened, or the prompt flagged by the scanner, cited by ID with the value redacted locally) ([opportunities](../../reference/evidence.md#opportunities)). Copy says only that it happened and where; it never shows the value.
- **Coaching**: the [guide](guide.md) helps the person identify actual secret locations without opening them, then request deny rules for those locations.
- `automate` advice (user-level rules for the person's usual secret locations) is offered only after the [automation gate](../../reference/progression.md#automation-gate).
- Keep secrets out is one of the [safety prerequisites](../../reference/progression.md#safety-prerequisites) for broader autonomy.

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. `permission_rule` is declared deny-only and has no fixed-pattern execution, and the collected-history fixture shape has no effective settings, file-scope facts or redaction findings. Matching a deny rule's text would accept rules that miss the real secret locations or that the session's mode skips; matching a read of `.env` would miss other locations. Either would substitute a weaker definition.

## Missing capabilities

- **Effective settings per session**: loaded sources, precedence, permission mode and how each tool route honours a deny rule.
- **Secret-location facts**: where the repository's secret files actually are, identified locally without reading values.
- **File-access records** mapped to those locations, including shell reads.
- **Local redaction findings** in person prompts, exposed as fact and location only.
- **Configuration history and attribution**: the rule at session time and whose it is.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- An effective `.env*` read-deny in a qualifying repository session is recognized; an agent reading `.env` without protection is an opportunity.
- User-level `.env`/credentials coverage is recognized where those are the actual locations; `.env`-only protection is rejected where secrets live in `config/secrets.yml`.
- A rule irrelevant to the current repository stays untested for it.
- A declaration skipped by mode or tool behaviour is not effective coverage.
- Guided rule discussion without effective coverage and application does not complete Seen.
- No secret value appears in any output, excerpt or telemetry; all fixtures use invented markers.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
