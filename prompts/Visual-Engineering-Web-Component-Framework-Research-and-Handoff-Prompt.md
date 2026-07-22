# Autonomous Research and Architecture Prompt: Cross-Project Web Component Framework

**Purpose:** Run this prompt from the root of the Visual Engineering repository.

**Primary outcome:** Produce a deeply researched, evidence-backed architecture and implementation plan for a reusable Web Component framework that can be adopted across projects, then produce a second autonomous agent prompt that will implement the approved architecture in the dedicated Web Components repository.

**Operating mode:** Research, challenge, test, document, and prepare the implementation handoff. Do not prematurely build the production framework in the Visual Engineering repository.

---

## Role

You are an autonomous principal frontend architect, design-systems engineer, web-platform researcher, accessibility specialist, developer-experience engineer, and repository archaeologist.

Your job is not to confirm an assumed Web Component architecture.

Your job is to determine what architecture should exist, why it should exist, what evidence supports it, where it may fail, and how another autonomous engineering agent can implement it safely in the dedicated Web Components repository.

Treat every architectural preference as a hypothesis until it survives research, repository analysis, counterexamples, and practical validation.

If evidence contradicts the current direction, the evidence wins.

---

## Canonical Research Standard

Locate and follow the repository's current Research Execution Package specification. At minimum, comply with REP v2.0 concepts including:

- Scientific Research Journal
- Research Execution Package
- Theory Registry updates
- Evidence Registry updates
- Stable identifiers for evidence, hypotheses, theories, experiments, concepts, and decision frameworks
- Explicit failed assumptions
- Evidence traceability
- Confidence changes
- Research debt
- Executable handoff instructions

Do not create an ordinary summary. Create a permanent scientific and engineering record from which another agent can reconstruct and continue the investigation without conversation history.

---

# Mission

Determine the best architecture, repository structure, authoring model, packaging strategy, integration model, update model, test system, documentation system, and governance process for a cross-project Web Component framework.

The framework must be:

- Reusable across unrelated projects
- Easy to consume from plain HTML and JavaScript
- Practical to consume from major application frameworks
- Easy to install, update, version, and migrate
- Compatible with the Visual Engineering research pipeline
- Capable of expressing multiple visual systems without duplicating behavioral components
- Accessible by default
- Responsive and mobile-friendly by default
- Testable in real browsers
- Searchable and machine-readable
- Maintainable by humans and autonomous agents
- Resistant to accidental breaking changes
- Designed for gradual adoption rather than forced rewrites
- Able to evolve without turning every project into a synchronized monolith

The final result must distinguish clearly between:

1. Web platform primitives
2. Component behavior
3. Semantic structure
4. Accessibility contracts
5. Visual styling
6. Design tokens
7. Theme or brand layers
8. Layout and composition primitives
9. Documentation and examples
10. Framework integrations
11. Build and release tooling
12. Project-specific extensions

---

# Required Repository Investigation

Before recommending an architecture, inspect the entire Visual Engineering repository.

## 1. Establish Repository Reality

Identify and document:

- Current directory structure
- Package managers and lockfiles
- Node and runtime expectations
- Existing build scripts
- Existing HTML, CSS, JavaScript, TypeScript, Web Component, design-system, or component-library experiments
- Existing design tokens or CSS variables
- Existing visual research artifacts
- Existing metadata schemas
- Existing generated websites or Markdown-to-HTML pipelines
- Existing accessibility guidance
- Existing testing tools
- Existing CI workflows
- Existing coding standards
- Existing architecture decisions
- Existing REP, theory, evidence, journal, and registry locations
- Existing cross-project reuse conventions
- Duplicate or contradictory approaches
- Files that are canonical, provisional, obsolete, generated, or unclear

Do not infer repository structure from filenames alone. Read relevant files and examine how the pieces relate.

## 2. Map Project Needs

Infer the actual consumers and use cases represented by the repository.

Create a consumer matrix that includes, where evidence supports them:

- Static HTML sites
- Markdown-generated research sites
- Documentation sites
- Interactive tools
- Forms
- Data-dense applications
- Visual demonstrations
- React applications
- Vue applications
- Other framework applications
- Server-rendered applications
- No-build or low-build environments
- Internal prototypes
- Production applications
- AI-generated interfaces

For each consumer, document:

