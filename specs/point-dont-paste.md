# Point, Don't Paste

## Overview

Source ID `point-dont-paste`; Context, rung 3. Give precise relevant context instead of broad exploration or excessive pasted material. Detection requires model judgement.

## Requirements

- Applies to requests needing codebase or external context.
- Seen requires specific files, symbols, docs or a concise relevant excerpt that the agent actually uses without broad exploration.
- Exclude irrelevant file mentions, instructions to read the whole repository and huge pastes when a small excerpt would suffice.
- Cite the person's request as completion, with supporting evidence that its pointers were used.
- Continuous requires an instruction-file codebase map that sessions use to find relevant material rather than explore broadly.
- Coach when avoidable exploration or an excessive paste displaced useful context. The guide asks the person to name relevant files/tests and include only needed log lines.

## Acceptance Criteria

- [ ] Recognize a billing rounding-file pointer plus the failing test used by the agent; reject “Find the bug somewhere in billing”.
- [ ] Recognize five relevant log lines; reject an unnecessary three-thousand-line log paste.
- [ ] A named file unused by the work cannot earn recognition.
- [ ] A guided answer identifying pointers without the person using them in a request does not count.

## Edge Cases

- The log-line examples illustrate relevance, not universal numeric limits; necessary large evidence must not be penalized solely for size.
- Later use corroborates a request-completing event; delayed-evidence window handling remains a CLI contract dependency.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [coaching content](coaching-content.md), [evaluation readiness](evaluation-readiness.md).
- Relevance/use judgement, exploration evidence and historical instruction maps; no command-only approximation can satisfy these requirements.
