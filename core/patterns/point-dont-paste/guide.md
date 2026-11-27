# Point, don't paste: guide

Send the agent straight to the code, test and log lines that matter.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. Precise pointers still help from your next request.

## 1. Pick your next real request that needs context

Choose a task in your own project that depends on existing code or a failure you have seen: a bug, a behaviour change, a failing build.

If your next task needs no existing context (a new standalone script, a general question), **stop here**: there is nothing to point at and nothing to recognize.

## 2. Find the pointers

Before you write the request, note:

- the **file** (or function) where the problem most likely lives;
- the **test** that shows it, if there is one;
- from any log or error, the **few lines** that show the failure, not the whole output.

If you are not sure where something lives, that is fine: name the closest thing you do know, or ask your agent for a codebase overview first and then pick from it.

## 3. Take the step: send a pointed request

Write the request with those pointers, for example:

> Invoices round half-cents the wrong way. The rounding is in `billing/rounding.py` and `test_round_half_cent` fails. Here are the five lines of the failure: …

Then watch whether the agent starts from what you named.

**Done:** your request named the relevant file, test or excerpt, and the agent actually used them to do the work. That is what this pattern recognizes once detection is available.

**Not done yet:** if you listed pointers while reading this guide but did not use them in a real request, or the files you named were not the ones the work needed, the pattern has not happened yet. That is fine. Nothing is recorded against you; try it on your next request.

## Later

Once several patterns happen on their own, a short codebase map in your instruction file can give the agent these pointers every session. That comes later and does not replace naming the right place in a request.
