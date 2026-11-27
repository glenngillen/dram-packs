# Check at the right cadence: scenarios

Every acceptance scenario for `glenngillen/right-cadence`, in full. All people, repositories, models, hooks and commands are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no model-conditioned configuration, no hook execution records with their model and no configuration history, and the pattern names no block the pinned build runs.

Applicable work is a repository with per-step checks and a final gate, where the person's work used more than one model tier.

## pos-1 Lighter-subagent per-edit type checks, premium Stop gate

- kind: source-positive
- expect: seen
- Setup: in `grebe-app`, the person's own lighter `implementer` subagent has a hook running `tsc --noEmit` after each edit; the premium main session runs no per-edit check, and the team Stop hook runs `pnpm test` at the end. In the window the subagent's type check runs after its edits, the main session edits without it, and the Stop hook runs on both.
- Why: person-configured differentiation, both observed model paths running as configured, final gate preserved. Citations: the configuration and runs under both variants.

## pos-2 Held across the window

- kind: mechanism-held
- expect: continuous
- Setup: the same configuration in `grebe-app` and `petrel-api`. Every applicable session in the window ran with its tier's cadence, both paths were observed in each repository, and the final gate ran on all work.
- Why: in place, applied and holding with the final gate. No block reaches `continuous` in the pinned build.

## pos-3 Guided review then a configured, observed change

- kind: guided-success
- expect: seen
- Setup: following the guide in `petrel-api`, the person reviews which checks ran, learns their harness supports per-subagent hooks, asks the agent to move the per-edit test run into the lighter subagent only, and keeps the Stop gate. Later sessions show both paths running as configured.
- Why: guided, configured and observed on real work. Guided work earns Seen only.

## neg-1 Full suite after every edit on every model

- kind: source-negative
- expect: none
- Setup: in `grebe-app`, a hook runs the full test suite after every edit in every session, whichever model is in use.
- Why: identical heavy checks everywhere are not this differentiated pattern. Not a miss either unless the opportunity condition below holds; the cadence is neutral here.

## neg-2 Only one observed model path

- kind: boundary
- expect: none
- Setup: in `skua-lib`, the differentiated configuration exists, but in the window only the premium main session ran; no lighter work happened.
- Why: only one observed path is insufficient for Seen. Untested, not a miss.

## neg-3 No checks at all

- kind: source-negative
- expect: none
- Setup: in `murre-tools`, there are no step checks and no final gate; sessions on both tiers edit freely.
- Why: no checks is never praised as efficiency and is outside this pattern's applicable work. Checking the work is the place to start.

## neg-4 Guided review without change or observed runs

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person asks which checks ran on recent work, reads the answer and keeps everything as it is.
- Why: reviewing cadence without configured and observed differentiated runs is incomplete. Keeping current checks is a valid decision; nothing is recorded.

## neg-5 Heavy premium step checks catching nothing

- kind: source-negative
- expect: opportunity
- Setup: in `petrel-api`, which has both per-step checks (Gate each step) and a Stop gate, the person's work in the window runs on two tiers: a premium main session and lighter subagents that, in the same window, update fixtures and docs in the same repository. The premium main session runs a four-minute integration suite after every edit, as does the lighter tier. Over the window the suite ran 60 times on premium work and caught no failures; the Stop gate still ran at the end of each task. The person's prompt "refactor the billing module" started that work.
- Why: the repository is applicable: both kinds of check and more than one model tier in use. An opportunity phrased neutrally: what ran and what it caught, beside the outcomes, citing the person's prompt. It does not say the checks are worthless or that premium work needs no checks.

## neg-6 Final gate removed to save time

- kind: boundary
- expect: none
- Setup: in `skua-lib`, the person keeps per-edit checks on the lighter subagent but deletes the Stop hook; premium work now runs with no checks.
- Why: removing the final gate is not a cadence. Without both step checks and a final gate the repository is outside applicable work.

## neg-7 Single model only

- kind: no-applicable-work
- expect: none
- Setup: in the window, all the person's work in `grebe-app` ran on one model.
- Why: there is no second tier to differentiate. Not a miss.

## neg-8 Hook records unavailable

- kind: missing-evidence
- expect: none
- Setup: `petrel-api` has differentiated configuration, but the session records carry no hook execution entries, so which checks ran under which model is unknown.
- Why: insufficient evidence: unassessed, not a miss and not a recognition.

## neg-9 Configured but premium path still runs step checks

- kind: mechanism-not-holding
- expect: none
- Setup: in `grebe-app`, the configuration should skip per-edit tests in the premium session, but a user-level hook still runs them there, so both tiers run the same cadence.
- Why: in place but premium work ran with the lighter tier's cadence: not holding. No person-authored moment shows a missed step, so no opportunity is reported.

## neg-10 Differentiated config never used

- kind: mechanism-unused
- expect: none
- Setup: the person configured per-subagent checks in `murre-tools`, but no session there in the window.
- Why: configured, never applied: untested.

## Scenarios the case format cannot label

### stage-boundary Escape past the final gate

- kind: stage-boundary
- Setup: in `grebe-app`, with the differentiated cadence held, a type error in premium work passes the final gate (which runs tests, not types) and is fixed after merge.
- Expected: reported beside the pattern as an Escapes outcome; the mechanism is not holding for that window because a problem the reduced checks would have caught escaped. No claim that the premium model was infallible.
- Why no case: the case format has no outcome expectation.
