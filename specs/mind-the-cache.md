# Mind the Cache

## Overview

Source ID `mind-the-cache`; Economics, rung 2. Avoid rebuilding large cold contexts after long breaks. Intended detection is a code check.

## Requirements

- Applicable situations involve a gap beyond the cache lifetime and a large previous context. Include the qualifying fresh-start choice in the assessment, not only resumes that miss it.
- Seen requires a fresh start using a handoff or `/clear` after that break instead of continuing the large cold context. Cite timestamps and the fresh start's first prompt as completion.
- Exclude short gaps and small contexts.
- Continuous requires an end-of-day command or Stop mechanism producing a handoff actually used after breaks, applied and holding.
- Coach on large contexts resumed after an hour or more away, using actual measured cost if available. Do not infer extra subscription billing from API-price estimates.
- Guide: before a real long break request a handoff, then start from it afterward.

## Acceptance Criteria

- [ ] Preserve a two-hour gap then fresh NOTES.md handoff as positive, and five-minute resume as outside scope, with compatible cache facts.
- [ ] Recognize an end-of-day handoff used next morning; reject resuming a large 150k-token context after lunch as successful cache management.
- [ ] Guided handoff creation without the later qualifying fresh start is incomplete.
- [ ] Unknown cache lifetime/context size produces no fabricated recognition or cost.

## Edge Cases

- The source's applicability says “sessions resumed” while Seen avoids resuming. This denominator inconsistency needs an explicit future contract.
- Cache lifetime and “large” use `cache_gap` (more than 1 hour) and `large_context_tokens` (150,000) from [pattern parameters](pattern-parameters.md). Both are provisional and tunable.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [hand it off](hand-it-off.md), [evaluation readiness](evaluation-readiness.md).
- Cache/usage facts, fresh/clear/resume provenance, pairing and mechanism use. Existing cold-cache recommendation estimates should be reused where applicable, not dismissed as unavailable.

