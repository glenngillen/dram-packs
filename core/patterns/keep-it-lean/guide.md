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

Size only counts as a cost problem when the measured share is **more than 12%** of the starting context ([`instruction_cost_share`](../../reference/parameters.md#instruction_cost_share), a provisional, tunable default). The boundary is strict: exactly 12% does not cross it.

- If there is no contradiction and the measured share is 12% or less (or there is no measurement), **stop here**. There is no conflict or cost problem to act on.

## 3. Decide what to keep

For each conflict, decide which line is right. If the files are large, decide which rules could load only when needed (for example, split into on-demand rules) rather than be deleted. Keep every rule you still want.

## 4. Take the step

Ask your agent to make the change, for example:

> Our two test commands disagree. Keep `make test` and remove the old `npm test` line. Show me the diff first.

**Done:** you asked for the reconciliation after seeing both conflicting lines, or for the trim or split after seeing a measured cost of more than 12% of the starting context. A request made at exactly 12% or below does not count for cost. That request is what this pattern recognizes as Seen once detection is available. When the edit is made and still in the default branch two weeks later, it has also stuck, and that is what counts toward the later stages.

**Not done yet:** if you looked at the conflict or the size and asked for nothing, or the agent rewrote the file without you asking, the step has not happened yet. That is fine and nothing is recorded against you; the next step is still to ask for the change.

## Later

Once several patterns happen on their own, a recurring check in your harness can flag new conflicts and loading cost for you to review. It suggests a review; it never deletes rules by itself.
