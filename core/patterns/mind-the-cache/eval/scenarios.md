# Mind the cache: scenarios

Every acceptance scenario for `glenngillen/mind-the-cache`, in full. All people, repositories, files, token counts and times are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape carries no gap/context facts as pattern inputs, no cache lifetime and no session-start provenance, and the pattern names no block the pinned build runs.

Applicable work is every return to the same work after a gap over [`cache_gap`](../../../reference/parameters.md#cache_gap) from a context over [`large_context_tokens`](../../../reference/parameters.md#large_context_tokens). A fresh start is a hit; a cold resume is a miss.

## pos-1 Two-hour gap, then a fresh NOTES.md handoff

- kind: source-positive
- expect: seen
- Setup: in `quokka-api`, a session reaches 180,000 tokens. The person asks for a handoff in `NOTES.md` and leaves. Two hours later they start a new session: "Read NOTES.md and continue with the retry handler".
- Why: a qualifying gap (two hours) from a large context, then a fresh start from the handoff. The gap timestamps and the first prompt are the citations.

## pos-2 End-of-day handoff used next morning

- kind: mechanism-held
- expect: continuous
- Setup: the person's own `/end-of-day` command writes `HANDOFF.md`. In the window, each evening it runs in large `quokka-api` sessions (over 150,000 tokens), and each next morning the person starts a fresh session from the file. There is no cold resume of a large context in the window.
- Why: the mechanism is in place, applied before each qualifying break and held. No block reaches `continuous` in the pinned build.

## pos-3 /clear after lunch, re-pointed at the work

- kind: boundary
- expect: seen
- Setup: in `ibis-web`, a 200,000-token session pauses for 90 minutes. On return the person types `/clear`, then "Read docs/plan.md and pick up at step 4".
- Why: a fresh start after a qualifying break can be `/clear` as well as a new session.

## pos-4 Guided handoff and fresh start

- kind: guided-success
- expect: seen
- Setup: following the guide, the person in `kiwi-cli` (170,000 tokens) asks for a handoff before a three-hour meeting, then starts a new session from it afterwards.
- Why: the guided step on real work, completed by the later fresh start after a qualifying gap. Guided work earns Seen only.

## neg-1 Five-minute resume

- kind: source-negative
- expect: none
- Setup: in `quokka-api`, a 180,000-token session pauses five minutes and continues.
- Why: the gap is not over `cache_gap`; this is outside scope, neither a hit nor a miss.

## neg-2 Large context resumed after lunch

- kind: source-negative
- expect: opportunity
- Setup: in `ibis-web`, a 160,000-token session pauses for 75 minutes over lunch. The person returns and writes "ok, where were we? carry on".
- Why: a cold resume of a large context after a qualifying gap is a miss, not successful cache management. The opportunity cites "ok, where were we? carry on" and shows the measured API-priced rebuild cost if the CLI has usage and prices, otherwise no cost.

## neg-3 Exactly one hour

- kind: boundary
- expect: none
- Setup: in `kiwi-cli`, a 200,000-token session pauses exactly 1 hour and the person continues it.
- Why: `cache_gap` is strict "more than"; exactly one hour is outside.

## neg-4 Exactly 150,000 tokens

- kind: boundary
- expect: none
- Setup: in `kiwi-cli`, a session at exactly 150,000 tokens pauses two hours and the person continues it.
- Why: `large_context_tokens` is strict "more than"; exactly 150,000 is outside.

## neg-5 Small context after a long gap

- kind: boundary
- expect: none
- Setup: a 40,000-token session in `marmot-docs` resumes after three hours.
- Why: small context: outside applicable work.

## neg-6 Handoff written, cold context continued

- kind: guided-no-action
- expect: opportunity
- Setup: reading the guide in `quokka-api` (190,000 tokens), the person asks for a handoff in `NOTES.md` before a two-hour break, then on return continues the old session with "continue".
- Why: guided handoff creation without the fresh start is incomplete, and the return is a cold resume. The opportunity cites "continue".

## neg-7 No large context and no long break

- kind: no-applicable-work
- expect: none
- Setup: in the window, the person's sessions in `marmot-docs` stay under 50,000 tokens and never pause longer than twenty minutes.
- Why: no qualifying return. Not a miss.

## neg-8 Context size unknown

- kind: missing-evidence
- expect: none
- Setup: in `ibis-web`, a session resumes after two hours, but the record has no usage data, so the prior context size is unknown.
- Why: unknown context size is insufficient: no recognition, no miss, no cost.

## neg-9 Mechanism in place, cold resume anyway

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person's `/end-of-day` command wrote `HANDOFF.md` in `kiwi-cli` (210,000 tokens), but next morning they resumed the old session with "morning, continue".
- Why: in place and applied, but the handoff was not used and the large cold context was continued: not holding. The opportunity cites "morning, continue".

## neg-10 End-of-day command never run before a break

- kind: mechanism-unused
- expect: none
- Setup: the person defined `/end-of-day`, but no session in the window reached a large context before a long break.
- Why: configured, never applied: untested. Not Seen and not a miss.

## neg-11 Pricing unknown for a cold resume

- kind: missing-evidence
- expect: opportunity
- Setup: in `quokka-api`, a 170,000-token session resumes after two hours with "carry on", timestamps and token counts known, but the model has no price in the CLI's pricing data.
- Why: the gap and context are known, so the cold resume is a miss and cites "carry on". The cost is unknown, so the opportunity carries no cost line; nothing is estimated and no subscription charge is inferred.

## Scenarios the case format cannot label

### stage-boundary Fresh starts and cold resumes share one denominator

- kind: stage-boundary
- Setup: over four weeks the person has five qualifying returns: three fresh starts and two cold resumes.
- Expected: three of five (60%) with at least four qualifying returns meets [`most`](../../../reference/parameters.md#most) for Established. Had only cold resumes been counted, the fresh starts would be invisible.
- Why no case: `expect` has no `established` value.

### stage-boundary Known cache lifetime replaces the default

- kind: stage-boundary
- Setup: the CLI supplies a model's cache lifetime of five minutes as a fact. A 180,000-token session pauses 20 minutes and is resumed.
- Expected: the supplied lifetime replaces the one-hour default, so this return is applicable. Without that fact the one-hour default applies and it is outside.
- Why no case: needs a cache-lifetime fact the fixture shape does not have.
