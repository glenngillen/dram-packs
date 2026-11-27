# Set Checkpoints: guide

Before a step that is hard to undo, tell the agent where to stop and wait for you. Then make the call yourself.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: it keeps the hard-to-undo decisions with you.

## 1. Find a real risky task

Look at your next real task in your own project. Does it include a step that is hard to undo: running a migration, deploying, deleting data or files, or changing a public API other code relies on?

If it does not, **stop here**. There is no exercise to do and nothing to recognize; come back before your next risky task. Ordinary steps like running tests or a local build do not need a checkpoint.

## 2. Name the checkpoint before the agent starts

When you give the agent the task, say exactly where it must stop and wait for you. For example:

> Draft the migration and ask me before running it.

or

> Prepare the deploy and show me what will change. Wait for my go-ahead before deploying.

If you are not sure which commands perform the risky step in this project, ask your agent to point them out first, without running them.

## 3. Take the step: decide at the checkpoint

When the agent stops and asks, read what it is about to do and decide: go ahead, go ahead with a change ("run it, skip the backfill"), or not now.

**Done:** you asked the agent to stop before the risky step, it actually stopped there, and you made the decision. That is this pattern, whatever you decided.

**Not done yet:** if the agent ran the step without stopping, or it stopped and you never answered, or you only wrote the checkpoint into a prompt and the task never reached the risky step, the pattern has not happened yet. That is fine. Nothing is recorded against you. If the agent skipped your checkpoint, tell it plainly and, if needed, undo the step. An auto-approve setting answering for you is not your decision.

## Later

Once you checkpoint risky steps by habit, an instruction rule naming the steps that need your decision, or an ask-permission rule on the commands that run them, can stop the agent every time. Ask your agent which ask rules this harness actually supports rather than guessing the syntax. That comes later, once several patterns happen on their own, and the decision always stays yours.
