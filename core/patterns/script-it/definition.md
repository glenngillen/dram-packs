# Script it

Source ID `script-it`; pattern `glenngillen/script-it`; Guides, rung 5. Use deterministic tooling for mechanical edits instead of repeating manual agent edits. Intended detection: judgement combined with execution and configuration evidence.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** For mechanical changes, the person has the agent use or build a deterministic tool (a codemod, a scaffolding script, a language server, a formatter) instead of editing by hand, so the result is exact and repeatable.

**Why it matters.** An agent editing forty files one by one is slow and can drift between files. A script makes the same change everywhere, is easy to review once, and can be run again.

**What a recognition shows.** That the person asked for, or configured, a deterministic tool, and running it is what made a mechanical change.

**Why the rules are drawn this way.**

- **Mechanical changes across many files.** That is where hand edits drift and a tool's exactness pays. Whether a change is mechanical is a model judgement citing the change. "Many" has no recognition threshold; ten files is only a coaching trigger, trying to capture "enough identical hand edits to be worth pointing out", and is a [calibration point](../../reference/principles.md#thresholds-are-calibration-points). A window with no such change reports nothing ([applicable work](../../reference/principles.md#applicable-work)).
- **The person requested or configured the tool.** A throwaway script the agent wrote on its own, or a tool it discovered, is the agent's initiative ([human intent only](../../reference/principles.md#human-intent-only)).
- **The tool's run made the change.** A script written but never run, run on nothing, or merely present does not make the result exact or repeatable ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)). The same is true for later stages, which count only instances whose run made the change ([follow-through](../../reference/principles.md#follow-through)).
- **Files edited one by one are excluded, even when identical.** That is the hand editing the pattern replaces.
- **Continuous needs a saved script or wrapper that is reused.** Saved in the repository, the next change of that kind goes through it without remembering ([stages](../../reference/principles.md#stages)); the same change made by hand while it was in place is not holding ([prevention](../../reference/principles.md#prevention-when-success-removes-the-signal)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. [`judge.md`](judge.md) is authoring prose for the mechanical-change judgement; the pinned CLI does not execute it.

## Applicable work

- A **mechanical change across many files**: renames, API migrations, boilerplate, import rewrites. Whether a change is mechanical is a model judgement citing the change.
- "Many" has **no recognition threshold**. Ten files is the source's **coaching trigger** ([`many_files_coach`](../../reference/parameters.md#many_files_coach)): coaching only, not recognition. It never earns or denies recognition and is not a universal definition of "many".
- A window with no mechanical multi-file change is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen**: for an applicable change, either

1. the person **requested** a script, codemod or tool ("write a codemod for the API rename and run it on src/"; "use the scaffold script to add the new endpoint") and its **execution actually made the change**; or
2. the person **configured** a language or MCP tool (for example a code-intelligence rename tool) and the agent **subsequently used it** to make the change.

Completing evidence: the person's request or configuration, and the tool execution that made the change, linked to the resulting edits.

## Exclusions

- **Unprompted throwaway scripts**: the agent deciding by itself to write a one-off script is spontaneous agent behaviour.
- Scripts **written but never run**, or run on nothing.
- Many files **edited individually** by the agent, even with identical edits.
- A tool the agent **discovered** on its own: agent discovery does not establish person configuration.
- Guided discussion of a script without the person's requested execution.
- A script's existence alone: it does not establish deterministic behaviour, correct changes or reuse.

## Evidence

- **Cite** the person's request (exact quote) or the attributable configuration, and the tool execution with the edits it produced.
- **Attribution**: a person prompt requesting the tool, or tool configuration in the person's user or repository settings.
- **Historical**: tool configuration must have existed when the session ran.
- **Evidence the pinned CLI does not supply**: linkage from a tool execution to the file edits it produced; tool provenance (person-configured or agent-discovered); a mechanical-change judgement; repeat-execution history of a saved script.

## Progression

Default [stages](../../reference/progression.md#stages), with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion): Seen counts the person's request with the run that made the change; Forming and Established count only instances whose run made the change, credited to the week it finished. A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is a **repository-saved script or command wrapper** for a recurring kind of mechanical change.

| Fact | For this pattern |
| --- | --- |
| In place | The script or wrapper existed in the repository during the window, attributable to the person or their team. |
| Applied | It was reused on a mechanical change in the window. |
| Held | Applicable mechanical changes of that kind went through it rather than file-by-file edits. |
| Not holding | The same kind of change was made by hand file by file while it was in place. |
| Untested | In place, with no applicable change in the window. |

## Opportunities and coaching

- **Opportunity**: a mechanical change made by editing files individually, citing the person's prompt that started it ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching trigger**: the same mechanical edit made by hand across [`many_files_coach`](../../reference/parameters.md#many_files_coach) (ten or more) files. Below ten files, coaching is not triggered, but that is not a recognition and not a statement that the change was not mechanical.
- The [guide](guide.md) asks for a script on the person's next real rename or migration and encourages them to review it before it runs.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) cannot link a tool run to the edits it made, tell a person-configured tool from one the agent discovered, or judge that a change was mechanical. Matching commands such as `sed` or a codemod name would count unprompted scripts and unrun ones, which the definition excludes.

## Missing capabilities

- **Execution-to-edit linkage**: which file changes a script or tool run produced.
- **Tool provenance**: person-configured language/MCP tools versus agent discovery, at the time of the session.
- **Mechanical-change judgement**, citing the change.
- **Request attribution**: linking the person's prompt to the script that ran.
- **Repeat-execution history** for saved scripts across sessions.
- **A runnable judge and checks**: only `tool_call_matches` and `tool_call_sequence` run, and neither expresses request, provenance or edit linkage.

## Verify before enabling

- "Write a codemod for the API rename and run it on src/" followed by its execution is recognized; forty files edited individually are rejected.
- "Use the scaffold script to add the new endpoint" with execution is recognized; a script never run is rejected.
- A configured code-intelligence tool actually used is recognized; agent discovery alone is rejected.
- Guided script discussion without requested execution earns nothing.
- Ten or more hand-edited files trigger coaching only and never change a recognition result.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.
