# Keep it lean: guide

Check the instruction files your agent loads for rules that contradict each other or take a large share of the starting context, and tidy them without losing rules you want.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. A consistent instruction file still helps from the next session on.

## 1. Pick a real repository with instructions

Choose a repository you work in that has an instruction file the agent loads (`CLAUDE.md`, `AGENTS.md`, rules files) or where you use a user-level instruction file.

- If you have no instruction files yet, **stop here**: there is nothing to keep lean. Give it instructions comes first.

## 2. Ask to see the actual conflicts and cost

Ask your agent:

> Read the instruction files you load here. Quote any two lines that contradict each other. If you can measure it, tell me how much of your starting context these files take, and how you measured it.

Look only at what it can show you: both conflicting lines, or a measured size. Do not act on a guess about cost, and do not remove a rule only because it is old or rarely needed.

- If there is no contradiction and the files are a small share of the context, **stop here**. They are already lean; nothing to do.

## 3. Decide what to keep

For each conflict, decide which line is right. If the files are large, decide which rules could load only when needed (for example, split into on-demand rules) rather than be deleted. Keep every rule you still want.

## 4. Take the step

Ask your agent to make the change, for example:

> Our two test commands disagree. Keep `make test` and remove the old `npm test` line. Show me the diff first.

**Done:** you asked for the reconciliation, trim or split and the change was made. If it is still in the default branch two weeks later, it has also stuck.

**Not done yet:** if you looked at the conflict or the size and changed nothing, or the agent rewrote the file without you asking, the step has not happened yet. That is fine and nothing is recorded against you; the next step is still to ask for the change.

## Later

Once several patterns happen on their own, a recurring check in your harness can flag new conflicts and loading cost for you to review. It suggests a review; it never deletes rules by itself.
