---
id: REP-VE-EVL-001
title: Evaluation, Measurement, and Experimentation Foundation and Falsification
abstract: Active research package establishing a construct model, minimum experiment record, and falsification program for Visual Engineering evaluation.
authors:
  - Kevin Miller
  - OpenAI Codex
created: 2026-07-24
updated: 2026-07-25
project: Visual Engineering
document_type: research-package
status: active-research-package
evidence_level: C
confidence: low
canonical: false
concepts:
  - research-methodology
  - evidence
related_documents:
  - prompts/visual-engineering/research-roadmap.md
  - prompts/visual-engineering/sections/evaluation-measurement/roadmap.md
tags:
  - measurement
  - experiments
  - falsification
  - replication
machine_readable: true
llm_ingest: true
---

# Evaluation, Measurement, and Experimentation Foundation and Falsification

## Executive synthesis

Wave 0 has begun. The first repository audit and external evidence pass do not support
treating a common usability score, gaze measure, response time, preference rating, or
confidence rating as a sufficient measure of visual-engineering success. Each observes
a different construct or proxy. The package therefore separates notice, identification,
comprehension, decision quality, action performance, error and recovery, confidence
calibration, workload, satisfaction, and trust behavior.

The initial evidence also weakens the idea that evidence quality can be represented by
one grade that is comparable across methods and projects. A study can be strong on
internal validity and weak on construct validity or transfer; transparent reporting can
make a weak design auditable without making its inference strong. Promotion decisions
need a validity profile plus an explicit claim scope.

These are provisional findings. The current pass establishes the research stack and
the next falsification work; it does not complete VE-EVL or authorize a universal
measurement standard.

## Objective and scope

This package tests:

- **VE-EVL-H1:** Common UX metrics adequately detect visual-engineering effects.
- **VE-EVL-H2:** Repository evidence grades are comparable across methods and projects.

It addresses three questions:

1. Which outcomes distinguish notice, comprehension, decision quality, error, and trust?
2. What minimum experiment metadata enables meaningful reproduction and replication?
3. How should population, task, stimulus, setting, and device heterogeneity constrain
   promotion?

It does not yet validate individual instruments, set numerical promotion thresholds,
or replace ethics and domain-safety review.

## Repository context

### Material examined

- Approved Visual Engineering research roadmap and VE-EVL domain roadmap.
- Repository metadata standard and Composition Science constitution.
- Repository-wide evidence, hypothesis, and experiment indexes.
- `EX-COMP-011`, which separates sensitivity from criterion and warns that gaze,
  response time, and confidence do not establish perceptual change.
- `EX-COMP-012`, which separates first-glance gist from verified understanding.
- `EX-WC-0001`, which mixes executed repository probes, source-backed comparisons,
  and deferred runtime experiments under one verified report.
- The research-methodology concept index.

### Repository diagnosis

The repository contains useful experimental distinctions but no shared construct
dictionary, minimum experiment schema, outcome hierarchy, or promotion profile.
The global registries are navigational placeholders rather than complete claim graphs.
Existing experiment reports vary substantially in participant, stimulus, apparatus,
procedure, analysis, uncertainty, and artifact reporting.

## External evidence: first pass

The following entries are proposed for the evidence registry. They are recorded here
until the Wave 0 integration checkpoint approves registry changes.

