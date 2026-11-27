# Save it

Source ID `save-it`; pattern `glenngillen/save-it`; Guides, rung 4. Turn repeated requests into the person's own reusable command or skill. Intended detection: model similarity judgement combined with ownership and run checks.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. [`judge.md`](judge.md) is authoring prose for the similarity judgement; the pinned CLI does not execute it.

## Applicable work

- A **repeated request**: a person prompt that repeats, nearly word-for-word, a request the person made in **at least two sessions** (main sessions only; [evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- "Nearly word-for-word" means the **same intent with substantially the same wording**, decided by model judgement with both prompts quoted. The pack defines **no similarity score**; none is invented here.
- Prompts that only share a topic ("fix the tests" on different failures) are not repeated requests.
- A window with no repeated request is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen**: in the window, the person

1. has a **new, person-owned** command or skill (for example `.claude/commands/pr-description.md`, or a hand-written skill) that captures a repeated request; and
2. **invoked it themselves** (for example typing `/pr-description`), and
3. the run **completed**.

Completing evidence: the person's invocation and the completed run. The saved file's existence is context, not completion.

"New" and the saved command's applicability (which earlier requests it replaces) need precise future semantics ([open questions](#open-questions)). A first-run fact can help show it is new, but a signal that counts **any** skill's first use cannot establish ownership or intention.

## Exclusions

- **Built-in or plugin commands**, for example built-in `/review`, or a marketplace plugin's command. They are not the person's own. (Second opinion may still count a built-in review; that is that pattern's rule, not this one's.)
- A command or skill **saved but never invoked** in the window.
- A skill the **agent invoked unasked**. The person's choice to run it is required; agent-only invocation never substitutes.
- A command invoked but whose run did not complete (aborted, errored before doing the work).
- A guided session where the person answered the guide's questions but saved or ran nothing.

## Evidence

- **Cite** the person-authored invocation (exact quote) and the completed run; for the applicable work, cite at least two earlier person prompts repeating the request (exact quotes, different sessions).
- **Attribution**: the command or skill file is in the person's user configuration or a repository they or their team maintain, and was created or substantially written by them (or written by their agent at their request and reviewed). Built-ins and third-party plugins never establish ownership.
- **Historical**: the command must have existed when it was invoked; today's command directory does not prove an earlier run.
- **Evidence the pinned CLI does not supply**: command and skill provenance (owned, built-in, plugin); first-use history; who invoked a command (person or agent); run completion; grouping of near-identical prompts across sessions.

## Progression

Draft overrides of the [stages](../../reference/progression.md#pattern-specific-overrides):

| Stage | For this pattern |
| --- | --- |
| Seen | One new owned command or skill, invoked by the person, run completed. |
| Forming | **Another run on a different day** in the person's local time. A second run on the same day does not meet it. |
| Established | [`most`](../../reference/parameters.md#most) repeated requests in the window used a saved version. Fewer than four repeated requests: not assessable, not a miss. |
| Continuous | **No request manually repeated across three or more sessions** without a saved version, **and** the [mechanism](#mechanism) applied and holding. Coverage alone is not enough. |

Forming and Established count only completed runs, each credited to the week the run finished ([stage-dependent completion](../../reference/progression.md#stage-dependent-completion)). A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the person's library of saved commands and skills, used in place of retyping.

| Fact | For this pattern |
| --- | --- |
| In place | Owned commands or skills existed during the window, attributable to the person or their team. |
| Applied | The person invoked them on repeated requests in the window. |
| Held | Repeated requests went through saved versions; none was typed by hand across three or more sessions. |
| Not holding | A request was retyped across three or more sessions while a saved version existed, or with no saved version. |
| Untested | Saved commands in place but no repeated request and no invocation in the window. |

## Opportunities and coaching

- **Opportunity**: a request repeated nearly word-for-word across sessions with no saved version. It cites the person's repeated prompts ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) uses the person's real repeated requests to make the repetition visible, asks them to request a saved command, then has them run it on another real case.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The definition needs a model judgement of near-identical intent across sessions plus facts the pinned CLI (revision `bdea6f6`) does not supply: who owns a command, whether it is new, and whether the person or the agent invoked it. Recognizing it from "a skill ran" would count built-ins and agent-invoked skills, a weaker definition the pack must not ship.

## Missing capabilities

- **Cross-session prompt grouping**: person prompts across main sessions with a model judgement of near-identical intent, citing both prompts.
- **Command/skill provenance**: owned (user or repository), built-in, or plugin; created by the person or reviewed by them.
- **First-use history**: when an owned command or skill first existed and first ran.
- **Invocation attribution**: whether the person typed the invocation or the agent chose to invoke a skill.
- **Run completion**: the invoked command's run finished.
- **A runnable judge and checks**: the pinned build runs only `tool_call_matches` and `tool_call_sequence`; neither expresses ownership, invocation by the person or similarity.

## Verify before enabling

- A new `.claude/commands/pr-description.md` followed by the person typing `/pr-description` is recognized; built-in `/review` is rejected.
- A hand-written skill first run in the window is recognized; creation without execution is rejected.
- A skill the agent invoked unasked is rejected.
- Guide questions answered without saving and using a command earn nothing; guided completion earns Seen only.
- A second run on the same day does not meet Forming; a run on a different day does.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- What makes a saved command "new" for Seen, and which earlier requests does it count as replacing?
  - evidence: The source says "a new person-owned command" without defining new (created in the window, first run in the window, or first run ever); the spec leaves it for future semantics.
  - options: First invocation in the window of a command created in the window; first invocation ever of an owned command; model judgement linking the command to cited repeated requests.
  - location: core/patterns/save-it/definition.md / Recognition
