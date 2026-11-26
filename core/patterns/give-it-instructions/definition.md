# Give it instructions

Source ID `give-it-instructions`; pattern `glenngillen/give-it-instructions`; Guides, rung 1. Recognize useful instructions loaded in repositories the person regularly uses. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. This is the pack's complete reference pattern.

## Applicable work

- A **repository is applicable** when it has **at least three** of the person's sessions in the window. Two sessions do not make it applicable; three do.
- Only **main sessions** the person started count toward the three. Subagent sessions, sidechains and Dram's own analysis sessions do not ([evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- A window with no applicable repository is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen**: in an applicable repository, the agent **actually read** a **non-trivial** instruction file in a session:

- `CLAUDE.md`, `AGENTS.md`, or an agent rules file (for example a rules directory the agent loads alongside `AGENTS.md`);
- with real content: build or test commands, or conventions the agent should follow.

Completing evidence: the instruction content (quoted from what was loaded) and the session in which it was loaded. Filename existence alone is never evidence.

"Non-trivial" has **no deterministic rule yet** (see [parameters](../../reference/parameters.md#unresolved-classification)). The catalogue settles two ends: a `CLAUDE.md` with build commands and conventions is non-trivial; a file containing only `# Project` is not. No byte count or line count stands in for the rule.

## Exclusions

- Heading-only files (for example `# Project` alone).
- Empty files.
- Template-only files: generated or copied scaffolding whose sections were never filled in.
- **Claude Code auto-memory**: notes the agent writes for itself are not instructions the person gave.
- Conventions repeated in prompts when no instruction file exists: that is the problem this pattern coaches on, not a recognition (and is Write it down's territory once a file exists).
- A file created during a guided session that was never reviewed or never loaded in a session.

## Evidence

- **Cite** the attributable instruction content and its use: the loaded file's path, a quoted excerpt of its meaningful content, and the session that loaded it.
- **Attribution**: a repository file committed to the repository, or a user-level file in the person's configuration. A file the agent wrote unreviewed is not attributable to the person.
- **Historical**: the file must have existed and been loaded **when the session ran**. Current configuration alone cannot prove a past session read it, and a modification time alone does not prove a substantive refresh.
- **Evidence the pinned CLI does not supply**: which instruction files a session loaded; their content at the time; instruction-file history per repository; per-repository session counts over the window.

## Progression

Draft overrides of the [stages](../../reference/progression.md#pattern-specific-overrides):

| Stage | For this pattern |
| --- | --- |
| Seen | One applicable repository with loaded, non-trivial instructions. |
| Forming | Present in **two or more** applicable repositories. |
| Established | Present in [`most`](../../reference/parameters.md#most) applicable repositories: at least 60%, with at least four applicable repositories. With fewer than four, Established is not assessable, which is not a miss. |
| Continuous | Every applicable repository covered, **or** a user-level instruction file applying everywhere that was **updated in the last four weeks**, **and** the [mechanism](#mechanism) applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is instruction coverage that loads without the person: repository instruction files in every applicable repository, or a maintained user-level instruction file.

| Fact | For this pattern |
| --- | --- |
| In place | The repository files or user-level file existed, attributable to the person or their team, during the window. |
| Applied | Sessions in applicable repositories actually loaded them. |
| Held | Every applicable repository's sessions started with meaningful instructions; for a user-level file, it was substantively updated in the last four weeks. |
| Not holding | Sessions in an applicable repository ran without loading meaningful instructions while they were in place (for example, an agent that does not read that file). |
| Untested | A user-level file in place with no applicable session in the window. |

**Stale** is distinct from not holding: a user-level file loaded everywhere but not updated in the last four weeks still earns Seen, but not Continuous. Whether an update is "substantive" needs the refresh rule below; modification time alone does not prove it.

## Opportunities and coaching

- **Opportunity**: an applicable repository, frequently used, whose sessions loaded no meaningful instructions. It cites a person-authored moment from that repository, such as a prompt repeating a convention or starting work there ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) suggests generating a starting file (for example with `/init` where the agent supports it), then having the person review it and add the convention they most often correct.
- `automate` advice (a maintained user-level file) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The intended code check needs facts the pinned CLI (revision `bdea6f6`) does not supply and blocks it does not run. Recognizing this pattern from file presence alone would substitute a weaker definition (a file existing is not the agent reading it, and a heading is not instructions), which the pack must not do.

## Missing capabilities

- **Instruction load evidence**: which instruction files (repository, nested and user-level) each session loaded, with their content at the time.
- **Instruction resolution and provenance**: which files the agent in use reads, and whether a file is the person's, a template, auto-memory or agent-written.
- **Repository/session aggregation**: per-repository counts of the person's main sessions in the window, excluding subagents and Dram's analysis sessions.
- **File history**: instruction-file content over time, for historical loading and the four-week refresh.
- **A deterministic non-trivial rule**, confirmed by a person (see [open questions](#open-questions)).
- **A runnable gate and check**: `repo_file_matches` is declared in the pinned registry but not implemented, and only `tool_call_matches` runs as a gate. Neither would express loading.

## Verify before enabling

- Loaded `CLAUDE.md` with build commands and conventions, and loaded root `AGENTS.md` plus rules, are recognized; `# Project` alone is rejected.
- Repeated conventions in prompts with no instruction file are not recognized.
- Two sessions do not make a repository applicable; three do.
- Guided file creation without loading or meaningful review does not prove the pattern.
- Unused, auto-memory and stale-for-Continuous cases produce distinct results.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- What deterministic rule makes an instruction file non-trivial rather than heading-only or template-only?
  - evidence: The catalogue rejects `# Project` alone and accepts build commands and conventions, but gives no general rule; the requirements forbid an arbitrary byte count.
  - options: Confirm a content rule (for example, at least one command or convention line outside headings and unchanged template text); make it a model judgement with cited content.
  - location: core/patterns/give-it-instructions/definition.md / Recognition
- What counts as a substantive refresh of a user-level instruction file for Continuous?
  - evidence: The source requires an update in the last four weeks; modification time alone does not prove a substantive change.
  - options: Any content change beyond whitespace; a change a person authored or reviewed; a change adding or revising a rule.
  - location: core/patterns/give-it-instructions/definition.md / Mechanism