- Installation expectations
- Rendering requirements
- Styling requirements
- Accessibility requirements
- Browser support requirements
- Integration friction
- Update risks
- Performance constraints
- Whether framework wrappers are necessary

## 3. Identify Existing Constraints

Separate constraints into:

- Confirmed constraints
- Likely constraints
- Preferences
- Unverified assumptions
- Historical accidents

Never turn a current repository pattern into a requirement without evidence.

---

# Research Program

Conduct external research using current, authoritative sources. Prefer specifications, standards, official documentation, source repositories, browser documentation, mature design systems, and documented engineering case studies.

Do not rely primarily on generic tutorials, trend articles, or popularity claims.

Research must include the following areas.

## A. Native Web Platform

Investigate:

- Autonomous custom elements
- Customized built-in elements and their practical browser limitations
- Shadow DOM
- Light DOM
- Declarative Shadow DOM
- HTML templates
- Slots and composition
- Custom element lifecycle behavior
- Custom element registration and collision risks
- Scoped custom element registries, including current readiness and limitations
- ElementInternals
- Form-associated custom elements
- Constraint validation
- Accessibility Object Model exposure where applicable
- CSS custom properties
- CSS Shadow Parts
- `:host`, `:host-context`, `::slotted`, and related styling boundaries
- Constructable stylesheets and adopted stylesheets
- CSS cascade layers
- Container queries
- CSS nesting and modern platform features relevant to the support matrix
- Server rendering and hydration
- Progressive enhancement
- Failure behavior before JavaScript loads or when JavaScript fails

## B. Authoring Approaches

Compare at least these architecture families:

1. Native `HTMLElement` with minimal utilities
2. Lit-based components
3. Lit HTML or rendering-library approaches without committing every element to a heavy base class
4. Compiler-based Web Component systems
5. Standards-first components with optional adapters
6. Mixed architecture where different component classes use different implementation strategies under one public contract

Do not assume one tool must be used for every component.

Evaluate each approach for:

- Standards alignment
- Long-term maintainability
- Dependency risk
- Bundle cost
- Runtime cost
- Authoring ergonomics
- Debuggability
- TypeScript support
- SSR and hydration
- Form support
- Accessibility
- Styling flexibility
- Testability
- Documentation tooling
- Framework interoperability
- Upgrade complexity
- Suitability for autonomous code generation
- Escape hatches
- Risk of library lock-in

## C. Component Boundary Philosophy

Challenge the assumption that every reusable pattern should become a custom element.

Develop criteria for deciding when to use:

- Native HTML only
- Native HTML plus CSS
- An attribute or utility behavior
- A headless controller
- A custom element
- A form-associated custom element
- A layout primitive
- A composite component
- An application-specific component

Explicitly examine the costs of wrapping already-correct native elements such as buttons, links, headings, inputs, labels, lists, dialogs, and details/summary.

Determine how the framework will preserve native semantics and browser behavior rather than replacing them unnecessarily.

## D. Shadow DOM Decision Model

Do not make one universal Shadow DOM rule without testing it.

Create a decision framework that evaluates Shadow DOM, Light DOM, or a hybrid approach per component category.

Test assumptions about:

- Encapsulation
- Theme inheritance
- Global styles
- Utility CSS compatibility
- Typography inheritance
- Localization
- Accessibility relationships across boundaries
- Form labels and descriptions
- Slots
- Portals and overlays
- Testing ergonomics
- Debugging
- Server rendering
- Visual customization
- CSS parts and custom property API burden
- Consumer ability to fix defects
- Long-term public styling contracts

The outcome may be a default with documented exceptions, but the default must be justified.

## E. Public Component Contracts

Design a stable public API philosophy covering:

- Element names and prefixes
- Attributes
- JavaScript properties
- Boolean attributes
- Methods
- Events
- Event naming
- Event payloads
- Event bubbling and composition
- Slots
- CSS custom properties
- CSS parts
- States
- Form values
- Validation
- Focus behavior
- Keyboard interactions
- Accessible names and descriptions
- Error messaging
- Internationalization
- Right-to-left layouts
- Deprecated APIs
- Experimental APIs

Define which surfaces are public, protected, private, experimental, or internal.

Avoid APIs that merely expose implementation details.

## F. Design Tokens and Visual Architecture

Determine how Visual Engineering research becomes implementable without coupling behavioral components to a single visual style.

Evaluate a layered token model such as:

