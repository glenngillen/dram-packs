# Checks by default: guide

Write your project's real check commands into the instructions your agent loads, with a rule to run them after changing code, so it checks its work without you asking.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: from the next session on, checks run by default.

## 1. Pick a real repository with checks

Choose a repository you change code in regularly that has tests, a type checker, a linter or a build.

- If its instructions already tell the agent to run checks after changes, and it does, you already do this here. Pick another repository, or stop.
- If you have no repository with any checks, **stop here**. There is no exercise and nothing to recognize.

## 2. Find the real commands

Ask your agent:

> Which test, type-check, lint and build commands does this project actually use? Show me where they are defined.

Use what the project really runs. Do not invent commands.

## 3. Add the rule

Ask your agent to draft a short rule for the instruction file it loads in this repository, for example:

> After changing code, run `make test` (and `npm run typecheck` for TypeScript changes) and show the result. Do not report work as done if they fail.

Review it, then save it (and commit it if the repository is shared). If you would rather use a hook, ask your agent to inspect which hook settings your agent actually supports before writing one; do not copy hook syntax from elsewhere.

## 4. Take the step: let it run on real work

Start a **new session** in that repository and make a real code change. Do not ask for the checks yourself.

**Done:** after an edit, the agent ran the check your rule names without you prompting it. Whether it passed or failed, the rule did its job; if it failed, the change is not finished yet.

**Not done yet:** if you only wrote the rule, or the next session changed code without running the check, or you stopped after reading this guide, the pattern has not happened yet. That is fine. Nothing is recorded against you; check that the agent actually loads the file and try again on your next change.

## Later

Once several patterns happen on their own, you can extend the rule to every repository you work in, or to a user-level rule or hook. That comes later.
