# Make failures actionable: guide

Make one check that often fails in your project tell the agent what to fix, and make sure the agent actually sees it.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: the next time that check fails, the agent can fix it in one step.

## 1. Pick a real, frequently failing check

Think of a project where your agent runs hooks or checks (lint, type checks, tests) during its work. Which check fails most often while the agent works?

- If none of your projects run checks during agent work, **stop here**. There is nothing to wire up yet; Checks by default is the earlier step.
- If you cannot think of a check that fails, **stop here** too. There is no exercise and nothing to recognize.

## 2. See what the agent actually sees

In that project, ask your agent:

> When the <check name> check fails during your work, what output do you receive? Show me exactly what reaches you, or tell me if it doesn't reach you at all.

Look for one of these problems:

- The output never reaches the agent (it goes to your terminal or a log file).
- It reaches the agent but only says *that* something failed, not *what to change*.

If the agent already receives a message naming the rule, the place and the fix, and acts on it, you already do this here. Pick another check or stop.

## 3. Make the failure actionable

Ask your agent to propose a change to your harness so the failure reaches it with:

- the rule that failed,
- where (file and line, or the component),
- what to do instead, ideally pointing at an existing example (for example "use the shared Button, see components/Button").

Hook and lint configuration differs between agents and tools. Ask your agent to inspect **its actual supported hook configuration** rather than guessing the syntax. Review the change yourself before it is saved; commit it if the repository is shared.

## 4. Take the step: let it fail on real work

Carry on with a real task. When that check next fails, watch what happens.

**Done:** the failure reaches the agent with the fix guidance, and the agent's very next step fixes the problem it named. That sequence, on real work, is what this pattern recognizes once detection is available.

**Not done yet:** if you configured the hook but no real failure has happened, or the failure was fed back and the agent ignored it, or the output still went only to a log, the pattern has not happened yet. That is fine. Nothing is recorded against you; keep working and check again the next time it fails.

## Later

Once several patterns happen on their own, giving each frequent failure a fix message becomes part of how you maintain your harness. That comes later; it does not replace reading what failed.