- Primitive or reference tokens
- Semantic tokens
- Component tokens
- State tokens
- Density tokens
- Motion tokens
- Typography tokens
- Layout and composition tokens
- Theme or brand mappings
- User preference and accessibility overrides

Investigate current Design Tokens Community Group specifications and ecosystem readiness rather than inventing a private format without comparison.

Determine:

- Source-of-truth format
- Generated formats
- Naming conventions
- Token validation
- Theme switching
- Dark mode
- High contrast and forced colors
- Reduced motion
- User overrides
- Project overrides
- Component-local fallback values
- Versioning and migration
- Whether runtime token transformation is justified

Explicitly separate visual invariants from theme choices.

## G. Layout and Composition

Decide what belongs in the component framework versus a layout/composition layer.

Evaluate:

- Stack, cluster, grid, sidebar, switcher, frame, center, reel, cover, and similar compositional primitives
- Container-query-driven layouts
- Semantic HTML preservation
- Whether layout primitives should be elements, classes, attributes, or generated utilities
- Responsive behavior without project-specific breakpoints
- Logical properties and writing modes
- Density and spacing systems
- How Visual Engineering research rules can be represented as constraints, tokens, recipes, or lintable metadata

Do not turn every CSS layout pattern into a JavaScript component.

## H. Accessibility Architecture

Accessibility is an architectural requirement, not a later audit.

Research and define:

- Native semantic preservation
- WCAG target level
- ARIA usage rules
- Keyboard contracts
- Focus management
- Focus visibility
- Screen-reader behavior
- High contrast and forced-colors support
- Reduced motion
- Zoom and reflow
- Touch target expectations
- Error identification
- Form-associated element behavior
- Labeling and description patterns
- Live regions
- Dialog, menu, combobox, tabs, tooltip, popover, and disclosure risks
- Shadow DOM accessibility limitations
- Automated versus manual testing boundaries

Every interactive component specification must include an accessibility contract and test matrix.

## I. Interoperability

Test actual consumption from:

- Plain HTML and ES modules
- TypeScript
- React
- Vue
- At least one server-rendered environment relevant to likely project use
- Markdown-generated or static sites

Evaluate:

- Property versus attribute passing
- Event handling
- Boolean behavior
- Object and array properties
- Children and slots
- Forms
- SSR
- Hydration
- Type definitions
- Editor support
- Tree shaking
- Lazy loading
- Duplicate registration
- Version coexistence

Determine whether official framework wrappers should be generated, handwritten, or avoided.

## J. Packaging and Repository Architecture

Compare monorepo and multi-repository strategies in the context of the existing project ecosystem.

Evaluate a package structure that may include, but is not limited to:

- Core platform utilities
- Components
- Forms
- Layout primitives
- Design tokens
- Themes
- Icons
- Accessibility helpers
- Testing utilities
- Framework adapters
- Documentation
- Examples
- Codemods
- CLI or generators
- Experimental laboratory

Determine whether components should be:

- One package
- One package per component
- Grouped packages
- Exported through a facade package
- Distributed both individually and collectively

Research and decide:

- npm workspace strategy
- Package manager
- ESM policy
- TypeScript build strategy
- Export maps
- Side effects declarations
- Tree shaking
- CSS distribution
- Asset handling
- Source maps
- Type declarations
- Browser targets
- Node support
- CDN and direct-browser consumption
- Package provenance and supply-chain controls
- Local development linking

## K. Metadata and Discoverability

Make component APIs machine-readable.

Evaluate Custom Elements Manifest as a canonical generated contract and determine how it can support:

- IDE completion
- API documentation
- Story generation
- Framework wrappers
- Search indexes
- Catalog pages
- Automated consistency checks
- AI consumption
- Compatibility analysis

Determine whether additional project metadata is required, and avoid duplicating data that can be generated from source.

## L. Documentation and Component Workbench

Compare Storybook and credible alternatives against project needs.

The documentation environment should support:

- Isolated component development
- Interactive examples
- API documentation
- Accessibility checks
- Interaction tests
- Responsive viewports
- Theme testing
- Visual regression
- Usage recipes
- Copyable code
- Framework integration examples
- Search
- Versioned documentation
- Experimental components
- Deprecation notices

Determine which documentation is authored manually and which is generated.

## M. Testing Strategy

Design a layered testing pyramid using real browser execution where platform behavior matters.

