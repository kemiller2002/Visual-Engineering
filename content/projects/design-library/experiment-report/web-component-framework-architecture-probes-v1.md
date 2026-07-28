---
id: EX-WC-0001
title: Web Component Framework Architecture Probes
abstract: Comparative architecture probes for the proposed Web Component framework, including executed repository probes and non-executed implementation probes deferred to the dedicated repository.
authors:
  - OpenAI Codex
created: 2026-07-22
updated: 2026-07-22
project: design-library
document_type: experiment-report
status: verified
canonical: false
concepts:
  - component-architecture
  - interoperability
related_documents:
  - content/projects/design-library/research-execution-package/rep-wc-0001-cross-project-web-component-framework.md
tags:
  - experiments
  - probes
keywords:
  - lit
  - react
  - vue
  - static html
machine_readable: true
llm_ingest: true
purposes:
  - verify
  - reproduce
audiences:
  - researcher
  - contributor
---

# Web Component Framework Architecture Probes

## Probe scope

This repository does not contain a JavaScript workspace or existing component build system. Therefore the probes performed here were limited to:

1. Executed repository reality probes.
2. Source-backed architecture probes using current official documentation.
3. Explicit deferral of runtime consumer fixtures to the dedicated Web Components repository.

## Executed probes

### EX-WC-001: Repository tooling probe

- Method:
  - Scanned for `package.json`, lockfiles, TS configs, and CI workflows.
  - Checked local runtime versions.
- Result:
  - No JS workspace exists in this repository.
  - Local tools available: Node `v25.6.0`, npm `11.8.0`, Python `3.14.3`.
- Consequence:
  - Production framework implementation in this repository would be premature and structurally mislocated.

### EX-WC-002: Registry and metadata probe

- Method:
  - Read repository architecture, metadata standard, and registry placeholders.
- Result:
  - The repository expects durable research artifacts, generated indexes, and traceable IDs.
- Consequence:
  - The correct output here is a research and handoff package, not framework source code.

## Source-backed comparative probes

### EX-WC-003: Authoring model probe

- Compared:
  - Native `HTMLElement`
  - Lit / `ReactiveElement`
  - Mixed architecture
- Result:
  - Native `HTMLElement` wins for minimal primitives and behavior-light elements.
  - Lit wins on ergonomics for complex interactive custom elements.
  - Mixed architecture best fits the category-specific evidence and avoids forcing layout recipes into Shadow DOM.
- Decision impact:
  - Adopt mixed authoring with one public contract model.

### EX-WC-004: Shadow DOM probe

- Compared:
  - Universal Shadow DOM
  - Universal Light DOM
  - Category-specific DOM strategy
- Result:
  - Universal Shadow DOM imposes too much styling and content-model friction.
  - Universal Light DOM loses protection for bounded interactive widgets.
  - Category-specific policy provides the best tradeoff.
- Decision impact:
  - Shadow DOM default only for bounded interactive widgets and selected form controls.

### EX-WC-005: Consumer integration probe

- Compared:
  - Plain HTML
  - React 19
  - Vue 3
  - SSR path
- Result:
  - Plain HTML remains the baseline contract.
  - React 19 reduces previous CE friction substantially.
  - Vue 3 interoperability is strong with clear property/event rules.
  - SSR remains valuable but must be fixture-validated before becoming contractual.
- Decision impact:
  - Core packages stay framework-agnostic; adapters remain optional.

## Required deferred probes

These probes were not executed in this repository and must be executed in the dedicated Web Components repository before broad library expansion:

1. Simple presentational component in native `HTMLElement` and Lit variants.
2. Slotted content component in Light DOM and Shadow DOM variants.
3. Low-risk interactive disclosure in plain HTML-enhancement and Lit variants.
4. Form-associated custom element with native form and validation fixture.
5. Themeable component demonstrating token flow and CSS parts/custom properties boundaries.
6. CSS-first layout primitive with container-query behavior.
7. React consumption fixture.
8. Vue consumption fixture.
9. Static HTML no-build fixture.
10. SSR/pre-render fixture.

## Conclusion

The probes performed here were sufficient to decide foundational architecture, but not sufficient to certify implementation ergonomics. That remaining work is implementation-phase validation debt and is captured in the readiness checklist and handoff prompt.

