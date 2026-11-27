# Write it down: scenarios

Every acceptance scenario for `glenngillen/write-it-down`, in full. All people, repositories and file contents are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the collected-history fixture shape has no field for person command provenance, instruction-file diffs or correction classification, and the pattern names no block the pinned build runs.

## pos-1 "We use tabs. Add that to CLAUDE.md"

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api` the agent indents a new file with spaces. The person writes: "We use tabs. Add that to CLAUDE.md." The agent adds "Indent with tabs in all source files." to the committed `CLAUDE.md`.
- Why: a convention correction, the person's request to persist it, then a substantive rule added. Cites the request and the edit.

## pos-2 Persisted `#` memory entry

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, after the agent proposes running a migration, the person types `# never run migrations locally`. The entry is written to the project's instruction file as a rule.
- Why: a person-entered memory command followed by a persisted rule.

## pos-3 Guided request, persisted

- kind: guided-success
- expect: seen
- Setup: the person follows the guide in `tidepool-web` on real work, names "always use the shared date helper", asks the agent to add it to `AGENTS.md`, checks the wording and the rule is saved.
- Why: the person's deliberate request and the persisted rule. Guided work earns Seen only.

## pos-4 Rule held in later relevant work

- kind: mechanism-held
- expect: continuous
- Setup: the tabs rule from pos-1 is in place in `CLAUDE.md`. In three later sessions in `lanternfish-api` the agent creates new source files; each session loaded `CLAUDE.md` and every file uses tabs. The person never mentions indentation again.
- Why: in place, applied to relevant later work, and held without renewed correction.
- Note: no block reaches `continuous` in the pinned build.

## neg-1 Unprompted instruction rewrite during refactoring

- kind: source-negative
- expect: none
- Setup: during a refactor in `marlin-cli`, the agent rewrites `CLAUDE.md` on its own, adding three rules. The person never asked it to and had corrected no convention.
- Why: unprompted agent instruction edits are excluded, and with no correction there is no applicable work.

## neg-2 "Remember to use tabs" without an edit

- kind: source-negative
- expect: none
- Setup: in `orchard-jobs` the person writes "Remember to use tabs." The agent acknowledges; no instruction file changes. The tabs convention is corrected only in this one session.
- Why: "remember this" without a persisted change is not recognized. One correction in one session does not meet the two-session coaching trigger, so no opportunity either.

## neg-3 Same convention corrected in two sessions

- kind: source-negative
- expect: opportunity
- Setup: in `orchard-jobs`, the person writes "use pnpm, not npm" on Monday and "pnpm, please, not npm" on Thursday. No rule is persisted.
- Why: the two-session coaching trigger. The opportunity cites the person's Thursday correcting prompt.

## neg-4 Guided answer with no request

- kind: guided-no-action
- expect: none
- Setup: the person reads the guide and replies "the thing I keep correcting is import order", then ends the session without asking for a rule. No other correction of import order in the window.
- Why: describing a convention without requesting or persisting it earns nothing; a guide answer is not a correction in real work.

## neg-5 No convention corrections

- kind: no-applicable-work
- expect: none
- Setup: in the window the person's corrections in `fern-docs` are all one-off defects ("that link is broken", "the heading level is wrong").
- Why: one-off defects are not conventions, so there is no applicable work.

## neg-6 Typo-only edit to CLAUDE.md

- kind: source-negative
- expect: none
- Setup: the person asks the agent to "fix the typo in CLAUDE.md"; it changes "biuld" to "build".
- Why: typo-only edits are excluded; no convention was recorded.

## pos-5 Rule in place, no later relevant work

- kind: mechanism-unused
- expect: seen
- Setup: in `basalt-sdk` the person asks for "never commit generated protobuf files" to be added to `CLAUDE.md`; it is. No later session in the window touches generated files.
- Why: Seen from the request and edit; untested for Continuous because no later relevant work ran.

## neg-7 Rule in place but correction recurs

- kind: mechanism-not-holding
- expect: opportunity
- Setup: `kestrel-app` has "Use the shared logger, never console.log" in `CLAUDE.md`, added at the person's request. Two weeks later, a session loads the file, the agent adds `console.log` calls and the person writes "again: use the shared logger".
- Why: the rule was in place and applied, and the convention needed correcting again: not holding. The opportunity cites the person's renewed correction.

## neg-8 Session records truncated

- kind: missing-evidence
- expect: none
- Setup: in `amber-lib` the person corrects quoting style; the session record is truncated after that prompt, so whether a rule was requested or saved cannot be seen.
- Why: truncated evidence is insufficient, not a miss and not a recognition.

## neg-9 Auto-memory written without a request

- kind: boundary
- expect: none
- Setup: in `slate-ui` the person corrects a naming convention once. The agent, unasked, writes the convention to its own auto-memory.
- Why: agent-initiated memory is not the person's deliberate request; one correction is below the coaching trigger.

## Scenarios the case format cannot label

### stage-boundary Seen now, Forming once kept and applied

- kind: stage-boundary
- Setup: pos-1 in week 1 (rule added), the rule followed in relevant work in week 3; pos-2 in week 2, its rule followed in week 2.
- Expected: Seen from week 1. Forming once instances' follow-through finishes in two distinct weeks (weeks 2 and 3 here), credited to the week each follow-through finished.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Reverted rule

- kind: stage-boundary
- Setup: a rule added at the person's request is removed by a later unrelated commit two days later.
- Expected: Seen (the deliberate act qualified); never counts toward Forming or Established, and cannot support Continuous.
- Why no case: as above.
