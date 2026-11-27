# Point, don't paste

Source ID `point-dont-paste`; pattern `glenngillen/point-dont-paste`; Context, rung 3. Give precise relevant context instead of broad exploration or excessive pasted material. Intended detection: model judgement of relevance and use.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Intent

**What it's for.** The person gives the agent precise pointers to what it needs (specific files, symbols, a failing test, a doc) rather than pasting large blobs or telling it to read everything.

**Why it matters.** Broad exploration and long pastes both fill the agent's context with material it does not need, leaving less room for what matters. Naming the right file and test, or pasting the few relevant log lines, gets the agent to the problem faster and keeps it focused, which keeps it sharp and cheap.

**What a recognition shows.** That a request gave the agent the relevant context the work needed, and the agent went straight to it instead of searching.

**Why the rules are drawn this way.**

- **Only requests that needed context.** A standalone script or a general question needs no pointer, so it is neither credit nor a miss ([applicable work](../../reference/principles.md#applicable-work)).
- **Pointers must be relevant and actually used.** A filename in a prompt proves nothing unless the work needed it and the agent read or ran it; crediting mentions alone would reward the wrong thing ([false positives are worse than misses](../../reference/principles.md#false-positives-are-worse-than-misses)). Whether a pointer was relevant is a judgement, so a model makes it ([code checks facts; a model judges the rest](../../reference/principles.md#code-checks-facts-a-model-judges-the-rest)).
- **Relevance, not length, decides.** The problem the pattern addresses is material the agent doesn't need, not size. The five log lines and three-thousand-line paste in the examples illustrate relevance and are not limits, so a large trace the work genuinely needs is not penalized.
- **Broad instructions and excessive pastes are excluded.** "Find the bug somewhere in billing" or a full log when a few lines show the failure are the opposite of the intent.
- **Pointers must come from the person.** Files the agent found through its own search are not the person's act ([human intent only](../../reference/principles.md#human-intent-only)).
- **Forming and Established need the work done from the pointed context.** Seen credits the request; later stages count only requests whose work was completed from it, credited to the week that finished, per a recorded decision ([follow-through](../../reference/principles.md#follow-through)).
- **Continuous is a codebase map in an instruction file.** It points the agent to the right place without the person naming it each time; it holds when sessions go straight to the material, and broad exploration despite the map is a not-holding finding ([prevention](../../reference/principles.md#prevention-when-success-removes-the-signal)).
- **A guided answer needs a real request.** Identifying pointers in a guide counts only once the person uses them in real work ([guided sessions reach Seen only](../../reference/principles.md#guided-sessions-reach-seen-only)).

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable. A [judge prompt](judge.md) is authored but not executed.

## Applicable work

- A person's **request needing codebase or external context**: fixing a bug, changing behaviour in existing code, or diagnosing a failure from logs or docs.
- Requests that need no context (a new standalone script, a general question) are not applicable.
- A window with no such request is **no applicable work**.

## Recognition

**Seen**: the person's request gives **precise, relevant context** and the agent **actually used** it:

- names specific **files, symbols, tests or docs** that are relevant to the work, **or** includes a **concise relevant excerpt** (for example the few log lines that show the failure); and
- the agent's subsequent work actually read and used those pointers (opened the named file, ran or read the named test, worked from the excerpt) **without broad exploration** first.

Completing evidence: the person's request (exact quotation) is the completing event; supporting evidence is the agent's later reads or actions showing the pointers were used. That corroboration can arrive later in the session than the request; how a delayed corroboration is handled at a window boundary is a CLI contract dependency (see [completion windows](../../reference/evidence.md#completion-windows)).

**Not a length rule.** Relevance, not size, decides. The source's five log lines and three-thousand-line paste illustrate relevance; they are not limits. Necessary large evidence (for example a full stack trace the work needs) is not penalized for its size, and a filename in a prompt is not proof of a pointer unless it was relevant and actually used.

## Exclusions

- **Irrelevant file mentions**: a file named in the request that the work did not need or the agent did not use.
- **Broad instructions**: "read the whole repository", "find the bug somewhere in billing".
- **Huge pastes when a small excerpt would suffice**: for example a three-thousand-line log where five lines show the failure.
- Pointers the agent found itself (its own search results) rather than the person giving them.
- A guided answer that identifies pointers without the person then using them in a real request.

## Evidence

- **Cite** the person's request (exact quotation) and at least one agent action showing a pointer was used (a read of the named file, a run of the named test).
- **Attribution**: the request is the person's. For Continuous, the codebase map must be in an instruction file the person or their team maintains, existing and loaded when the session ran.
- **Evidence the pinned CLI does not supply**: linkage from a request's named files, symbols and excerpts to the agent's later reads and tool calls; a measure of exploration (broad search and read activity before relevant work); a relevance judgement for pasted material; historical instruction-file content and load evidence for a codebase map. No command-only approximation (for example counting searches or prompt length) can satisfy this definition.

## Progression

Default [stages](../../reference/progression.md#stages) apply, with [stage-dependent completion](../../reference/progression.md#stage-dependent-completion):

| Stage | For this pattern |
| --- | --- |
| Seen | One request whose relevant pointers the agent actually used. |
| Forming, Established | Instances whose follow-through finished: the work the request asked for was completed from the pointed context. Credited to the week that finished. Established uses [`most`](../../reference/parameters.md#most) of applicable requests. |
| Continuous | The [mechanism](#mechanism) in place, applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is an **instruction-file codebase map**: where the main areas, their tests and relevant docs live.

| Fact | For this pattern |
| --- | --- |
| In place | The map was in an instruction file the person or their team maintains during the window. |
| Applied | Sessions loaded it on requests needing codebase context. |
| Held | Those sessions used the map to go straight to the relevant material rather than explore broadly. |
| Not holding | With the map loaded, sessions still explored broadly for material it pointed to. |
| Untested | The map in place, but no applicable request in a repository it covers. |

## Opportunities and coaching

- **Opportunity**: a request where **avoidable exploration** or an **excessive paste** displaced useful context, for example a vague "somewhere in billing" followed by broad searching, or a three-thousand-line paste for a failure five lines show. It cites the person's request ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) asks the person to name the relevant files and tests, and include only the log lines needed.
- `automate` advice (a codebase map) is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The intended recognizer judges whether a request's pointers were relevant and actually used, and whether exploration was avoidable. The pinned CLI (revision `bdea6f6`) does not execute pack-authored judges and has no block that links a request's named files or excerpts to the agent's later reads. `tool_call_matches` could see a read of a file, but not that the person named it, that it was relevant or that exploration was avoided; enabling on that fragment would substitute a filename heuristic for the definition.

## Missing capabilities

- **Pointer-to-use linkage**: which files, symbols, tests or excerpts in a person's request the agent later read or ran.
- **Exploration evidence**: broad search and read activity before the relevant work, distinguished from targeted reads.
- **Relevance judgement** for named files and pasted material, executed and verified by the CLI.
- **Historical instruction-file content and load evidence** for a codebase map.
- **Delayed-corroboration window handling**: how later-session use is credited to a request near a window boundary.

## Verify before enabling

- A billing rounding-file pointer plus the failing test, both used by the agent, is recognized; "Find the bug somewhere in billing" is rejected.
- Five relevant log lines are recognized; an unnecessary three-thousand-line log paste is rejected; a necessary large trace is not penalized for size.
- A named file unused by the work cannot earn recognition.
- A guided answer identifying pointers without a real request using them does not count.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- How is a request completed in one window credited when the agent's use of its pointers is only visible after the window ends?
  - evidence: The spec says later use corroborates a request-completing event and leaves delayed-evidence handling to the CLI contract.
  - options: Credit the request's window once corroborated; hold the instance pending until corroboration and credit the corroborating window.
  - location: core/patterns/point-dont-paste/definition.md / Recognition
