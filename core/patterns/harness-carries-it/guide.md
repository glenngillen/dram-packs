# Let the harness carry it: guide

Try a real routine task on a lighter model in a repository where your checks run on every change, and let those checks decide whether it is good enough.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. Even once it is available, the change must still be in the default branch fourteen days later, so recognition can only follow after that.

## 1. Pick a repository with working checks

Choose a repository you work in where checks actually run on the agent's changes: an instruction rule or hook that runs tests, a final gate, or CI on the pull request. Ask your agent to confirm which ones run and whether they block on failure.

If none of your repositories has checks that run on changes, **stop here**. There is no exercise; [Checks by default](../checks-by-default/guide.md) or [Gate "done"](../gate-done/guide.md) comes first.

## 2. Pick a real routine task

A rename, docstrings, formatting, a version bump or a simple fix you need anyway. If you have none right now, **stop here** and come back when you do.

## 3. Take the step: do it on a lighter model

Ask your agent how this harness switches models, and switch to a lighter one yourself before the task. Let the work go through the usual checks and merge it as you normally would. If the lighter model cannot do it, it is fine to switch back; that run simply is not this pattern.

**Done:** the routine change was made on the lighter model, its checks ran and passed, and it was merged. It completes this pattern once it is still in the default branch fourteen days later.

**Not done yet:** if the checks did not run, the change failed and was finished on the premium model, it was reverted, or you only read this guide, the pattern has not happened yet. That is fine. Nothing is recorded against you; try another routine task.

## Later

Once several patterns happen on their own, your harness can route routine work to a lighter model by default or through your own pinned command or subagent, with your gates deciding. That comes later, not as a shortcut.
