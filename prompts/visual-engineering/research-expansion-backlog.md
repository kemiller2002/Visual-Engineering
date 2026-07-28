---
id: RBL-VE-001
title: Visual Engineering Research Expansion Backlog
abstract: Prioritized opportunities to extend the repository's data, results, research, and validation program.
created: 2026-07-28
updated: 2026-07-28
project: Visual Engineering
document_type: research-backlog
status: research-draft
canonical: false
concepts:
  - research-methodology
  - evidence
related_documents:
  - prompts/visual-engineering/research-roadmap.md
  - prompts/visual-engineering/research-priority-matrix.md
  - prompts/visual-engineering/research-dependency-map.md
  - content/projects/evaluation-measurement/research-execution-package/rep-ve-evl-001-foundation-and-falsification.md
purposes:
  - orient
  - decide
  - integrate
audiences:
  - contributor
  - researcher
machine_readable: true
llm_ingest: true
---

# Visual Engineering Research Expansion Backlog

## Status and use

This is a proposed, noncanonical backlog derived from the repository state on
2026-07-28. It does not promote research claims or authorize production standards.
Items are prioritized by dependency leverage, uncertainty reduction, reuse across
domains, feasibility, and the cost of acting on an unsupported claim.

The corpus is strongest at theory synthesis, construct definition, and falsifiable
protocol design. Its recurring weakness is the gap between proposed experiments and
executed comparative data. The first expansion priority is therefore not another broad
theory pass. It is a shared measurement and reporting foundation followed by small,
high-information tests.

## Priority key

- **P0:** unlocks or protects multiple research domains
- **P1:** high-value domain evidence that should follow the shared measurement gate
- **P2:** important extension with narrower or longer-term payoff
- **Mode — synthesis:** repository or literature work without new participant data
- **Mode — probe:** reproducible technical or expert-analysis work
- **Mode — study:** participant, field, or longitudinal data collection

## Recommended sequence

1. Complete P0-01 through P0-04 as the Wave 0 measurement and governance gate.
2. Run P0-05 and P0-06 as the first shared benchmark and ecological-transfer pilots.
3. Execute P1 items in parallel only when their records conform to the shared core.
4. Begin P2 work after at least one integration review identifies which models survive
   contact with comparative data.

## P0 — Shared foundations and highest-information tests

### P0-01 — Reporting-framework crosswalk and experiment record v0.2

- **Question:** What is the smallest record that preserves decision-relevant evidence
  across participant studies, source syntheses, expert analyses, technical probes,
  secondary-data analyses, and proposed experiments?
- **Mode:** synthesis plus structured repository audit
- **Expansion:** Crosswalk JARS, CHI transparency guidance, relevant
  CONSORT/SPIRIT fields, accessibility and participatory-research practice, and the
  repository metadata standard. Add an explicit execution-state vocabulary.
- **Deliverables:** universal record schema, method-specific extensions, field
  definitions, three worked examples, migration map from existing artifacts.
- **Success test:** existing artifact types can be represented without falsely implying
  participant data or completed execution.
- **Source basis:** `REP-VE-EVL-001`, `AUD-VE-EVL-001`, and `JR-VE-EVL-001`.

### P0-02 — Validity-profile reliability comparison

- **Question:** Does the proposed multidimensional validity profile improve reviewer
  agreement and risk detection over the repository's current single evidence grade?
- **Mode:** study or structured independent-review probe
- **Expansion:** Create three contrasting claim packets and have independent reviewers
  apply both systems.
- **Measures:** inter-rater agreement, review time, missed risks, confidence, and quality
  of decision rationale.
- **Deliverables:** preregistered protocol, anonymized ratings, analysis, revised
  profile, and explicit retirement/retention decision for single grades.
- **Dependency:** P0-01.
- **Source basis:** `REP-VE-EVL-001`, Stack C.

### P0-03 — Governance usability and registry integration pilot

- **Question:** Can contributors maintain the required evidence, hypothesis, experiment,
  and decision records without the process becoming stale or performative?
- **Mode:** probe plus contributor study
- **Expansion:** Apply the governance foundation prompt to a small set of live claims,
  test stable IDs and lineage, and measure completion and update burden.
- **Deliverables:** populated pilot registries, provenance edges, promotion checklist,
  contradiction workflow, owner model, and governance burden report.
- **Success test:** two contributors can independently update a claim and reconstruct
  its source, status, scope, and revision history.
- **Dependencies:** P0-01; coordinate with `PRM-VE-GOV-001`.

### P0-04 — Source and result data normalization

- **Question:** Which existing conclusions are artifacts of inconsistent metadata,
  duplicated sources, missing execution state, or incompatible outcome definitions?
