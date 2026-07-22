---
id: EVR-WC-0001
title: Web Component Framework Evidence Registry
abstract: Source-indexed evidence registry for the cross-project Web Component framework architecture recommendation.
authors:
  - OpenAI Codex
created: 2026-07-22
updated: 2026-07-22
project: Design Library
document_type: evidence-registry
status: verified
canonical: false
concepts:
  - component-architecture
  - accessibility
  - design-tokens
  - framework-interoperability
related_documents:
  - content/projects/design-library/research-execution-package/rep-wc-0001-cross-project-web-component-framework.md
tags:
  - web-components
  - evidence-registry
keywords:
  - custom elements
  - shadow dom
  - lit
  - storybook
machine_readable: true
llm_ingest: true
---

# Web Component Framework Evidence Registry

## EV-WC-001

- Claim: Autonomous custom elements are the practical default custom-element form; customized built-in elements are not a safe interoperability baseline.
- Source: WHATWG HTML custom elements; MDN `Using custom elements`.
- Date accessed: 2026-07-22
- Relevance: Customized built-ins preserve native behavior, but Safari still does not plan support, so shared framework architecture should avoid relying on them.
- Limitation: Does not prove customized built-ins are never useful in a controlled environment.

## EV-WC-002

- Claim: Form-associated custom elements and `ElementInternals` are broadly available enough to consider, not universally safe enough to treat casually.
- Source: MDN `ElementInternals`, `attachInternals()`.
- Date accessed: 2026-07-22
- Relevance: Supports approving form-associated controls only for targeted categories with explicit browser tests.
- Limitation: Availability alone does not guarantee equivalent UX or AT behavior to native controls.

## EV-WC-003

- Claim: Scoped custom element registries remain a proposal rather than a stable foundation.
- Source: WICG Scoped Custom Element Registries proposal.
- Date accessed: 2026-07-22
- Relevance: The framework must tolerate global registry constraints and naming collisions today.
- Limitation: Future browser adoption could reduce current registration risks.

## EV-WC-004

- Claim: Declarative Shadow DOM is usable for SSR-oriented strategies, but not a foundation to assume without validation.
- Source: MDN `Using shadow DOM`; Lit SSR overview.
- Date accessed: 2026-07-22
- Relevance: SSR can be supported, but must remain a tested capability rather than a blanket architecture claim.
- Limitation: Browser and integration maturity may continue changing.

## EV-WC-005

- Claim: Constructable stylesheets via `adoptedStyleSheets` are broadly available.
- Source: MDN `Document.adoptedStyleSheets`.
- Date accessed: 2026-07-22
- Relevance: Supports shared stylesheet primitives inside Shadow DOM packages.
- Limitation: Does not remove the need for public styling contracts.

## EV-WC-006

- Claim: CSS shadow parts are a viable exposed-styling mechanism, but every exposed part becomes public API.
- Source: MDN `CSS shadow parts`.
- Date accessed: 2026-07-22
- Relevance: Supports a minimal-parts policy.
- Limitation: Parts help external styling but do not solve broader composition concerns.

## EV-WC-007

- Claim: Container queries are broadly available and fit reusable layout primitives.
- Source: MDN `container-type` and `Container queries`.
- Date accessed: 2026-07-22
- Relevance: Supports CSS-first layout primitives instead of JS layout components.
- Limitation: Does not alone define a spacing or composition system.

## EV-WC-008

- Claim: The Design Tokens Community Group format is now mature enough to use as source-of-truth input rather than inventing a private schema.
- Source: DTCG site; W3C Design Tokens Community Group page.
- Date accessed: 2026-07-22
- Relevance: Supports DTCG JSON as canonical token input and generated CSS/TS outputs downstream.
- Limitation: Community-group status still requires pragmatic implementation choices.

## EV-WC-009

- Claim: Lit is standards-based, lightweight, and ergonomic for complex custom elements.
- Source: Lit docs `What is Lit?`, `ReactiveElement`, component overview.
- Date accessed: 2026-07-22
- Relevance: Supports Lit as the default authoring tool for bounded interactive components, not as a mandatory base for every package.
- Limitation: Lit defaults to Shadow DOM patterns that are not appropriate for every component category.

## EV-WC-010

- Claim: Lit SSR exists but is still documented under Lit Labs / experimental status.
- Source: Lit SSR overview.
- Date accessed: 2026-07-22
- Relevance: SSR support should be optional, fixture-tested, and decoupled from the core public contract.
- Limitation: Experimental status may improve.

## EV-WC-011

- Claim: React 19 materially improves custom-elements support, including CE Everywhere parity.
- Source: React 19 blog post.
- Date accessed: 2026-07-22
- Relevance: Weakens the need for wrappers for simple components, while wrappers may still help with ergonomics, typing, and event mapping.
- Limitation: Non-primitive SSR prop handling still has caveats.

## EV-WC-012

- Claim: Vue 3 consumes custom elements well and supports explicit property binding and CE authoring.
- Source: Vue `Web Components` guide and Custom Elements API docs.
- Date accessed: 2026-07-22
- Relevance: Supports treating Vue wrappers as optional rather than foundational.
- Limitation: Event naming and type ergonomics still require documented conventions.

## EV-WC-013

- Claim: Storybook supports Web Components with docs, a11y, interactions, and test-runner features.
- Source: Storybook framework feature support docs.
- Date accessed: 2026-07-22
- Relevance: Supports Storybook as primary component workbench.
- Limitation: Storybook is not the release contract; CEM and source docs must remain canonical.

## EV-WC-014

- Claim: Playwright executes component and browser tests in real browsers and supports visual testing patterns.
- Source: Playwright component testing docs.
- Date accessed: 2026-07-22
- Relevance: Supports Playwright as browser-integration and visual-regression foundation.
- Limitation: Component testing alone does not replace package-consumer fixtures.

## EV-WC-015

- Claim: Open UI exists specifically because native controls are valuable and design systems repeatedly reimplement them.
- Source: Open UI home, charter, working mode.
- Date accessed: 2026-07-22
- Relevance: Reinforces native-first component boundary rules.
- Limitation: Open UI is standards work, not direct implementation guidance for every local component.

## EV-WC-016

- Claim: Visual Engineering currently needs a generated research/knowledge site more than a component runtime inside this repository.
- Source: `knowledge-platform/website-architecture.md`, `build-pipeline.md`, `search-architecture.md`.
- Date accessed: 2026-07-22
- Relevance: Confirms this task should produce architecture and handoff artifacts rather than a production framework here.
- Limitation: Future repository evolution could add a local application workspace.

