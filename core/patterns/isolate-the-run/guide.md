# Isolate the run: guide

Give your next unattended or parallel run its own working copy, so it cannot trample another session's files.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: separate working copies stop two runs mixing their changes.

## 1. Find a real qualifying task

You need one of:

- a real task you are about to let the agent run **unattended** (headless, or an interactive session working for **at least fifteen minutes** without a prompt from you); or
- a real task you want to run in a **second session** while another session is still working in the same repository.

If you have neither right now, **stop here**. There is no exercise and nothing to recognize; come back when you next run work unattended or in parallel.

## 2. Create a separate working copy

A different branch in the same directory is **not** enough: switching branches rewrites the same files the other session is using. Ask your agent:

> Propose the simplest way to give my next task its own working copy of this repository, such as a git worktree or a second clone. Show me the commands and where it will live, and do not touch uncommitted changes in my current copy.

Review the commands, then let it create the worktree (or clone, or container with its own checkout).

## 3. Take the step: run the task there

Start the unattended or second session **inside the new working copy** and let it do the real work.

**Done:** the run was unattended (headless, or at least fifteen minutes of continued agent work without a prompt from you) or overlapped another working session, and it did its work in its own working copy while the other copy was left alone. That is this pattern.

**Not done yet:** if you created the worktree but have not run anything in it, the run was interactive and stopped for your prompts in under fifteen minutes with no second session working at the same time, or both sessions still worked in one directory on different branches, the pattern has not happened yet. That is fine. Nothing is recorded against you; use the worktree for your next qualifying task.

## Later

Once several patterns happen on their own, a command or script you own can create the working copy for every unattended or parallel run. That comes later, not as a shortcut.
