# Pattern parameters

The single list of tunable defaults the pattern definitions depend on. Patterns link to a parameter here, for example [`most`](#most), instead of restating its number, so one change updates every dependent pattern.

**Every value is provisional.** The user decided that the source's worked examples become provisional defaults and approved proposed defaults where the source gave none. They are starting points to calibrate during private staff evaluation. None has been validated or calibrated, and none is reported as measured.

Rules that apply to all of them:

- **Prose only.** The pinned Dram schema has no field for these values, so they live here rather than in `pattern.yaml`. No schema field is invented to hold them. Where an implemented block later accepts an equivalent parameter, use the value below.
- **A default does not enable a detector.** Enabling still needs the supporting capability and the evaluation bar in [authoring and readiness](authoring.md#readiness-vocabulary).
- **Unknown inputs produce nothing.** Unknown context size, missing timestamps or an unknown model tier give no recognition and no cost claim; a default never substitutes for missing data (see [insufficient evidence](evidence.md#insufficient-evidence)).
- **Boundaries.** Gap and token thresholds are strict "more than": exactly 1 hour or exactly 150,000 tokens does **not** qualify. Coverage thresholds are inclusive "at least": exactly 60% **does** qualify.

| Parameter | Default | Origin | Used by | Status |
| --- | --- | --- | --- | --- |
| `cache_gap` | Break of more than 1 hour between turns | Source example | Mind the cache | Provisional |
| `large_context_tokens` | 150,000 tokens of prior context | Source example | Mind the cache, Hand it off | Provisional |
| `long_session` | Context over `large_context_tokens`, or any compaction | Approved proposal | Hand it off | Provisional |
| `substantial_work_prompts` | At least 6 person prompts on the prior task before `/clear` | Approved proposal | Clear between tasks | Provisional |
| `instruction_cost_share` | Instruction files loading more than 12% of initial context | Source example | Keep it lean | Provisional |
| `most` | At least 60% of applicable items, with at least 4 applicable items | Source Established threshold, applied consistently | Give it instructions, Save it, Let the harness carry it, Fix the harness, [progression](progression.md) | Provisional |
| `fix_followup` | At least 2 later applicable sessions within 14 days of the harness change, with no recurrence | Approved proposal | Fix the harness | Provisional |
| `routine_work` | Renames, docstrings, formatting, version bumps and simple fixes | Source example list | Right-size it, Let the harness carry it | Provisional |
| `many_files_coach` | 10 or more files | Source coach trigger (coaching only, not recognition) | Script it | Provisional |
| `handoff_pairing` | Previous main session in the same repository ending within 24 hours | Source | Hand it off | Provisional |
| `unattended_gap` | Headless, or 15 minutes or more of agent work without a person prompt | Source | [Evidence contract](evidence.md#completion-windows) | Provisional |
| `kept_window` | 14 days in the default branch | Source | [Outcomes](outcomes.md) | Provisional |
| `several_parallel` | 3 or more independent parts run in parallel | Approved proposal | Fan out | Provisional |
| `long_turn` | Agent turn running 5 minutes or more while the person waits | Approved proposal | Two at once | Provisional |
| `fast_check` | Per-step check usually finishing within 60 seconds | Approved proposal | Gate each step | Provisional |

## Boundaries and notes

### `cache_gap`

Strictly more than 1 hour between turns. A five-minute gap is outside Mind the cache's applicable work; exactly one hour is outside; two hours is inside. If the CLI supplies a model's known cache lifetime as a fact, that lifetime replaces the default; otherwise the default applies.

### `large_context_tokens`

Strictly more than 150,000 tokens of prior context. A 40,000-token context is outside; exactly 150,000 is outside. A two-hour gap after more than 150,000 tokens is inside Mind the cache's applicable work. Unknown context size gives no recognition and no cost claim.

### `long_session`

Context over [`large_context_tokens`](#large_context_tokens), or any compaction. Defines which sessions Hand it off applies to.

### `substantial_work_prompts`

At least 6 person prompts (inclusive) on the prior task before `/clear`. A `/clear` after 3 person prompts is not after substantial work; after 6 it is. Tool results, hook output and compaction summaries are not person prompts.

### `instruction_cost_share`

Strictly more than 12% of the initial context loaded by instruction files. The source's 12% figure is an illustration of the boundary; exactly 12% does not exceed it.

### `most`

At least 60% of applicable items **and** at least 4 applicable items. With 3 applicable items "most" cannot be met; that is **not assessable**, not a miss. 3 of 5 (60%) meets it.

### `fix_followup`

At least 2 later applicable sessions within 14 days of the harness change, with no recurrence of the correction. One later applicable session is not enough; a recurrence within 14 days is not holding.

### `routine_work`

The source's example list. Work outside the list is **not automatically non-routine**: classifying it is a judgement the model-judged recognizer must justify with evidence.

### `many_files_coach`

A coaching trigger only. Ten or more files edited by hand can prompt Script it's coaching; it never earns or denies recognition.

### `handoff_pairing`

The previous main session in the same repository that ended within 24 hours before the new session began.

### `unattended_gap`

A headless run, or at least 15 minutes (inclusive) of continued agent work without a person prompt.

### `kept_window`

A change still present in the default branch 14 days later. A change younger than 14 days is **unassessed**, not a failed kept change. A one-day revert measure is not fourteen-day survival.

### `several_parallel`

Three or more independent parts running in parallel (inclusive). Sequential fan-out does not count.

### `long_turn`

An agent turn running 5 minutes or more (inclusive) while the person waits.

### `fast_check`

A per-step check that usually finishes within 60 seconds. How "usually" is measured is not yet specified.

## Unresolved classification

- "Non-trivial" instruction files in Give it instructions have **no value**. No byte count or line count stands in for it, and that detection stays disabled until a deterministic rule is confirmed.

## Open questions

- What deterministic rule makes an instruction file non-trivial rather than heading-only or template-only?
  - evidence: The source gives examples (`# Project` alone is trivial) but no rule; the parameters spec leaves it without a value.
  - options: Confirm a content rule (for example, at least one command or convention line beyond headings); keep it a model judgement.
  - location: core/reference/parameters.md / Unresolved classification
- How is "usually" measured for `fast_check`?
  - evidence: The approved proposal says "usually finishing within 60 seconds" without a statistic.
  - options: Median duration over the window; a fixed share of runs under 60 seconds.
  - location: core/reference/parameters.md / fast_check
