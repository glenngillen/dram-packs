# Schedule the clean-up: guide

Hand a maintenance chore you keep doing by hand to a headless agent run, and make sure what it produces gets used.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide still helps: one run whose result you use is worth more than a schedule nobody reads.

This guide does not create, edit or launch any schedule for you, and it never touches CI or scheduler settings unless you ask your agent to.

## 1. Pick a real chore

Think of a repository you maintain and a chore that keeps coming back: updating dependencies, sweeping flaky tests, clearing lint warnings.

- If you already have a scheduled run for it whose output you act on, you already do this. Pick another chore, or stop.
- If you do not maintain a repository, or nothing recurs, **stop here**. There is no exercise to do and nothing to recognize.

## 2. Write the run down

With your agent, describe the chore as a single prompt or saved command a headless run could follow, for example "check dependencies, update what is safe, open a pull request". Ask your agent what this repository and your setup already support:

> What ways do I already have to run you headless on a schedule for this repository, and what permissions would that run need?

Keep the run's permissions narrow; do not reach for permission bypass to make it work.

## 3. Run it once and use the result

Run it headless once, by hand, and look at what it produced. Merge the pull request, fix the issue it filed, or decide it is not useful yet and change the prompt.

## 4. Take the step: schedule it and act on it

If the run is useful, set up the schedule yourself, or ask your agent to and review the change before it is saved. Then, when the next scheduled run produces something, act on it.

**Done:** a run launched by your schedule produced a pull request you merged, an issue you fixed, or a result you used. That is what this pattern recognizes once detection is available.

**Not done yet:** if you set up a schedule but no run has happened, or runs happen and nobody looks at the output, or you only read this guide, the pattern has not happened yet. Nothing is recorded against you; the next step is still to use one run's output.

## Later

Once several patterns happen on their own, more chores can move to owned schedules. That comes later and never replaces reading what the runs produce.
