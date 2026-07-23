---
id: RDM-VE-GOV-001
title: Research Governance and Knowledge System Research Roadmap
abstract: Research-program artifact for the Visual Engineering repository.
created: 2026-07-23
updated: 2026-07-23
project: Visual Engineering
document_type: roadmap
status: research-draft
canonical: false
concepts:
  - governance-knowledge-system
---

# Research Governance and Knowledge System Research Roadmap

## A. Identity and scope

- **Identifier:** VE-GOV
- **Area and disciplines:** Research Governance and Knowledge System; governance comparison, schema threat modeling, repository audits, workflow usability tests
- **Repository paths:** `knowledge-platform/`, `content/concepts/evidence/`, `content/concepts/knowledge-graph/`, `content/projects/composition-science/canonical/`
- **Why it exists:** Make claims, evidence, decisions, failures, and updates reconstructable without freezing provisional theory.
- **In scope:** mechanisms, boundary conditions, measurement validity, engineering translation.
- **Out of scope:** untested style preference presented as universal guidance.
- **Adjacent sections:** product-semantics, component-systems, domain-safety.
- **Taxonomy judgment:** merge governance, ontology, graph, and evidence operations. This boundary follows mechanisms and decisions, not current folders.

## B. Current state

- **Maturity / confidence / priority:** Structured / medium / P0.
- **Understanding:** The repository contains useful models and examples, but uneven traceability and little independent replication.
- **Existing theory/evidence:** Inspect the paths above; treat registries and REPs as claims to audit, not truth.
- **Contradictions and failed assumptions:** Preserve reversals, null results, inaccessible citations, and project-specific exceptions.
- **Research debt:** representative populations, production transfer, preregistration, shared outcome measures, and independent evidence.
- **Missing perspectives:** accessibility, cross-cultural research, statistics, implementation operations, and affected domain experts.

## C. Critical evaluation

- **Strongest claim class:** relational and context-dependent effects are more plausible than universal constants.
- **Weakest claim class:** numerical defaults or standards inferred from historical authority, preference, or small laboratory studies.
- **Hidden assumptions:** Stable IDs and registries produce traceability and cumulative learning; A shared ontology can align heterogeneous disciplines without distortion.
- **Rivals:** Documentation overhead causes stale or performative records; Premature ontology stabilizes disputed categories and hides disagreement.
- **Category-error risks:** preference→performance, correlation→causation, human→agent, descriptive→normative.
- **Premature-standardization risk:** constraints may encode narrow populations or tasks and make contradictory evidence harder to see.

## D. Research questions

- **Foundational:** What is the minimum durable research record?
- **Explanatory:** How are conflicts, supersession, and uncertainty represented?
- **Comparative:** Which automated checks detect orphan claims, broken provenance, and stale standards?
- **Boundary-condition:** What is the minimum durable research record?
- **Applied engineering:** How are conflicts, supersession, and uncertainty represented?
- **Measurement:** Which automated checks detect orphan claims, broken provenance, and stale standards?
- **Ethical/accessibility:** What is the minimum durable research record?
- **Cross-disciplinary:** How are conflicts, supersession, and uncertainty represented?

## E. Hypothesis portfolio

### VE-GOV-H1

- **Statement:** Stable IDs and registries produce traceability and cumulative learning.
- **Rationale:** This assumption is implicit in current repository framing.
- **Support:** Repository material is suggestive but not sufficient for promotion.
- **Contradiction/rivals:** Documentation overhead causes stale or performative records.
- **Predicted observation:** A preregistered intervention improves a consequential task measure across specified contexts.
- **Disconfirming observation:** The effect fails, reverses, or is explained by the rival under representative conditions.
- **Boundary conditions:** population, task, expertise, language, impairment, device, environment, and time pressure.
- **Confidence / cost of error:** low-to-medium / high.
- **Method:** governance comparison, schema threat modeling, repository audits, workflow usability tests.

### VE-GOV-H2

- **Statement:** A shared ontology can align heterogeneous disciplines without distortion.
- **Rationale:** This assumption is implicit in current repository framing.
- **Support:** Repository material is suggestive but not sufficient for promotion.
- **Contradiction/rivals:** Premature ontology stabilizes disputed categories and hides disagreement.
- **Predicted observation:** A preregistered intervention improves a consequential task measure across specified contexts.
- **Disconfirming observation:** The effect fails, reverses, or is explained by the rival under representative conditions.
- **Boundary conditions:** population, task, expertise, language, impairment, device, environment, and time pressure.
- **Confidence / cost of error:** low-to-medium / high.
- **Method:** governance comparison, schema threat modeling, repository audits, workflow usability tests.

## F. Research streams

### Stream 1 — Foundation and falsification

- **Objective:** map credible evidence and directly challenge VE-GOV-H1/H2.
- **Disciplines/sources/method:** governance comparison, schema threat modeling, repository audits, workflow usability tests; primary research, reviews, standards, failures, and counterexamples.
- **Artifacts:** REP, evidence/hypothesis updates, contradiction ledger, coverage table.
- **Dependencies:** evaluation-measurement.
- **Parallelization:** source-class and population audits may run independently, then integrate.
- **Saturation:** new searches cease changing confidence, boundaries, or rival coverage.
- **Impact:** determines whether theory should be retained, narrowed, replaced, or withheld.

### Stream 2 — Engineering translation and validation

- **Objective:** turn only supported mechanisms into testable engineering guidance.
- **Artifacts:** candidate constraints, benchmark tasks, experiment protocol, counterexamples, adoption gate.
- **Dependency:** Stream 1 and the evaluation-measurement protocol.
- **Saturation:** predictions are measurable and failure/rollback criteria are explicit.

## G. Prioritization

P0 because the section has important upstream dependencies but high cross-section reuse, consequential error cost, and falsifiable assumptions. Foundation work precedes translation because available documentation is not equivalent to validated evidence. Accessibility and external-validity audits run in parallel to reduce avoidable rework.

## H. Execution sequence

1. Run `01-foundation-falsification-research-prompt.md`.
2. Integrate at the evidence/hypothesis registry checkpoint; re-score confidence.
3. Run `02-engineering-validation-prompt.md` only for hypotheses that survive.
4. Block standards on unresolved validity, safety, or population gaps.
5. Reopen when replication fails, a new domain reverses an effect, standards change, or production monitoring conflicts.

## I. Completion and saturation criteria

- **Provisional theory:** convergent independent evidence plus investigated rivals and explicit scope.
- **Engineering principle:** measurable prediction, representative task evidence, constraints, and rollback condition.
- **Reusable standard/component:** replication across required contexts, accessibility review, conformance tests, and ownership.
- **Insufficient:** preference evidence, analogy, single-source authority, or unresolved high-cost contradiction.
- **Diminishing return:** additional sources no longer change claim, confidence, boundaries, or next experiment.

## J. Expected repository updates

Update the REP, research journal, evidence/hypothesis/theory registries, ontology/glossary, roadmap, knowledge graph, generated catalog, experiments, and examples/counterexamples as warranted. Never silently overwrite history.