Evaluate:

- Static analysis
- Type checking
- Unit tests
- DOM contract tests
- Accessibility automation
- Accessibility-tree snapshots
- Keyboard tests
- Form tests
- Interaction tests
- Cross-browser tests
- Visual regression tests
- SSR and hydration tests
- Framework integration tests
- Package-consumer fixture tests
- Performance budgets
- Bundle-size budgets
- Memory and lifecycle leak tests
- Mutation and reconnection behavior
- Upgrade and migration tests

Define which tests are mandatory for every component category.

Avoid excessive snapshot testing that obscures behavioral intent.

## N. Versioning, Releases, and Updating

The framework must be easy to update without destabilizing every consumer.

Research and define:

- Semantic versioning policy
- Changeset or equivalent workflow
- Automated releases
- Pre-release channels
- Experimental packages
- Deprecation windows
- Migration guides
- Codemods
- Compatibility tests
- Consumer contract tests
- Lockstep versus independent package versions
- Release notes
- Provenance
- Rollback strategy
- Update automation
- Versioned documentation

Model what happens when:

- A token changes
- A CSS part changes
- A component event changes
- An accessibility defect requires behavior change
- A package is renamed
- A component is replaced
- Two projects need incompatible versions

## O. Security and Trust Boundaries

Evaluate:

- HTML injection risks
- Unsafe template directives
- URL handling
- Trusted Types
- Content Security Policy
- Cross-origin assets
- Dependency risk
- Supply-chain controls
- Publishing permissions
- Provenance and integrity
- Whether components accept or render arbitrary HTML

## P. AI and Agent Maintainability

Because autonomous agents will help maintain the system, determine how to make architecture legible and enforceable.

Evaluate:

- Machine-readable API manifests
- Architecture decision records
- Component specification templates
- Required test templates
- Repository instructions
- Generated indexes
- Dependency graphs
- Naming validation
- Contract linting
- Token linting
- Public API diffing
- Automated documentation checks
- Examples that agents can imitate safely
- Guardrails that prevent agents from creating inconsistent one-off patterns

---

# Required Hypothesis Program

Create an explicit hypothesis registry before choosing the architecture.

At minimum, investigate and attempt to falsify these hypotheses:

- **HY-WC-001:** Native Web Components are the correct cross-project interoperability boundary.
- **HY-WC-002:** Lit provides the best default authoring model for this project ecosystem.
- **HY-WC-003:** A mixed implementation strategy can preserve one stable public component contract without producing excessive inconsistency.
- **HY-WC-004:** Shadow DOM should be the default for interactive components.
- **HY-WC-005:** Light DOM is preferable for layout, typography, and content-oriented components.
- **HY-WC-006:** Design tokens can separate behavioral components from project-specific visual identity.
- **HY-WC-007:** Custom Elements Manifest can serve as the canonical machine-readable API layer.
- **HY-WC-008:** Framework wrappers should be generated from the canonical component contract.
- **HY-WC-009:** A monorepo with independently publishable packages provides the best balance of reuse and change isolation.
- **HY-WC-010:** Storybook is the best primary component workbench for the project.
- **HY-WC-011:** Playwright-centered browser testing should be the integration and visual test foundation.
- **HY-WC-012:** Most layout primitives should remain CSS-first rather than JavaScript custom elements.
- **HY-WC-013:** Form-associated custom elements are mature enough for production use within the defined browser matrix.
- **HY-WC-014:** The framework can support progressive enhancement and useful pre-upgrade rendering.
- **HY-WC-015:** Independent package versioning reduces consumer disruption more than it increases release complexity.
- **HY-WC-016:** The framework should avoid customized built-in elements due to interoperability constraints.
- **HY-WC-017:** A strict public API classification and automated API diffing will materially reduce accidental breaking changes.
- **HY-WC-018:** Visual Engineering rules can be encoded as tokens, recipes, constraints, and metadata without embedding subjective design logic into every component.

Add new hypotheses as the research exposes hidden decisions.

For every hypothesis, record:

- Statement
- Motivation
- Supporting evidence
- Contradicting evidence
- Counterexamples
- Experiments or repository probes
- Confidence before research
- Confidence after research
- Status: supported, partially supported, rejected, unresolved, or superseded
- Architectural consequence

---

# Required Comparative Experiments

Perform small, disposable architecture probes where repository access and time permit. These are not production components.

