# Learn from production: guide

Next time production tells you something is wrong, give your agent the actual signal and get a check that would catch it again, before the fix.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The habit still pays off: the next regression gets caught by a test instead of an alert.

This guide never fetches production logs or connects to your error or alerting tools. You bring the signal yourself, redacted.

## 1. Find a real production problem

Think of a real alert, error or log line from a service you work on that runs in production, recent or still open.

- If the problem already has a fix with a test that reproduces it, you already did this. Pick another, or stop.
- If you do not work on a production service, or there is no real production problem to hand, **stop here**. There is no exercise to do and nothing to recognize.

## 2. Redact the signal

Copy the error message, stack trace or log excerpt. Remove credentials, tokens, customer names and identifiers. Keep the parts that show what failed.

## 3. Take the step: signal first, then a reproducing test

In the service's repository, give your agent the redacted signal and ask for the test first:

> Here's the error from the alert: [redacted error]. Write a test that reproduces it and show me it failing, then fix it so the test passes.

Check that the test really fails for the reason in the error before you accept the fix.

**Done:** the fix you keep includes a new test (or other check) that would catch this problem next time, and your request carried the real signal. That is what this pattern recognizes once detection is available.

**Not done yet:** if you described the problem in your own words without the signal, or the fix shipped without a new check, or you only read this guide and explained the alert, the pattern has not happened yet. Nothing is recorded against you; the next step is still to bring the real signal to the next fix.

## Later

Once several patterns happen on their own, your team may want alerts to start this agent work automatically, with narrow permissions and a person reviewing each fix. That comes later.
