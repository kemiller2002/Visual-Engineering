---
id: HYR-WC-0001
title: Web Component Framework Hypothesis Registry
abstract: Statused hypothesis registry for the cross-project Web Component framework architecture decision set.
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
  - interoperability
related_documents:
  - content/projects/design-library/research-execution-package/rep-wc-0001-cross-project-web-component-framework.md
tags:
  - hypotheses
  - web-components
keywords:
  - lit
  - shadow dom
  - storybook
machine_readable: true
llm_ingest: true
---

# Web Component Framework Hypothesis Registry

| ID | Status | Confidence after | Architectural consequence |
| --- | --- | --- | --- |
| HY-WC-001 | Supported | High | Use native Web Components as one cross-project boundary, not the only reuse boundary. |
| HY-WC-002 | Partially supported | Medium | Lit is the preferred authoring default for bounded interactive components, not for every package. |
| HY-WC-003 | Supported | High | Mixed implementation strategy is acceptable when the public contract and metadata remain uniform. |
| HY-WC-004 | Partially supported | Medium-high | Shadow DOM is the default for bounded interactive widgets, with explicit exceptions. |
| HY-WC-005 | Supported | High | Light DOM is preferred for layout, typography, content composites, and open semantic structures. |
| HY-WC-006 | Supported | High | Layered tokens can separate behavior from visual identity when token scopes stay disciplined. |
| HY-WC-007 | Supported | High | Custom Elements Manifest should be the canonical machine-readable API layer. |
| HY-WC-008 | Partially supported | Medium | Wrappers should be generated or handwritten only where consumer ergonomics justify them. |
| HY-WC-009 | Supported | Medium-high | A monorepo with publishable packages is the best starting architecture for the dedicated repo. |
| HY-WC-010 | Supported | Medium-high | Storybook is the best primary workbench, but not the canonical source of contract truth. |
| HY-WC-011 | Supported | High | Playwright should anchor browser, interaction, keyboard, a11y, and visual checks. |
| HY-WC-012 | Supported | High | Most layout primitives should remain CSS-first recipes or utilities. |
| HY-WC-013 | Partially supported | Medium | Form-associated custom elements are acceptable for selected cases after explicit fixture validation. |
| HY-WC-014 | Supported | Medium-high | Progressive enhancement and meaningful pre-upgrade rendering are achievable and should be required. |
| HY-WC-015 | Partially supported | Medium | Independent package versioning is useful, but a lockstep major policy should be retained initially. |
| HY-WC-016 | Supported | High | Avoid customized built-in elements as shared-framework dependencies. |
| HY-WC-017 | Supported | High | Public API classification and automated diffing are required guardrails. |
| HY-WC-018 | Supported | Medium-high | Visual Engineering rules can be encoded as tokens, recipes, constraints, and metadata. |

## Notable revisions

- Rejected stronger form of HY-WC-002:
  - Lit is not the right default for layout and content-oriented packages.
- Rejected stronger form of HY-WC-004:
  - Shadow DOM should not be universal.
- Weakened HY-WC-008:
  - Framework wrappers are helpful but should not define the core contract.
- Weakened HY-WC-015:
  - Independent versions reduce churn only if release automation, compatibility testing, and docs are mature.