- **Mode:** synthesis and data engineering
- **Expansion:** Normalize bibliographic records, study populations, task and stimulus
  fields, devices, outcomes, uncertainty, execution state, and duplicate lineage.
- **Deliverables:** clean source table, artifact-to-source graph, duplicate report,
  missing-data report, and a reproducible export for analysis.
- **Success test:** every claim selected for P0/P1 testing resolves to its evidence and
  can distinguish planned, executed, replicated, and failed work.
- **Source basis:** repository manifest, measurement audit, and current placeholder
  registries.

### P0-05 — First-glance versus verified-comprehension benchmark

- **Question:** Do first-glance hierarchy and gist measures predict verified
  relationship comprehension and correct next action?
- **Mode:** study
- **Expansion:** Implement the smallest viable version of `EX-COMP-012` with controlled
  layouts and separate notice, identification, comprehension, decision, confidence,
  and recovery outcomes.
- **Deliverables:** stimuli, accessible protocol, task data, analysis notebook,
  counterexamples, and benchmark fixture set.
- **Success test:** quantify where rapid-impression measures agree with or diverge from
  verified understanding.
- **Dependencies:** P0-01 and ethics/accessibility review.
- **Source basis:** `REP-VE-EVL-001`, Stack D, and `EX-COMP-012`.

### P0-06 — Ecological transfer fixture set

- **Question:** Which laboratory-supported mechanisms survive in realistic interfaces
  and which reverse under task, semantic, and interaction context?
- **Mode:** probe followed by study
- **Expansion:** Build matched fixtures for editorial pages, dashboards, forms, command
  surfaces, mobile workflows, and one safety-relevant display. Manipulate spacing,
  grouping, salience, density, and semantic structure independently where possible.
- **Deliverables:** open fixture corpus, manipulation specification, task definitions,
  pilot results, and reversal log.
- **Success test:** identify at least one robust transfer and one boundary or reversal.
- **Dependencies:** P0-01 and P0-04.
- **Source basis:** recurring ecological-transfer gap in Perception, Composition Science,
  Project Atlas, Product Genome, and Clinical Communication.

## P1 — High-value domain expansions

### P1-01 — Density, grouping, and crowding model comparison

- **Question:** Do element count, feature congestion, eccentricity-scaled spacing, and
  task-aligned grouping predict search and identification independently?
- **Mode:** study
- **Expansion:** Compare competing models on matched complex displays rather than
  treating density as raw object count.
- **Measures:** detection, localization, identification, search time, errors, eye
  movements where justified, and workload.
- **Deliverables:** model comparison, coefficient ranges by task, and explicit limits on
  any spacing or density token.
- **Source basis:** `composition-science-visual-density-crowding-and-perceptual-separation`
  and `GN-100`.

### P1-02 — Familiarity and migration-cost learning curves

- **Question:** How many repetitions are required for different interaction classes to
  reach stable performance, and when does a novel design repay retraining and error
  costs?
- **Mode:** longitudinal study
- **Expansion:** Compare familiar, structurally transparent, and arbitrary mappings over
  first use, spaced practice, delay, and convention switching.
- **Measures:** first-use success, learning rate, retained performance, practiced
  efficiency, capture errors, recovery cost, transfer, and subjective fluency.
- **Deliverables:** learning curves, plateau estimates, migration-cost model, and
  boundary conditions by expertise.
- **Source basis:** `intuitive-is-just-familiar-predictive-fit-rep-v2`.

### P1-03 — Typography constraint diagnostic

- **Question:** Can a short protocol distinguish whether performance is limited by
  acuity, contrast, crowding, glyph confusability, line capacity, eye movement, lexical
  processing, comprehension, fatigue, or navigation?
- **Mode:** study
- **Expansion:** Construct diagnostic tasks that isolate layers before testing font,
  width, size, spacing, and personalization interventions.
- **Measures:** letter and word identification, reading speed, comprehension, fixation
  behavior where useful, workload, fatigue, and task completion.
- **Deliverables:** diagnostic battery, decision tree, validation study, and guidance on
  when aggregate reading speed conceals compensation.
- **Source basis:** `RP-ATLAS-TYPO-TRANSFER-001`.

### P1-04 — Contrast metric tournament with affected users

- **Question:** Which contrast models best predict representative reading and interface
  task outcomes across low vision, color-vision deficiency, polarity, fonts, devices,
  and viewing conditions?
- **Mode:** preregistered systematic review followed by study
- **Expansion:** Compare WCAG ratios, APCA, and relevant local/appearance measures
  without assuming any is a universal standard.
