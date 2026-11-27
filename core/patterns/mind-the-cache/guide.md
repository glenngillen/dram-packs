# Mind the cache: guide

Before a real long break from a big session, have the agent write a short handoff. When you come back, start a fresh session from it.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a fresh start from a handoff avoids sending a large cold context again.

## 1. Check that it applies

This matters when both are true of a session you are about to leave:

- the context is large: more than 150,000 tokens by default ([`large_context_tokens`](../../reference/parameters.md#large_context_tokens));
- you will be away longer than the cache lasts: more than one hour by default ([`cache_gap`](../../reference/parameters.md#cache_gap)).

If you are not sure how large the context is, ask your agent how this harness reports it. If your session is small, or your break is short, **stop here**: there is no exercise and nothing to recognize.

## 2. Ask for a handoff before the break

Ask your agent:

> I am about to take a long break. Write a short handoff to a file I choose: the goal, decisions made, what is done, what is next and anything I must not lose.

Read it. Add anything it missed.

## 3. Take the step: start fresh after the break

When you come back, start a new session (or `/clear` the old one) and point the agent at the handoff, for example "Read NOTES.md and continue from the next step".

**Done:** after a break longer than the cache lasts, you started fresh from the handoff instead of continuing the large session.

**Not done yet:** if you wrote the handoff but continued the old session when you came back, or your break was no longer than the cache lasts (the model's known cache lifetime when one is supplied; one hour is only the default when no lifetime is known), or you only read this guide, the pattern has not happened yet. That is fine. Nothing is recorded against you; try it before your next long break.

## Later

Once several patterns happen on their own, an end-of-day command or a Stop hook of your own can write the handoff for you. That comes later, not as a shortcut.
