# Set the expectations yourself: guide

Own the test for a real bug before the agent writes the fix, so the fix cannot decide what "passing" means.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a test you read first catches the fix that only looks right.

## 1. Pick the next real bug

Choose a bug you are about to fix in your own project, where a test can reproduce it.

- If you have no bug or feature with tests to work on right now, **stop here**. There is no exercise and nothing to recognize.

## 2. Ask for a failing reproduction, not a fix

> Write a test that reproduces this bug and show me it fails. Don't change the implementation yet.

Or write the test yourself and commit it.

## 3. Read the test

Check that the test describes what *should* happen, not what the code does today. Add the case you think is missing (an empty input, a boundary value). "ok, go" without reading it does not make it your expectation.

## 4. Take the step: ask for the fix

> Now make this test pass without changing the test.

**Done:** the test existed and you had read it before the fix, and the fix then made it pass. That is what this pattern recognizes once detection is available.

**Not done yet:** if you reviewed the test but the fix has not been made to pass it yet, or the tests were written alongside or after the code, the pattern has not happened yet. That is fine; nothing is recorded against you.

## Later

Once several patterns happen on their own, a test-first rule or command can make the agent stop for your review every time. It only counts when it is followed.
