# Guard destructive commands: guide

Make the commands you cannot easily undo stop for a rule or for your decision, instead of relying on the agent remembering to ask.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: the guard is there the one time the agent would not have asked.

**You never run a destructive command to try this out.** The guard is checked by reading its configuration and by real work, not by provoking it.

## 1. Pick a real repository with something to lose

Think of a repository you work in that deploys, migrates a database, changes infrastructure, or where a forced push would hurt. Unattended runs count too, wherever they run.

- If none of your work involves commands like that, **stop here**. There is no exercise and nothing to recognize.

## 2. Name its most dangerous command

Ask your agent:

> Without running anything, list the commands in this repository (scripts, make targets, infrastructure and git commands) that would be hard to undo. Which one would do the most damage if run by mistake?

Pick one or two. Guard the commands the repository really uses, not a generic list.

## 3. Ask for a guard

Ask your agent to inspect **its actual supported permission and hook configuration** and propose either a rule that blocks the command, a rule that makes it ask you first, or a check that runs before each tool call. Ask it to tell you:

- **which permission modes would skip the guard**: an ask rule does nothing in a mode that never asks;
- **what it would miss**: other spellings, aliases, wrappers or compound commands. A pattern match narrows the risk; it does not block every form of the command.

Review the proposal before it is saved. Do not test it by running the dangerous command.

## 4. Take the step: do real work with the guard in effect

Do your next real task in that repository, or your next unattended run, in a mode that keeps the guard active.

**Done:** a real session ran with the guard effective for that repository's destructive commands. If the agent attempted the command and was blocked, or stopped to ask you, that shows the guard holding.

**Not done yet:** if you configured the guard but have had no session in that repository since, or the session ran in a mode that skips it, or the guard covers a command this repository never uses, the pattern has not happened yet. That is fine. Nothing is recorded against you, and there is nothing to provoke; do your next real task with the guard in place.

## Later

Once several patterns happen on their own, guards for your destructive commands can live in user-level or team settings, so unattended and parallel runs are covered wherever they start. That comes later.
