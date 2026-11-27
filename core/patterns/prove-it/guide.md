# Prove it: guide

When your agent says a change is done, ask it to show you: run the check that covers the change and let you read the output.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: it catches unfinished work before you build on it.

## 1. Work on a real change

Use your next real coding task in your own project: a bug fix, a small feature, a refactor. Let the agent make the change as usual.

If you have no code change to make right now, **stop here**. There is no exercise to do and nothing to recognize; come back when you next change code with your agent.

## 2. Wait for "done"

Let the agent finish and report that the change is done (or fixed, or passing). Notice whether it ran anything **after its last edit**. A test run earlier in the turn does not cover edits made after it.

## 3. Take the step: ask for proof

Ask for evidence about this change, for example:

> Run the tests that cover this change and show me the output.

or

> Did you lint it? Run the linter and show me.

If you are not sure which check fits, ask your agent which test, build, lint or type-check commands this project actually uses.

**Done:** after your request, the agent actually ran a relevant check and you can see the output. That is this pattern, whether the check passed or failed. If it failed, the change is not finished: ask the agent to fix it and run the check again.

**Not done yet:** if the agent answered "yes, they pass" without running anything, or you asked before any change was made, or you stopped after reading this guide, the pattern has not happened yet. That is fine. Nothing is recorded against you; ask again after your next change and insist on seeing the output.

## Later

Once several patterns happen on their own, you can make checks run without asking: an instruction rule or hook that runs them after changes (Checks by default), and a final gate before the agent finishes (Gate "done"). That comes later, not as a shortcut.
