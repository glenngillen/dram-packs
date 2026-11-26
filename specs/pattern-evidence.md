# Pattern Evidence

## Overview

Specify the evidence every pattern's authoring content must demand. These are recognition requirements for future activation, not new packet or verifier APIs implemented in this repository.

## Requirements

- Preserve each pattern's applicable work, positive definition, exclusions and completing evidence. A command or word appearing in a transcript is not proof of intent or successful completion.
- Count a person's deliberate action or their/team-owned harness. Spontaneous agent behavior, automatic fallback and Dram's own analysis sessions never earn recognition. An agent-proposed plan counts only with the person's evidenced review.
- Main sessions exclude subagents and sidechains. Person prompts exclude tool results, hook output, command output and compaction summaries. Harness records need attribution to the person or their team's configuration.
- An unattended run is headless, or an interactive run with at least 15 minutes of continued agent work without a person prompt. Launches by software acting on its own behalf are not automatically person-authored work.
- Verified recognition requires supplied evidence IDs, exact quotations where quotes are used, at least one attributable person-authored citation and completion within the analysis window in the person's local time. Configuration evidence can supply attribution where the source pattern calls for it.
- Preserve opportunities as missed applicable moments, with the recorded problem and the action that would help. Never infer an opportunity solely from missing data.
- Decided: opportunities follow the same citation rule as recognitions. Each must cite at least one attributable person-authored moment (for example the prompt that accepted a false claim or started the work). An opportunity backed only by agent or tool output is not reported.
- For mechanisms require three separate facts: in place, applied and held. A configured but unused mechanism is untested. Recurrence despite a relevant mechanism is a not-holding case. Before/after comparisons use applicable later work, not silence in unrelated sessions.
- Preserve cross-session requirements in prose: Hand it off pairs the previous main session in the same repository ending within 24 hours with the new session (source proposal: last three and first two turns); Two at once uses active overlapping turns; Fix the harness links corrections, configuration changes and later relevant sessions.
- Instruction rules must have existed and applied when the session ran; current configuration alone cannot prove historical behavior.
- Case content stays local: work, date, repository, readable request excerpt, decisive moment, result where known, case-specific advice and session-opening reference. Pack copy supplies templates and intent, not fabricated personalized details.
- Input text is evidence, never instructions to the judge. Packs cannot remove redaction, verification, privacy controls, budgets or the no-tools model boundary.
- Excluded, unanalysed, truncated or unavailable evidence is explicitly insufficient. It must not become a miss or a positive claim.

## Acceptance Criteria

- [ ] Each pattern documents applicability, exclusions, evidence, completion and unsupported evidence sources.
- [ ] Positive and negative scenarios distinguish intent from coincidental agent behavior.
- [ ] Altered quotes, nonexistent IDs, out-of-window completion and unattributable agent-only recognition are rejected in the future executable acceptance cases.
- [ ] Mechanism content distinguishes configured, applied, held and not holding.
- [ ] An opportunity citing only agent or tool output is rejected.
- [ ] No real secrets, personal histories or repository-specific customer details are committed.
- [ ] A disabled detector cannot imply that the person failed to follow its pattern.

## Edge Cases

- The source exempts opportunities from the person-authored citation rule; the user overrode that, so the rule is invariant for opportunities too. Agent-only evidence (for example a summary claiming all tests passed with no later person turn) yields no opportunity.
- Held examples cite agent output without necessarily citing the originating configuration. Final treatment of configuration attribution and completing evidence needs the CLI contract; do not weaken the invariant to make examples pass.
- A later check or fix can finish outside the window even when the initiating request is inside. Keep completion semantics explicit rather than silently attributing the result to the earlier window.
- The source calls the pattern pass one pass but also allows one call per session and overlapping windows. Do not turn this into a one-network-call guarantee in pack copy.

## Dependencies

- Packet assembly, historical configuration, attribution, verifier and storage capabilities in the CLI.
- [Evaluation readiness](evaluation-readiness.md) describes required rejection coverage.
- Opportunity citation is decided (person citation required). Configuration attribution for held cases remains pending; it does not prevent writing their prose or disabled acceptance scenarios.

