---
id: RDM-VE-001
title: Visual Engineering Research Roadmap
abstract: Research-program artifact for the Visual Engineering repository.
created: 2026-07-23
updated: 2026-07-24
project: Visual Engineering
document_type: roadmap
status: approved
canonical: true
concepts:
  - research-methodology
---

# Visual Engineering Research Roadmap

## Approval

Approved as the canonical research-program roadmap on 2026-07-24. This approval governs the taxonomy, sequencing, dependencies, and operationalization gates. It does not promote provisional research claims, domain prompts, or generated engineering guidance beyond their independently recorded evidence and status.

## Executive judgment

The repository has substantial research artifacts but is not yet one unified validated theory. Its project folders mix mechanisms, applications, infrastructure, and implementation. This roadmap replaces project-as-taxonomy with twelve research domains connected by evidence and decision dependencies. It merges composition/spacing/hierarchy, wayfinding/familiarity/learning, and governance/ontology/graph operations. It creates explicit sections for evaluation, accessibility/cultural transfer, product semantics, and human–agent communication. No existing source is deleted or declared obsolete; duplicate archived material remains evidence of provenance.

## Canonical standard resolution

This program follows `knowledge-platform/metadata-standard.md` and the Composition Science governance workflow: journal → REP → registry/graph updates, stable IDs, preserved history, and explicit uncertainty. The local governance file uses legacy `RP` while newer packages use `REP`; generated prompts say “current REP equivalent” and require agents to use the receiving project's convention. The repository-wide registries are placeholders, so prompts propose changes but must not invent silent canonical state.

## Proposed taxonomy

| ID | Domain | Decision | Maturity | Confidence | Priority |
|---|---|---|---|---|---|
| VE-PER | Perception and Attention | retain and narrow | Evidence-building | medium | P0 |
| VE-TYP | Typography and Legibility | retain; separate legibility from preference | Evidence-building | medium | P1 |
| VE-COL | Color, Contrast, and Appearance | retain; split measurement from semantic use | Theory-forming | medium | P1 |
| VE-SPA | Spatial Composition, Density, and Hierarchy | merge composition, spacing, hierarchy, and density | Theory-forming | medium | P0 |
| VE-WAY | Wayfinding, Familiarity, and Learning | merge wayfinding with familiarity and learning | Theory-forming | medium | P0 |
| VE-SEM | Product Semantics and Information Architecture | create from Product Genome and ontology work | Structured | low | P0 |
| VE-CMP | Components, Tokens, and Declarative Systems | retain; broaden beyond framework choice | Evidence-building | medium | P1 |
| VE-EVL | Evaluation, Measurement, and Experimentation | create as foundational shared infrastructure | Exploratory | low | P0 |
| VE-ACC | Accessibility, Individual Difference, and Cultural Transfer | create; prohibit edge-case treatment | Unframed | low | P0 |
| VE-HAC | Human–Agent Visual Communication | create as distinct domain | Unframed | low | P1 |
| VE-GOV | Research Governance and Knowledge System | merge governance, ontology, graph, and evidence operations | Structured | medium | P0 |
| VE-DOM | Domain Adaptation, Trust, and Safety | retain Clinical Communication as exemplar; generalize cautiously | Exploratory | low | P1 |

Projects remain application/coordination containers: Project Atlas contributes visual primitives; Composition Science contributes scene construction and cognition; Product Genome contributes semantic architecture; Design Library contributes implementation; Clinical Communication Engineering is a consequential-domain exemplar.

## Largest unknowns and highest-risk assumptions

- Whether laboratory perception, historical design systems, and preference findings predict consequential production tasks.
- Whether shared semantic/component systems reduce total error rather than relocating it.
- Whether “intuitive” behavior is familiarity, semantic transparency, feedback, or an interaction.
- Whether evidence generalizes across disability, age, language, culture, expertise, device, and domain.
- Whether visual fluency improves calibrated trust or creates dangerous overconfidence.
- Whether evidence grades and current measures support theory promotion.

## Priority waves and rationale

### Wave 0 — research infrastructure

- [Evaluation, Measurement, and Experimentation](sections/evaluation-measurement/roadmap.md)
- [Research Governance and Knowledge System](sections/governance-knowledge-system/roadmap.md)

### Wave 1 — foundational mechanisms

- [Perception and Attention](sections/perception-attention/roadmap.md)
- [Product Semantics and Information Architecture](sections/product-semantics/roadmap.md)
- [Accessibility, Individual Difference, and Cultural Transfer](sections/accessibility-cultural-transfer/roadmap.md)

### Wave 2 — visual systems

- [Spatial Composition, Density, and Hierarchy](sections/spatial-composition/roadmap.md)
- [Typography and Legibility](sections/typography-legibility/roadmap.md)
- [Color, Contrast, and Appearance](sections/color-contrast/roadmap.md)
- [Wayfinding, Familiarity, and Learning](sections/wayfinding-familiarity/roadmap.md)

### Wave 3 — implementation and interaction

- [Components, Tokens, and Declarative Systems](sections/component-systems/roadmap.md)
- [Human–Agent Visual Communication](sections/human-agent-communication/roadmap.md)

### Wave 4 — consequential transfer

- [Domain Adaptation, Trust, and Safety](sections/domain-safety/roadmap.md)

Infrastructure comes first because weak measures can make every later result confidently wrong. Perception and semantics can proceed in parallel because they have different evidence bases. Visual-system streams then consume shared measurement and boundary protocols. Components and agents depend on semantic results. Domain standards are last because transfer and error costs require the strongest gate.

## Parallel assignments and integration

Within a wave, foundation prompts may run in parallel. Integrate at four checkpoints: evidence-ID collision and source-quality audit; cross-section contradiction review; accessibility/external-validity review; theory-to-engineering promotion review. Shared needs are benchmark tasks, population/context descriptors, preregistration templates, effect/uncertainty reporting, provenance graphs, accessible prototypes, and failure corpora.

## Operationalization gates

Component framework mechanics and limited color/typography measurements may support scoped implementation, but no repository-wide universal standard is justified. Spatial hierarchy, intuitiveness, human–agent trust, and cross-cultural claims must not become mandatory standards until representative replication and reversal tests exist.

## Revision criteria

Revise this roadmap when a replicated result changes a dependency, a domain shows a reversal, a new population invalidates scope, evidence quality changes, an ontology boundary repeatedly fails, or two consecutive integration reviews find low information gain. Preserve the prior roadmap and record supersession.
