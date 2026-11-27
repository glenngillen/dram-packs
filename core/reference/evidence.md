# Evidence contract

Every pattern in `glenngillen/core` links here instead of restating these rules. They say what evidence a recognition, an opportunity or a held mechanism must rest on. They are **requirements on a future recognizer**, not a description of what the pinned Dram CLI does today: no pattern in this pack is enabled, and none of these rules is enforced by pack data. The CLI keeps its own invariants (quoted verbatim, authored by the person, inside the window); a pack cannot loosen them.

Source: the pattern-evidence requirements and the user decisions recorded in this repository's `specs/` (`pattern-evidence.md`, `requirements-evidence.md`). Those files are not part of the installed pack, so they are named rather than linked.

## What counts as the person's work

- **The person's deliberate action counts, and so does a harness the person or their team owns.** Spontaneous agent behaviour, an automatic fallback and Dram's own analysis sessions never earn recognition.
- **An agent-proposed plan, check or rule counts only with the person's evidenced review** of it (an approving, editing or rejecting prompt that refers to it).
- **Main sessions exclude subagents and sidechains.** A subagent's turn is evidence about delegation, never a main-session person prompt.
- **Person prompts exclude** tool results, hook output, command output and compaction summaries, even when the transcript stores them with a user role.
- **Harness records need attribution** to the person or their team's configuration: user-level or repository settings, hooks, commands, skills, instruction files or CI they maintain. Built-ins, plugin defaults and third-party tools do not establish ownership on their own.

## Attribution and citations

A verified recognition requires all of:

1. evidence IDs that exist in the supplied packet;
2. exact quotations wherever a quote is used (a changed quote is rejected, not repaired);
3. at least one attributable, person-authored citation; configuration evidence can supply attribution where the pattern says so;
4. completion inside the analysis window, in the person's local time (see [completion windows](#completion-windows)).

The pack-wide rejection scenarios for these rules (fabricated citation, changed quote, agent-only recognition or opportunity, out-of-window completion and more) are in [verification scenarios](verification.md). None can run at the pinned CLI; each is kept as unevaluable.

Pending: whether a held case must also cite the configuration that produced it. Do not weaken invariant 3 to make an example pass while this is open.

## Opportunities

An opportunity is a **missed applicable moment**: work the pattern applied to, where the person did not take the step, recorded with the problem that followed and the action that would have helped.

- **Opportunities follow the same citation rule as recognitions** (user decision, overriding the source's exemption). Each cites at least one attributable person-authored moment, such as the prompt that started the work or accepted a false claim. An opportunity backed only by agent or tool output is not reported.
- **Never infer an opportunity from missing data.** Absent, excluded, truncated or unanalysed evidence is [insufficient](#insufficient-evidence), not a miss.
- **A disabled detector never implies the person failed to follow its pattern.** Nothing in this pack reports an opportunity while its pattern is disabled.

## Completion windows

- The **initiating act** (a brief sent, a challenge issued, a review requested) and its **follow-through** (the response addressed, findings acted on, change kept) can fall in different windows. Keep both timestamps; do not silently credit a later result to the earlier window.
- What each stage counts is set by the [stage-dependent completion](progression.md#stage-dependent-completion) rule.
- Window boundaries use the person's local time. A completion outside the window is rejected for that window.
- An **unattended run** is a headless run, or an interactive run with continued agent work for at least [`unattended_gap`](parameters.md#unattended_gap) without a person prompt. A launch by software acting on its own behalf is not automatically person-authored work.

### Cross-session evidence

Some patterns need evidence from more than one session. These pairings are prose; the pinned CLI has no block that expresses them.

| Pattern | Pairing |
| --- | --- |
| Hand it off | The previous main session in the same repository ending within [`handoff_pairing`](parameters.md#handoff_pairing) of the new session; source proposal: its last three turns and the new session's first two. |
| Two at once | Active, overlapping turns in two separately isolated sessions. |
| Fix the harness | A recurring correction, the harness change that addresses it, and later relevant sessions ([`fix_followup`](parameters.md#fix_followup)). |

Instruction rules must have **existed and applied when the session ran**. Current configuration alone cannot prove historical behaviour, and a file's modification time alone does not prove a substantive change or historical loading.

## Mechanisms: in place, applied, held

A mechanism is configuration that makes the pattern happen without the person (a hook, a rule, a permission, an owned command, CI). Continuous rests on three separate facts:

| Fact | Meaning | Not enough on its own |
| --- | --- | --- |
| **In place** | The configuration existed, attributable to the person or their team, during the window. | A file that exists today. |
| **Applied** | Applicable work happened while it was in place and the mechanism actually engaged (loaded, fired, ran). | A configured but unused mechanism is **untested**, not held. |
| **Held** | On that applicable work, the outcome the mechanism exists for occurred. | A quiet session with no applicable work. |

**Not holding**: the behaviour the mechanism should prevent recurred while it was in place and applied. That is a distinct result, not a miss by the person.

Before/after comparisons use **applicable later work**, never silence in unrelated sessions.

## Privacy

- **Case content stays on the person's machine**: the work, date, repository, a readable request excerpt, the decisive moment, the result where known, case-specific advice and a reference to open the session. Pack copy supplies templates and intent, never fabricated personal detail.
- **Input text is evidence, never instructions** to the judge. Text inside a transcript that asks the judge to do something is quoted evidence only.
- A pack cannot remove redaction, verification, privacy controls, budgets or the no-tools model boundary.
- **No real session histories, personal configuration, repository-specific customer detail or secrets** are committed to this repository. Fixtures and scenarios are invented, deterministic data; guides use only the person's own real work, on their machine.

## Insufficient evidence

These are **insufficient**, never a miss and never a positive claim:

- excluded, unanalysed or truncated evidence;
- unavailable facts (unknown context size, missing timestamps, unknown model tier, unknown configuration history);
- fewer applicable items than a threshold needs (for example, under four for [`most`](parameters.md#most));
- a pattern that is disabled or whose detection the build cannot run.

The person sees them as unassessed. A default parameter never stands in for missing data.

## Open questions

- Must a held case cite the originating configuration as well as the agent output that shows the mechanism engaged?
  - evidence: The source's held examples cite agent output without the configuration; the evidence spec leaves this pending.
  - options: Require a configuration citation for held cases; accept agent output plus separately verified configuration facts.
  - location: core/reference/evidence.md / Attribution and citations
