# Brief It

## Overview

Source ID `brief-it`; Briefing, rung 1. Help the person give the agent the goal and the constraints or context needed to avoid guessing. Detection requires model judgement.

## Requirements

- Applies to the first request of a piece of work, including a new task within a session.
- Seen requires a goal plus at least one substantive constraint or relevant contextual fact, followed by work that did not need to ask or guess about those details.
- Exclude a goal alone, irrelevant background, and an agent-written brief accepted with “ok”.
- Cite the person's request as the completing evidence, retaining the later work needed to establish that its context mattered.
- Continuous requires a person-used saved command, skill or issue template that asks for the goal and constraints, applied and holding in the window.
- Coach when an open request led to a wrong assumption the person corrected. The guide asks what done looks like and what must not change, then has the person include both in their real request.

## Acceptance Criteria

- [ ] Recognize “Add password reset. Use the existing email service, links expire after an hour” when relevant to the work; reject “Add password reset” alone.
- [ ] Recognize an inclusive end-date request that protects existing timezone handling; reject lengthy background the work did not use.
- [ ] Asking guide questions without the person sending a substantive brief earns nothing; a completed guided brief can earn Seen only.
- [ ] A template existing without actual use cannot establish Continuous.

## Edge Cases

- A request may be concise and sufficient; length alone is neither positive nor negative evidence.
- Decided by [stage-dependent completion](pattern-progression.md#stage-dependent-completion): Seen completes on the person's brief; Forming and Established count only briefs whose later work shows the context was used, credited to the week that corroboration finished.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [coaching content](coaching-content.md), [evaluation readiness](evaluation-readiness.md).
- Missing pack-driven task-boundary/intent recognition and attributable template-use evidence; follow the disabled baseline in [pack compatibility](pack-compatibility.md).