At minimum, compare representative implementations for:

1. A simple presentational component
2. A slotted content component
3. An interactive disclosure or equivalent low-risk interactive component
4. A form-associated field or control
5. A themeable component
6. A layout primitive
7. A React consumption fixture
8. A Vue consumption fixture
9. A static HTML consumption fixture
10. An SSR or pre-rendering fixture

Use the probes to test assumptions about:

- API clarity
- Code size
- Runtime dependencies
- Styling
- Theming
- Accessibility
- Form behavior
- Framework events and properties
- Server rendering
- Testing
- Documentation generation
- Developer experience
- Build output

Place experiments in a clearly temporary or research-specific location. Do not mix them into production packages. Document whether each experiment should be retained, archived, or removed.

---

# Research Iteration Protocol

Operate in repeated research cycles.

Each cycle must:

1. Review the current repository evidence and prior cycle results.
2. Identify the largest remaining architectural uncertainty.
3. Generate or refine hypotheses.
4. Define evidence that would support or falsify them.
5. Research authoritative sources and relevant production systems.
6. Inspect relevant repository evidence.
7. Run a focused probe or comparison when useful.
8. Seek counterexamples and failure modes.
9. Update confidence levels.
10. Record findings in the research journal.
11. Update the proposed architecture.
12. Select the highest-value next cycle.

Do not stop after one research pass.

Continue until significant diminishing returns are demonstrated.

## Diminishing Returns Gate

You may stop only when all of the following are true:

- No unresolved critical architecture decision remains.
- High-risk decisions have multiple independent supporting sources or practical tests.
- Major competing architectures have been compared fairly.
- At least one serious attempt has been made to falsify each high-impact conclusion.
- New research cycles are producing mostly duplicate evidence, minor implementation detail, or low-impact refinements.
- Remaining uncertainty is explicitly documented as research debt.
- The implementation agent can proceed without guessing about foundational decisions.

Document the evidence that the diminishing-returns threshold was reached. Do not merely state that it was reached.

---

# Decision Method

For every major architectural decision, produce a decision record containing:

- Decision identifier
- Problem
- Context
- Constraints
- Options considered
- Evaluation criteria
- Evidence
- Counterevidence
- Tradeoffs
- Failure modes
- Reversibility
- Migration cost
- Selected decision
- Confidence
- Conditions that would invalidate the decision
- Review date or trigger

Use weighted scoring only when the criteria and weights are justified. Do not use numeric scoring to disguise weak qualitative judgment.

Classify decisions as:

- **Foundation:** costly to reverse; requires strong evidence
- **Policy:** shared convention; reversible with migration
- **Default:** preferred path with documented exceptions
- **Experiment:** intentionally provisional
- **Project choice:** should not be imposed by the shared framework

---

# Required Architecture Output

Produce a concrete target architecture, not a vague recommendation.

It must include:

## 1. System Context

- Purpose of the framework
- Intended consumers
- Non-goals
- Trust boundaries
- Relationship to Visual Engineering research
- Relationship to project-level applications

## 2. Layer Model

Define each layer, its responsibilities, dependencies, and prohibited responsibilities.

At minimum address:

- Web platform layer
- Authoring/runtime layer
- Behavioral primitives
- Accessible interactive components
- Form controls
- Layout/composition
- Tokens
- Themes
- Icons/assets
- Documentation
- Testing
- Framework adapters
- Release tooling
- Project extensions

## 3. Dependency Rules

Specify legal and illegal dependency directions.

Provide a dependency diagram in Mermaid and a machine-readable representation if practical.

## 4. Proposed Repository Layout

Provide an explicit directory tree for the Web Components repository.

For each directory and package, state:

- Purpose
- Source-of-truth files
- Generated files
- Public outputs
- Dependencies
- Owners or responsibility boundary
- Test requirements
- Documentation requirements
- Release behavior

## 5. Package Map

For every proposed package, define:

- Package name pattern
- Public exports
- Side effects
- Build outputs
- Type declarations
- CSS/assets
- Versioning model
- Consumer use case

## 6. Component Anatomy

Define the standard anatomy of a component package including likely files for:

- Source
- Styles
- Tests
- Stories/examples
- Accessibility contract
- Component specification
- Custom Elements Manifest annotations or source
- README or generated docs
- Changelog
- Migration notes

## 7. Component Taxonomy

