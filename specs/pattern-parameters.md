# Pattern Parameters

## Overview

One table of the tunable defaults that pattern definitions depend on. The user decided that the source's worked examples become provisional defaults, and approved proposed defaults where the source gives no example. Every value is tunable: it is a starting point to calibrate during staff evaluation, not a validated threshold.

## Requirements

- Pattern content refers to these named parameters instead of restating bare numbers, so one change updates every dependent pattern.
- Each parameter is marked **provisional** in pack documentation, with its origin (source example or approved proposal).
- Parameters stay prose in the pack until the current schema accepts them as block parameters. Do not invent schema fields to hold them. Where an implemented block accepts an equivalent parameter, use the value below.
- A default does not enable a detector. Enabling still requires the supporting capability and the evaluation bar in [evaluation readiness](evaluation-readiness.md).
- Unknown inputs (for example unknown context size, missing timestamps or unknown model tier) produce no recognition and no cost claim. A default never substitutes for missing data.

| Parameter | Default | Origin | Used by |
| --- | --- | --- | --- |
| `cache_gap` | Break of more than 1 hour between turns | Source example | [Mind the cache](mind-the-cache.md) |
| `large_context_tokens` | 150,000 tokens of prior context | Source example | [Mind the cache](mind-the-cache.md), [Hand it off](hand-it-off.md) |
| `long_session` | Context over `large_context_tokens`, or any compaction | Approved proposal | [Hand it off](hand-it-off.md) |
| `substantial_work_prompts` | At least 6 person prompts on the prior task before `/clear` | Approved proposal | [Clear between tasks](clear-between-tasks.md) |
| `instruction_cost_share` | Instruction files loading more than 12% of initial context | Source example | [Keep it lean](keep-it-lean.md) |
| `most` | At least 60% of applicable items, with at least 4 applicable items | Source Established threshold, applied consistently | [Give it instructions](give-it-instructions.md), [Save it](save-it.md), [Harness carries it](harness-carries-it.md), [Fix the harness](fix-the-harness.md), [Pattern progression](pattern-progression.md) |
| `fix_followup` | At least 2 later applicable sessions within 14 days of the harness change, with no recurrence | Approved proposal | [Fix the harness](fix-the-harness.md) |
| `routine_work` | Renames, docstrings, formatting, version bumps and simple fixes | Source example list | [Right-size it](right-size-it.md), [Harness carries it](harness-carries-it.md) |
| `many_files_coach` | 10 or more files | Source coach trigger (coaching only, not recognition) | [Script it](script-it.md) |
| `handoff_pairing` | Previous main session in the same repository ending within 24 hours | Source | [Hand it off](hand-it-off.md) |
| `unattended_gap` | Headless, or 15 minutes or more of agent work without a person prompt | Source | [Pattern evidence](pattern-evidence.md) |
| `kept_window` | 14 days in the default branch | Source | [Outcome content](outcome-content.md) |
| `several_parallel` | 3 or more independent parts run in parallel | Approved proposal | [Fan out](fan-out.md) |
| `long_turn` | Agent turn running 5 minutes or more while the person waits | Approved proposal | [Two at once](two-at-once.md) |
| `fast_check` | Per-step check usually finishing within 60 seconds | Approved proposal | [Gate each step](gate-each-step.md) |

- “Non-trivial” instruction files in [Give it instructions](give-it-instructions.md) still have no value; it stays unresolved and keeps that detection disabled.

## Acceptance Criteria

- [ ] Every parameter above appears once in pack documentation, labelled provisional, with its origin.
- [ ] Dependent pattern content links to the parameter rather than hard-coding a different value.
- [ ] A five-minute gap or a 40k-token context is outside Mind the cache's applicable work; a two-hour gap after 150k tokens is inside.
- [ ] A `/clear` after 3 person prompts is not "after substantial work"; a `/clear` after 6 is.
- [ ] Fix the harness is not recognized when only one later applicable session exists, or when the correction recurs within 14 days.
- [ ] "Most" with 3 applicable items cannot be met; 3 of 5 (60%) can.
- [ ] No parameter is reported as validated or calibrated before staff evaluation measures it.

## Edge Cases

- Exactly at a boundary (exactly 1 hour, exactly 150,000 tokens, exactly 60%): the gap and token thresholds are strict "more than"; the coverage threshold is inclusive "at least".
- A model whose cache lifetime is known to differ from 1 hour: use the known lifetime only if the CLI supplies it as a fact; otherwise use the default.
- Work outside the routine example list is not automatically non-routine; classification beyond the list is a judgement the model-judged recognizer must justify with evidence.
- Fewer than 4 applicable items: "most" is not assessable, which is not a miss.

## Dependencies

- User decisions recorded in [requirements evidence](requirements-evidence.md).
- CLI facts for context size, compaction, timestamps, model tiers and configuration history.
