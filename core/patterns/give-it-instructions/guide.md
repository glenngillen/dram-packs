# Give it instructions: guide

Give your agent the build commands and conventions for a project you actually work in, in a file it loads at the start of every session.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: the file helps from the next session on.

## 1. Pick a real repository

Think of the repository you have worked in most recently: one with **at least three of your main sessions** in the last few weeks. Two sessions do not make a repository part of this pattern; three do. (Subagent sessions and Dram's own analysis sessions do not count toward the three.)

- Does it already have a `CLAUDE.md`, `AGENTS.md` or rules file with real content (how to build, how to test, conventions)? A file's name or existence alone is not enough: first confirm that your agent actually loads it, by asking in a new session in that repository:

  > Which instruction files did you load at the start of this session? Quote one build or test command from them.

  If it names the file and quotes from it, you already do this here: pick another repository with at least three of your sessions, or stop, because there is nothing to do. If it does not load the file, or quotes something else, continue to step 2 and work out with your agent which file it does read.
- If you have no repository with at least three of your sessions, **stop here**. There is no exercise to do and nothing to recognize; come back when a project becomes regular work. A file you add in a repository with fewer than three sessions is still useful, but it is below this pattern's boundary and would not count toward it.

## 2. Draft a starting file

In that repository, ask your agent to draft an instruction file (or, if a file exists but is not loaded, to find which file it reads and move or merge the content there). If your agent has a command for this (Claude Code has `/init`), use it. If you are not sure which file your agent reads, ask it:

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

**Done:** the agent answers from the file in a fresh session, in a repository with at least three of your main sessions in the last few weeks. That loaded, reviewed file in such a repository is what this pattern recognizes once detection is available.

**Not done yet:** if you stopped after reading this guide or answering its questions, or the file was generated but not reviewed, or no new session loaded it, the pattern has not happened yet. That is fine. Nothing is recorded against you; the next step is still to review the file and use it in a new session. If the repository has fewer than three of your sessions, the loaded file is still useful, but it does not yet meet this pattern's boundary; it would once you work there regularly.

## Later

Once several patterns happen on their own, a user-level instruction file with the conventions you carry between projects can make every repository start with them. That comes later. It does not replace a project's own file.