- **Measures:** discrimination, reading, comprehension, completion, errors, confidence,
  fatigue, and abandonment.
- **Deliverables:** systematic-review dataset, metric comparison, participant review,
  and bounded engineering recommendations.
- **Source basis:** `REP-VE-COL-001`.

### P1-05 — Modern display and adaptive-color edge cases

- **Question:** How do images, gradients, transparency, wide gamut, HDR, outdoor mobile
  viewing, forced colors, and user-selected polarity alter contrast and semantic-color
  performance?
- **Mode:** technical probe plus affected-user study
- **Expansion:** Establish calibrated fixtures and cross-browser/component-library
  observations before selecting participant subsets.
- **Deliverables:** device/browser matrix, local-contrast cases, forced-colors failure
  corpus, and repair patterns.
- **Dependency:** P1-04 can share stimuli and outcome definitions.

### P1-06 — Category fit, novelty, and beauty transfer

- **Question:** Does controlled novelty within a recognizable category outperform both
  generic prototypicality and category-inappropriate novelty?
- **Mode:** corpus pilot plus study
- **Expansion:** Build the dated, viewport-specific multi-category corpus and execute
  `BDE-EX-001`.
- **Measures:** beauty, appropriateness, trust, clarity, distinction, perceived
  usability, objective performance, desire, and exploration as separate outcomes.
- **Deliverables:** coded corpus, controlled prototypes, cross-category analysis,
  counterexamples, and category-transfer boundaries.
- **Source basis:** `REP-BDE-0001`, Recommended Cycle 2.

### P1-07 — Complete-experience aesthetic evaluation

- **Question:** How do judgments change between screenshots, first task, failure and
  recovery states, loading, accessibility states, and repeated sessions?
- **Mode:** longitudinal study
- **Expansion:** Compare the same products across complete experience states and time.
- **Deliverables:** state-sensitive evaluation protocol, temporal judgment curves, and
  evidence about whether screenshot preference predicts sustained use.
- **Dependency:** reuse the P1-06 corpus.

### P1-08 — Semantic durability transformation matrix

- **Question:** Can one invariant semantic model support editorial, registry,
  expressive, mobile, low-vision, print, and action-oriented contexts without misleading
  order or variant proliferation?
- **Mode:** technical and expert probe
- **Expansion:** Execute `EX-CLF-001` with long, translated, RTL, incomplete, dynamic,
  actionable, and contradictory records.
- **Measures:** DOM and focus order validity, screen-reader comprehension, exception
  rate, duplicated content, CSS complexity, accessibility failures, and redesign blast
  radius.
- **Deliverables:** fixture implementation, transformation matrix, failure cases, and
  decision among universal, core-plus-context, and specialized models.
- **Source basis:** semantic-durability research package.

### P1-09 — Product-legibility cross-category validation

- **Question:** Does the six-gate Product Legibility Profile predict outcomes across
  radically different physical and hybrid products?
- **Mode:** comparative study
- **Expansion:** Test discoverability, interpretability, executability, feedback, and
  consequence comprehension without collapsing severe failures into a mean.
- **Deliverables:** cross-product dataset, normalization analysis, learning effects,
  and bounded pass/caution/failure rules.
- **Success test:** determine whether profiles predict critical errors better than a
  single aggregate score.
- **Source basis:** Product Genome Run 02; operational definition is 85% complete but
  empirical cross-product validation is 0%.

### P1-10 — Clinical communication governance and cognitive fieldwork

- **Question:** Which communication failures, workflow constraints, and urgency
  semantics matter in actual clinical contexts before a design system is tested?
- **Mode:** stakeholder review, field study, then simulation
- **Expansion:** Complete Phase 0 governance, clinician and patient review, workflow
  observation, and the first comparative simulation.
- **Measures:** omission, misinterpretation, action selection, time, recovery, confidence
  calibration, and workload.
- **Deliverables:** approved governance record, specialty-bounded task model, simulation
  protocol, and stop criteria.
- **Constraint:** no production standard or generalized specialty threshold before
  local validation and regulatory review.
- **Source basis:** `REP-CCE-0001` and `RDM-CCE-0001`.

### P1-11 — Cross-cultural and non-Latin visual semantics

- **Question:** Which findings about category fit, semantic color, typography,
  directionality, and “intuitive” mappings transfer across cultures, languages, and
  scripts?
- **Mode:** synthesis, participatory design, and study
- **Expansion:** Begin with translation/RTL fixture audits, then test selected claims
  with locally informed researchers and participants.
- **Deliverables:** scope descriptors, measurement-invariance analysis, reversal cases,
  and rules prohibiting unsupported cultural generalization.
