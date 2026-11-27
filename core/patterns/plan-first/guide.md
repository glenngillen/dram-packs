# Plan first: guide

Agree a plan with your agent before it edits several files on a real change.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a plan is cheaper to fix than edits.

## 1. Pick an upcoming change that will touch several files

Choose real work in your own project that you expect to change two or more files: a refactor, a feature across layers, a migration.

- If your next task is a one-file change, or you have no change to make right now, **stop here**. There is no exercise and nothing to recognize.

## 2. Ask for a plan before any edit

If your agent has a plan mode, enter it. Otherwise ask:

> Propose an approach for this change: which files you'll edit and what changes in each. Don't change anything yet.

If you are not sure how your agent supports planning, ask it to describe its actual options rather than guessing.

## 3. Take the step: review the plan, then let it edit

Read the plan. Approve it, adjust it ("keep the old API", "split the migration into its own step") or ask about anything unclear. Only then let the agent make the edits.

**Done:** the plan came before the edits, you reviewed it, and the change then edited at least two files. That is what this pattern recognizes once detection is available.

**Not done yet:** if the plan went unanswered, edits started before you looked, or the change turned out to touch only one file, the pattern has not happened yet. That is fine; nothing is recorded against you.

## Later

Once several patterns happen on their own, default plan mode or a plan-first rule can make every multi-file change start with a plan. You still review each one; automatic approval does not count.
