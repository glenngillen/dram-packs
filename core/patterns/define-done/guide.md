# Define done: guide

Decide how a real feature or fix will be judged before the agent writes any code, then have the agent check against it.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: you will know whether the work is finished.

## 1. Pick your next real feature or fix

Choose a feature or bug fix you are about to ask for in your own project. Questions and exploration do not need this.

- If you have no feature or fix to start right now, **stop here**. There is no exercise to do and nothing to recognize.

## 2. Write two or three "done when" lines

Before asking for code, write them yourself. Make each one checkable:

- an example input and the expected result;
- a test you want to pass, by name;
- a behaviour someone could observe ("an expired reset link shows an error; a used link cannot be used again").

"Make sure it works" is not a criterion. If the agent drafts criteria for you, read and change them until they are yours.

## 3. Take the step: send them before the code, then check

Send the request with the lines included, or point at a spec you wrote that contains them. When the agent says it is finished, ask:

> Check the result against each "done when" line and show me the evidence for each.

**Done:** your criteria were there before the first edit, and the work was checked against them. That is what this pattern recognizes once detection is available.

**Not done yet:** if you discussed this guide but wrote no criteria, wrote them after the code, or never checked against them, the pattern has not happened yet. That is fine; nothing is recorded against you.

## Later

Once several patterns happen on their own, a template or command that asks for "done when" lines before any work can prompt you every time. A spec folder you never use does not count.
