# Gate each step: guide

Run a fast check after each agent edit or before each commit, so a type or lint problem comes back at the step that caused it.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: problems come back while the agent is still on that change.

## 1. Pick a real repository with a fast check

Think of a repository you work in regularly that has a type check, linter or quick unit tests.

- If it already runs one after agent edits or before commits, and it has caught something, you already do this there. Pick another repository, or stop.
- If none of your repositories has a type check, linter or quick tests, **stop here**. There is no exercise and nothing to recognize.

## 2. Find the fast check

Ask your agent:

> What is this project's fastest useful check (type check, linter or quick unit tests), and how long does it usually take?

It should usually finish within about a minute. A slower check belongs at the end of the task instead (see Gate "done"). A formatter does not count: it rewrites code, it does not catch problems.

## 3. Run it at each step

Ask your agent to inspect **its actual supported hook configuration**, or the repository's pre-commit setup, and propose running that check after edits (some agents call this PostToolUse) or before commits. Ask it to confirm the check's failure reaches it, and not to bypass the check (for example with `--no-verify`).

Review the change before it is saved. Commit it if the repository is shared.

## 4. Take the step: let it catch something on real work

Carry on with real tasks in that repository.

**Done:** the check fires on an agent edit or commit and blocks it or feeds a problem back at least once. That catch, on real work, is what this pattern recognizes once detection is available.

**Not done yet:** if the check is configured but has only passed so far, or has not fired, or commits skip it, the pattern has not happened yet. That is fine. Nothing is recorded against you; keep working and it will show its value the first time it catches something.

## Later

Once several patterns happen on their own, running fast checks after every edit from your user-level harness can cover each repository you work in. That comes later, and it never replaces the final check before the work is done.
