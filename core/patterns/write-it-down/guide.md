# Write it down: guide

Turn a convention you keep correcting into a rule your agent loads every session.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The rule still helps from the next session on.

## 1. Find the correction you repeat

Think about your recent work in one project. What have you told the agent more than once? A formatting choice, a library to use, a command it must not run, where files go.

- If it is a **one-off bug** ("that function is wrong"), it is not a convention. Look for something that applies to future work.
- If nothing comes to mind and you have not corrected the agent on a convention lately, **stop here**. There is nothing to write down yet; come back when you notice yourself repeating a correction.

## 2. Ask your agent to record it

In that project, during real work, ask your agent to persist the rule. For example:

> We use tabs, not spaces. Add that to the instruction file you load.

If your agent supports a quick memory entry (Claude Code accepts a line starting with `#`), you can use that instead. If you are not sure which file it loads, ask it.

## 3. Check the wording

Ask to see the exact line before it is saved. Make it specific ("Indent with tabs in all source files") rather than vague ("format nicely"). Do not let the agent rewrite other rules at the same time.

## 4. Take the step

**Done:** the rule is saved in the instruction file because you asked for it. In a later session, when the agent does that kind of work and follows the rule without you saying it again, the rule is holding.

**Not done yet:** if you described the convention while reading this guide but did not ask for it to be saved, or you said "remember this" and no file changed, nothing has been written down yet. That is fine and nothing is recorded against you; the next step is still to ask for the rule to be saved.

## Later

If you find you are still correcting the same thing after it is written down, the rule may be unclear or not loaded. Fixing that, perhaps with a check rather than an instruction, is a later pattern (Fix the harness).
