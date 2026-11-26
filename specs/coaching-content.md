# Coaching Content

## Overview

Provide useful, faithful wording and one guide per pattern, ready for the hosts that can render or launch it.

## Requirements

- Each pattern supplies its display name, summary, applicability, recognition explanation, next step, advice, automation explanation where applicable, and a guide. Runtime copy uses only current schema fields; additional explanatory content stays in Markdown.
- Copy describes behavior and evidence. It never scores the person, implies unsupported detection is working, invents counts, claims official trust, or guarantees savings.
- A preview note describes provisional status; disabled content additionally says detection is unavailable. Do not equate preview with having passed an evaluation when it has not.
- Every guide works on a real task in the person's own project. It asks and explains; it performs no pattern action, creates no sample repository and changes no settings unless the person asks their agent to do so.
- Guides include the positive completion step that would earn Seen and a clear non-completion branch. Merely answering coaching questions does not count. Explain when detection is disabled so completing a guide does not promise an immediate recognition.
- Save it's repetition exercise uses real existing tasks selected by the person, never manufactured code. If no appropriate task exists, stop without claiming the pattern was done.
- Provide an incremental next action and, where the pattern supports it, a prompt for the preventive mechanism. Do not present generic text as a personalized case. Case-specific substitution belongs to the host and requires evidence.
- Preserve safety dependencies in autonomy guides: Hands off requires scoped unattended permissions; Two at once requires isolation; broader autonomy requires the relevant Safety mechanisms. Do not recommend permission bypass as a shortcut.
- Fix prompts ask for the person's intended change; they cannot replace the CLI's safety wrapper. Avoid destructive copy-paste commands or a blanket instruction to approve all permissions.
- No live moments, featured focus, announcements or milestones are activated merely to show catalogue coverage. Their behavior depends on host support, evaluation and separate product decisions.
- Use `dram` in current usage instructions. Historical source names remain only in clearly marked source context.

## Acceptance Criteria

- [ ] All 41 patterns have distinct guides tied to their intended behavior and completion evidence.
- [ ] Each guide has a person-takes-the-step scenario and an asks-but-does-not-act scenario.
- [ ] Copy for unsupported recognition says so and makes no false promise of Seen or Continuous.
- [ ] Advice and fix prompts preserve the pattern's safety prerequisites and the person's control.
- [ ] Generic text is recognizable as general advice; only actual evidence supplies session-specific facts.
- [ ] Copy review is required before release; no review is claimed merely because content was drafted.

## Edge Cases

- No applicable task: offer an explanation and finish without an exercise or recognition.
- Unknown command, model, hook or platform setting: ask the person's agent to inspect its actual supported configuration rather than prescribing invented syntax.
- A host cannot render a purpose: its absence is a host limitation; pack content must not redirect coaching into warnings or interruptions.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [pattern progression](pattern-progression.md), per-pattern guide requirements.
- Host guide launching, guided markers, personalized evidence rendering and fix-prompt wrappers are outside this pack-only change.