Define categories such as:

- Native HTML recipes
- CSS/layout primitives
- Behavioral primitives
- Interactive components
- Form-associated controls
- Composite patterns
- Project-specific components
- Experimental components

For each category, define default architecture and required tests.

## 8. Styling and Theming Contract

Define:

- Token flow
- Theme application
- Shadow and Light DOM styling rules
- CSS parts policy
- CSS custom property policy
- Global style policy
- Project override policy
- Forced colors and user preference handling
- Versioning implications

## 9. Public API Rules

Define naming, attributes, properties, methods, events, slots, parts, variables, form behavior, and deprecation rules.

## 10. Integration Model

Provide usage examples and constraints for:

- Plain HTML
- TypeScript
- React
- Vue
- Static/Markdown-generated site
- SSR environment

## 11. Documentation Architecture

Define authored versus generated documentation and how API metadata, examples, research, and searchable JSON connect.

## 12. Test Architecture

Provide:

- Test layers
- Required tools
- Browser matrix
- CI matrix
- Accessibility checks
- Visual regression strategy
- Performance and bundle budgets
- Consumer fixture tests
- Release gates

## 13. Release and Update Model

Define:

- Branching expectations
- Changeset/release workflow
- Versioning
- Pre-releases
- Deprecation
- Migration tooling
- Automated dependency updates
- Rollback
- Compatibility guarantees

## 14. Governance

Define:

- How a new component is proposed
- Evidence required
- Specification review
- Accessibility review
- API review
- Visual review
- Experimental graduation
- Deprecation
- Removal
- Exception process

## 15. Adoption Strategy

Create a phased adoption plan that allows existing projects to adopt the framework incrementally.

Include:

- First pilot components
- Selection criteria
- Consumer fixtures
- Migration sequencing
- Feedback loops
- Success metrics
- Stop conditions
- Rollback conditions

---

# Required Visual Engineering Repository Artifacts

Determine the repository's actual conventions before selecting exact paths. Prefer existing canonical locations when they are clear and compatible.

Create or update the following artifacts in the Visual Engineering repository:

1. **Scientific Research Journal**
   - Chronological research cycles
   - Queries and sources
   - Repository observations
   - Hypothesis changes
   - Experiment outcomes
   - Decisions and reversals

2. **Research Execution Package**
   - Fully compliant with the current REP specification
   - Includes evidence, hypothesis, failed-assumption, risk, debt, and handoff sections

3. **Architecture Recommendation**
   - Human-readable target architecture
   - Repository layout
   - Dependency diagrams
   - Package map
   - Public contract rules
   - Test and release architecture

4. **Architecture Decision Records**
   - One record per foundational decision or a clearly indexed consolidated ADR set

5. **Evidence Registry Updates**

6. **Hypothesis Registry Updates**

7. **Theory Registry Updates**
   - Include affected principles, new principle candidates, confidence changes, and invalidated predictions

8. **Research Debt and Open Questions**

9. **Implementation Readiness Checklist**
   - Must distinguish blockers, required work, optional improvements, and deferred research

10. **Final Web Components Repository Implementation Prompt**
    - This is the final executable handoff prompt for the implementation agent
    - It must be stored in the Visual Engineering repository
    - Suggested filename if repository conventions do not dictate another:

```text
prompts/web-components/implement-cross-project-web-component-framework.md
```

If that path conflicts with established repository organization, choose the correct canonical path and document the reason.

11. **Research Index Entry**
    - Ensure the new artifacts are discoverable through existing indexes, metadata, generated search data, or repository navigation.

Do not leave valuable work only in terminal output or conversation text.

---

# Final Implementation Prompt Requirements

The final file placed in the Visual Engineering repository must be a self-contained prompt intended to run from the root of the dedicated Web Components repository.

It must include all context required for an autonomous engineering agent to implement the framework without access to this conversation.

The implementation prompt must contain:

## A. Role and Operating Principles

- Principal framework engineer role
- Evidence over preference
- Preserve public contracts
- Prefer standards and semantic HTML
- Accessibility by construction
- Small, validated increments
- No broad implementation before foundation checks pass

## B. Inputs

- Paths to the REP, architecture recommendation, ADRs, registries, diagrams, and readiness checklist in the Visual Engineering repository
- Instructions for importing or reading those artifacts
- Rules for resolving discrepancies
- Clear source-of-truth precedence

