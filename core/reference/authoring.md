# Authoring and readiness

How every pattern directory in this pack is built, what each pattern must cover before it counts as authored, and the words used for its readiness. [Give it instructions](../patterns/give-it-instructions/definition.md) is the complete reference pattern; copy its shape.

## Pattern directory

| File | Read by the pinned CLI? | Contents |
| --- | --- | --- |
| `pattern.yaml` | Yes, schema-validated | Identity (`id: glenngillen/<source-id>`, `version`, `status: preview`, `group`, `rung`), **`enabled: false`**, `opportunities`, `seen.when`, `continuous.held` prose and `automate`. Only fields and blocks the pinned schema and registry accept. No unsupported runtime binding, even though the pattern is disabled: the loader validates every block on every pattern. |
| `text.yaml` | Yes, schema-validated | Copy a person reads. Placeholders only where the CLI fills them: `report.seen` takes `{cases}` and `{applicable}`, `report.not_seen` takes `{count}`, `report.slipped` takes `{session}`; every other field takes none. `preview_note` says detection is unavailable. |
| `guide.md` | Read as prose | One guide on a real task in the person's own project (see [guide rules](#guide-rules)). |
| `definition.md` | Read as prose | The full recognition definition: the [required sections](#definition-sections) below. |
| `judge.md` | Read as prose; **not executed** | Only for a pattern whose intended definition needs model judgement. Its presence does not mean the CLI runs it: the active recommendation prompt is built inside the CLI. |
| `eval/cases.jsonl` | Yes, schema-validated; run by `dram pack eval` | One line per scenario the case format can label. |
| `eval/scenarios.md` | Not read by the loader | Every scenario in full prose, one heading per case ID, plus scenarios the case format cannot label. |

Shared rules live in the references, not in each pattern: [evidence](evidence.md), [parameters](parameters.md), [progression](progression.md) and [outcomes](outcomes.md). A pattern links to them and states only its own overrides.

### Definition sections

`definition.md` has these `##` sections, in this order:

1. **Intent**: what the pattern is for, the problem it solves and why it matters, what a recognition proves, and why its rules are drawn the way they are. Each rule's reason traces to the pattern's intent, a [principle](principles.md) or a recorded decision; a reason that isn't known is marked as not recorded rather than invented. Thresholds are [calibration points](principles.md#thresholds-are-calibration-points): say what each tries to capture, never justify the number.
2. **Status**: disabled, and the readiness term that applies.
3. **Applicable work**: what the pattern is counted against, with linked parameters.
4. **Recognition**: what earns Seen, and the completing evidence.
5. **Exclusions**: what never counts.
6. **Evidence**: citations required, and evidence sources the pinned CLI does not yet supply.
7. **Progression**: the pattern's own overrides of the [stages](progression.md#stages).
8. **Mechanism**: what Continuous means for this pattern (in place, applied, held, not holding), or why it has none of its own.
9. **Opportunities and coaching**: the missed moment and the coaching trigger.
10. **Why disabled**: the specific reason this pattern is off.
11. **Missing capabilities**: each CLI capability needed, named precisely.
12. **Verify before enabling**: the behaviour that must be demonstrated, not just a version number.

Add `## Open questions` only when something is genuinely open.

### Cases and scenarios

- **IDs and polarity.** `pos-N` cases expect `seen` or `continuous`; `neg-N` cases expect `opportunity` or `none`. A positive is never relabelled `none` to make disabled detection pass.
- **`none` means genuinely nothing applicable.** It is not what a detector that cannot run produces.
- **Unevaluable cases.** A pattern naming no block the pinned build runs gives **every** case an `unevaluable` reason naming the missing capability. The pinned evaluator reports such a case, never runs it and never counts it as a pass. A pattern whose cases are all unevaluable makes `dram pack eval` red; that is the honest result, not something to hide.
- **Packets.** When a collected-history fixture can express the scenario, `packet` is `fixtures/<name>.json` in the pinned fixture shape. When it cannot (for example, the shape has no field for which instruction files were loaded), `packet` is `scenarios.md#<case-id>`: the prose scenario. Never invent fixture fields.
- **Fixtures** are invented and deterministic: invented repositories, paths and people. Nothing is copied from a real transcript or configuration.

### Required scenarios

Each pattern's `eval/scenarios.md` labels every scenario with a `- kind:` line. Every pattern needs:

| Kind | What it covers |
| --- | --- |
| `source-positive` | Each positive example the catalogue supplies, even if it looks redundant. |
| `source-negative` | Each negative example the catalogue supplies. |
| `guided-success` | The person follows the guide and takes the step on real work. Earns Seen only. |
| `guided-no-action` | The person reads or answers the guide but does not act. No recognition. |
| `no-applicable-work` | Nothing in the window the pattern applies to. |
| `missing-evidence` | Required evidence is unavailable, excluded or truncated: insufficient, not a miss. |

A pattern with a mechanism also needs `mechanism-unused` (in place, never applied), `mechanism-held` and `mechanism-not-holding`. Add `boundary` scenarios at each parameter threshold, and `stage-boundary` for stage rules the case format cannot express (it has no `forming` or `established` expectation).

## Authoring checklist

A pattern counts as **authored** only when all of these hold:

- [ ] `pattern.yaml`: `glenngillen/<source-id>` ID, group and rung from the catalogue, `status: preview`, explicit `enabled: false`.
- [ ] No block, field or placeholder the pinned CLI does not accept; no unimplemented block included because the pattern is disabled.
- [ ] `definition.md` has every [required section](#definition-sections), links the shared references, and states which capabilities are missing and what must be verified before enabling.
- [ ] Parameters are linked to [parameters](parameters.md), never restated with a different value.
- [ ] Recognition, opportunities and mechanisms are kept distinct; no loose keyword or command match stands in for intent.
- [ ] Every catalogue example and every [required scenario](#required-scenarios) is in `eval/scenarios.md`; each labelable one has a matching case.
- [ ] `text.yaml` copy describes behaviour and evidence. No score, grade, count invented by the pack, savings guarantee or claim of official status. `preview_note` says detection is unavailable.
- [ ] `guide.md` follows the [guide rules](#guide-rules).
- [ ] `judge.md` exists only when model judgement is part of the definition.
- [ ] A readiness row in [readiness](readiness.md).
- [ ] Local checks pass: `bash scripts/run-tests.sh`.

### Guide rules

- Works on a **real task in the person's own project**. Asks and explains; performs no pattern action itself, creates no sample repository and changes no settings unless the person asks their agent to.
- Has a **positive completion step** that would earn Seen, and a clear **non-completion branch**. Answering the guide's questions does not count.
- Says that **detection is currently disabled**, so finishing the guide does not promise a recognition.
- Ends with **no exercise and no recognition** when there is no applicable task.
- For an unknown command, model, hook or platform setting, asks the person's agent to inspect its actual supported configuration rather than prescribing invented syntax.
- Preserves Safety prerequisites; never suggests permission bypass as a shortcut or blanket approval of permissions.

## Readiness vocabulary

Each term is a separate claim. One never implies the next.

| Term | Means | Established by |
| --- | --- | --- |
| **Authored** | Every item in the [checklist](#authoring-checklist) is present. | Review and the local content checks. |
| **Structurally valid** | The pack loads in the pinned CLI with this pattern in it: schema, block registry, references and placeholders accepted. | `dram pack validate` on the pinned build, plus the local checks. **Not an evaluation.** |
| **Evaluable** | At least one of the pattern's cases is actually run by the pinned evaluator, rather than reported unevaluable. | `dram pack eval` showing passed or failed cases for the pattern. |
| **Preview** | Enabled with `status: preview`: every applicable recognition case runs and passes. Results stay on the person's machine. | A green `dram pack eval` for the pattern, plus the capability it depends on. |
| **Stable** | Preview plus every applicable field-quality bar from the evaluation-readiness requirements (copy review, guides with staff users, precision, recall, opportunity usefulness, verification, cost, held cases, case advice, code fixtures, real configurations). | Private staff evaluation with recorded aggregate evidence. |

`status: preview` in `pattern.yaml` labels content as provisional; it is **not** the Preview readiness state while `enabled: false`. Every pattern in this delivery is authored, at most structurally valid, and disabled.
