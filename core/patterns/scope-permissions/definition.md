# Scope permissions

Source ID `scope-permissions`; pattern `glenngillen/scope-permissions`; Safety, rung 2. Grant the tools/commands the work needs without broad approval. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. Named as one of the first activation candidates; it still needs the capabilities below.

## Applicable work

- **Every main session** in the window, interactive or **unattended** ([`unattended_gap`](../../reference/parameters.md#unattended_gap)); unattended work matters most.
- **Excluded (neutral)**: a session that bypassed permissions (approval-skipping modes such as Claude Code's `bypassPermissions` / `--dangerously-skip-permissions`, or Codex's approval-skipping flags) **inside a qualifying sandbox**. User decision: it is neither credit nor a miss here, it does not count against Continuous coverage, and it is recognized only by [Sandbox autonomy](../sandbox-autonomy/definition.md).
- A bypassed session whose execution environment is **unknown** cannot be classified as sandboxed or not: it is unassessed, not applicable work and not a miss.
- A window with no main sessions is **no applicable work**.

## Recognition

**Seen** requires all of:

1. **An attributable allow list**: configured by the person or their team.
2. **Scoped**: it approves specific commands and tools the work needs (for example running the tests, `git status`). An unrestricted entry (`Bash(*)`, or any wildcard that approves every command) is not scoped. No universal breadth metric is defined, and a non-empty list is not assumed to be least privilege.
3. **Effective**: after **settings precedence** across every loaded source, the session actually ran under that scoped list. A restrictive file that a broader user, project or local setting **overrides** is insufficient.
4. **Not bypassed**: the session ran in a normal approval mode, not a permission-bypass mode.

Completing evidence: the effective configuration and the session's permission mode. The **run scope** (interactive or unattended) is recorded with the recognition, so that [Hands off](../hands-off/definition.md) suggestions can require this pattern Seen specifically for unattended work.

## Exclusions

- **Unrestricted allow lists** such as `Bash(*)`.
- **Permission bypass** outside a qualifying sandbox (an opportunity where the coaching trigger applies).
- **Sandboxed bypass**: neutral, excluded from applicable work; this pattern is never awarded merely because a run is sandboxed.
- **Overridden scoped files**: a narrow list that a broader effective setting supersedes.
- **Guided permission edits** without an observed scoped session.

## Evidence

- **Cite** the effective configuration (sources and the entries in force) and the session's permission mode and run type. A person-authored citation can be supplied by configuration attribution where the [evidence contract](../../reference/evidence.md#attribution-and-citations) allows, plus the person's launch or first prompt in the session.
- **Historical**: the configuration and mode must be those in force when the session ran; current settings cannot prove a past session.
- **Evidence the pinned CLI does not supply**: effective settings per session after precedence; allow-list semantics (what an entry approves); permission mode per session; run-type attribution (interactive, unattended, launched by software on its own behalf); sandbox classification of the execution environment; repository facts such as production access or deploy scripts for coaching.

## Progression

Uses the default [stages](../../reference/progression.md#stages) with a coverage qualification for Continuous ([pattern-specific overrides](../../reference/progression.md#pattern-specific-overrides)):

| Stage | For this pattern |
| --- | --- |
| Seen | One applicable session under an effective scoped allow list without bypass. The run scope is recorded. |
| Forming | Such sessions in at least two distinct weeks of the last four. |
| Established | At least 60% of applicable sessions, with at least four applicable sessions ([`most`](../../reference/parameters.md#most)). |
| Continuous | **All** applicable sessions, unattended ones included, under scoped permissions through an applied and holding configuration. Coverage alone is not advertised as enough: the [mechanism](#mechanism) must hold. |

Sandboxed bypassed sessions are excluded from every denominator. A guided edit establishes Seen only once a scoped session is observed ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the scoped permission configuration.

| Fact | For this pattern |
| --- | --- |
| In place | An attributable scoped allow list existed during the window for the repositories or user. |
| Applied | Sessions actually ran under it as the effective configuration. |
| Held | Every applicable session, including unattended ones, ran scoped and without bypass, and no broader entry took effect. |
| Not holding | While in place, a session bypassed permissions outside a sandbox, or a broader setting overrode the scoped list. |
| Untested | Configured for a repository with no session in the window. |

## Opportunities and coaching

- **Opportunity**: a session bypassed permissions **outside a sandbox** in a repository with production access or deploy scripts. It cites the person-authored moment (the attributable launch, or the first prompt of that session) ([opportunities](../../reference/evidence.md#opportunities)). The same bypass inside a qualifying sandbox is not an opportunity.
- An unrestricted allow list is not recognized; it is not reported as an opportunity on its own, because the coaching trigger is bypass.
- **Coaching**: the [guide](guide.md) identifies the commands the person actually approves often and lets them request a narrow allow list.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate). Scope permissions is a [safety prerequisite](../../reference/progression.md#safety-prerequisites) for Hands off (scoped unattended permissions) and for broader autonomy; that prerequisite is prose, not a `requires` binding.

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. Its permission block is declared deny-only, with no allow-list or permission-mode contract and no fixed-pattern execution, and the collected-history fixture shape has no effective settings, mode or run type. Matching allow-list text would accept overridden files and unrestricted entries, and could not tell sandboxed from host bypass.

## Missing capabilities

- **Effective settings precedence** per session across all loaded sources.
- **Allow-list semantics**: what each entry approves, including wildcards.
- **Permission mode** per session (normal, bypass).
- **Run-type attribution**: interactive versus unattended, and who launched it.
- **Sandbox classification** of the execution environment, shared with Sandbox autonomy.
- **Repository risk facts** (production access, deploy scripts) for the coaching trigger.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- A narrow test/`git status` allow list in normal mode is recognized; `--dangerously-skip-permissions` in the main repository on a credentialed host is an opportunity.
- An unattended run with a scoped allow list is recognized with its unattended run scope; `Bash(*)` is rejected.
- A restrictive file overridden by effective broader settings is insufficient.
- A sandboxed bypassed session neither earns Seen nor counts against Continuous coverage; the same bypass on a credentialed host is an opportunity.
- Guided permission edits without an observed scoped session do not earn Seen.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
