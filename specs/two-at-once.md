# Two at Once

## Overview

Source ID `two-at-once`; Delegation, rung 6. Use waiting time for independent work in another isolated active session. Detection combines model judgement and timing facts.

## Requirements

- Applies to turns running for several minutes while the person waits; the source supplies no exact duration threshold.
- Seen requires two sessions in separate working copies (as defined in [Isolate the run](isolate-the-run.md)) doing real editing in overlapping minutes, with at least one interactive session.
- Exclude idle overlap, sessions sharing one directory (whatever their branches), and a parent with its own subagent.
- Cite each session's person prompt starting work during the overlap and an edit in each; completion requires the paired evidence.
- Continuous requires an owned command/script starting isolated parallel sessions, used and holding in the window.
- Suggest only after Isolate the run is at least Seen. Guide: select two independent real tasks and have the person run them in isolated sessions.

## Acceptance Criteria

- [ ] Recognize interleaved refactor/fix edits in separate worktrees; reject one working session with one idle.
- [ ] Recognize edits in two repositories during the same minutes; reject sessions ten minutes apart without overlap.
- [ ] A parent session plus its subagent cannot count as two independent main sessions.
- [ ] Guided setup without actual paired active work does not earn Seen.
- [ ] Missing isolation prerequisite suppresses the suggestion.

## Edge Cases

- Session start/end intervals alone overcount idle overlap; edit/turn evidence is required.
- Branch-only separation in a shared directory does not qualify, per the isolation decision in Isolate the run.

## Dependencies

- [Isolate the run](isolate-the-run.md), [pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Paired active turns, environment facts, person prompts and run-scoped prerequisite enforcement.

