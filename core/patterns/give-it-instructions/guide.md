# Give it instructions: guide

Give your agent the build commands and conventions for a project you actually work in, in a file it loads at the start of every session.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: the file helps from the next session on.

## 1. Pick a real repository

Think of the repository you have worked in most in the last few weeks.

- Does it already have a `CLAUDE.md`, `AGENTS.md` or rules file with real content (how to build, how to test, conventions)? If so, you already do this here. Pick another repository you use regularly, or stop: there is nothing to do.
- If you have no repository you work in regularly, **stop here**. There is no exercise to do and nothing to recognize; come back when a project becomes regular work.

## 2. Draft a starting file

In that repository, ask your agent to draft an instruction file. If your agent has a command for this (Claude Code has `/init`), use it. If you are not sure which file your agent reads, ask it:

> Which instruction file do you load at the start of a session in this repository, and where should it live?

Do not accept the draft as is. A generated file is a starting point, and a file nobody reviewed does not count.

## 3. Review it and add what you keep correcting

Read the draft with your agent:

- Are the build and test commands right? Fix any that are not.
- Remove anything vague or wrong.
- Add **the one convention you most often have to correct** in this project: a naming rule, a library to use or avoid, where tests go.

Ask your agent to save the file only when you are happy with it. Commit it if the repository is shared.

## 4. Take the step: use it on your next task

Start a **new session** in that repository and do a real task. Early on, ask something only the file answers, for example:

> How do I run this project's tests?

**Done:** the agent answers from the file in a fresh session. That loaded, reviewed file in a repository you use regularly is what this pattern recognizes once detection is available.

**Not done yet:** if you stopped after reading this guide or answering its questions, or the file was generated but not reviewed, or no new session loaded it, the pattern has not happened yet. That is fine. Nothing is recorded against you; the next step is still to review the file and use it in a new session.

## Later

Once several patterns happen on their own, a user-level instruction file with the conventions you carry between projects can make every repository start with them. That comes later. It does not replace a project's own file.
