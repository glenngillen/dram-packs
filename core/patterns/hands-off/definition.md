# Hands off

Source ID `hands-off`; pattern `glenngillen/hands-off`; Delegation, rung 4. Run a trusted owned workflow unattended and use its output. Intended detection: code facts combined with model judgement.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern. The intended judge prompt is [judge.md](judge.md) (authoring prose; not executed by the pinned CLI).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- An **owned command or skill** (one the person or their team defined: a custom slash command, skill or saved workflow) that the person has **already run interactively at least three times** (three interactive runs, in any number of sessions) before the run being assessed. That history is what makes the workflow familiar enough to hand off.
- Built-in commands, third-party or plugin commands and ad-hoc prompts are not owned workflows and are not applicable.
- Only the person's **main sessions** count toward the interactive history; subagents, sidechains and Dram's own analysis sessions do not ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with no owned command run interactively at least three times is **no applicable work**: nothing is reported, not a miss.

Keep two counts distinct:

| Count | Used for |
| --- | --- |
| At least **three interactive runs** of the owned command | Applicability: the command is familiar enough for an unattended run to be assessed. |
| The command repeated interactively across **three or more sessions** | The coaching trigger (see [opportunities](#opportunities-and-coaching)). Three runs in one session meet applicability but not this trigger. |

## Recognition

**Seen** needs all of:

1. **An applicable owned command or skill** (above), with its ownership attributable to the person or their team's configuration.
2. **An unattended run** of it, as defined by [`unattended_gap`](../../reference/parameters.md#unattended_gap): a headless run, or an interactive run with at least 15 minutes (inclusive) of continued agent work without a person prompt ([completion windows](../../reference/evidence.md#completion-windows)).
3. **A person-authored launch**: the person started the run, or a schedule or trigger the person or their team configured started it. A launch by software acting on its own behalf (a third-party service or bot running an agent for its own purposes) is not automatically the person's work.
4. **The output actually used**: the produced notes published, labels applied, a branch merged, a report acted on. Use is judged from later evidence, not from the run finishing.

Completing evidence: the run's **first prompt** (the command invocation that started it) and the **output's actual use**. The run alone, without use, is not completion. Use that happens after the window closes is credited to the window in which it happened, not silently back to the run ([completion windows](../../reference/evidence.md#completion-windows)).

## Exclusions

- **Ad-hoc headless prompts** (for example `claude -p "summarise this file"`): not an owned workflow, so not applicable.
- **Interactive runs** of the owned command with no qualifying unattended work: the person watched it, which is the applicability history, not this pattern.
- **Discarded output**: an unattended run whose result was never used, or was redone by hand.
- **Launches by software acting on its own behalf**, even if it runs the person's command.
- An owned command run unattended **before** it reached three interactive runs: not yet applicable, so neither Seen nor a miss.
- **Guided setup** without a qualifying unattended run whose output was used.

## Evidence

- **Cite** the run's first prompt (exact quote of the invocation, from a person prompt or an attributable configured trigger) and the evidence that its output was used (the later person prompt, commit, merge or publish step).
- **Applicability history**: the three earlier interactive runs, with their session IDs and timestamps.
- **Ownership**: the command's definition, attributable to the person or their team, existing when the runs happened. Current configuration alone cannot prove what existed then ([cross-session evidence](../../reference/evidence.md#cross-session-evidence)).
- **Run scope**: whether the run was headless or met `unattended_gap`, and the permission scope it ran under. Run scope is kept so the Scope permissions prerequisite can be checked for unattended work specifically.
- Missing, truncated or excluded run records, or an unknown later use, are [insufficient](../../reference/evidence.md#insufficient-evidence): unassessed, never a miss.
- **Evidence the pinned CLI does not supply**: owned-command provenance; per-command interactive run counts; headless versus interactive launch facts; continued-work timing without person prompts; launch provenance (person, configured trigger or software acting for itself); output-use linkage across sessions and repositories.

## Progression

No override of the [stages](../../reference/progression.md#stages) beyond the [stage-dependent completion](../../reference/progression.md#stage-dependent-completion) rule:

| Stage | For this pattern |
| --- | --- |
| Seen | One unattended run of an applicable owned command whose output was used. |
| Forming | Such runs in at least two distinct weeks of the last four, each credited to the week its output was used. |
| Established | At least 60% of applicable owned-command runs in the window ran unattended with output used, with at least four applicable runs ([`most`](../../reference/parameters.md#most)). |
| Continuous | A configured schedule or trigger, in place, applied and holding (see [mechanism](#mechanism)). |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is a **schedule or trigger the person or their team configured** that runs the owned workflow unattended.

| Fact | For this pattern |
| --- | --- |
| In place | The attributable schedule or trigger existed during the window, pointing at an owned command or skill. |
| Applied | It actually ran the workflow in the window. |
| Held | Its output was used each time it produced something (labels applied, notes published, findings acted on). |
| Not holding | It ran while in place but its output went unused, was redone by hand, or its failures were left unacted on. |
| Untested | Configured but did not run in the window. |

A high share of unattended runs alone is not Continuous: the configured trigger must be in place, applied and holding ([mechanisms](../../reference/evidence.md#mechanisms-in-place-applied-held)).

## Opportunities and coaching

- **Prerequisite.** This suggestion is offered **only after Scope permissions is at least Seen specifically for unattended work** ([safety prerequisites](../../reference/progression.md#safety-prerequisites)). Seen for Scope permissions on interactive sessions only does not satisfy it. The pinned `requires` field takes bare pattern IDs and cannot say "Seen, for unattended runs", so it is not used to encode a weaker version; the requirement stays here in prose. A missing prerequisite **suppresses the suggestion only**: evidence collection for this and other patterns continues.
- **Opportunity**: an owned command repeated interactively across **three or more sessions**, with the person watching each run and the prerequisite met. It cites the person-authored prompt invoking the command in the latest of those sessions ([opportunities](../../reference/evidence.md#opportunities)). Three runs inside one session do not trigger it.
- **Coaching**: the [guide](guide.md) has the person choose a sufficiently familiar owned command, inspect its scoped permissions, then request an unattended run and use its output. It never suggests permission bypass.
- `automate` advice (a configured schedule or trigger) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

Recognition needs ownership provenance, interactive run history per command, unattended classification, launch provenance and judgement of whether output was used. The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. Matching a command name would accept ad-hoc headless prompts, interactive runs, software-launched runs and discarded output, all of which the definition excludes. The run-scoped Scope permissions prerequisite cannot be encoded by `requires`.

## Missing capabilities

- **Owned-workflow provenance**: whether a command or skill is the person's or their team's, as configured when it ran.
- **Interactive run history** per owned command, with session boundaries, to apply the three-run applicability and three-session coaching counts separately.
- **Unattended classification**: headless launch facts and continued-agent-work timing against `unattended_gap`.
- **Launch provenance**: person, configured trigger, or software acting on its own behalf.
- **Output-use linkage**: connecting a run's output to its later use (publish, label, merge, acted-on report) across sessions.
- **Run-scoped prerequisite enforcement**: checking Scope permissions Seen for unattended work before suggesting.
- **A runnable model judge** for output use; [judge.md](judge.md) is not executed. Nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- Unattended `/release-notes` whose notes are published, after three interactive runs, is recognized; the same command run only interactively is rejected.
- Scheduled `/triage` whose labels are applied is recognized; ad-hoc `claude -p "summarise this file"` is rejected.
- No output-use evidence means no completed recognition.
- Missing scoped unattended permissions suppresses the suggestion, not unrelated evidence collection.
- Guided setup without a qualifying run and use is incomplete.
- Exactly 15 minutes without a person prompt is unattended; 14 minutes is not.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
