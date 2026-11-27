# Fan out: guide

When the same kind of work has to happen in three or more independent places, run one subagent per part at the same time and bring their results together.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: independent parts stop waiting on each other.

## 1. Pick real independent parts

Look for real work in your own project with **three or more parts that do not depend on each other**: updating a client library in each service, auditing several modules, investigating three unrelated failures.

If the parts depend on each other, or there are only one or two, **stop here**. There is no exercise and nothing to recognize.

## 2. Check what each subagent can do

Parallel subagents each act with your permissions. Ask your agent:

> Which commands and files can subagents use in this project under my current permission settings?

Keep your existing scoped permissions, secret-file protection and guards on destructive commands. Do not turn off permission prompts to make this smoother; if something needs a new permission, decide on it narrowly.

## 3. Take the step: fan out and combine

Ask your agent, for example:

> Use one subagent per service to update the payments client, running at the same time. When they're all done, summarise what changed in each and anything that failed.

Then read the combined summary and act on it.

**Done:** three or more subagents ran at the same time on the parts you asked for, and you used their combined result. That is this pattern.

**Not done yet:** if the agent worked through the parts one after another, started only one subagent, or you never looked at the combined result, the pattern has not happened yet. That is fine. Nothing is recorded against you; try again with your next multi-part task.

## Later

Once several patterns happen on their own, you can save a fan-out you repeat as a command or workflow you own. That comes later, not as a shortcut, and only with the Safety settings above in place.
