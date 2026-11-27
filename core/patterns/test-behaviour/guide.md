# Test behaviour: guide

On your next real change to an API or user flow, ask for one check written from the caller's side, and run it.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a caller-side check catches the change that passes unit tests but breaks someone downstream.

## 1. Pick a real change that callers will notice

Think of a change you are making now, or next, to something other code or people rely on: an endpoint, an export format, a command's output, emails or events it sends, a user flow.

- If your current work changes nothing a caller or user would notice, **stop here**. There is no exercise to do and nothing to recognize; come back on your next API or flow change.

## 2. Name the caller and what they rely on

Ask your agent:

> Who calls or uses the behaviour this change touches, and what exactly do they rely on: inputs, outputs, side effects?

Correct the list from what you know about the callers. This is the part only you can supply.

## 3. Take the step: request one caller-side check

Ask for **one** check written from the caller's side, before or alongside the change, not a test that mirrors the code afterwards. For example:

> Write a contract test for the export that asserts the columns and types the billing client reads. Show me the test before running it.

or

> Record the emails it sends in the test and show me.

Your agent can use whatever test tool the project already has; what matters is what the check asserts. If it records output or a snapshot, **read it** before accepting it.

## 4. Run it

Have the agent run the check and show you the result. If it fails, that is the check doing its job: fix the change or the expectation, deliberately.

**Done:** you requested or wrote a behaviour-level check (or reviewed its recorded output) and it was run. That is what this pattern recognizes once detection is available.

**Not done yet:** if you only read this guide, discussed callers without a check being written and run, accepted tests the agent wrote after the code without asking for caller-side ones, or accepted a regenerated snapshot without reading it, the pattern has not happened yet. That is fine. Nothing is recorded against you; the next step is still one caller-side check, run, on a real change.

## Later

Once several patterns happen on their own, the behaviour checks for your APIs and flows can run automatically from a hook or CI on every change. That comes later, and it does not replace deciding which behaviour matters.
