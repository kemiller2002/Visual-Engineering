---
id: AUD-VE-EVL-001
title: Visual Engineering Measurement Audit v0.1
abstract: Artifact-level audit of measures, inference targets, execution state, replication fields, and proxy risks in the repository's principal evaluation documents.
authors:
  - Kevin Miller
  - OpenAI Codex
created: 2026-07-25
updated: 2026-07-25
project: visual-engineering
document_type: audit
status: working-draft
confidence: medium
canonical: false
concepts:
  - research-methodology
  - evidence
related_documents:
  - content/projects/evaluation-measurement/research-execution-package/rep-ve-evl-001-foundation-and-falsification.md
tags:
  - measurement
  - audit
  - replication
machine_readable: true
llm_ingest: true
purposes:
  - verify
  - reproduce
audiences:
  - researcher
  - contributor
---

# Visual Engineering Measurement Audit v0.1

## Audit question

Can another researcher determine what was observed, what was inferred, what was merely
proposed, and the population, task, apparatus, analysis, uncertainty, artifacts, and
transfer boundary associated with each evaluation claim?

## Scope and method

The audit enumerated Markdown artifacts in these claim-bearing directories:

- `experiment-report`
- `case-study`
- `comparative-study`
- `audit`
- `research-plan`
- `research-execution-package`

Fourteen files were found, including the active VE-EVL package. Thirteen predecessor
artifacts were coded using the construct model and minimum experiment record in
`REP-VE-EVL-001`. Coding used only repository content; absence means the field could
not be reconstructed from the artifact, not that the underlying research never
considered it.

This is an artifact audit, not a re-appraisal of every external citation.

## Execution-state vocabulary proposed by the audit

| State | Meaning |
|---|---|
| `plan` | Questions or intended research sequence; no claim of evaluation execution. |
| `proposed-experiment` | Design and predictions specified; data not collected. |
| `repository-probe` | Files, tooling, schemas, or builds directly inspected or executed. |
| `expert-analysis` | A design or system interpreted against a framework without participant data. |
| `source-synthesis` | Conclusions derived from external literature, standards, or documentation. |
| `secondary-data-analysis` | Existing observations or datasets reanalyzed. |
| `human-study` | New participant observations collected under a recorded protocol. |
| `mixed` | Multiple states present; every conclusion must identify its supporting state. |

`status` and `execution_state` answer different questions and should not substitute for
one another.

## Artifact inventory

| Artifact | Execution state | Principal constructs/measures | Missing or ambiguous record fields | Main inference or proxy risk |
|---|---|---|---|---|
| `EX-COMP-011` Context Reliability Reversal | proposed-experiment | identification accuracy, reaction time, first fixation, confidence/calibration; notice and identification | population, sample rationale, stimuli, apparatus, primary outcome, scoring, analysis model, artifacts, ethics | Gaze and latency could be mistaken for changed perception; the file itself warns against this. |
| `EX-COMP-012` First Glance Versus Verified Understanding | proposed-experiment | gist, identity/state, relationship comprehension, next-step prediction, confidence | population, sample rationale, stimulus family, apparatus, scoring, primary outcome, mask details, analysis model, artifacts, ethics | Above-chance gist could be promoted as actionable comprehension; the file explicitly prohibits that shortcut. |
| `EX-WC-0001` Web Component Framework Architecture Probes | mixed: repository-probe + source-synthesis + deferred probes | repository/tooling presence, architecture compatibility judgments | per-probe evidence links, decision rubric, uncertainty, reproducible command outputs, artifact versions, clear executed/deferred field | A `verified` document can make source-backed architectural judgment appear equivalent to executed runtime validation. |
| `REP-WC-0001` Web Component Framework | source-synthesis + repository-probe | architecture feasibility, interoperability, semantic durability, accessibility risk | consistent claim-to-probe mapping, comparative scoring rules, runtime population/tasks, effect/uncertainty model | “Foundation-scoped certainty” may exceed implementation evidence; remaining tests are acknowledged as deferred. |
| `RP-COMP-005` Visual Scene Construction | source-synthesis + proposed-experiments | rapid gist, context, fixation-dependent evidence, verification cost, confidence | review protocol, screening/export record, claim-level effect sizes, population/stimulus transfer matrix | Literature synthesis supports candidate mechanisms, but candidate laws can read like executed repository validation. |
| `REP-CCE-0001` Clinical Communication Engineering | source-synthesis | comprehension, decision, workload, accessibility, error and trust-related safety outcomes | direct experiment protocol, concrete comparator, participant and setting details, analysis plan | Consequential engineering recommendations depend on later representative validation; the document acknowledges local validation needs. |
| Letter Confusion Data Audit | source-synthesis + data-model design | resemblance, substitution probability, identification accuracy, information retention | reproducible search/export, dual screening, dataset-level sample/apparatus completeness | Geometry and similarity corpora may be mistaken for human confusion probabilities; the audit explicitly identifies this gap. |
| Account Settings Case Study | expert-analysis | relative separation ratios, predicted grouping, section recognition, action selection | stable ID, participants, task protocol, variants as artifacts, scoring, uncertainty, analysis, accessibility states | High confidence labels describe expert diagnosis, not measured user effects; pixel ratios risk appearing prescriptive. |
| Ribbon Comparative Study | expert-analysis | ordinal recognition, density, discoverability, recall, task context | front matter/ID, operational definitions, evidence, participants, tasks, source versions, rubric, uncertainty | High/medium/low judgments are unsupported ordinal ratings and may convert preference or familiarity into performance claims. |
| `REP-ATLAS-0002` Relational Legibility Envelope | source-synthesis + proposed-experiments | grouping reconstruction, identification, search slope, retention, transformation preservation, recovery and consequence-weighted error | executed-study separation, protocol-specific sample/apparatus/analysis, calibrated profile values | Strong metric design is present, but literature-backed laws, metric proposals, and unexecuted experiments are easy to conflate. |
| `REP-ATLAS-0004` Visual Design Consolidation | source-synthesis | broad perception, spacing, typography, color, hierarchy, accessibility and wayfinding outcomes | systematic review protocol, claim-level traceability, comparable confidence calibration, effect/uncertainty table | Breadth and mature language may imply a single unified validation level across evidence of unequal strength. |
| `REP-VE-COL-001` Color/Contrast/Low Vision/CVD | source-synthesis + proposed-experiments | discrimination, identification, reading accuracy/rate, completion, errors, confidence, fatigue, abandonment | preregistered protocol, concrete stimuli, sample rationale, device calibration, analysis plan, ethics; accurately states no participant testing | Strongly separates metrics from task outcomes, but proposed metric tournaments could be mistaken for completed validation if execution state is omitted. |
| Project Atlas Foundation Research Plan | plan | proposed distance, density, confidence, perception and cognition constructs | stable metadata, operational definitions, sources, execution records, calibration | Early universal and numeric language—such as confidence `0.99`—has no defined calibration and conflicts with later bounded methodology. |

