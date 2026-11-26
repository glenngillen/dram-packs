# Fan Out

## Overview

Source ID `fan-out`; Delegation, rung 3. Run independent parts through parallel subagents and use their combined work. Detection requires model judgement.

## Requirements

- Applies to work with several independent parts.
- Seen requires a person request for parallel subagents, concurrent execution and use of the combined result.
- Exclude a single subagent and discarded parallel results. Cite the request and used combined result as completion.
- Continuous requires a saved command/workflow causing fan-out in the window, applied and holding.
- Coach when independent repeated work is done serially. The guide asks the person to choose suitable real parts and request one subagent per part, with results brought together.
- Keep safety prerequisites for parallel/autonomous work explicit in advice; do not invent a numeric stage requirement absent from the source.

## Acceptance Criteria

- [ ] Recognize “Use a subagent per service to update the client, then summarise” when concurrent work is used; reject one subagent.
- [ ] Preserve a used `/audit-services` workflow fanning out per service as a mechanism example; reject parallel results thrown away.
- [ ] Sequential subagents do not satisfy concurrency.
- [ ] Guided requests without parallel execution and result use are incomplete.

## Edge Cases

- The source gives no universal number for “several”; at least distinguish one from multiple without fabricating a stronger threshold.
- Independent investigations need not edit files, unlike Two at once's explicit edit requirement.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md), [coaching content](coaching-content.md).
- Concurrent subagent timing, independent-part judgement, result use and workflow provenance.

