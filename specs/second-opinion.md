# Second Opinion

## Overview

Source ID `second-opinion`; Checking the work, rung 8. Obtain and use an independent review before accepting a change. Detection combines model judgement with review provenance.

## Requirements

- Applies to changes committed or opened as a pull request.
- Seen requires an independent review requested/run by the person and its findings acted on, or an evidenced clean result accepted.
- Allow an own review agent/command, `/review`, a different model or a fresh reviewer session that did not write the code.
- Exclude asking the implementing session “is this right?” and ignored findings.
- Cite the review request and result as source completion, retaining the follow-through needed to prove it was used.
- Continuous requires automated review by a hook, CI or PR mechanism actually running and holding on the person's changes.
- Coach on unreviewed merges needing fix-ups. The guide has the person request independent review of their next real diff.

## Acceptance Criteria

- [ ] Recognize `@agent-reviewer` review followed by two fixes; reject “Looks right to you?” in the implementing session.
- [ ] Recognize a fresh session reviewing the branch for bugs and using the result; reject findings ignored.
- [ ] Built-in review can count here despite built-ins being excluded from Save it; preserve pattern-specific rules.
- [ ] Guided review requests without independent execution/result use do not count.

## Edge Cases

- A different name does not prove an independent reviewer; provenance must show it did not implement the change.
- Decided by [stage-dependent completion](pattern-progression.md#stage-dependent-completion): Seen completes on the review request with its result; Forming and Established count only reviews whose findings were acted on, credited to the week that action finished.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md).
- Reviewer provenance, change linkage, substantive response recognition and automated review run evidence.

