# Reuse your harness: guide

Move one command, hook or rule you have defined in more than one repository into a single place both repositories use.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: one maintained copy stops the copies drifting apart.

## 1. Find a duplicate of your own

Think of the repositories you have worked in recently. Ask your agent, in one of them:

> Which commands, skills, hooks or rules in this repository did I write that I also have in my other projects?

Only count things you or your team wrote. Built-in commands and plugins someone else maintains are not part of this.

- If you work in only one repository, **stop here**. There is no exercise to do and nothing to recognize.
- If you have no duplicates, or your shared items already live in user configuration, your own plugin or a template you maintain, you already do this. Stop.

## 2. Compare the copies

Ask your agent to show the differences between the copies. Decide which version you want to keep.

## 3. Move one copy into user configuration

Ask your agent where it reads user-level commands, hooks or rules; ask it to inspect its actual configuration rather than guessing. Then:

> Put this version in my user configuration. Show me the file before saving. Do not delete the repository copies until I say so.

Remove the repository copies only when you are happy the shared one works.

## 4. Take the step: use it in both repositories

On real work, use the shared item in each of the two repositories.

**Done:** the same command, hook or rule from your user configuration ran in two repositories you work in.

**Not done yet:** if you only moved the file, or used it in one repository so far, or answered this guide's questions, the pattern has not happened yet. That is fine. Nothing is recorded against you; use it in the second repository when the work comes up.

## Later

Once several patterns happen on their own, keeping your whole harness in one maintained place (user configuration, your own plugin or a template) is the next step. That comes later.
