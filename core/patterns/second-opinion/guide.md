# Second opinion: guide

Before you accept your next real change, have a reviewer that did not write it look at the diff, and act on what it finds.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: an independent reader catches what the author missed.

## 1. Pick a real change

Think of a change your agent has made that you are about to commit or open as a pull request.

- If you have no such change in front of you, **stop here**. There is no exercise to do and nothing to recognize; come back with your next real diff.

## 2. Choose an independent reviewer

The session that wrote the change is not independent: asking it "is this right?" gets it agreeing with itself. Pick one of:

- your own review agent or command, if you have one;
- your agent's built-in review command, if it has one (Claude Code has `/review`);
- a different model;
- a **fresh session** that did not write the code.

If you are not sure what your agent supports, ask it to check its actual commands rather than guessing.

## 3. Take the step: request the review

Ask the reviewer to review the real diff, for example:

> Review the changes on this branch for bugs, missed edge cases and behaviour callers would notice. You did not write them. List each finding with file and line, and say which must be fixed.

## 4. Use what it found

Read the findings. Fix the ones that matter (ask your implementing session to make the fixes), and answer the ones you disagree with, saying why. If the review is clean, accept it knowing what it checked.

**Done:** you requested an independent review of the change and it returned its findings or an evidenced clean result before you accepted the change. That is what this pattern recognizes as Seen once detection is available. Acting on its findings (or accepting its clean result knowing what it checked) is the follow-through that later stages count; ignoring them never counts toward those stages.

**Not done yet:** if you only read this guide, asked the session that wrote the change to check itself, or accepted the change before the review returned, the pattern has not happened yet. That is fine. Nothing is recorded against you; the next step is still to get one independent review used on a real change.

## Later

Once several patterns happen on their own, an independent review can run automatically from a hook, CI job or pull request reviewer, so every change gets one. That comes later, and you still need to act on what it finds.
