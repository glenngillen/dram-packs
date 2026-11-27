# Fix the harness: guide

Pick a correction you keep making and stop it at the source with a rule, check or gate.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a correction you prevent is one you stop paying for.

## 1. Find a correction you keep making

Think about the last few weeks of work in one repository, or ask your agent:

> Looking at my recent sessions in this repository, what have I corrected you on more than once?

Use only corrections that really happened: "use the shared Button component", "don't skip failing tests", "use pnpm".

- If nothing recurs, **stop here**. There is no exercise to do and nothing to recognize.
- If a rule or check already prevents it and it has not come back, you already do this for that correction.

## 2. Choose how to prevent it

Ask your agent:

> Propose the smallest change that would prevent this: an instruction rule, a lint or test check, or a gate before you finish. Explain which would catch it most reliably.

Prefer a check or gate when the mistake is mechanical; a rule when it needs judgement. If you are not sure what hooks or checks your agent supports, ask it to inspect its actual configuration rather than guessing syntax.

## 3. Review and keep the change

Read the proposed change, edit it, and save or commit it only when you agree with it.

## 4. Take the step: keep working and watch

Carry on with real work in that repository. Over the next two weeks, notice whether you have to make the same correction again.

**Done:** you made the change, and at least two later sessions doing related work went by without that correction.

**Not done yet:** if you only answered this guide's questions, or made the change but have not yet done related work, the pattern has not happened yet. That is fine; nothing is recorded against you. If the correction comes back, the change did not hold: adjust it.

## Later

Once several patterns happen on their own, having the agent propose a harness fix when a correction recurs is the next step. That comes later.
