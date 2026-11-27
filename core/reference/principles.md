# Principles

Why the framework works the way it does. Every pattern's `## Intent` section links here instead of restating these reasons, and every rule in a pattern should trace back to one of them, to the pattern's own intent, or to a recorded decision. Where none applies, the pattern says the reason is not recorded rather than inventing one.

## What the pack is for

Most engineers using coding agents can't see their own habits. They don't notice that their sessions run long and lose focus, that routine work runs on the most expensive model, that they type the same request every week, or that they accept "done" without proof. Each of these costs time, money or quality, and each has a simple pattern that fixes it.

The pack makes those habits visible to the one person who can change them, then helps them change, in the tools they already use:

- **Analysis:** an honest picture of how someone works with agents, grounded in their own sessions and git history, with every finding citing its evidence.
- **Action:** specific patterns to try, chosen from their own missed moments, with a guide in their own agent when the moment hasn't come up yet.
- **Progress:** later analysis shows whether the pattern took hold, and finally whether the harness does it for them.

A **pattern** is a specific, recognisable way of working with a coding agent that makes the work better: a proven solution to a recurring problem. Patterns are grouped by the part of the harness they build (the instructions, checks, mechanisms and habits a person puts around their agent), and each group is ordered from foundational to advanced.

## Patterns, not grades

There is no grade, level, score, percentage or single number that summarises a person, anywhere.

- **A grade invites ranking.** A single number is the easiest thing to compare between people, and comparing people is not something this pack does in any form.
- **It overstates what we know.** A model's reading of a sample of sessions isn't precise enough to justify a number that looks objective.
- **It punishes choices.** An overall score marks someone down for a pattern that doesn't matter in their work. People decide what matters; a pattern they don't need never counts against them.

Progress on specific patterns replaces it: something the person actually did or set up, tracked for how reliably it happens.

## Behaviour, never the person

Findings describe what happened in sessions ("premium model on short requests"), never the person ("inefficient engineer"). Copy never uses scoring, ranking, streak, productivity, time-saved or guarantee language. A slip back is said plainly and without judgement.

## Human intent only

A pattern is recognised from something the person chose to do or set up: a prompt, a command, a mode, a session they started, a file they asked for, configuration they or their team wrote.

- **The agent's own initiative never counts.** Running tests unprompted with no instruction telling it to, starting its own subagents or falling back to a cheaper model is the agent's behaviour, not a habit the person built. Crediting it would teach the person that a pattern is in place when nothing they did put it there.
- **The person's harness does count.** When the agent does something because a guide, rule or hook the person (or their team) wrote tells it to, that's the person's harness at work, and it counts for the pattern that guide implements.
- **Some patterns are about the response, not the first step.** Where the value is in how the person responds, the agent may start it, as long as the person's response is in the evidence: the agent proposes a plan and the person reviews it.
- **Software acting on its own behalf is not the person.** Sessions started by Dram itself or by other agents never count as the person's work.

This is why most exclusion lists rule out agent-only, built-in, third-party and auto-generated material: it is not evidence of what the person did.

## False positives are worse than misses

A missed pattern can be recognised next time. A false recognition teaches the wrong thing and erodes trust in every other finding. When the evidence is ambiguous, the pack chooses not to recognise.

This is why recognitions need **completing evidence** (the specific event that makes the pattern true, not a proxy for it), why filename existence, configuration presence or command matches alone are never enough, and why "unknown" is always preferred to "unsupported".

## Evidence for everything

Every stage, finding and recognised pattern cites the sessions or commits behind it, and the person can open them: what they asked, where it went well or wrong, and what would have helped in that moment.

- At least one citation is **person-authored**, so the recognition is grounded in the person's own act ([evidence](evidence.md#attribution-and-citations)).
- Quotes are exact, and citations must exist in the evidence. A claim that fails these checks is dropped with its reason ([verification](verification.md)).
- The completing evidence falls in the analysis window, so a stage reflects the period it reports on.
- **Every case ends with what to do:** a missed moment says what to do next time, specific to that case, and how to stop that class of problem recurring.

