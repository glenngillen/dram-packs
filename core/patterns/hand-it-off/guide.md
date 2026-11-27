# Hand it off: guide

When a session has grown long, write down what matters and carry it into a fresh session.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The handoff still helps the next session start well.

## 1. Find a long session on real work

You need a session in one of your own repositories that has grown long (it has been compacted, or the agent reports a very full context) and work you intend to continue.

If your current sessions are short, or the work is finished, **stop here**: there is nothing to hand off and nothing to recognize.

## 2. Ask for a handoff

In the long session, ask:

> Write a short handoff for continuing this work in a new session: the goal, the decisions we made and why, what is done, what is left, and any traps to avoid. Save it as a file in this repository and tell me its path.

Read it. Correct anything wrong or missing, especially decisions you do not want revisited.

## 3. Take the step: start fresh from it

Start a **new** session in the same repository, ideally soon (within a day). Do not resume or continue the old session; that brings the long context back. Make your first prompt point at the handoff:

> Read HANDOFF.md and continue from where it says we are.

(Use your file's actual path.) If you are not sure how your tool starts a new session rather than resuming, ask your agent.

**Done:** a fresh session in the same repository started from the handoff, and the agent continued the work from it. That is what this pattern recognizes once detection is available.

**Not done yet:** if you wrote the handoff but never started a fresh session from it, or you resumed the old session instead, or you only read this guide, the pattern has not happened yet. That is fine. Nothing is recorded against you; the next step is to start a fresh session that reads the handoff.

## Later

Once several patterns happen on their own, a hook or saved command can write the handoff for you when a session gets long. That comes later and does not replace starting fresh from it.
