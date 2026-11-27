# Set Checkpoints: scenarios

Every acceptance scenario for `glenngillen/set-checkpoints`, in full. All people, repositories, commands and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs model judgement of the checkpoint request and the person's decision, the request/stop/decision sequence, risk classification and effective ask rules, and names no block the pinned build runs. The pinned `permission_rule` block is deny-only, so an ask rule cannot be bound. The scenarios are kept in full so they can become fixtures when those capabilities exist.

Applicable work is a risky decision point (migration, deploy, deletion, public API change) in the person's main session.

## pos-1 "Ask before running it", stop, "Run it, skip the backfill"

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, the person writes "Draft the migration and ask before running it". The agent writes `migrations/0042_add_region.sql`, does not run it, and asks "Ready to run the migration; it also backfills 2M rows. Proceed?" The person replies "Run it, skip the backfill". The agent runs the migration without the backfill.
- Why: request, actual stop and the person's decision, in that order.

## pos-2 Ask rule on `db:migrate` stopped the agent twice

- kind: mechanism-held
- expect: continuous
- Setup: the person's team settings in `quillmark` include an ask-permission rule on `rake db:migrate`, in place all window, and sessions ran in normal permission mode. Twice in the window the agent tried to run `rake db:migrate`; both times the rule stopped it and the person approved (once with "yes, but run it on staging first").
- Why: in place, applied (it stopped the agent) and held (every covered step stopped and decided). No block reaches `continuous` in the pinned build, and the ask rule cannot be bound: `permission_rule` accepts deny only.

## pos-3 Guided checkpoint before a real deploy

- kind: guided-success
- expect: seen
- Setup: following the guide before a real deploy in `marlin-cli`, the person writes "Prepare the release and show me what will change. Wait for my go-ahead before publishing." The agent prepares it and stops. The person replies "go ahead".
- Why: the guided step on real risky work, completed by the stop and the decision. Guided work earns Seen only.

## pos-4 Checkpoint honoured, person declines

- kind: boundary
- expect: seen
- Setup: in `tidepool-web`, the person writes "Before deleting the old `legacy_cart` table, stop and ask me." The agent stops and asks. The person replies "Not yet; leave it until next release."
- Why: the decision can be "no". The request, the stop and the person's decision complete Seen.

## neg-1 Unprompted "Shall I proceed?"

- kind: source-negative
- expect: none
- Setup: in `orchard-jobs`, the person asks for a schema change with no checkpoint request. Before running the migration, the agent asks on its own "Shall I proceed?". The person says "yes" and the migration runs without trouble.
- Why: a spontaneous agent question is not the person's checkpoint, so not Seen. Nothing was undone, so this is not the coaching opportunity either.

## neg-2 Unanswered checkpoint

- kind: source-negative
- expect: none
- Setup: in `fern-docs-api`, the person writes "ask me before deploying". The agent stops and asks; the person never answers and the session ends.
- Why: a checkpoint nobody answered is not complete: there is no person decision.

## neg-3 Requested stop bypassed

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the instruction file in `basalt-sdk` says "stop and ask before running migrations", in place all window. In one session the agent runs `make migrate` without stopping. The person writes "I said to ask first; roll that back" and the migration is reverted.
- Why: a covered risky step went ahead without the stop: not holding, and not Seen. The unapproved step was undone, so it is an opportunity citing the person's "roll that back" prompt.

## neg-4 Automatic approval answered the ask rule

- kind: boundary
- expect: none
- Setup: in `heron-service`, an ask rule covers `./deploy.sh`, but the session runs in an auto-approve mode, so the deploy proceeds with no person prompt. Nothing is undone.
- Why: automatic approval cannot stand in for the person's decision: not Seen, and for the mechanism not holding. With nothing undone and no person moment to cite, no opportunity.

## neg-5 Ask rule in place, never reached

- kind: mechanism-unused
- expect: none
- Setup: the person added an ask rule on `terraform apply` in `slate-ui` settings, but no session in the window reached a deploy or apply step.
- Why: configured but never applied: untested, not held and not a miss.

## neg-6 Guided checkpoint wording, step never reached

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person writes in `kestrel-app` "draft the migration and ask before running it". The agent drafts part of it; the person ends the session before the migration is ready.
- Why: wording alone, without the actual stop and decision, is incomplete. Not a miss.

## neg-7 Unapproved deploy rolled back

- kind: boundary
- expect: opportunity
- Setup: in `pewter-tools`, the person asks "fix the config so it's ready to deploy, but do not deploy it yet". The agent edits the config and then runs the deploy anyway. The person sees an error and writes "roll it back, that broke staging".
- Why: the request was preparation only, so the deploy went ahead without the person's approval, and the person undid it: the coaching moment. Unapproved rests on the explicit "do not deploy it yet", not on the failure or rollback. The opportunity cites the preparation-only request and "roll it back".

## neg-8 Stop requested before a non-risky step

- kind: boundary
- expect: none
- Setup: in `amber-lib`, the person writes "ask me before running the unit tests"; the agent stops, the person says "go".
- Why: running unit tests is not a risky decision point. Risk is evidence-based; not every command is dangerous. No applicable work.

## neg-9 No risky step

- kind: no-applicable-work
- expect: none
- Setup: in the window, the person's sessions in `saffron-jobs` only edited code and ran tests. No migration, deploy, deletion or public API change.
- Why: no applicable work; nothing is reported.

## neg-10 Record truncated after the stop

- kind: missing-evidence
- expect: none
- Setup: in `cobalt-infra`, the person writes "ask before applying". The agent stops and asks; the record is truncated before any later person prompt.
- Why: whether the person decided cannot be seen. Insufficient, not a miss and not a recognition.

## Scenarios the case format cannot label

### stage-boundary Forming credited to the week of the decision

- kind: stage-boundary
- Setup: a checkpoint request on Sunday of week 1 (person's local time); the agent stops and the person decides on Monday of week 2. Another complete checkpoint in week 4.
- Expected: Seen in week 2, when the decision completed the checkpoint. For Forming, instances in weeks 2 and 4: two distinct weeks of the last four.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Ask rule held once, bypassed once

- kind: stage-boundary
- Setup: an ask rule on `db:migrate` stopped the agent once in week 1 (decided), and in week 3 a permission-skipping mode let the migration run without a stop.
- Expected: applied, but not holding in the window: Continuous is not awarded. The week-1 decision can still support Seen.
- Why no case: the case format cannot express mixed held and not-holding evidence within one window.
