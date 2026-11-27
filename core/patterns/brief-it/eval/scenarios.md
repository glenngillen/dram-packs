# Brief it: scenarios

Every acceptance scenario for `glenngillen/brief-it`, in full. All people, repositories and content are invented. Each `pos-`/`neg-` heading has a matching line in `cases.jsonl`. Every case is **unevaluable** on the pinned CLI: the pattern needs a model judgement of a first request and linkage to the later work, the collected-history fixture shape has no task boundaries or request-to-work linkage, and the pattern names no block the pinned build runs.

Applicable work is the first request of a piece of work in a main session, including a new task within a session.

## pos-1 Password reset with the email service and expiry

- kind: source-positive
- expect: seen
- Setup: in `lanternfish-api`, the person opens a session with "Add password reset. Use the existing email service, links expire after an hour." The agent reuses `mailer.Send` and sets a one-hour expiry without asking about either.
- Why: goal plus two substantive constraints, both applied by the later work. The brief is the Seen event; the applying edits are its corroboration.

## pos-2 Inclusive end date that protects timezone handling

- kind: source-positive
- expect: seen
- Setup: in `quillmark`, mid-session, the person starts a new task: "Add an end-date filter to the report. The end date is inclusive, and don't touch the existing timezone conversion." The agent filters through end of day and leaves `tz.go` unchanged.
- Why: a new task within a session with a goal and relevant constraints the work relied on.

## pos-3 Guided brief on real work

- kind: guided-success
- expect: seen
- Setup: in `tidepool-web`, after reading the guide, the person writes "Add CSV export of invoices. Reuse the existing invoice query; amounts stay in cents." The agent reuses the query and keeps cents.
- Why: the person's own brief on a real task, applied by the work. Guided work earns Seen only.

## pos-4 Owned brief template used and holding

- kind: mechanism-held
- expect: continuous
- Setup: the person's team keeps a `/task` command in the repository that asks for goal, done-when and must-not-change. In the window the person started five pieces of work with it, each request carrying a constraint the agent applied without guessing.
- Why: an owned template in place, applied and holding.
- Note: no block reaches `continuous` in the pinned build.

## pos-5 Concise brief is sufficient

- kind: boundary
- expect: seen
- Setup: in `marlin-cli`, the person writes "Rename `--out` to `--output`; keep `--out` as a hidden alias." The agent does exactly that.
- Why: length is neither positive nor negative; one line carried the goal and the constraint that mattered.

## pos-6 Brief sent, corroboration still pending

- kind: boundary
- expect: seen
- Setup: on the last day of the window, the person sends "Add rate limiting to the upload endpoint. Use the existing Redis client; limit per API key, not per IP." The agent has not yet made its first edit when the window ends.
- Why: the brief completes Seen when sent. Corroboration is pending, so it does not yet count toward Forming; that is not a miss.

## neg-1 Goal alone, then a corrected assumption

- kind: source-negative
- expect: opportunity
- Setup: in `orchard-jobs`, the person writes "Add password reset." The agent adds a new SMTP client and 24-hour links. The person replies "No, use the existing email service, and links should expire after an hour."
- Why: a goal alone is not a brief. The wrong assumption the person corrected makes it an opportunity, citing both person prompts.

## neg-2 Lengthy background the work did not use

- kind: source-negative
- expect: opportunity
- Setup: in `fern-docs`, the person opens with four paragraphs about the project's history and team, then "add an end-date filter". The agent treats the end date as exclusive; the person corrects it.
- Why: background the work never used is not a constraint; length does not make a brief. The correction makes it an opportunity.

## neg-3 Agent-written brief accepted with "ok"

- kind: source-negative
- expect: opportunity
- Setup: in `basalt-sdk`, the person writes "add retries". The agent replies with its own brief (exponential backoff, five attempts, all errors). The person writes "ok". Later the person corrects it: "don't retry 4xx errors."
- Why: an agent-written brief accepted with unread approval is not the person's brief. The later correction, a person prompt, makes it an opportunity.

## neg-4 Guide questions answered, goal sent alone

- kind: guided-no-action
- expect: none
- Setup: in `kestrel-app`, the person reads the guide and answers its questions in conversation, then sends only "add dark mode". No wrong assumption is corrected in the window.
- Why: answering guide questions earns nothing, and with no correction there is no opportunity.

## neg-5 Only questions and exploration

- kind: no-applicable-work
- expect: none
- Setup: the person's only sessions in the window ask "how does the cache layer work?" and "where is auth configured?"
- Why: questions and exploration are not a piece of work to brief.

## neg-6 Session start truncated

- kind: missing-evidence
- expect: none
- Setup: in `amber-lib`, the session record is truncated before the person's first prompt; the agent's later edits are visible.
- Why: the request cannot be seen, so the evidence is insufficient, not a miss and not a recognition.

## neg-7 Brief template present but unused

- kind: mechanism-unused
- expect: none
- Setup: `heron-service` has an issue template asking for goal and constraints. In the window the person never used it; their only work was a one-line typo fix with no correction.
- Why: a template existing without use is untested and cannot establish Continuous; nothing else is applicable to report.

## neg-8 Template used but a needed constraint still missing

- kind: mechanism-not-holding
- expect: opportunity
- Setup: the person starts work in `slate-ui` with their `/task` command, filling only the goal and leaving must-not-change empty. The agent restyles a shared button; the person corrects: "don't change the shared Button component."
- Why: the mechanism was applied but did not hold; the person's correction is the citation.

## neg-9 Agent-only evidence of an assumption

- kind: boundary
- expect: none
- Setup: in `pewter-tools`, the person writes "add a health check". The agent's summary says "assumed port 8080". No later person prompt corrects or questions it.
- Why: an opportunity needs a person-authored citation of the corrected assumption; agent output alone yields none.

## neg-10 Constraints supplied only after a wrong guess

- kind: boundary
- expect: opportunity
- Setup: in `garnet-web`, the person writes "add pagination", the agent uses offset pagination, and the person replies "use cursor pagination like the orders API."
- Why: the constraint came as a correction, not in the brief. It is an opportunity, citing both prompts; the correction itself is Steer, don't stop territory.

## Scenarios the case format cannot label

### stage-boundary Corroboration in a later week

- kind: stage-boundary
- Setup: a qualifying brief in week 1 (pos-6 style); the agent's applying edits finish in week 2. Another corroborated brief finishes in week 3.
- Expected: Seen in week 1. Forming from two distinct corroboration weeks (2 and 3), each credited to the week the corroboration finished, not the week the brief was sent.
- Why no case: `expect` accepts only `seen`, `continuous`, `opportunity` and `none`.

### stage-boundary Pending corroboration does not count toward Forming

- kind: stage-boundary
- Setup: two briefs in two different weeks; one has corroboration, the other's work has not started.
- Expected: Seen, not Forming. The pending instance is not a miss.
- Why no case: as above.

### stage-boundary Guided brief only

- kind: stage-boundary
- Setup: pos-3 plus a second guided brief in another week, no independent briefs.
- Expected: Seen only; guided work does not earn Forming.
- Why no case: as above.
