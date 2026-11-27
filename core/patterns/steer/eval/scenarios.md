# Steer, Don't Stop: scenarios

Every acceptance scenario for `glenngillen/steer`, in full. All people, repositories, commands and outputs are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs model judgement that a person's correction explains what was wrong or why, interrupt attribution and judgement that the agent changed course, and names no block the pinned build runs. The scenarios are kept in full so they can become fixtures when those capabilities exist.

Applicable work is a moment in the person's main session where the agent went wrong: an interrupt, a failed or repeated attempt, or a wrong approach.

## pos-1 Interrupt, then "the limit belongs in Options"

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, the agent starts adding a `MaxRows` constant to `config/global.go`. The person interrupts and writes "the limit belongs in Options because callers set it per request". The agent removes the constant and adds a `Limit` field to `query.Options`, threading it through the handler.
- Why: an explained redirect at a wrong approach (Seen), and the agent changed course (follow-through, which also counts toward later stages in the week it finished).

## pos-2 "Don't change the schema; the slow part is the query"

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, the agent proposes adding an index column and edits a migration to speed up a report. The person writes "Don't change the schema; the slow part is the query". The agent reverts the migration edit and rewrites the report query's join.
- Why: the correction names the actual cause; the agent then worked on the query. Seen on the redirect, with changed course as corroboration.

## pos-3 Guided redirect at a real wrong turn

- kind: guided-success
- expect: seen
- Setup: following the guide during a real fix in `marlin-cli`, the agent starts patching the output formatter for a parsing bug. The person writes "That's the wrong layer: the bad value comes from the tokenizer, the formatter just prints it." The agent moves to `tokenizer.rs`.
- Why: the guided step on real work. Guided work earns Seen only; later stages need independent work.

## pos-4 Explained correction the agent ignored

- kind: boundary
- expect: seen
- Setup: in `tidepool-web`, the agent keeps retrying a CSS z-index fix. The person writes "It's not z-index: the modal is rendered inside the overflow-hidden container, move it to the portal." The agent replies "Understood" and changes z-index again. The person stops the session.
- Why: the redirect is explained, so the deliberate act qualifies for Seen. The agent ignored it, so the complete definition (explanation **and** changed course) is not met: this instance **never** counts toward Forming or Established.

## pos-5 Explained redirect, record truncated afterwards

- kind: missing-evidence
- expect: seen
- Setup: in `cobalt-infra`, after a failing deploy-script edit, the person writes "Stop editing deploy.sh; the failure is the missing IAM role in the module, fix it there." The session record is truncated immediately afterwards.
- Why: the redirect is recorded and explained: Seen. Whether the agent changed course is **unknown**; nothing counts toward later stages until a changed course is visible. The truncation is not treated as an ignored correction.

## neg-1 Interrupt, then "continue"

- kind: source-negative
- expect: opportunity
- Setup: in `orchard-jobs`, the agent keeps editing `retry.py` with a fix that fails the same test. The person interrupts, then types "continue". The agent resumes the same approach and the test fails again.
- Why: an interrupt alone does not prove steering, and "continue" resumes the same approach. A bare stop followed by the same failing approach is an opportunity, citing the person's "continue".

## neg-2 "Still failing"

- kind: source-negative
- expect: opportunity
- Setup: in `fern-docs-api`, the agent's fix to `server.go` fails `make test`. The person writes "Still failing". The agent tries a near-identical change, which fails again.
- Why: "still failing" says it failed, not what is wrong or why. The opportunity cites the person's "Still failing".

## neg-3 Three retries before a bare "try again"

- kind: boundary
- expect: opportunity
- Setup: in `basalt-sdk`, the agent tries the same timeout-wrapping fix three times; the same test fails each time. Only then does the person write "try again".
- Why: the same failing approach was retried **three times** before intervention (the coaching trigger), and the intervention was bare. The opportunity cites "try again".

## neg-4 Agent retries, no person turn

- kind: boundary
- expect: none
- Setup: in `heron-service`, the agent retries a failing approach four times on its own and the session ends with no further person prompt.
- Why: an opportunity must cite a person-authored moment. Agent and tool output alone is not reported.

## neg-5 Taste-only change

- kind: boundary
- expect: none
- Setup: in `slate-ui`, the agent adds a working `getAll` helper with passing tests. The person writes "actually, call it fetchAll". The agent renames it.
- Why: nothing was wrong; a change of taste with no error is not a correction of a wrong turn. No applicable moment.

## neg-6 Agent corrects itself

- kind: boundary
- expect: none
- Setup: in `pewter-tools`, the agent notices its own test failure, says "I was editing the wrong module", and switches files. No person prompt intervenes.
- Why: self-correction is not the person's act, and there is no person-authored moment to cite.

## neg-7 Guided question, no redirect

- kind: guided-no-action
- expect: none
- Setup: reading the guide, the person asks in `kestrel-app` "what might go wrong with this approach?" and the agent lists some risks. The task completes without the agent going wrong and without any correction.
- Why: answering coaching questions is not a redirect, and there was no wrong turn. No recognition, not a miss.

## neg-8 Nothing went wrong

- kind: no-applicable-work
- expect: none
- Setup: in the window, the person's sessions in `amber-lib` completed without interrupts, failed attempts or wrong approaches.
- Why: no applicable moment; nothing is reported.

## neg-9 Record truncated before the person replied

- kind: missing-evidence
- expect: none
- Setup: in `saffron-jobs`, the agent's fix fails twice; the record is truncated before the person's next prompt.
- Why: missing evidence is insufficient, not a miss and not a recognition.

## Scenarios the case format cannot label

### stage-boundary Follow-through credited to the week it finished

- kind: stage-boundary
- Setup: an explained redirect at 23:55 on Sunday of week 1 (person's local time); the agent's changed approach finishes at 00:20 on Monday of week 2. Another explained redirect with a changed course in week 3.
- Expected: Seen in week 1 on the redirect. For Forming, the instances are credited to weeks 2 and 3 (the weeks the changed course finished): two distinct weeks of the last four.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Ignored corrections never count later

- kind: stage-boundary
- Setup: across four weeks, five explained redirects; the agent changed course after two and ignored three.
- Expected: Seen holds. Only the two changed-course instances count toward Forming or Established; 2 of 5 is below [`most`](../../../reference/parameters.md#most), so not Established. The ignored ones are not misses by the person.
- Why no case: the case format has no `forming` or `established` expectation.

### stage-boundary Continuous comes from Fix the harness

- kind: stage-boundary
- Setup: the person writes the recurring "the limit belongs in Options" reason into the repository's instruction file and it holds in later sessions.
- Expected: recognized under Fix the harness, not as Continuous for this pattern. No stage is transferred automatically.
- Why no case: the case format cannot express cross-pattern stage separation.
