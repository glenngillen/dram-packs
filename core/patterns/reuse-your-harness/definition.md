# Reuse your harness

Source ID `reuse-your-harness`; pattern `glenngillen/reuse-your-harness`; Guides, rung 6. Recognize the person's maintained harness following them across repositories. Intended detection: a code check.

Shared rules: [evidence](../../reference/evidence.md), [parameters](../../reference/parameters.md), [progression](../../reference/progression.md), [authoring and readiness](../../reference/authoring.md). This file states only what is specific to this pattern.

## Status

**Disabled** (`enabled: false`). Readiness: authored; structurally valid on the pinned CLI; **not evaluable**. Every case in `eval/cases.jsonl` is reported unevaluable.

## Applicable work

- The person worked in **at least two repositories** in the window (their main sessions; [evidence](../../reference/evidence.md#what-counts-as-the-persons-work)).
- One repository in the window is **no applicable work**: nothing is reported, not a miss.

## Recognition

**Seen**: the **same owned** command, skill, hook or rule was **used in at least two repositories**, shared through:

- the person's **user configuration**;
- **their own plugin** (one they wrote and maintain); or
- a **template** they or their team maintain, from which the repositories take the identical item.

Completing evidence: the item's ownership, the common configuration it comes from, and its use (invoked, fired or loaded) in each of the repositories. Sharing is never inferred **solely from matching filenames**.

## Exclusions

- **Diverged copies**: the same-named command defined separately in each repository with differing content. That is the problem this pattern coaches on.
- **Built-in commands and third-party plugins** the person did not build, such as a marketplace plugin. Using one everywhere does not make it their harness.
- A shared item **in place but unused** in at least one of the two repositories.
- A **single repository**, however much harness it has.
- A guided relocation into user configuration without later use in two repositories.

## Evidence

- **Cite** ownership (the user configuration, the person's plugin or the template), the common configuration identity, and usage records in each repository.
- **Attribution**: user configuration, a plugin whose authorship is the person's or their team's, or a template they maintain. Team ownership and template identity need attributable facts; the person is never claimed as the author of a third-party dependency.
- **Historical**: the shared item must have existed and applied when each session ran.
- **Evidence the pinned CLI does not supply**: configuration identity and provenance (user, own plugin, template, third-party); per-repository use of a given command, skill, hook or rule; configuration history for the four-week update; content comparison between copies.

## Progression

Default [stages](../../reference/progression.md#stages), with this pattern's coverage qualification for Continuous:

| Stage | For this pattern |
| --- | --- |
| Seen | One owned item used in two or more repositories. |
| Forming, Established | Default thresholds over repositories worked in. Established uses [`most`](../../reference/parameters.md#most); fewer than four applicable repositories is not assessable, not a miss. |
| Continuous | The maintained harness applies to **every** repository worked in, was **updated in the last four weeks**, **and** the [mechanism](#mechanism) applied and holding. |

A guided session establishes Seen only ([guided sessions](../../reference/progression.md#guided-sessions)).

## Mechanism

The mechanism is the person's maintained, shared harness: user configuration, their own plugin or their template.

| Fact | For this pattern |
| --- | --- |
| In place | The shared configuration existed during the window, attributable to the person or their team. |
| Applied | Its items were used in the repositories the person worked in. |
| Held | It applied to every repository worked in and was updated in the last four weeks. |
| Not holding | A repository worked in ran without it while it was in place, or a separate diverged copy replaced it there. |
| Untested | In place, but the person worked in fewer than two repositories, or its items were not used. |

**Stale** is distinct from not holding: a shared harness used everywhere but not updated in the last four weeks still earns Seen, not Continuous. What counts as "updated" needs confirmation ([open questions](#open-questions)).

## Opportunities and coaching

- **Opportunity**: duplicate, separately defined commands or hooks across the person's repositories, citing a person-authored moment such as the person invoking each copy ([opportunities](../../reference/evidence.md#opportunities)).
- **Coaching**: the [guide](guide.md) identifies one of the person's own duplicates and has them move one copy into user configuration.
- `automate` advice is offered only after the [automation gate](../../reference/progression.md#automation-gate).

## Why disabled

The pinned CLI (revision `bdea6f6`) has no configuration identity, provenance or cross-repository usage facts, and its fixed-pattern check interface cannot see them. Recognizing sharing from matching filenames would count diverged copies and third-party plugins, which the definition excludes.

## Missing capabilities

- **Configuration identity**: whether two repositories use the same item rather than copies, and whether copies are equivalent.
- **Provenance**: user configuration, the person's own plugin, a maintained template, or third-party.
- **Cross-repository usage**: per-repository records that the item was invoked, fired or loaded.
- **Configuration history**: content over time, for historical application and the four-week update.
- **A runnable check**: `tool_call_matches` and `tool_call_sequence` cannot express any of these.

## Verify before enabling

- A user-level PR-description command used across three repositories is recognized; three diverging copies are rejected.
- The person's own maintained plugin with hooks used across their repositories is recognized; a marketplace plugin they did not write is rejected.
- A single repository, or a shared file unused in the second repository, does not establish the pattern.
- Guided relocation without use across two repositories does not yet meet Seen.
- Every case in `eval/cases.jsonl` runs (none unevaluable) and passes on the enabling CLI build.

## Open questions

- When are separately stored copies the "same" item rather than diverged copies?
  - evidence: The spec says equality or semantic equivalence of independently copied configuration needs confirmation before activation.
  - options: Byte-identical content only; identical after whitespace normalization; template-derived with a recorded template identity.
  - location: core/patterns/reuse-your-harness/definition.md / Recognition
- What counts as "updated in the last four weeks" for a shared harness?
  - evidence: The source requires an update for Continuous without defining it; modification time alone does not prove a substantive change.
  - options: Any content change by the person; a change adding or revising an item; a reviewed change.
  - location: core/patterns/reuse-your-harness/definition.md / Mechanism
