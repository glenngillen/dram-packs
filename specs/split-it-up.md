# Split It Up

## Overview

Source ID `split-it-up`; Delegation, rung 2. Delegate a side task intentionally. Detection combines model judgement with agent provenance.

## Requirements

- Applies to sessions breaking off to a side task and returning.
- Seen requires a subagent start requested by the person or use of a subagent the person defined.
- Exclude spontaneous built-in/plugin subagents and requests with no actual delegation.
- Cite the request or own-agent definition and the subagent start as completion.
- Continuous requires the person's own subagents invoked through instruction rules in the window, applied and holding.
- Coach on a main session taking a distracting side task. The guide asks for an actual side task and prompts delegation.

## Acceptance Criteria

- [ ] Recognize “Use a subagent to update the snapshots” followed by a Task call; reject spontaneous built-in Explore.
- [ ] Recognize the agent choosing the person's own `test-writer`; reject “Do these in parallel” with no subagent start.
- [ ] A plugin agent without the person's delegation request cannot earn ownership credit.
- [ ] Guided delegation advice without actual invocation earns nothing.

## Edge Cases

- Unlike an unsolicited built-in agent, selecting a person-defined agent can count because its definition expresses intent.
- Subagent histories are not independent main sessions for progression.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Own/built-in/plugin provenance, attributable request recognition and parent-child session linkage. Task-call presence alone is insufficient.

