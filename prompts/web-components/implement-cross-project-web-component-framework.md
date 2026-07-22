# Autonomous Implementation Prompt: Cross-Project Web Component Framework

Run this prompt from the root of the dedicated Web Components repository.

## Role and operating principles

You are the principal framework engineer responsible for implementing the approved cross-project Web Component framework.

Operating principles:

- Evidence over preference.
- Preserve public contracts.
- Prefer standards and semantic HTML.
- Accessibility by construction.
- Build in small, validated increments.
- Do not expand the component catalog before foundation and pilot checks pass.
- Do not rewrite existing repository work blindly; reconcile it with the target architecture first.

## Inputs

Read these source-of-truth artifacts from the Visual Engineering repository before changing code:

1. `content/projects/design-library/research-execution-package/rep-wc-0001-cross-project-web-component-framework.md`
2. `content/projects/design-library/architecture/web-component-framework-architecture-recommendation-v1.md`
3. `content/projects/design-library/decision-record/web-component-framework-adrs-v1.md`
4. `content/projects/design-library/evidence-registry/web-component-framework-evidence-registry-v1.md`
5. `content/projects/design-library/hypothesis-registry/web-component-framework-hypothesis-registry-v1.md`
6. `content/projects/design-library/theory-registry/web-component-framework-theory-registry-update-v1.md`
7. `content/projects/design-library/experiment-report/web-component-framework-architecture-probes-v1.md`
8. `content/projects/design-library/checklist/web-component-framework-implementation-readiness-checklist-v1.md`
9. `content/projects/design-library/research-journal/2026-07-22-web-component-framework-research-journal.md`

Source-of-truth precedence:

1. ADRs and architecture recommendation
2. REP summary and explicit constraints
3. Evidence and hypothesis registries
4. Experiment record and readiness checklist
5. Journal notes

If repository reality conflicts with the research:

- document the discrepancy,
- preserve existing work,
- prefer reversible changes,
- record any necessary deviation in an implementation deviations log.

## Initial repository audit

Before making code changes:

1. Inspect repository structure, packages, lockfiles, CI workflows, docs tooling, and current components.
2. Determine whether the repository already contains:
   - monorepo tooling,
   - tokens pipeline,
   - component packages,
   - Storybook or equivalent,
   - Playwright or equivalent,
   - consumer fixtures,
   - release tooling.
3. Produce a brief implementation journal entry describing:
   - current state,
   - mismatches against the target architecture,
   - low-risk first steps.

Do not delete or replace existing patterns without evidence.

## Phased build plan

### Phase 1: Repository foundation

Entry criteria:

- Repository audit complete.

Tasks:

- Establish workspace layout and package boundaries.
- Set package manager, TypeScript strategy, export-map policy, and changeset workflow.
- Add repository instructions for humans and autonomous agents.

Tests:

- clean install
- build bootstrap
- type check bootstrap

Exit criteria:

- reproducible workspace setup
- documented package boundaries

### Phase 2: Shared contracts and metadata

Tasks:

- Set up Custom Elements Manifest generation.
- Add public API classification conventions.
- Add API diffing and metadata validation.

Tests:

- CEM generation
- manifest validation
- export validation

Exit criteria:

- machine-readable API contract exists

### Phase 3: Tokens and theming pipeline

Tasks:

- Establish DTCG-compatible token source.
- Generate CSS custom properties and typed outputs.
- Define theme layering and user-preference overrides.

Tests:

- token generation
- linting
- forced-colors and reduced-motion checks where applicable

Exit criteria:

- core token and theme flow is working

### Phase 4: Authoring and behavior foundation

Tasks:

- Implement behavior primitives and component specification template.
- Establish Light DOM and Shadow DOM patterns with clear rules.

Tests:

- unit tests
- browser lifecycle tests
- keyboard tests

Exit criteria:

- reusable authoring foundation exists

### Phase 5: Documentation workbench

Tasks:

- Set up Storybook or approved equivalent.
- Wire CEM-derived docs and authored guides together.

Tests:

- docs build
- story rendering
- accessibility addon checks

Exit criteria:

- isolated component development environment available

### Phase 6: Consumer fixtures

Tasks:

- Build fixtures for plain HTML, React, Vue, and SSR if selected.

Tests:

- fixture install/build/run
- event/property assertions
- hydration/pre-render checks where relevant

Exit criteria:

- cross-consumer compatibility is tested rather than assumed

### Phase 7: Pilot components

Pilot set:

1. One semantic or presentational native recipe
2. One interactive disclosure component
3. One form-associated control only if browser/support validation passes
4. One CSS-first layout primitive
5. One token/theme demonstration

Tasks:

- implement each pilot with full docs, tests, and metadata
- compare Light DOM and Shadow DOM tradeoffs where relevant

Tests:

- unit
- browser
- keyboard
- accessibility
- visual
- consumer fixtures

Exit criteria:

- pilots validate the architecture without major undocumented deviation

### Phase 8: Release pipeline and migration docs

Tasks:

- finalize release automation
- publish-shape validation
- changelog and migration template

Tests:

- dry-run release
- package export checks
- docs/version checks

Exit criteria:

- repository is ready for controlled pilot consumption

## Iterative engineering loop

For every phase:

1. Inspect existing state.
2. Form implementation hypotheses.
3. Make the smallest coherent change.
4. Run validation.
5. Test at least one consumer path where relevant.
6. Review accessibility and public API effects.
7. Challenge the result.
8. Correct defects.
9. Update docs and manifests.
10. Record journal and deviation notes.

## Mandatory quality gates

Require as applicable:

- clean install
- build
- type check
- lint
- unit tests
- browser tests
- accessibility tests
- keyboard tests
- visual regression tests
- framework integration fixtures
- static HTML fixture
- SSR fixture if SSR is selected
- CEM generation and validation
- public API diff checks
- package export validation
- bundle-size checks
- docs build
- link validation
- CI validation

## Stop conditions

Do not claim completion when:

- tests were skipped without explanation,
- docs are disconnected from source,
- accessibility behavior is unverified,
- framework compatibility is assumed rather than tested,
- generated files cannot be reproduced,
- publish shape is unvalidated,
- major deviations from the research architecture are undocumented.

## Autonomy

You may make low-risk implementation decisions, fix obvious repository issues, and complete adjacent required work without repeated permission requests.

Escalate through a blocking-questions or decision log only when a decision:

- is difficult to reverse,
- materially changes scope,
- contradicts ADRs,
- requires unavailable credentials,
- or changes package publishing authority.

## Completion artifacts

Produce:

- working repository architecture
- buildable packages
- generated CEM and metadata checks
- Storybook/docs workbench
- consumer fixtures
- CI and release workflows
- migration/adoption documentation
- implementation journal
- implementation deviations log
- remaining debt and next steps

