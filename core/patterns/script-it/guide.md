# Script it: guide

Use a script for the next mechanical change across many files, instead of having your agent edit each file by hand.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a reviewed script makes the change consistently.

## 1. Wait for a real mechanical change

This guide works on real work: a rename, an API migration, boilerplate for a new endpoint, an import rewrite across your own project.

- If you have no such change coming up, **stop here**. There is no exercise to do and nothing to recognize. Come back when one arrives.
- Do not invent a rename to practise on.

## 2. Ask for a script, not edits

When the change comes up, ask:

> This change is mechanical across many files. Write a script or codemod that makes it, and show me the script and the files it will touch before running it.

If your project already has a scaffold script or codemod for this kind of change, ask your agent to use that instead. If you are unsure whether a language tool (for example a rename tool) is set up for your agent, ask it to inspect its actual configuration.

## 3. Review the script

Read it. Check it targets the right files and makes the change you mean. A script that exists is not proof it does the right thing.

## 4. Take the step: run it

Have the script run and look at the result (the diff, and your tests).

**Done:** a script or tool you asked for made the change. If it is worth keeping, ask your agent to save it in the repository for next time.

**Not done yet:** if you only discussed a script, the script was written but never run, or the agent ended up editing each file by hand, the pattern has not happened yet. That is fine. Nothing is recorded against you; ask for a script on the next real change.

## Later

Once several patterns happen on their own, keeping working scripts in the repository behind a command makes them reusable. That comes later.
