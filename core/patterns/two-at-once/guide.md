# Two at once: guide

When an agent turn will take a while, use the wait for a second, independent real task in its own working copy.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: waiting time becomes working time without the two tasks colliding.

## 1. Check the prerequisite: separate working copies

Two sessions must never share one directory, even on different branches: they would overwrite each other's files. If you have not yet run a session in its own worktree or clone (see Isolate the run), do that guide first.

## 2. Pick two independent real tasks

Choose two real tasks in your own projects that do not touch the same files: for example a refactor in one module and a bug fix in another, or work in two different repositories. One of them should be something the agent will take **at least five minutes** on in a single turn; a shorter turn is not the waiting time this pattern is about.

If you do not have two independent tasks right now, **stop here**. There is no exercise and nothing to recognize.

## 3. Give the second task its own working copy

If both tasks are in the same repository, ask your agent:

> Create a separate git worktree (or clone) for my second task. Show me the commands and where it will live first, and do not touch my current working copy.

## 4. Take the step: run both

Start the longer task in the first session. While it works, start the second session in the other working copy and give it its task. Let both make real edits.

**Done:** while one agent turn ran for at least five minutes, both sessions, each in its own working copy, were editing during the same minutes, and you started the work in each. That is this pattern.

**Not done yet:** if the long turn finished in under five minutes, the second session only sat open, the two shared a directory, or the second "session" was a subagent of the first, the pattern has not happened yet. That is fine. Nothing is recorded against you; try again on your next long turn.

## Later

Once several patterns happen on their own, a command or script you own can create the working copies and start both sessions. That comes later, not as a shortcut.
