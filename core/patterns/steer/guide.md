# Steer, Don't Stop: guide

When your agent heads the wrong way, don't just stop it: tell it what is wrong, or why, so it has something to change.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: an explained redirect usually saves several rounds of retries.

## 1. Work on a real task

Use your next real task in your own project with your agent: a bug, a feature, a refactor. Work as usual and keep half an eye on what the agent is doing.

If you have no task to work on right now, **stop here**. There is no exercise to do and nothing to recognize; come back when you next work with your agent.

## 2. Notice a real wrong turn

Watch for a moment the agent actually goes wrong: it edits the wrong file or layer, chases the wrong cause, or tries the same failing fix again. A change you would simply prefer for taste, when nothing is wrong, is not this moment.

If the agent never goes wrong during the task, that is fine: **stop here**. Nothing is recorded against you.

## 3. Take the step: redirect with a reason

Interrupt if you need to, then say in a sentence what is wrong or why, and what to do instead. For example:

> Don't change the schema; the slow part is the query. Look at how the report query joins orders.

or

> The limit belongs in Options because callers set it per request, not in the global config.

If you are unsure what is wrong, ask the agent to say what it thinks went wrong first, then correct that.

**Done:** you redirected the agent with a correction that explains what was wrong or why. That is this pattern. Then watch its next response: when it changes course to follow your correction, that is the follow-through that later stages count. If it carries on with the same approach, say so plainly and repeat the reason.

**Not done yet:** if you only said "no", "stop", "try again" or "still failing", or you interrupted and then said "continue", or you read this guide and answered its questions without the agent going wrong, the pattern has not happened yet. That is fine. Nothing is recorded against you; try it at the next real wrong turn.

## Later

If you find yourself giving the same correction in session after session, write the reason into an instruction or command so the agent starts from it (Fix the harness). That comes later, once several patterns happen on their own, not as a shortcut.