- **Source basis:** repeated gaps in BDE, color, typography, familiarity, and the master
  roadmap.

### P1-12 — Multi-impairment and adaptation study

- **Question:** How do combinations of low vision, CVD, photophobia, motor constraints,
  cognitive differences, aging, zoom, polarity, and assistive technology change the
  effect of visual interventions?
- **Mode:** participatory study
- **Expansion:** Replace diagnosis-isolated assumptions with representative profiles
  and user-controlled adaptations.
- **Deliverables:** interaction-effects dataset, adaptation preferences, failure corpus,
  and evidence about when personalization outperforms a fixed default.
- **Source basis:** `REP-VE-COL-001`, typography transfer work, and VE-ACC roadmap.

## P2 — Strategic extensions

### P2-01 — Human–agent visual communication benchmark

- Test whether agents correctly infer hierarchy, relationships, uncertainty, state, and
  intended action from the same fixtures used with humans.
- Compare screenshot-only, DOM/accessibility-tree, structured metadata, and multimodal
  inputs; record confident misinterpretation and provenance loss.
- Depend on P0 measurement and governance work so agent accuracy is not reduced to one
  generic score.

### P2-02 — Design-token causal traceability

- Trace changes from tokens and component anatomy through perceptual variables to task
  outcomes. Test whether the knowledge graph can explain why a token exists, which
  evidence supports it, and which populations or contexts bound it.

### P2-03 — Failure and reversal corpus

- Collect cases where whitespace hurts, grouping misleads, salience distracts,
  familiarity preserves a bad convention, accessibility compliance fails real users,
  beauty undermines trust, or semantic stability produces the wrong task order.
- Use the corpus for falsification, reviewer calibration, agent evaluation, and
  regression testing.

### P2-04 — Temporal trend and visual-fashion records

- Track the origin, adoption, saturation, decline, and context of visual trends.
- Separate durable mechanisms from fashion, production-budget signals, brand
  reputation, and retrospective selection bias.

### P2-05 — Representative benchmark-task library

- Create reusable tasks at increasing consequence and complexity: notice, identify,
  compare, comprehend, decide, act, recover, and retain.
- Pair tasks with population, device, setting, state, and consequence descriptors so
  results can be compared without pretending contexts are identical.

### P2-06 — Replication and external-lab package

- Select two strongest and two most fragile findings, freeze stimuli and analysis plans,
  and prepare reproducible packages for independent replication.
- Treat successful artifact reproduction, result replication, and contextual
  generalization as separate outcomes.

## Fast, low-cost expansions

These can begin before participant recruitment, provided they do not delay P0-01:

1. Normalize execution state and full citations for all experiment-like artifacts.
2. Populate a pilot claim-to-source graph for the Evaluation and Color packages.
3. Convert existing proposed experiments into the shared preregistration template.
4. Build the semantic-durability fixture corpus and run automated accessibility checks.
5. Assemble the first-glance/verified-comprehension stimuli from `EX-COMP-012`.
6. Build the BDE dated-capture protocol and pilot a small category corpus.
7. Create the initial failure/reversal corpus from counterexamples already documented.
8. Audit existing claims for population, language, device, task, and setting scope.

## Work that should not be expanded yet

- Do not create universal spacing, density, hierarchy, or visible-item limits from the
  existing synthesis.
- Do not mandate APCA, OKLCH distance, a categorical palette, or a universal internal
  contrast ratio.
- Do not convert beauty, trust, fluency, usability, confidence, or gaze into proxies for
  one another.
- Do not bulk-expand the component catalog before runtime pilots pass.
- Do not promote a universal Product Legibility score before cross-category validation.
- Do not turn the clinical baseline into a production standard before governance,
  stakeholder review, fieldwork, and simulation.
- Do not generalize from screenshots, Western/English samples, fluent adult readers, or
  diagnosis-isolated accessibility samples to all users.

## Suggested first three saved work packages

### Package A — Measurement Core

Combine P0-01, P0-02, and P0-03. This is the main roadmap unlock.

### Package B — Comprehension and Ecological Transfer

Combine P0-05, P0-06, and P1-01 using a shared fixture family. This tests the central
bridge from visual mechanisms to consequential understanding.

### Package C — Inclusive Reading and Contrast

Combine P1-03, P1-04, P1-05, and P1-12 where recruitment and ethics allow. This avoids
testing typography, contrast, and impairment in isolation when their effects interact.

## Review checkpoint

Review this backlog after P0-01 produces the common record, after the first independent
validity-profile comparison, or when a new result reverses a dependency. At review,
record completed work, blocked work, negative results, newly discovered dependencies,
and any item that should be merged, split, demoted, or retired.