## C. Initial Repository Audit

Before changing code, the implementation agent must inspect the Web Components repository and reconcile its current state with the target architecture.

It must not delete or rewrite existing work blindly.

## D. Phased Build Plan

At minimum:

1. Repository foundation
2. Toolchain and package boundaries
3. Shared contracts and metadata
4. Tokens and theme pipeline
5. Component authoring foundation
6. Test infrastructure
7. Documentation workbench
8. Consumer fixtures
9. First pilot components
10. Framework adapters if justified
11. Release pipeline
12. Migration and adoption documentation

Each phase must have entry criteria, tasks, tests, outputs, and exit criteria.

## E. Iterative Engineering Loop

For each phase:

1. Inspect existing state.
2. Form implementation hypotheses.
3. Make the smallest coherent change.
4. Run tests and validation.
5. Test at least one consumer path where relevant.
6. Review accessibility and public API effects.
7. Challenge the result.
8. Correct defects.
9. Update documentation and manifests.
10. Commit or checkpoint coherent work according to repository policy.

## F. Mandatory Quality Gates

Require, as applicable:

- Clean install
- Build
- Type check
- Lint
- Unit and browser tests
- Accessibility tests
- Keyboard tests
- Visual tests
- Framework integration fixtures
- Static HTML fixture
- SSR fixture if selected architecture requires it
- Custom Elements Manifest generation and validation
- Public API diff checks
- Package export validation
- Bundle-size checks
- Documentation build
- Link and search-index validation
- CI validation

## G. Pilot Components

Specify pilot components selected by the research, with reasons. The prompt must prevent the implementation agent from expanding the library before the pilots validate the architecture.

Pilot selection should cover distinct risk classes, such as:

- One semantic/presentational element or recipe
- One interactive element
- One form-associated element if approved
- One layout primitive or CSS recipe
- One token/theme demonstration

## H. Completion Artifacts

Require the implementation agent to produce:

- Working repository architecture
- Buildable and testable packages
- Documentation site/workbench
- Machine-readable component metadata
- Consumer examples
- CI and release workflows
- Migration/adoption guide
- Architecture deviations log
- Implementation journal
- Final implementation REP or engineering handoff package
- Remaining debt and next steps

## I. Stop Conditions

The implementation agent must not claim completion when:

- Tests are skipped without explanation
- Documentation is disconnected from source
- Public APIs are undocumented
- Accessibility behavior is unverified
- Framework integrations are assumed rather than tested
- Generated files cannot be reproduced
- Package publishing shape is unvalidated
- Repository instructions are incomplete
- Major deviations from the research architecture are undocumented

## J. Autonomy

The implementation prompt should authorize the agent to make reasonable low-risk decisions, correct obvious repository issues, and complete adjacent required work without repeatedly asking permission.

It must require escalation through a documented decision or blocking-questions file only when a decision is irreversible, materially changes scope, contradicts foundational research, or requires unavailable credentials or external authority.

---

# Anti-Patterns to Actively Prevent

The research and final implementation prompt must guard against:

- Choosing a library because it is familiar
- Treating Web Components as a reason to replace semantic HTML
- Using Shadow DOM everywhere without a decision model
- Avoiding Shadow DOM everywhere because theming appears easier
- Building styling APIs after component internals are already fixed
- Creating one-off component APIs
- Reflecting every property to an attribute
- Emitting non-composed events that frameworks cannot consume
- Exposing internal DOM as a public contract accidentally
- Making CSS selectors into undocumented APIs
- Duplicating design-token values across packages
- Mixing project branding into core behavior
- Building a giant package that defeats tree shaking
- Creating dozens of tiny packages without release justification
- Depending on framework-specific concepts in the core
- Assuming SSR works without a fixture
- Assuming React or Vue compatibility without tests
- Testing Web Components primarily in a simulated DOM
- Treating automated accessibility checks as complete accessibility validation
- Using visual snapshots as the only behavioral tests
- Publishing without API manifests, types, export validation, and provenance
- Letting generated documentation drift from source
- Creating a custom metadata format when an established standard is adequate
- Hiding unresolved decisions inside implementation code
- Allowing experimental components to become de facto stable APIs
- Building the full component catalog before validating architecture with pilots
- Optimizing prematurely for every hypothetical consumer
- Copying a public design system without validating local needs and constraints

---

# Required Critical Questions

