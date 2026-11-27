# Back it up in CI: guide

Send your next real agent change to the default branch through a branch or pull request where CI runs the tests.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: CI catches what passes only on your machine.

## 1. Pick a real repository and a real change

Think of a repository where your agent's changes land, and a change you are about to make there.

- If you have no agent change to integrate soon, **stop here**. There is no exercise to do and nothing to recognize; come back when you have one.
- If agent changes there already go through a branch or pull request with CI that runs the tests, you already do this. Stop, or pick another repository where they do not.

## 2. Find out what CI actually runs

Ask your agent to read the repository's real CI configuration rather than guessing:

> Which CI workflows in this repository run the tests, and on which events (push, pull request, which branches)? Which jobs only build docs, lint or format?

If no workflow runs tests, that is the first thing to fix with your team; a docs-only or lint-only workflow does not back up a change. Do not let the agent change CI configuration unless you ask it to and review the change.

## 3. Fast local checks, slower CI checks

Talk through your workflow with your agent:

- **Local checks** (formatting, type checks, focused unit tests) are fast. Keep running them while you work.
- **CI** runs the slower and broader checks (the full suite, integration tests) in a clean environment, before the change reaches everyone else.

CI supplements your local checks; it does not replace them.

## 4. Take the step: integrate the change through CI

When the change is ready, ask your agent to commit it to a **branch**, push the branch and open a **pull request**, instead of pushing to the default branch. Wait for CI to run. If it fails, fix the change and let CI run again. Merge once CI has run the tests.

**Done:** the agent change reached the default branch through a branch or pull request on which test-running CI ran. That is what this pattern recognizes once detection is available.

**Not done yet:** if you only read this guide, talked about CI, set up a workflow without integrating a change through it, or pushed the change directly to the default branch, the pattern has not happened yet. That is fine. Nothing is recorded against you; the next step is still to send one real change through CI.

## Later

Once several patterns happen on their own, you can make the pull request the normal merge path for agent work so every change gets CI without you remembering. That comes later, and it does not replace fast local checks.
