---
id: ADR-WC-INDEX-0001
title: Web Component Framework ADR Set
abstract: Consolidated architecture decision record set for the proposed cross-project Web Component framework.
authors:
  - OpenAI Codex
created: 2026-07-22
updated: 2026-07-22
project: Design Library
document_type: decision-record
status: verified
canonical: false
concepts:
  - component-architecture
  - governance
related_documents:
  - content/projects/design-library/architecture/web-component-framework-architecture-recommendation-v1.md
tags:
  - adr
  - web-components
keywords:
  - decisions
  - architecture
machine_readable: true
llm_ingest: true
---

# Web Component Framework ADR Set

## ADR-WC-001

- Decision class: Foundation
- Problem: What is the smallest stable interoperability boundary?
- Selected decision: Use native Web Components as one shared interoperability boundary for selected categories, while keeping native HTML recipes and CSS-first patterns as first-class citizens.
- Why: Cross-framework delivery matters, but not every reusable artifact benefits from becoming a custom element.
- Invalidation trigger: If consumer testing shows wrappers or native CE consumption are materially unreliable across the target matrix.

## ADR-WC-002

- Decision class: Foundation
- Problem: Should one authoring model define every package?
- Selected decision: Adopt a mixed authoring strategy:
  - native `HTMLElement` or utilities for minimal primitives,
  - Lit for bounded interactive components,
  - CSS-first authoring for layout/composition.
- Why: Best balance of standards alignment, ergonomics, and avoidance of unnecessary runtime abstraction.
- Invalidation trigger: If mixed-authoring metadata and testing become too inconsistent to govern.

## ADR-WC-003

- Decision class: Foundation
- Problem: What is the default DOM strategy?
- Selected decision: Use Light DOM for content, layout, and semantic composites; use Shadow DOM for bounded interactive widgets and selected protected controls.
- Why: Preserves content openness and theming where needed while retaining encapsulation where it earns its cost.
- Invalidation trigger: If consumer theming or accessibility failures show the category split is wrong.

## ADR-WC-004

- Decision class: Foundation
- Problem: How should visual styling stay decoupled from behavior?
- Selected decision: Use layered DTCG token sources that generate CSS custom properties and typed package outputs.
- Why: Shared token source with generated outputs is more durable than hand-authored per-package token APIs.
- Invalidation trigger: If DTCG format cannot represent required token relationships without excessive private extensions.

## ADR-WC-005

- Decision class: Policy
- Problem: What is the machine-readable public contract?
- Selected decision: Make Custom Elements Manifest the canonical generated API contract, with source annotations and API diffing in CI.
- Why: Supports docs, wrappers, search, IDE support, and agent-safe automation from one artifact.
- Invalidation trigger: If CEM proves structurally insufficient for required package metadata.

## ADR-WC-006

- Decision class: Default
- Problem: What is the primary documentation workbench?
- Selected decision: Use Storybook as the interactive workbench, backed by CEM and authored usage docs.
- Why: Strong Web Components support, a11y add-ons, interactions, docs, and visual workflows.
- Invalidation trigger: If Web Components support or generated-doc ergonomics fail during pilot implementation.

## ADR-WC-007

- Decision class: Foundation
- Problem: What is the browser test foundation?
- Selected decision: Use Playwright for browser contract, keyboard, a11y, and visual checks, supplemented by unit tests and consumer fixtures.
- Why: Real-browser execution is required for platform behavior.
- Invalidation trigger: If the selected repo stack requires a different real-browser test runner for critical gaps.

## ADR-WC-008

- Decision class: Policy
- Problem: How should packages be structured and versioned?
- Selected decision: Start with a monorepo of publishable packages, independently releasable but governed by a lockstep-major policy until maturity.
- Why: Balances isolation with shared tooling and reduces early-release chaos.
- Invalidation trigger: If release complexity outweighs reuse benefits after pilots.

