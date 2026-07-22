---
id: THY-WC-0001
title: Web Component Framework Theory Registry Update
abstract: Theory and engineering-principle updates produced by the cross-project Web Component framework research cycle.
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
  - accessibility
  - composition
related_documents:
  - content/projects/design-library/research-report/component-library-foundations-research-report.md
  - content/projects/design-library/research-execution-package/rep-wc-0001-cross-project-web-component-framework.md
tags:
  - theory-registry
  - design-library
keywords:
  - engineering principles
  - design tokens
  - shadow dom
machine_readable: true
llm_ingest: true
---

# Web Component Framework Theory Registry Update

## Affected principles

### PR-WC-001: Native first, custom when justified

- Status: Strengthened
- Confidence change: Medium -> High
- Update: Native semantic HTML and native controls should remain the default author-facing contract unless a measurable requirement cannot be met.

### PR-WC-002: Encapsulation is category-dependent

- Status: Strengthened
- Confidence change: Medium -> High
- Update: DOM strategy must vary by component class. Shadow DOM is a tool, not a doctrine.

### PR-WC-003: Visual identity must not own behavior

- Status: Strengthened
- Confidence change: Medium -> High
- Update: Token and theme layers should flow into components through narrow public styling contracts rather than direct component-internals control.

### PR-WC-004: Machine-readable contracts are required for long-lived reuse

- Status: New candidate principle
- Confidence: High
- Update: CEM, API diffing, metadata linting, and generated docs are first-class architecture, not optional tooling.

### PR-WC-005: Accessibility is a shared contract

- Status: Strengthened
- Confidence change: Medium-high -> High
- Update: Component internals can guarantee intrinsic behavior, but product semantics, labeling, hierarchy, and instructions remain partly consumer-owned.

## Invalidated predictions

- Invalidated: One framework or base class should define every reusable artifact.
- Invalidated: The best shared boundary is "all UI becomes custom elements."
- Invalidated: Theme flexibility alone can absorb most redesign pressure.

## New theory candidates

1. Reuse durability increases when the smallest public contract is semantic and behavioral, while visual contracts remain layered and explicit.
2. Shadow DOM improves long-term maintainability only when the component has protected internal invariants worth the styling and composition cost.
3. AI-maintainable component systems require machine-readable contracts and package guardrails, not just human-authored docs.