The final research must answer, or explicitly mark unresolved, at least these questions:

1. What is the smallest stable interoperability boundary?
2. Which component categories genuinely need custom elements?
3. What must remain native HTML?
4. What is the default rendering strategy, and what are its exceptions?
5. What is the default Shadow/Light DOM policy, and why?
6. How are public APIs declared, generated, tested, and versioned?
7. How do projects customize visuals without forking behavior?
8. How are tokens represented and distributed?
9. How are layout and visual-composition rules shared without unnecessary JavaScript?
10. How does a component work before upgrade, during upgrade, and after JavaScript failure?
11. How do form-associated components participate in native forms and validation?
12. How are React, Vue, static HTML, and SSR consumers verified?
13. How are components loaded individually and collectively?
14. How are duplicate registrations and version conflicts handled?
15. How does the library avoid breaking projects during updates?
16. What documentation is generated from source?
17. What is the role of Custom Elements Manifest?
18. What tests are required for each component category?
19. What browser and assistive-technology support matrix is realistic?
20. How are visual regressions distinguished from intentional theme changes?
21. How are experimental APIs isolated?
22. How does an autonomous agent know whether a proposed component is consistent with the framework?
23. What belongs in the shared Web Components repository versus Visual Engineering versus individual projects?
24. What would cause the architecture to be reconsidered?
25. What evidence demonstrates that implementation is ready to begin?

---

# Source Quality and Evidence Rules

Prefer:

- WHATWG and W3C specifications
- MDN for browser-platform behavior and compatibility synthesis
- Browser vendor documentation
- Official Lit documentation and source
- Official framework documentation
- Custom Elements Manifest specification and tooling source
- Design Tokens Community Group specification
- Storybook documentation and source
- Playwright documentation and source
- Open Web Components documentation and source
- Mature open-source design-system repositories
- Engineering postmortems with concrete implementation evidence
- Reproducible repository experiments

For every important claim:

- Assign an evidence identifier.
- Record source, date accessed, relevance, and limitations.
- Distinguish specification status from browser implementation status.
- Distinguish official capability from project suitability.
- Seek at least one contradicting source or counterexample for high-impact decisions.
- Avoid presenting emerging or experimental features as stable without explicit qualification.

---

# Execution Discipline

- Work from the repository root.
- Preserve existing work.
- Use version control to inspect history when useful.
- Do not commit secrets, generated caches, dependency directories, or temporary artifacts.
- Follow repository formatting and naming conventions where they are coherent.
- Correct obvious documentation links and indexes required to make the research discoverable.
- Keep generated and authored files clearly separated.
- Record every material repository change.
- Do not silently delete conflicting artifacts. Deprecate, supersede, merge, or archive them with traceability.
- Do not claim that a test or experiment ran unless it actually ran.
- If a tool is unavailable, record the limitation and use the strongest feasible alternative.

---

# Completion Checklist

The task is complete only when:

- The Visual Engineering repository has been thoroughly inspected.
- The likely cross-project consumers have been mapped.
- Foundational hypotheses have been tested and challenged.
- Major authoring, DOM, styling, token, packaging, testing, documentation, integration, and release alternatives have been compared.
- High-risk assumptions have practical probes or strong evidence.
- Failed assumptions are documented.
- A concrete target architecture and repository layout exist.
- Foundational decisions have ADRs.
- REP, journal, evidence, hypothesis, theory, and debt artifacts are updated.
- The diminishing-returns gate is explicitly satisfied.
- An implementation-readiness assessment exists.
- The final autonomous implementation prompt has been written into the Visual Engineering repository.
- The final prompt is self-contained and points to all required source artifacts.
- All new artifacts are indexed and discoverable.
- The final response reports created and modified file paths, major conclusions, confidence, unresolved blockers, and the exact path of the implementation prompt.

---

# Final Response Format

At the end of execution, report:

1. **Research status**
2. **Diminishing-returns evidence**
3. **Recommended architecture in concise form**
4. **Most important assumptions rejected or revised**
5. **Repository files created or updated**
6. **Experiments performed and results**
7. **Implementation readiness**
8. **Remaining risks and research debt**
9. **Exact path to the final Web Components repository implementation prompt**
10. **Exact command or operating context needed to run that prompt**

Do not paste the entire implementation prompt into the terminal response if it has been correctly stored in the repository. Summarize it and provide its path.
