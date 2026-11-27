# Guard destructive commands

Source ID `guard-destructive`; pattern `glenngillen/guard-destructive`; Safety, rung 3. Require effective protection around hard-to-undo commands. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** Commands that can't be undone (force pushes, recursive deletes, production database or deploy commands) are blocked or need explicit approval, whatever mode the session is in.

**Why it matters.** An agent that usually asks first will not always ask. A deny rule, an ask rule or a pre-tool-use guard makes the stop happen by configuration. It is a Safety prerequisite for broader autonomy ([autonomy and safety advance together](../../reference/principles.md#autonomy-and-safety-advance-together)).

**What a recognition shows.** That a guard the person or their team configured, covering destructive commands relevant to the repository or run, was effective in a session there.

**Why the rules are drawn this way.**

- **Repositories with deploy, migration or infrastructure commands, and every unattended run, apply.** Those are where an irreversible command can run, and an unattended run has nobody watching. Elsewhere nothing is reported ([applicable work](../../reference/principles.md#applicable-work)). The `unattended_gap` boundary tries to capture "nobody was watching this run" and is a [calibration point](../../reference/principles.md#thresholds-are-calibration-points).
- **Destructive commands come from the repository's actual commands.** The guard is judged against what could cause irreversible harm there, not against every shell command.
- **A configured guard, not the agent's habit of asking.** An agent's own "shall I force push?" can be skipped the next time ([human intent only](../../reference/principles.md#human-intent-only)).
- **Relevant and effective in the session's mode.** A guard for commands the repository never uses, or one a bypass mode skips, doesn't protect that session; these are facts code reads ([code checks facts; a model judges the rest](../../reference/principles.md#code-checks-facts-a-model-judges-the-rest)).
- **No universal blocking is claimed.** Spellings, aliases, wrappers and compound commands can get past a pattern-matching guard, so coverage is judged for commands as actually invoked ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **Evidence is never manufactured.** Nobody runs a destructive command to prove a guard works; a guard with no applicable session stays untested ([guided sessions reach Seen only](../../reference/principles.md#guided-sessions-reach-seen-only)).
- **Continuous needs guards wherever unattended or parallel work runs, with evidence they held.** That is where a missing guard costs most; silence counts only where the guard applied ([prevention: when success removes the signal](../../reference/principles.md#prevention-when-success-removes-the-signal)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. Named as one of the first activation candidates; it still needs the capabilities below.

## Applicable work

- A **repository with deploy, migration or infrastructure commands** (for example a deploy script, a database migration task, infrastructure apply) where the person had a main session in the window.
- **Every unattended run** ([`unattended_gap`](../../reference/parameters.md#unattended_gap)), wherever it runs.
- Which commands count as destructive is decided from the repository's actual commands and evidence, not by classifying every shell command as dangerous.
- A window with neither is **no applicable work**.

## Recognition

**Seen** requires all of:

1. **An attributable guard**: a deny rule, an ask rule or a pre-tool-use guard (a PreToolUse hook or equivalent), configured by the person or their team.
2. **Relevant coverage**: it covers destructive commands actually relevant to the repository or run (a guard for a command the repository never uses does not prove coverage).
3. **Effective in the session**: the session's **permission mode** did not skip it. An ask rule protects only in modes that still ask; a bypass mode that skips the guard makes it ineffective for that session. Configuration presence alone cannot establish protection "whatever the mode".
4. **Applied**: a main session or unattended run in that repository ran while the guard was effective.

Completing evidence: the effective configuration and the relevant session. An actual block, or an ask followed by the person's decision, is the clearest evidence but is not required for Seen.

**No universal blocking is claimed.** Shell spelling, aliases, wrappers and compound commands can get past a pattern-matching guard. Coverage is assessed for the commands as actually invoked, never promised from a simple regex.

## Exclusions

- **Trusting the agent to ask**: an agent's own "shall I force push?" with no rule or guard is not protection.
- **Guards the session's bypass mode skips**.
- **Guard text unrelated** to the actual commands or repository.
- **Guided setup with no applicable session**: it stays untested; nobody runs a destructive command to produce evidence. The guide does not run a destructive command to manufacture evidence.

## Evidence

- **Cite** the effective configuration and the relevant session (with its permission mode). Where the guard fired, cite the block or the ask and the person's decision. A person-authored citation can be supplied by configuration attribution where the [evidence contract](../../reference/evidence.md#attribution-and-citations) allows, plus the person's prompt in the session.
- **Historical**: the guard and mode must be those in force when the session ran.
- **Evidence the pinned CLI does not supply**: effective deny, ask and hook enforcement per session; permission mode; which destructive commands the repository uses; how commands were actually spelled and invoked; block, ask and approval records; configuration history and attribution.

## Progression

Uses the default [stages](../../reference/progression.md#stages) with a coverage qualification for Continuous ([pattern-specific overrides](../../reference/progression.md#pattern-specific-overrides)):

| Stage | For this pattern |
| --- | --- |
| Seen | One applicable session or unattended run with an effective guard covering its relevant destructive commands. |
| Forming | Such sessions in at least two distinct weeks of the last four. |
| Established | At least 60% of applicable sessions guarded, with at least four applicable sessions ([`most`](../../reference/parameters.md#most)). |
| Continuous | Effective guards **wherever unattended or parallel work runs**, with evidence they held in the window (for example an actual block), **and** the [mechanism](#mechanism) holding. |

A guided setup establishes Seen only once an applicable session runs under the effective guard ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the guard itself.

| Fact | For this pattern |
| --- | --- |
| In place | An attributable deny rule, ask rule or guard covering the relevant commands existed during the window. |
| Applied | It was effective in an applicable session, given the session's mode; or it fired on an attempted command. |
| Held | Where unattended or parallel work ran, covered destructive commands that were attempted were blocked, or the agent stopped and the person decided. |
| Not holding | While in place, a destructive command it should have covered ran without approval: a bypass mode skipped it, or a spelling, alias, wrapper or compound command got past it. |
| Untested | Configured where no applicable session ran in the window. |

## Opportunities and coaching

- **Opportunity**: a destructive command ran without the person's approval in an applicable session. It cites the person-authored moment (the prompt that started the work in which it ran) ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) helps the person guard their most dangerous relevant command. It never runs that command, or any destructive command, to produce evidence.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate). Guard destructive commands is a [safety prerequisite](../../reference/progression.md#safety-prerequisites) for broader autonomy.

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. Its permission block is declared deny-only (no ask rules, no hook guards, no permission mode) with no fixed-pattern execution, and `hook_configured` is declared but not implemented. Matching guard text would accept guards the mode skips or that cover irrelevant commands, and matching commands cannot show whether a guard stopped them.

## Missing capabilities

- **Effective enforcement**: deny, ask and pre-tool-use guard behaviour per session, given its permission mode.
- **Command coverage**: the repository's destructive commands and whether each invocation, as actually spelled, was covered.
- **Invocation and approval records**: blocks, asks and the person's decisions.
- **Run-type attribution**: unattended and parallel runs.
- **Configuration history and attribution**.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- An effective pre-tool-use guard for force pushes and recursive removal is recognized; an unguarded agent force push is an opportunity.
- An effective ask rule on `terraform apply` is recognized; a guard skipped by permission bypass is rejected and reported as not holding.
- Guard text unrelated to the actual command or repository does not prove coverage.
- Guided setup with no applicable session stays untested and never prompts a destructive trial.
- A command that evaded a pattern-matching guard is reported as not holding, never as covered.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
