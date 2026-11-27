# Evidence, not claims: guide

When the agent summarises its work, check the summary against the output above it, and challenge anything that does not match.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a summary that disagrees with the output is the cheapest bug to catch.

## 1. Use a real task that runs checks

On your next real coding task in your own project, let the agent make a change and run the tests, build or linter as it normally would.

If nothing you are doing right now runs any checks, **stop here**. There is no exercise and nothing to recognize; come back on a task where checks run.

## 2. Compare the summary with the output

When the agent says something like "all tests pass" or "done, all four cases handled", scroll up to the actual output and compare:

- Do the pass/fail counts match the summary?
- Are any tests **skipped** or **errored** that the summary does not mention?
- Did as many cases run as you expected?

If the output is cut off, ask the agent to run the check again and show the full result rather than guessing.

## 3. Take the step: challenge a real gap

If the output contradicts the summary, say so specifically, for example:

> You said all pass but 3 failed above. Fix those first.

or

> I expected four cases and only three ran. Where is the fourth?

**Done:** you pointed at a real gap between the summary and the output, and the agent then dealt with it (fixed the failures, ran the missing case, or showed why the result was expected).

**Not done yet:** if the summary matched the output, there was nothing to challenge, and that is fine: it is not a miss and nothing is recorded. If you noticed a gap but accepted the summary anyway, or stopped after reading this guide, the pattern has not happened yet. Nothing is recorded against you; compare the next summary you get.

## Later

Once several patterns happen on their own, you can make the harness insist on evidence: an instruction rule or a Stop hook requiring the actual check output alongside any completion claim. That comes later, not as a shortcut.