| ID | Source | Evidence contribution | Limits |
|---|---|---|---|
| EV-VE-EVL-001 | [ISO 9241-11:2018](https://www.iso.org/standard/63500.html) | Defines usability in relation to users, goals, and context; supports contextualized effectiveness, efficiency, and satisfaction rather than a context-free score. | Standard-level conceptual framework; not proof that a particular metric predicts consequential outcomes. |
| EV-VE-EVL-002 | [Flake and Fried, 2020](https://doi.org/10.1177/2515245920952393) | Shows how undisclosed construct and scoring choices threaten construct, internal, statistical-conclusion, and external validity; supports measure-level transparency. | Psychology-focused methodological synthesis; transfer to every Visual Engineering method must be tested. |
| EV-VE-EVL-003 | [Yarkoni, 2022](https://doi.org/10.1017/S0140525X20001685) | Shows that claims often generalize over stimuli, tasks, and settings not represented in statistical models; supports explicit generalization targets. | Diagnosis and methodological argument rather than a Visual Engineering replication. |
| EV-VE-EVL-004 | [CHI 2025 transparency guidance](https://chi2025.acm.org/guide-to-a-successful-submission/) | Requires enough detail and artifacts to evaluate, reproduce, and replicate quantitative and technical work; supports recording software, hardware, instruments, data, and analysis. | Venue guidance, not an empirical estimate of which fields are sufficient. |
| EV-VE-EVL-005 | [CHI replication guidance](https://chi2024.acm.org/submission-guides/contributions-to-chi/) | Requires replications to distinguish what stayed constant and what changed across experimenter, participants, software, hardware, measures, and procedures. | Reporting guidance; does not establish promotion thresholds. |
| EV-VE-EVL-006 | [CONSORT 2025](https://doi.org/10.1136/bmj-2024-081123) | Provides a current minimum reporting model covering protocol, analysis plan, data sharing, intervention, comparator, setting, eligibility, deviations, outcomes, and harms. | Optimized for randomized health trials; use as a source class, not a wholesale HCI template. |
| EV-VE-EVL-007 | [Kern et al., 2016](https://doi.org/10.1177/0002764216665362) | Finds that generalization methods can fail when observed covariates do not explain effect heterogeneity; supports declaring target populations and sensitivity limits. | Survey-experiment setting; applicability depends on the Visual Engineering design. |
| EV-VE-EVL-008 | [Tipton et al., 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC6298071/) | Demonstrates an empirical way to compare treatment-effect heterogeneity across representative and nonrepresentative samples and cautions against assuming heterogeneity without examination. | Evidence does not justify universal homogeneity; it illustrates the need to test rather than presume transfer. |

## Construct and outcome model v0.1

Measures must be attached to a named construct and inference. The following constructs
must not be collapsed merely because they correlate:

| Layer | Construct | Candidate observations | Invalid shortcut |
|---|---|---|---|
| 1 | Availability | exposure, viewport presence, rendering state | assuming rendered means perceivable |
| 2 | Notice and orienting | detection accuracy, latency, first fixation under calibrated apparatus | treating fixation as comprehension |
| 3 | Identification | identity/state discrimination, sensitivity and criterion | using response time without accuracy |
| 4 | Comprehension | relationship, consequence, and next-step answers | treating scene gist as actionable understanding |
| 5 | Decision quality | choice accuracy, omission, prioritization, calibration | treating confidence as correctness |
| 6 | Action performance | completion, time, path, correction, abandonment | treating speed alone as success |
| 7 | Error and recovery | severity, detectability, recovery success and cost | averaging critical and trivial errors |
| 8 | Experience | workload, satisfaction, preference, perceived clarity | treating preference as performance |
| 9 | Trust behavior | reliance, verification, override, appropriate non-use | treating stated trust as calibrated reliance |
| 10 | Transfer | retention and performance across time, context, device, population | generalizing from one stimulus or task |

Primary outcomes must correspond to the claim being tested. Proxy outcomes require a
stated mechanism and evidence connecting the proxy to the consequential outcome.

## Minimum experiment record v0.1

Every proposed, preregistered, completed, replicated, or failed experiment should record:

1. Stable experiment ID, version, status, owners, dates, and source hypothesis.
2. Claim type and exact target of inference.
3. Construct definitions and the role of every measure.
4. Primary, secondary, exploratory, safety, and negative-control outcomes.
5. Operational definitions, instruments, scoring rules, transformations, and known
   validity evidence.
6. Population, recruitment, eligibility, exclusions, accessibility characteristics,
   language, expertise, and target population.
7. Tasks, stimuli, content, comparator, randomization unit, counterbalancing, and
   exposure schedule.
8. Device, viewport, input, software/build, browser, display, environment, and
   assistive-technology configuration where relevant.
9. Design, sample-size rationale, stopping rule, missing-data policy, and analysis plan.
10. Manipulation checks, data-quality rules, protocol deviations, and adverse or
    critical-error events.
11. Effect estimates with uncertainty and raw group summaries, not significance alone.
12. Heterogeneity variables chosen before analysis and justified by mechanism or risk.
13. Materials, code, data, data dictionary, artifact hashes or versions, and access
    restrictions with reasons.
14. Results for every prespecified outcome, including null and contradictory findings.
15. Replication relation: what was held constant, what changed, and why.
16. Claim boundary, unresolved threats, confidence change, decision impact, owner,
    review date, and rollback/reopening condition.

Transparency is necessary for appraisal; completion of this record does not itself
establish validity.

## Hypothesis update

### VE-EVL-H1 — narrowed and weakened

- **Prior confidence:** low-to-medium.
- **Current confidence:** low.
- **Reason:** the repository and external sources distinguish multiple constructs and
  contexts. Common metrics can contribute evidence but are not adequate as a generic
  class unless matched to the claim and consequential outcome.
- **Revised hypothesis:** A prespecified, claim-linked portfolio containing at least one
  consequential performance or error outcome plus relevant mechanism and experience
  measures detects visual-engineering effects more validly than any generic single
  usability metric.
- **Disconfirmation:** a single metric repeatedly predicts the relevant consequential
  outcome across prespecified tasks, populations, devices, and replications with no
  material reversals missed by the portfolio.

### VE-EVL-H2 — rejected in its current form

- **Prior confidence:** low-to-medium.
- **Current confidence:** very low.
- **Reason:** evidence quality is claim-relative and multidimensional. Reporting
  completeness, construct validity, causal identification, precision, and transfer can
  diverge.
- **Replacement hypothesis:** A claim-to-evidence validity profile yields more
  reconstructable and appropriately scoped promotion decisions than a single ordinal
  evidence grade.
- **Disconfirmation:** independent reviewers using a defined single grade reach equally
  reproducible decisions and preserve the same decisive validity limitations across
  heterogeneous methods.

## Proposed validity profile

Retain `evidence_level` for compatibility, but do not use it alone for promotion.
Each claim-evidence link should separately record:

- construct validity;
- internal validity or causal identification;
- statistical-conclusion validity and uncertainty;
- reporting and computational reproducibility;
- population, task, stimulus, setting, and device transfer;
- independence and replication;
- accessibility and subgroup coverage;
- consequential-error and safety relevance;
- current confidence and unresolved threats.

Values and calibration rules remain research debt. No composite score is approved.

## Contradictions and counterexamples

- A fast response can reflect fluency, guessing, a speed–accuracy tradeoff, or premature
  action.
- A first fixation can show orienting without identification or understanding.
- High satisfaction can coexist with poor error detection.
- High confidence can coexist with miscalibration and inappropriate reliance.
- A transparent study can still use an invalid construct or weak comparison.
- A randomized study can identify an effect in its sample without supporting transfer
  to new tasks, stimuli, populations, or devices.
- Multimethod agreement can be manufactured by combining correlated proxies into one
  score; disagreement may reveal construct boundaries rather than measurement failure.

## Engineering implications

Effective immediately for new research drafts:

- State the construct and inference before selecting a metric.
- Do not use gaze, speed, preference, workload, satisfaction, confidence, or a composite
  score as stand-alone evidence of comprehension or decision quality.
- Separate critical errors from aggregate completion metrics.
- Report effect estimates and uncertainty, including nulls and reversals.
- Declare the target population, task, stimulus family, device, and context.
- Label deviations from prespecified measures and analyses.

These are provisional research controls, not a canonical engineering standard.

## Next research stacks

### Stack A — repository measurement audit

Inventory every experiment and claim-bearing evaluation. Map each measure to the
construct model, identify missing record fields, and locate proxy-to-outcome leaps.

### Stack B — reporting-framework crosswalk

Crosswalk JARS, CHI transparency, CONSORT/SPIRIT where applicable, accessibility
research practice, and repository metadata. Separate universal record fields from
method-specific extensions.

### Stack C — validity-profile reliability test

Create three contrasting claim packets and have independent reviewers apply both the
current single grade and the proposed profile. Compare agreement, time, missing-risk
detection, and decision rationale.

### Stack D — outcome benchmark

Use `EX-COMP-012` as the first candidate. Specify a smallest viable implementation that
tests whether first-glance measures predict verified relationship and next-step
comprehension. Do not collect human-participant data without appropriate consent,
privacy, accessibility, and ethics review.

### Stack E — governance integration

After the reporting crosswalk stabilizes, run `PRM-VE-GOV-001` against the minimum
record and validity profile. Test whether the required documentation is usable enough
to remain current rather than becoming performative.

## Repository updates

- Created this active REP.
- Created `JR-VE-EVL-001` as the durable research journal.
- Completed Stack A as `AUD-VE-EVL-001`, covering thirteen predecessor artifacts.
- Proposed eight evidence entries; no canonical registry was silently changed.
- Proposed replacements for VE-EVL-H1 and VE-EVL-H2.
- Established construct model and minimum experiment record v0.1.

## Handoff and exact resume point

Resume with Stack B. Crosswalk JARS, CHI transparency, CONSORT/SPIRIT where applicable,
accessibility and participatory-research practice, and the repository metadata
standard. Separate a small universal record from method-specific extensions. Include
the execution-state vocabulary discovered in `AUD-VE-EVL-001`. Do not begin the
engineering-validation prompt until Stacks A–C have been reviewed at the
evidence/hypothesis integration checkpoint.

## Completion checklist

- [x] Repository context inspected.
- [x] Priority hypotheses precisely challenged.
- [x] Initial primary standards and methodological sources recorded.
- [x] Contradictions and counterexamples preserved.
- [x] Provisional hypothesis changes recorded.
- [x] Durable continuation point recorded.
- [x] Repository-wide measurement audit complete.
- [ ] Reporting frameworks and accessibility practice crosswalked.
- [ ] Independent validity-profile reliability test complete.
- [ ] High-value source classes saturated.
- [ ] Integration checkpoint held.
- [ ] Engineering-validation gate evaluated.

## Self-audit

- **Expected:** metrics and evidence grades would need refinement.
- **Most challenging finding:** measurement transparency is a prerequisite for judging
  validity, but must not be mistaken for validity itself.
- **Strongest conclusion:** outcomes must be separated by construct and claim.
- **Most fragile conclusion:** the exact minimum record has not yet undergone a
  usability or replication test.
- **Overgeneralization risk:** clinical reporting guidance may impose irrelevant fields
  on low-risk HCI experiments.
- **Missing stakeholders:** accessibility researchers, research participants,
  statisticians, psychometricians, research-operations owners, and domain-safety
  experts.
- **Likely expert dispute:** whether a common core can span experimental, qualitative,
  technical-probe, and field-study methods without becoming vague.
- **Evidence most likely to change the roadmap:** a replicated comparison showing a
  simpler record or single metric preserves the same decision-relevant information.
