---
id: RP-WC-0001
title: Cross-Project Web Component Framework Research Execution Package
abstract: REP v2-style architecture package for a reusable cross-project Web Component framework, including repository audit, evidence, hypotheses, decisions, architecture recommendation, research debt, and implementation handoff.
authors:
  - OpenAI Codex
created: 2026-07-22
updated: 2026-07-22
project: Design Library
document_type: research-report
status: verified
canonical: false
concepts:
  - component-architecture
  - design-tokens
  - accessibility
  - interoperability
related_documents:
  - content/projects/design-library/research-report/component-library-foundations-research-report.md
  - content/projects/design-library/research-note/2026-07-21-semantic-durability-research-execution-package.md
  - content/projects/design-library/architecture/web-component-framework-architecture-recommendation-v1.md
  - content/projects/design-library/decision-record/web-component-framework-adrs-v1.md
  - content/projects/design-library/experiment-report/web-component-framework-architecture-probes-v1.md
  - prompts/web-components/implement-cross-project-web-component-framework.md
tags:
  - rep
  - web-components
  - architecture
keywords:
  - web component framework
  - rep v2
  - handoff
machine_readable: true
llm_ingest: true
---

# Cross-Project Web Component Framework Research Execution Package

## Research status

Status: Complete for architecture and handoff.

This repository phase produced a concrete target architecture and implementation prompt. It did not build the production framework inside Visual Engineering, because repository evidence showed that would be structurally premature.

## Repository reality

### Confirmed constraints

- Visual Engineering is currently a research repository.
- No JS workspace, lockfile, package graph, or CI workflow exists here.
- Existing Design Library work already established a hybrid, native-first direction.
- The repository values traceability, stable IDs, registries, and generated knowledge artifacts.

### Likely consumers represented by repository evidence

| Consumer | Evidence | Implication |
| --- | --- | --- |
| Static HTML sites | knowledge-platform website recommendations | Plain HTML must be first-class. |
| Markdown-generated research sites | `content/`, website architecture, build pipeline | Progressive enhancement matters. |
| Documentation sites | Storybook/workbench recommendation, generated docs need | Searchable API docs and recipes required. |
| Interactive tools | graph/search architecture | Selective client interactivity required. |
| React apps | prompt requirements plus likely future consumers | React fixtures required. |
| Vue apps | prompt requirements plus likely future consumers | Vue fixtures required. |
| SSR environments | prompt requirements, static/prefetched site use | SSR must be validated, not assumed. |
| No-build environments | plain HTML requirement | ES module and CDN-safe distribution required. |

### Unverified assumptions rejected

- That every reusable artifact should be a custom element.
- That Shadow DOM should be universal.
- That token substitution can absorb structural redesign.
- That framework wrappers should define the core contract.

## Major conclusions

1. The smallest stable interoperability boundary is a selective Web Component layer, not an all-components-as-custom-elements policy.
2. Component architecture must remain category-specific:
   - native HTML recipes,
   - CSS-first layout/composition,
   - Light DOM semantic composites,
   - Shadow DOM bounded widgets,
   - native-first form strategy.
3. Lit is the best default authoring tool for bounded interactive components, but not for every package.
4. CEM should be the canonical machine-readable API layer.
5. Storybook plus Playwright is the best current docs-and-validation foundation.
6. The dedicated Web Components repository should start with a monorepo of publishable packages and pilot components.

## Diminishing-returns evidence

The stopping gate is satisfied because:

- no unresolved foundation decision remains,
- major competing architectures were compared,
- multiple high-impact hypotheses were falsified or weakened,
- remaining uncertainty is implementation-scoped, not foundation-scoped,
- additional cycles inside this repository would mostly duplicate already sufficient evidence.

## Failed assumptions

- Failed assumption FA-WC-001:
  - "A single base class should unify all reusable UI."
  - Outcome: rejected.
- Failed assumption FA-WC-002:
  - "Shadow DOM should be the safe default."
  - Outcome: rejected.
- Failed assumption FA-WC-003:
  - "Framework wrappers are the real public API."
  - Outcome: rejected.
- Failed assumption FA-WC-004:
  - "This repository is the right place to start implementing the framework."
  - Outcome: rejected.

## Decision summary

- Foundation decisions: ADR-WC-001 through ADR-WC-008.
- Recommended architecture: `ARC-WC-0001`.
- Experiment record: `EX-WC-0001`.

## Research debt

- Runtime pilot fixtures still must be executed in the dedicated repository.
- Final browser and AT support matrix remains to be pinned down by implementation owners.
- Exact wrapper-generation strategy remains implementation debt, not a research blocker.

## Implementation handoff

Implementation handoff prompt:

- `prompts/web-components/implement-cross-project-web-component-framework.md`

Implementation readiness:

- Ready for pilot-first implementation.
- Not ready for bulk component-catalog expansion before pilots pass.