## Missing is not low

Anything that can't be assessed shows as not assessed, with the reason, never as a miss. Missing timestamps, truncated output, unknown models or unknown pricing produce no recognition and no claim ([insufficient evidence](evidence.md#insufficient-evidence)). Weeks that weren't analysed never move a pattern down.

## Code checks facts; a model judges the rest

Mechanisms (hooks, instruction files, schedules, permissions, working copies) are facts code can read exactly, so they are checked by code, not judged. Whether a person deliberately did something in a session is a judgement, so a model makes it, and code then verifies every claim. Many patterns use both: a model recognises the person doing it, and code recognises the mechanism that makes it continuous.

## Applicable work

A frequency only means something against the work where the pattern applies. Each pattern defines its **applicable work**, and progress is measured against it. A week with no applicable work counts neither for nor against the pattern, so nobody is marked down for a pattern their work rarely needs. This is why every pattern states what "no applicable work" looks like, and why that case reports nothing rather than a miss.

## Stages

Each pattern moves from **Seen** (it happened), to **Forming** (it's happening repeatedly), to **Established** (it happens in most work where it applies), to **Continuous** (it happens without the person remembering) ([progression](progression.md#stages)).

- **Stages describe reliability, never volume.** More sessions, tokens or hours never count for more.
- **Continuous needs a mechanism.** Someone who remembers every single time is at Established. Continuous means the harness does it, so it holds when they're tired, rushed or running five sessions. A high rate on its own is never enough.
- **Continuous can be reached directly.** A gate that runs the tests makes a checking pattern continuous the first time it fires, whatever the person did before.
- **Stages reflect recent work, not the best ever.** A pattern that drops below its stage shows where it is now.
- **Why a ladder at all:** people keep changes they understand. Automation set up without the habit behind it can be copied without understanding, or switched off at the first annoyance, and visible progress keeps people coming back. For people already automating, next steps also offer the automated version ([automation gate](progression.md#automation-gate)).

### Follow-through

For patterns whose value lies in what happens next (a review whose findings are acted on, a correction the agent follows), **Seen** completes on the person's act, so the first instance is credited promptly. **Forming** and **Established** count only instances whose follow-through finished, credited to the week it finished ([stage-dependent completion](progression.md#stage-dependent-completion)). Repeated acts with no effect are not a habit worth crediting.

## Prevention: when success removes the signal

Many patterns work by making a problem stop happening. Once a rule is in an instruction file, the agent stops making that mistake, so the person stops correcting it. Once a gate blocks failing tests, nothing slips through to notice. If patterns were recognised only by the person doing something, or by the problem recurring, the people who solved a problem best would look like they'd stopped making progress.

So once a mechanism is in place, the evidence changes from "the person did it" to "the mechanism held where it applied" ([mechanisms](evidence.md#mechanisms-in-place-applied-held)):

- **In place:** the mechanism exists where the person works. Cheap and exact, but not enough on its own.
- **Applied:** sessions where the mechanism was relevant, whether or not anything went wrong.
- **Held:** in those sessions, the mechanism did its job.
- **Not holding is a finding, not a failure.** A rule that exists while the problem keeps recurring is shown as a specific case, often with a stronger mechanism to try. That's often more useful than the original suggestion.
- **Silence is only credit when it's applicable.** "Nothing went wrong" counts as held only where the mechanism applied. A mechanism that never applied is in place but untested, never held.
- **Specific mechanisms are easier to credit.** "Use components/Button for buttons" is easy to spot applying; "write clean code" isn't. Vague rules may stay untested, which is a fair outcome.

## Guided sessions reach Seen only

Each pattern has a guide the person runs in their own agent, on their own real work. A guided session can make a pattern Seen, never later: Forming and beyond need the pattern on the person's own, because a habit is what happens when nobody is prompting ([guided sessions](progression.md#guided-sessions)).

- **The pattern stays the person's.** The guide asks and explains; it never performs the step for them.
- **Their own work only.** No sample code, synthetic exercises or manufactured cases. A guide that manufactured the situation would teach the steps without the judgement of when they apply.
- **Stop when it doesn't apply.** Every guide has an exit for work where the pattern isn't relevant.

## Outcomes keep it honest

Advanced patterns can be gamed or overdone: more parallel sessions, a bigger harness. Each group is shown with outcome measures (changes kept, rework, escapes, repeated corrections, cost for kept work) so a bigger harness never looks like progress on its own ([outcomes](outcomes.md)). Outcomes are shown as facts with their cases, only against the person's own past. A pattern moving up while its outcomes get worse is called out, so the person can decide whether it's paying off.

## Autonomy and safety advance together

Next steps never suggest unattended, parallel or permission-skipping work to someone whose Safety patterns aren't in place for that kind of run ([safety prerequisites](progression.md#safety-prerequisites)). More autonomy means more the agent could break; the safeguards come first. This is why several Delegation patterns name a Safety prerequisite, and why guides never instruct anyone to skip permissions or disable checks.

## Next steps: few, and from the person's own work

The person sees at most two next steps, each named as a pattern, with a reason from their own sessions when one exists ([next-step ordering](progression.md#next-step-ordering)). Foundations come first, then the next rung of groups already started, ranked by how often and how costly the missed moments were. Fewer, specific steps get acted on; a long list doesn't.

## Private by default

The analysis is for the person. It stays on their machine; nothing about their sessions goes anywhere else ([privacy](evidence.md#privacy)). Secret values are never read or reproduced.

## Thresholds are calibration points

Every number in the pack (three sessions, six prompts, 24 hours, five minutes, 60%, 14 days and the rest) is a **deliberately arbitrary starting point**. This first implementation exists to calibrate what feels right in real use. None is derived from data, none has been validated, and none should be read as a claim that the boundary is correct. Each lives once in [parameters](parameters.md) so it can be changed in one place as evidence comes in. Patterns cite the parameter; they don't justify the number.

What *is* deliberate is the **kind** of rule a threshold expresses (for example, "the person regularly works here", "the session got long enough to degrade", "the person was actually waiting"). Each pattern's Intent says what its thresholds are trying to capture.

## Groups

The eight groups, foundational to advanced, each covering a part of the harness. The order inside each group is a ladder: later rungs usually build on earlier ones.

| Group | What it's for |
| --- | --- |
| **Briefing** | The person as the agent's guide for each piece of work: what to do, what done means, and how to get there. Without acceptance criteria, correctness is outside anything that checks the work. |
| **Guides** | What the agent knows before it starts: instructions, conventions, saved workflows and tools. Guides are how one correction becomes permanent. |
| **Context** | What's in the agent's working memory during a session. Keeping it relevant keeps the agent sharp and cheap. |
| **Checking the work** | How the work gets checked, and where checks are enforced: from the person checking, to the agent running checks, to checks that block it at each step and before "done", to CI, independent reviews and checks that keep running after the work ships. Quality is kept as early as possible. |
| **Correcting course** | Correcting the agent while the work is under way: redirecting it when it goes wrong, and setting checkpoints ahead of time so it stops and asks. Making a correction permanent is Fix the harness, in Guides. |
| **Delegation** | Handing the agent work at the right size and letting it run: subagents, unattended runs, isolation, parallel sessions. These pay off most once Checking the work is in place. |
| **Economics** | Getting the same results for less: the right model for the task, the harness doing the work a bigger model would, and context that stays cached. |
| **Safety** | Giving the agent autonomy in proportion to what it could break. These advance alongside Delegation: next steps don't suggest more autonomy without them. |
