# Evaluation Readiness

## Overview

Separate complete content from executable acceptance, preview readiness and proven stable quality. Requirements describe future checks; no test implementation or test run belongs to this phase.

## Requirements

- Preserve every positive and negative example from the supplied catalogue as a labeled acceptance scenario, including apparently redundant examples. Add boundary cases without deleting the original intent.
- Each pattern includes guided-success and guided-no-action scenarios. Mechanism patterns include in-place-but-unused, held and not-holding scenarios. Cover no applicable work and missing required evidence.
- Repository fixtures created during building must be invented, deterministic data. Do not copy staff/customer transcripts or private configuration into a public pack. Staff evaluation happens privately, with only non-sensitive aggregate readiness evidence retained.
- Use the existing collected-history fixture shape and current `cases.jsonl` contract where representable. If required data or expected results cannot be expressed, retain the complete scenario in prose and mark the corresponding executable case unevaluable with its precise dependency.
- Do not fabricate fixture fields, model answers or APIs and claim the CLI supports them. Recorded model responses test supported replay behavior, not the accuracy of an uncalled model.
- `none` means genuinely no applicable finding, not a detector which cannot run. Never relabel intended positives as `none` to make disabled code pass.
- Keep all unavailable cases visible. The existing evaluator's red verdict for patterns with no evaluable cases is expected until dependencies are met; do not patch the evaluator, hide cases or claim a green full-pack evaluation.
- Only enable Preview after all applicable recognition cases can run and pass. Stable additionally needs the source's field-quality bars below. All initial content remains disabled until support and readiness are evidenced.
- Record pack/rule versions, compatible CLI revision, evaluation date, actual commands, pass/fail/unevaluable counts, remaining gaps and review status in the eventual readiness notes. No placeholder metrics are reported as measured.

### Stable bars retained from the source

| Area | Required evidence |
| --- | --- |
| Copy | Intent, report, coach and guide wording reviewed |
| Guides | Three of three staff users perform the pattern in their real work and receive recognition |
| Model evaluation | Every catalogue case plus at least ten additional staff-history cases labeled by two reviewers; all correct in three runs on the quick model |
| Recognition precision | At most one false recognition among twenty reviewed recognitions (at least 95%) |
| Recognition recall | At least seven of ten deliberately performed instances (at least 70%) |
| Opportunities | At least seventeen of twenty opportunities judged useful; noisy opportunities permit Seen only until fixed |
| Verification | Fabricated/changed quotes, inappropriate attribution and out-of-window evidence rejected |
| Cost | Pattern share of the pass fits the budget at the ninetieth percentile; measure, do not assume |
| Held cases | At least eighteen of twenty applicable held cases correct; every recurrence fixture produces not holding |
| Case advice | At least eighteen of twenty misses have case-specific next-time and preventive advice with a faithful setup prompt |
| Code fixtures | Every evaluable configuration/transcript case correct, without a passing average masking a failure |
| Real configurations | Runs without errors on staff machines; agreement on every result in a sample of twenty |

## Acceptance Criteria

- [ ] No supplied catalogue example or guided boundary is lost.
- [ ] Disabled and unevaluable cases are explicitly reported without becoming passes.
- [ ] Synthetic automated evaluation and private human field evaluation are distinguished.
- [ ] No pattern is declared stable without the full applicable bar; unsupported patterns stay disabled.
- [ ] A bad or unavailable capability cannot be hidden by a successful negative fixture.
- [ ] Requirements-phase notes distinguish source inspection from validation or execution.

## Edge Cases

- Whole-pack evaluation may remain red while schema validation succeeds. The initial content-only deliverable can document this honestly; it cannot advertise a runnable preview release.
- Ambiguous source semantics are not resolved by choosing a convenient fixture label. Track the ambiguity before encoding a hard expectation.
- The source's privacy rule forbids real data in external artifacts even when a redaction process is available; use synthetic public cases and private staff evaluations.

## Dependencies

- The CLI's evaluator, fixture data model, recognition verifier and supported blocks.
- Staff review, live model evaluation, dogfooding, cost measurement and release approval are future activities, not performed in this requirements phase.
- No designated spec lint was found in the target repository guidance. Spec lint is not run; builds, unit tests, fixture suites and `pack eval` must not be substituted in this phase.