## Coverage summary

| Minimum-record dimension | Coverage judgment |
|---|---|
| Stable identity and status | Uneven; several legacy artifacts lack a canonical ID or controlled status. |
| Execution state | Absent as a common field; inferred from prose. |
| Claim and target inference | Often present conceptually, rarely encoded per measure. |
| Construct and measure role | Strongest in recent Atlas and Composition Science work; weakest in comparative/expert analyses. |
| Primary versus secondary outcome | Generally absent. |
| Population and target population | Usually absent in proposals; bounded populations appear in recent accessibility research. |
| Tasks and stimuli | Often sketched, rarely versioned as reproducible artifacts. |
| Apparatus and environment | Generally absent. |
| Sample rationale and stopping | Absent because most participant studies are proposed, but execution gating is not machine-readable. |
| Analysis plan and uncertainty | Analysis cautions appear; executable plans and uncertainty reporting are sparse. |
| Artifacts, code, and data | Repository files are available, but experiment materials and data packages are mostly prospective. |
| Nulls, reversals, and contradictions | Strong cultural coverage in recent REPs. |
| Transfer boundary | Frequently discussed in prose; not consistently attached to individual claims. |

## Cross-repository findings

### F1 — Execution state is the largest immediate traceability gap

The repository is predominantly a research and design-knowledge corpus, not a corpus of
completed original human experiments. That is acceptable, but readers and machines
must not infer execution from mature document status or from the presence of an
experiment design.

### F2 — The best recent artifacts already reject single-metric evaluation

`EX-COMP-011`, `EX-COMP-012`, `REP-ATLAS-0002`, and `REP-VE-COL-001` independently
separate accuracy, latency, gaze, confidence, comprehension, error, and transfer. This
convergence further weakens VE-EVL-H1.

### F3 — Confidence is not calibrated across artifact types

“High” confidence can refer to an expert diagnosis, a literature-level mechanism, an
architecture decision, or an empirical result. The Atlas foundation plan even uses
`0.99` without a calibration model. Confidence is therefore not presently comparable
across projects or methods.

### F4 — Proposed experiments have useful falsification logic but incomplete protocols

The repository is comparatively strong at predictions, counterexamples, and warnings
against proxy misuse. It is weak at sample rationale, primary-outcome designation,
apparatus/version capture, analysis specification, ethics state, and reproducible
materials.

### F5 — Expert analyses are the highest proxy-to-outcome risk

The Account Settings and Ribbon studies generate useful hypotheses, but their
confidence and ordinal comparisons are not participant outcomes. They should be
classified as expert analysis until tested.

## Immediate controls proposed

For every new claim-bearing artifact:

```yaml
execution_state: plan | proposed-experiment | repository-probe | expert-analysis | source-synthesis | secondary-data-analysis | human-study | mixed
data_collection_status: none | planned | active | complete
```

For `mixed` documents, each major conclusion should identify its evidence IDs and
execution state.

Before an experiment moves from proposed to active, require:

- named primary outcome and construct;
- participant/target-population definition;
- sample rationale and stopping rule;
- versioned tasks, stimuli, software, apparatus, and accessibility conditions;
- analysis and missing-data plan;
- consent, privacy, ethics, and risk disposition;
- artifact and data-access plan.

## Recommended corrections by priority

1. Add execution-state fields to the metadata standard and new templates.
2. Split the executed, source-backed, and deferred portions of `EX-WC-0001` at the
   claim-to-evidence level.
3. Mark the Account Settings and Ribbon documents explicitly as expert analyses.
4. Expand `EX-COMP-011` and `EX-COMP-012` into preregistration-ready protocols before
   implementation.
5. Replace unsupported numeric confidence in the Atlas foundation plan with an
   uncalibrated/provisional label or an explicit model.
6. Test the minimum experiment record on one proposed perceptual experiment, one
   architecture probe, and one expert analysis before canonical adoption.

## Audit limits

- The audit did not re-screen all citations in the large REPs.
- It did not include every research note or canonical theory document containing a
  proposed measure.
- No document owner was interviewed.
- “Missing” means absent from the audited artifact.
- No human-participant data were collected.

## Decision

Stack A is complete enough to proceed to the reporting-framework crosswalk, with one
additional action carried forward: the crosswalk must accommodate multiple execution
states rather than assuming every evaluation is a randomized or participant study.

