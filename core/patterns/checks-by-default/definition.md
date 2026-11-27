# Checks by default

Source ID `checks-by-default`; pattern `glenngillen/checks-by-default`; Checking the work, rung 3. Recognize checks that run because the person's harness asks for them. Intended detection: configuration checks combined with model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- A **session is applicable** when it is one of the person's **main sessions** that **changed code**, in a **repository with relevant checks** (tests, type checks, lint or build that apply to the changed code).
- **Coverage is over applicable repositories**, not every directory on the machine: a scratch folder with no checks is not counted against.
- A window with no code-changing session in a repository with checks is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen** needs, in this order:

1. An **instruction rule or hook** directing checks after changes (for example a `CLAUDE.md` line "after editing Go files, run `make test`", or a PostToolUse hook running `tsc --noEmit` after edits), **attributable** to the person or their team, and **in place and loaded when the session ran**.
2. A **code edit** in the session.
3. A **relevant check executing after that edit** (`make test`, `tsc`, `ruff check .`, ...) **without a fresh person prompt** asking for it between the edit and the check.

Completing evidence: the attributable rule or hook and the resulting check execution. The check ran because the harness asked, not because the person asked this time (that is [Prove it](../prove-it/definition.md)) and not because the model happened to.

**Execution is not passing.** A check that ran and failed is recorded honestly; the rule worked as a trigger, so it still counts for Seen. Mere execution cannot establish that an unresolved violation held: a directed check left failed and unresolved when the session ended is a [not-holding](#mechanism) case, and a missing check result leaves holding unassessed.

## Exclusions

- **Spontaneous model habits**: the agent ran tests with no instruction or hook asking it to.
- **Rules never followed**: a rule in place whose sessions changed code without the check running (that is the not-holding case, not Seen).
- **Configuration with no execution**: a hook or rule configured, but no check ran in any session.
- A check run because the **person asked in a fresh prompt**: that is Prove it, even when a rule also exists.
- A rule **added after the session**: current configuration cannot prove it caused that session's check. The rule must have existed and applied **when the session ran** (historical instruction resolution).
- A check that ran **before** the edit, or an irrelevant command (for example `git status`).
- Rules from third-party templates or auto-memory the person never adopted (not attributable).

## Evidence

- **Cite** the rule or hook (file path and quoted line, or hook definition) attributable to the person or team, its presence when the session ran, the edit, and the check's tool call with its output. Keep the edit and check order and confirm no person prompt intervened.
- **Historical**: instruction and hook configuration must be resolved as of the session, not from today's files ([cross-session evidence](../../reference/evidence.md#cross-session-evidence)).
- **Missing or truncated** session records or configuration history are insufficient, never a miss.
- **Evidence the pinned CLI does not supply**: historical instruction and hook resolution per session; hook run records (declared hook checks do not execute in the fixed-pattern engine); check-kind classification; prompt/edit/check ordering; which repositories have relevant checks; model judgement linking a check to the rule that directed it.

## Progression

Overrides of the [stages](../../reference/progression.md#stages):

| Stage | For this pattern |
| --- | --- |
| Seen | One code-changing session where an owned rule or hook caused a check after an edit. |
| Forming | Such sessions in at least two distinct weeks of the last four. |
| Established | At least 60% of applicable code-changing sessions, with at least four applicable sessions ([`most`](../../reference/parameters.md#most)). |
| Continuous | The rule or hook in **every applicable repository** and followed in the window, **and** the shared [mechanism](#mechanism) requirement. Coverage alone is not enough. |

A guided session establishes Seen only, and only once a later session follows the rule ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the after-change check rule or hook itself.

| Fact | For this pattern |
| --- | --- |
| In place | The rule (in a loaded instruction file) or hook existed, attributable to the person or team, when the session ran. |
| Applied | A code-changing session loaded the rule or the hook fired after an edit. |
| Held | The directed check ran after edits, without prompting, in every applicable repository's code-changing sessions, and no directed check was left failed and unresolved when the session ended. Execution alone does not establish holding. |
| Not holding | While in place and applied, a code-changing session ended with no directed check after the last edit, **or** a directed check ran, failed and remained unresolved when the session ended. |
| Untested | In place, but no code-changing session in that repository in the window. |
| Unassessed | The check ran but its result is missing or truncated: insufficient evidence for held or not holding. Seen still rests on the execution. |

## Opportunities and coaching

- **Opportunity**: code-changing sessions ending without any check after the last edit, in a repository with checks. It cites a person-authored moment, such as the prompt that started the work or accepted the result ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) asks the person to add their real test or type-check commands to their instructions with an after-change requirement.
- `automate` advice (coverage everywhere, or a user-level rule) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs historical configuration (which rule or hook was in place and loaded when the session ran), hook run records, edit/check/prompt ordering and judgement that the check was caused by the harness. Declared hook checks currently do not execute in the pinned fixed-pattern engine (revision `bdea6f6`), and `tool_call_matches` on a test command alone would count spontaneous habits and person-requested checks, which the definition excludes.

## Missing capabilities

- **Historical instruction resolution**: which instruction files and rules each session loaded, with their content at the time.
- **Hook configuration history and run records**: whether a hook was in place and fired after an edit.
- **Prompt/edit/check ordering**: a check after an edit with no intervening person prompt.
- **Check-kind classification** and **repository coverage**: which repositories have relevant checks.
- **Causation judgement**: linking the check to the rule or hook that directed it.
- **A runnable model judge**: [judge.md](judge.md) is not executed by the pinned CLI.

## Verify before enabling

- `CLAUDE.md` instructing `make test` after edits, followed without prompting, is recognized; unprompted tests with no rule are rejected.
- An owned PostToolUse hook running `tsc` after edits is recognized; configuration with no execution is rejected.
- An instruction added after the session does not prove it caused that session's check.
- Guided rule creation without a later followed session is incomplete for Seen.
- A failing check is recorded as executed, not passed.
- Unused, held and not-holding mechanism cases produce distinct results; coverage counts only applicable repositories.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
