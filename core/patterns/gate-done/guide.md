# Gate "done": guide

Make your agent run your project's real check before it can say it has finished, and fix what fails.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: from the next task on, "done" means the check passed.

## 1. Pick a real repository with checks

Think of a repository you work in regularly that has tests, a build or a type check.

- If it already has a final gate that runs those checks when the agent finishes, you already do this there. Pick another repository, or stop.
- If none of your repositories has tests, a build or a type check, **stop here**. There is no exercise and nothing to recognize.

## 2. Choose the check

Ask your agent:

> What is the command that tells us this project's work is correct: tests, a build or a type check? How long does it take?

Use the real command (for example `make test` or the project's build). A formatter alone is not enough: it does not tell you the work is correct.

## 3. Add the final gate

Ask your agent to inspect **its actual supported hook configuration** and propose a gate that runs when it is about to finish (some agents call this a Stop hook). Ask it to explain:

- what happens when the check fails: it should **block** finishing and show the failure, so the agent fixes it;
- that the hook must not swallow failures (for example by always reporting success).

Review the proposal before it is saved. Commit it if the repository is shared.

## 4. Take the step: finish a real task through the gate

Do a real task in that repository and let the agent finish.

**Done:** the gate fires when the agent finishes. Ideally you see it block once on a real failure and the agent fix it before finishing. A gate that fired on real work is what this pattern recognizes once detection is available.

**Not done yet:** if you configured the gate but have not finished a session with it yet, or it runs only a formatter, or a failure was bypassed, the pattern has not happened yet. That is fine. Nothing is recorded against you; finish your next real task with the gate in place.

## Later

Once several patterns happen on their own, a user-level gate that runs each repository's own check can cover every project you work in. That comes later; it does not replace choosing a check that really tests the work.
