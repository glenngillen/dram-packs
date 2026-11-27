# Check at the right cadence: guide

Look at which checks actually ran on your recent work, on which model, and what they caught. Then decide for yourself whether any cadence should change. The final gate stays either way.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: it shows what your checks cost and catch, so any change you make is informed.

## 1. Check that it applies

You need a repository where you have **both** per-step checks (after edits or before commits) **and** a final gate, and where your work uses more than one model (for example a premium main session and lighter subagents).

If you have no final gate, **stop here**: [Gate "done"](../gate-done/guide.md) comes first. If you use only one model there, or have no step checks, stop here too: there is nothing to differentiate and nothing to recognize.

## 2. Look at what actually ran

Ask your agent:

> Show me the step checks and final gate this repository runs, which of them ran on my recent work, under which model, how long they took and what each caught.

Read the answer as evidence, not a verdict. Quiet checks do not prove quality, and no model is beyond checking.

## 3. Find out what your harness supports

Ask your agent to inspect **its actual supported configuration**: can step checks differ by model, for example through a lighter subagent's own hooks? If it cannot, say so and **stop here**; do not invent settings.

## 4. Take the step, if you decide to

If you decide the cadence should differ, ask the agent to propose the change, review it, and keep the final gate for all work. Then do real work on both tiers.

**Done:** your configured step checks ran on lighter-model work, the reduced cadence ran on premium work, both were observed on real work, and the final gate ran on both.

**Not done yet:** if you reviewed the checks but changed nothing, or only one model path has run since, or you removed the final gate, the pattern has not happened yet. Keeping your current checks is a valid decision. Nothing is recorded against you.

## Later

Once several patterns happen on their own, you can carry a cadence that works to other repositories, keeping each final gate. That comes later, not as a shortcut.
