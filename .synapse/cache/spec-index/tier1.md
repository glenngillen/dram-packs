# Spec Abstracts

Generated from specs/*.md. Read the referenced specs for authoritative detail.

## actionable-failures.md

**Title:** Make Failures Actionable

Source ID `actionable-failures`; Checking the work, rung 4. Feed failures back with enough detail for the agent to fix the problem. Intended detection is a code check.

## back-it-up-in-ci.md

**Title:** Back It Up in CI

Source ID `back-it-up-in-ci`; Checking the work, rung 7. Confirm agent changes reach the default branch through tested CI. Detection uses configuration and git/run evidence.

## brief-it.md

**Title:** Brief It

Source ID `brief-it`; Briefing, rung 1. Help the person give the agent the goal and the constraints or context needed to avoid guessing. Detection requires model judgement.

## checks-by-default.md

**Title:** Checks by Default

Source ID `checks-by-default`; Checking the work, rung 3. Recognize checks that run because the person's harness asks for them. Detection combines configuration checks with model judgement.

## clear-between-tasks.md

**Title:** Clear Between Tasks

Source ID `clear-between-tasks`; Context, rung 1. Reset working memory when changing to unrelated work. Detection requires model judgement with a genuine clear event.

## coaching-content.md

**Title:** Coaching Content

Provide useful, faithful wording and one guide per pattern, ready for the hosts that can render or launch it.

## core-catalogue.md

**Title:** Core Catalogue

Provide the complete initial Dram core pack: evidence-based coaching about a person's use of coding agents, expressed as 41 patterns in eight groups. This is a requirements draft for pack content, not an implementation of the CLI or the wider product.

## define-done.md

**Title:** Define Done

Source ID `define-done`; Briefing, rung 2. Establish how feature or bug-fix work will be judged before implementation. Detection requires model judgement.

## evaluation-readiness.md

**Title:** Evaluation Readiness

Separate complete content from executable acceptance, preview readiness and proven stable quality. Requirements describe future checks; no test implementation or test run belongs to this phase.

## evidence-not-claims.md

**Title:** Evidence, Not Claims

Source ID `evidence-not-claims`; Checking the work, rung 2. Challenge an agent's summary when the actual result contradicts it. Detection requires model judgement.

## fan-out.md

**Title:** Fan Out

Source ID `fan-out`; Delegation, rung 3. Run independent parts through parallel subagents and use their combined work. Detection requires model judgement.

## fix-the-harness.md

**Title:** Fix the Harness

Source ID `fix-the-harness`; Guides, rung 7. Recognize a recurring correction eliminated by a relevant harness change. Detection combines model judgement with configuration history.

## gate-done.md

**Title:** Gate Done

Source ID `gate-done`; display name `Gate "done"`; Checking the work, rung 5. Require a final check before an agent finishes. Intended detection is a code check.

## gate-each-step.md

**Title:** Gate Each Step

Source ID `gate-each-step`; Checking the work, rung 6. Catch issues through fast checks after edits or before commits. Intended detection is a code check.

## give-it-instructions.md

**Title:** Give It Instructions

Source ID `give-it-instructions`; Guides, rung 1. Recognize useful instructions loaded in repositories the person regularly uses. Intended detection is a code check.

## guard-destructive.md

**Title:** Guard Destructive Commands

Source ID `guard-destructive`; Safety, rung 3. Require effective protection around hard-to-undo commands. Intended detection is a code check.

## hand-it-off.md

**Title:** Hand It Off

Source ID `hand-it-off`; Context, rung 2. Carry decisions from a long session into a genuinely fresh one. Detection requires paired-session judgement and mechanism checks.

## hands-off.md

**Title:** Hands Off

Source ID `hands-off`; Delegation, rung 4. Run a trusted owned workflow unattended and use its output. Detection combines code facts with model judgement.

## harness-carries-it.md

**Title:** Let the Harness Carry It

Source ID `harness-carries-it`; Economics, rung 3. Establish that a lighter model's routine work passes checks and survives. Detection is specified as code checks plus git evidence.

## isolate-the-run.md

**Title:** Isolate the Run

Source ID `isolate-the-run`; Delegation, rung 5. Keep unattended or parallel runs from interfering with other working copies. Intended detection is a code check.

## keep-it-lean.md

**Title:** Keep It Lean

Source ID `keep-it-lean`; Guides, rung 3. Suggest reviewing conflicting or measurably expensive instructions while preserving valuable rules. Detection combines model contradiction judgement with code-computed cost.

## keep-secrets-out.md

**Title:** Keep Secrets Out

Source ID `keep-secrets-out`; Safety, rung 1. Keep secret files outside the agent's reach and credentials out of prompts. Intended detection is a local code check.

## learn-from-production.md

**Title:** Learn From Production

Source ID `learn-from-production`; Checking the work, rung 11. Turn actual production signals into agent fixes with a regression check. Detection requires model judgement.

## mind-the-cache.md

**Title:** Mind the Cache

Source ID `mind-the-cache`; Economics, rung 2. Avoid rebuilding large cold contexts after long breaks. Intended detection is a code check.

## outcome-content.md

**Title:** Outcome Content

Document the five intended quality measures and their group associations without inventing unsupported measurements or formulas.

## own-the-expectations.md

**Title:** Set the Expectations Yourself

Source ID `own-the-expectations`; Briefing, rung 4. Separate the expectations from an implementation that could otherwise define its own success. Detection uses model judgement and git evidence.

## pack-compatibility.md

**Title:** Pack Compatibility

Keep the new content consumable by the existing Dram pack loader without changing the CLI or implying that a schema-valid definition is an implemented detector.

## pattern-evidence.md

**Title:** Pattern Evidence

Specify the evidence every pattern's authoring content must demand. These are recognition requirements for future activation, not new packet or verifier APIs implemented in this repository.

## pattern-parameters.md

**Title:** Pattern Parameters

One table of the tunable defaults that pattern definitions depend on. The user decided that the source's worked examples become provisional defaults, and approved proposed defaults where the source gives no example. Every value is tunable: it is a starting point to calibrate duri...

## pattern-progression.md

**Title:** Pattern Progression

Specify the progression content: stages, the automation gate and the stage-dependent completion rule. The user decided to keep stages with automation gating. The current CLI supports milestones only, so this content is documented in prose. This file does not authorize a new stage...

## plan-first.md

**Title:** Plan First

Source ID `plan-first`; Briefing, rung 3. Recognize the person's review of a plan before a multi-file change. Detection uses model judgement, plus configuration checks for its mechanism.

## point-dont-paste.md

**Title:** Point, Don't Paste

Source ID `point-dont-paste`; Context, rung 3. Give precise relevant context instead of broad exploration or excessive pasted material. Detection requires model judgement.

## prove-it.md

**Title:** Prove It

Source ID `prove-it`; Checking the work, rung 1. Ask for evidence after an agent reports a code change done. Detection requires model judgement.

## requirements-evidence.md

**Title:** Requirements Evidence

Source record for this requirements draft. The user's full production spec and pack-only scope decision are sufficient primary evidence; failure to retrieve its original web artifact is no longer a content gap.

## reuse-your-harness.md

**Title:** Reuse Your Harness

Source ID `reuse-your-harness`; Guides, rung 6. Recognize the person's maintained harness following them across repositories. Intended detection is a code check.

## right-cadence.md

**Title:** Check at the Right Cadence

Source ID `right-cadence`; Economics, rung 4. Match check frequency to the work and model without removing the final quality gate. Intended detection is a code check.

## right-size-it.md

**Title:** Right-size It

Source ID `right-size-it`; Economics, rung 1. Intentionally choose a lighter model for routine work. This is model selection, not the existing IaC resource-sizing pattern. Detection combines judgement with model provenance.

## sandbox-autonomy.md

**Title:** Sandbox Autonomy

Source ID `sandbox-autonomy`; Safety, rung 4. Contain unattended or broadly permissioned runs. Intended detection is a code check.

## save-it.md

**Title:** Save It

Source ID `save-it`; Guides, rung 4. Turn repeated requests into the person's own reusable command or skill. Detection combines model similarity judgement with ownership/run checks.

## schedule-the-clean-up.md

**Title:** Schedule the Clean-up

Source ID `schedule-the-clean-up`; Checking the work, rung 10. Use scheduled agent maintenance whose output is acted on. Intended detection is a code check.

## scope-permissions.md

**Title:** Scope Permissions

Source ID `scope-permissions`; Safety, rung 2. Grant the tools/commands the work needs without broad approval. Intended detection is a code check.

## script-it.md

**Title:** Script It

Source ID `script-it`; Guides, rung 5. Use deterministic tooling for mechanical edits instead of repeating manual agent edits. Detection combines judgement with execution/configuration evidence.

## second-opinion.md

**Title:** Second Opinion

Source ID `second-opinion`; Checking the work, rung 8. Obtain and use an independent review before accepting a change. Detection combines model judgement with review provenance.

## set-checkpoints.md

**Title:** Set Checkpoints

Source ID `set-checkpoints`; Correcting course, rung 2. Require a decision before a risky or hard-to-undo step. Detection uses model judgement and configuration checks.

## size-it.md

**Title:** Size It

Source ID `size-it`; Delegation, rung 1. Break large work into achievable tasks. Detection requires model judgement.

## split-it-up.md

**Title:** Split It Up

Source ID `split-it-up`; Delegation, rung 2. Delegate a side task intentionally. Detection combines model judgement with agent provenance.

## steer.md

**Title:** Steer, Don't Stop

Source ID `steer`; Correcting course, rung 1. Diagnose and redirect a wrong approach rather than merely stopping it. Detection requires model judgement.

## test-behaviour.md

**Title:** Test Behaviour

Source ID `test-behaviour`; Checking the work, rung 9. Check observable behavior that callers or users rely on. Detection requires model judgement.

## two-at-once.md

**Title:** Two at Once

Source ID `two-at-once`; Delegation, rung 6. Use waiting time for independent work in another isolated active session. Detection combines model judgement and timing facts.

## write-it-down.md

**Title:** Write It Down

Source ID `write-it-down`; Guides, rung 2. Turn a corrected convention into instructions instead of repeating it. Detection requires model judgement.

