# Gate each step

Source ID `gate-each-step`; pattern `glenngillen/gate-each-step`; Checking the work, rung 6. Catch issues through fast checks after edits or before commits. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [outcomes](../../reference/outcomes.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** Fast checks run and block at each step (after an edit, before a commit), so problems are caught where they're cheapest.

**Why it matters.** A type or lint error found at the end means unpicking several steps of work built on it. A fast check after each edit sends the problem back while the agent is still on that change. It keeps quality as early as possible, ahead of the final gate in [Gate "done"](../gate-done/definition.md).

**What a recognition shows.** That a step gate the person or their team configured, running a fast check, actually stopped a step or returned a problem to the agent during real work.

**Why the rules are drawn this way.**

- **Fast checks only.** A check that usually finishes within 60 seconds tries to capture "quick enough to run at every step"; the boundary comes from a recorded decision and is a [calibration point](../../reference/principles.md#thresholds-are-calibration-points). A slower check may still count as a final gate.
- **The gate must be owned.** The agent running a linter on its own is not a gate ([human intent only](../../reference/principles.md#human-intent-only)). Configuration and runs are facts, so code checks them ([code checks facts; a model judges the rest](../../reference/principles.md#code-checks-facts-a-model-judges-the-rest)).
- **It must block or feed back at least once.** The intent is catching problems at the step; a run that passed shows execution, not a catch, so quiet runs are not Seen ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)).
- **Formatters, end-only checks and never-fired hooks are excluded.** A formatter rewrites rather than gates; a check run only at the end is Gate "done"; a hook that never fired has done nothing yet.
- **Always-bypassed checks are excluded, not untested.** A commit made with `--no-verify` is evidence the gate did not run, never that it passed.
- **The fix is not required here.** What the agent does with the feedback belongs to [Make failures actionable](../actionable-failures/definition.md); this pattern needs only the block or feedback, and invents no window for a fix.
- **Established is measured against defects introduced at a step.** A defect caught at its step counts; one found only later is a miss; quiet passing runs are neither ([applicable work](../../reference/principles.md#applicable-work)).
- **Continuous needs every applicable repository covered and the gate holding.** Coverage alone is not enough: it must fire, and what it caught must be fixed at that step ([stages](../../reference/principles.md#stages)).
- **A guided setup reaches Seen only once it blocks or feeds back on real work** ([guided sessions reach Seen only](../../reference/principles.md#guided-sessions-reach-seen-only)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. Named as one of the first activation candidates; it still needs the capabilities below.

## Applicable work

- A **repository with fast type, lint or unit checks**: a check that usually finishes within [`fast_check`](../../reference/parameters.md#fast_check) (provisional: 60 seconds), where the agent edits or commits in the person's main sessions in the window.
- A window with no such repository is **no applicable work**: nothing is reported, not a miss.
- **"Fast" boundary**: a check that usually takes longer than `fast_check` is not this pattern's fast gate. It may still count toward [Gate "done"](../gate-done/definition.md) as a final gate. How "usually" is measured is not yet specified.

## Recognition

**Seen** requires all of:

1. **An owned step gate**: a PreToolUse or PostToolUse hook, or a pre-commit check, that the person or their team configured, running a type check, linter or unit checks (for example a PostToolUse `tsc --noEmit`, or a pre-commit linter).
2. **It fired** during agent work: after an edit, before a tool action, or on a commit the agent made.
3. **It blocked or fed back at least once**: it stopped the step (for example rejected the commit) or returned the problem to the agent (for example a type error after an edit).

Completing evidence: the attributable configuration and the relevant run that blocked or fed back.

**Quiet runs** (the check fired and passed) establish execution but are not Seen: the Seen definition specifically requires a blocking or feedback instance.

**Next step versus next turn**: when the gate feeds back, what the agent does next belongs to Make failures actionable. This pattern needs the block or feedback itself; it does not require the fix to follow in a particular step or turn, and does not invent a window for one.

## Exclusions

- **Formatter-only hooks** (for example a PostToolUse hook running only a code formatter): they rewrite, they do not gate.
- **Never-fired hooks**: configured but no run during agent work.
- **Pre-commit checks always bypassed**: for example every agent commit made with `--no-verify`, so the check never runs. A configured but always-bypassed check is excluded, not untested.
- **The agent running a linter on its own** with no owned configuration: spontaneous agent behaviour, not a gate.
- **Guided hook creation without an actual feedback or block event**.
- **Checks run only at the end** of the task (that is Gate "done", not a per-step gate).

## Evidence

- **Cite** the attributable configuration (hook or pre-commit) and the run that blocked or fed back, with its output as recorded. Person-authored attribution comes from the person's configuration where the [evidence contract](../../reference/evidence.md#attribution-and-citations) allows, plus the person's prompt that started the work.
- **Historical**: the configuration must have existed when the session ran.
- **Bypass detection**: a commit made with `--no-verify` or an equivalent skip is evidence the gate did not run, not that it passed.
- **Evidence the pinned CLI does not supply**: hook and pre-commit run results (event, command, exit status, output, duration); bypass flags; check classification (type, lint, unit test or formatter); configuration attribution and history; repository coverage.

## Progression

Uses the default [stages](../../reference/progression.md#stages) with a coverage qualification for Continuous ([pattern-specific overrides](../../reference/progression.md#pattern-specific-overrides)):

| Stage | For this pattern |
| --- | --- |
| Seen | One owned step gate that fired and blocked or fed back. |
| Forming | Blocking or feedback instances in at least two distinct weeks of the last four. |
| Established | Qualifying blocking or feedback instances on at least 60% of applicable cases, with at least four applicable cases ([`most`](../../reference/parameters.md#most)). An applicable case is a step at which the agent introduced a type, lint or unit-check defect in an applicable repository; it counts when the owned step gate blocked it or fed it back at that step, and as a miss when the defect was found only later. Quiet passing runs are neither qualifying instances nor applicable cases. |
| Continuous | Step-gate coverage of **every** applicable repository and actual firing in the window, **and** the [mechanism](#mechanism) holding. |

A guided setup establishes Seen only once it actually blocks or feeds back on real work ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the step gate itself.

| Fact | For this pattern |
| --- | --- |
| In place | The owned hook or pre-commit check existed during the window, covering the repository. |
| Applied | It fired on agent edits or commits in an applicable session (not bypassed). |
| Held | Every applicable repository is covered, it fired in the window, and problems it caught were fixed at that step. |
| Not holding | It was bypassed, did not fire on agent edits or commits, or a type or lint defect it should have caught was found only at the end. |
| Untested | Configured but never fired on agent work in the window. |

## Opportunities and coaching

- **Opportunity**: in an applicable repository, an early type or lint defect was found only at the end (by the final check, CI or the person). It cites the person-authored moment, such as the prompt reporting the defect or starting the work ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) asks for an edit-time type check that the person's actual harness supports.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate), and never removes the final gate.

## Why disabled

The pinned CLI (revision `bdea6f6`) runs only `tool_call_matches` and `tool_call_sequence`. Matching `tsc` or a lint command in tool calls would accept the agent running checks by choice, formatter runs and quiet passes, and cannot see hook runs, pre-commit results or `--no-verify` bypasses. Hook presence alone would accept never-fired gates. Either would substitute a weaker definition.

## Missing capabilities

- **Hook and pre-commit run records**: event (PreToolUse, PostToolUse, pre-commit), command, exit status, output and duration.
- **Blocking and feedback**: whether a run stopped the step or returned output to the agent.
- **Bypass detection**: commits made with `--no-verify` or equivalent.
- **Check classification**: type check, lint or unit tests versus formatter-only, and its usual duration against `fast_check`.
- **Configuration attribution, history and repository coverage**.
- **Mechanism evaluation**: nothing reaches the `continuous` stage in the pinned build.

## Verify before enabling

- A PostToolUse `tsc --noEmit` check blocking after an edit is recognized; a pre-commit always run with `--no-verify` is rejected.
- A pre-commit linter blocking a commit is recognized; formatter-only hooks are rejected.
- A configured but unused gate remains untested.
- Guided hook creation without an actual feedback or block event does not earn Seen.
- Quiet passing runs are reported as execution, not as Seen.
- A check slower than `fast_check` is not recognized here (and is left for Gate "done").
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- How is "usually finishing within 60 seconds" measured for `fast_check`?
  - evidence: The parameter is provisional and says only "usually"; no sample size or statistic is given.
  - options: Median duration over the window's runs; a stated proportion of runs under 60 seconds; the configured timeout.
  - location: core/patterns/gate-each-step/definition.md / Applicable work
