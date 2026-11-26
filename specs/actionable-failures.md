# Make Failures Actionable

## Overview

Source ID `actionable-failures`; Checking the work, rung 4. Feed failures back with enough detail for the agent to fix the problem. Intended detection is a code check.

## Requirements

- Applies to repositories with agent-run hooks/checks.
- Seen requires a person-configured hook feeding failure output to the agent and the agent fixing the problem in its next step.
- Exclude failure output never seen by the agent and failures ignored.
- Cite hook configuration, the fed-back failure and the fix as completion.
- Continuous requires hooks/lint rules with actionable fix guidance actually feeding back in the window and holding where applicable.
- Coach on repeated attempts caused by uninformative errors. The guide chooses a real frequently failing check and asks the person to wire actionable feedback into the harness.

## Acceptance Criteria

- [ ] Recognize a lint hook saying “use the shared Button, see components/Button” followed by the replacement; reject a pre-commit failure the agent never saw.
- [ ] Recognize a custom fix-guidance message acted on next turn; reject a fed-back failure ignored.
- [ ] A hook merely writing logs elsewhere cannot establish agent-visible feedback.
- [ ] Guided hook setup without a real failure/fix sequence does not earn recognition.

## Edge Cases

- Source wording alternates “next step” and “next turn”; do not invent a window that makes a delayed unrelated fix count.
- Determining that an edit fixes the named issue needs a reliable relationship, not simply any edit after an error.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Hook execution/status/output records, feedback delivery and fix linkage. Their deterministic contract is unresolved; no new block interface is prescribed here.

