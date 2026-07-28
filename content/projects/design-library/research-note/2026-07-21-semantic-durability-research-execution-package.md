---
identifier: RP-CLF-002
title: Semantic Durability Across Interface Contexts
research_area: Component Library Foundations
discipline:
  - Web Architecture
  - Accessibility Engineering
  - Information Architecture
  - Design Systems
author_agent: OpenAI Autonomous Engineering Research Agent
version: 1.0
confidence: Moderate
completion: Research plan complete; empirical execution pending
priority: Critical
related_projects:
  - Design Library
  - Component Library
related_documents:
  - component-library-foundations-research-report.md
  - Research-Execution-Package-Specification-v2.md
  - Composition_Science_Markdown_Template_v1(1).md
supersedes: null
superseded_by: null
tags:
  - semantic-html
  - component-boundaries
  - stable-markup
  - accessibility
  - information-architecture
  - progressive-enhancement
keywords:
  - semantic durability
  - DOM order
  - visual order
  - component anatomy
  - content model
  - redesign blast radius
llm_ingest: true
machine_readable: true
status: active-research-package
summary: |
  This package defines the next foundational investigation for the component
  library: whether one durable semantic content model can support substantially
  different editorial, application, mobile, marketing, low-vision, and print
  presentations without inaccessible reordering, presentation-specific markup,
  or variant proliferation. Preliminary standards evidence supports semantic
  stability only when meaning and interaction remain stable. The package
  therefore treats stable markup as a bounded hypothesis, establishes competing
  models, measurable failure thresholds, evidence schemas, and handoff instructions
  for executing the study before production component APIs are designed.
project: design-library
purposes:
  - integrate
  - verify
audiences:
  - executive
  - practitioner
  - researcher
---

# Semantic Durability Across Interface Contexts

## Research State Snapshot

**Theory Version:** Pre-theory; foundational report version 0.1  
**Knowledge Base Version:** CLF-KB-0.2  
**Highest Confidence Areas:** Native-first controls; meaningful DOM sequence; contextual layout ownership  
**Lowest Confidence Areas:** Durability of composite content anatomy; limits of one semantic model across product contexts  
**Largest Remaining Unknown:** Whether a shared semantic structure survives major changes in visual hierarchy, interaction, and information density  
**Active Research Streams:** Semantic durability; encapsulation by category; token boundaries; native-control substitution criteria  
**Recently Invalidated Ideas:** Universal custom-element strategy; default Shadow DOM; immutable markup as a goal  
**Priority Changes:** Semantic durability moved ahead of token architecture because an incorrect content model cannot be repaired by tokens or CSS

------------------------------------------------------------------------

# Executive Summary

The foundational report concluded that semantic HTML can remain relatively stable across visual redesign, but only when the markup represents durable meaning rather than a current visual grouping. That conclusion is plausible and standards-aligned, but it has not yet been tested against the project’s actual range of interface contexts.

This package converts that broad conclusion into an executable investigation.

The central hypothesis is:

> A domain-oriented content model can support six structurally different presentations without changing its essential semantic relationships, while presentation-only differences remain in CSS and parent composition.

The investigation must not define production component APIs. It must compare alternative information structures and determine which relationships are truly invariant. It will use one complex domain object rather than a generic card, because “card” is a visual container and may conceal the real semantic unit.

The recommended test object is a **research evidence record** containing:

- identity,
- proposition or finding,
- explanatory summary,
- confidence,
- status,
- provenance,
- supporting relationships,
- contradicting relationships,
- limitations,
- and optional actions.

The same information must be modeled in six contexts:

1. Minimal editorial narrative
2. Dense analytical registry
3. Expressive overview or marketing presentation
4. Mobile-first inspection flow
5. High-accessibility or low-vision presentation
6. Print-oriented research report

Three competing semantic models should be evaluated:

- **M1: Universal record model** — one canonical sequence and anatomy in every context.
- **M2: Core-plus-context model** — invariant semantic core with explicitly contextual supplementary regions.
- **M3: Specialized semantic models** — separate editorial, registry, and action-oriented structures sharing data but not markup.

The likely answer is not total stability or total specialization. Preliminary evidence favors M2: a small invariant semantic core combined with context-owned composition and, where interaction meaning changes, specialized structures. This remains a hypothesis until the transformations are modeled and tested.

No implementation should begin from a generic card API until this study establishes whether “card,” “record,” “finding,” or another domain concept is the durable boundary.

------------------------------------------------------------------------

# Original Objective

Determine what semantic and structural foundation the future component library can safely rely on before production implementation begins.

Specifically:

- identify which content relationships remain stable across radically different visual systems;
- distinguish visual rearrangement from semantic change;
- determine when CSS and parent composition are sufficient;
- determine when markup must change to preserve meaning or interaction;
- detect whether a generic visual abstraction such as a card conceals several incompatible semantic models;
- and produce evidence that can guide later component boundaries without prematurely designing APIs.

------------------------------------------------------------------------

# Scope

## Included

- semantic content relationships;
- document order and meaningful sequence;
- visual hierarchy versus reading hierarchy;
- focus order when optional actions are present;
- content anatomy across six contrasting contexts;
- progressive enhancement and no-JavaScript comprehension;
- localization, right-to-left writing, text enlargement, and print implications;
- comparison of universal, core-plus-context, and specialized models;
- measurable redesign blast radius at the structural level.

## Excluded

- production custom elements;
- naming conventions;
- final attributes, properties, events, slots, or parts;
- token implementation;
- final CSS architecture;
- framework adapters;
- build tooling;
- visual polish;
- final component catalog.

## Boundary condition

Small throwaway semantic diagrams and non-production prototypes may be used as experimental instruments. They must not be treated as library implementation or carried forward without a separate architectural decision.

------------------------------------------------------------------------

# Repository Context

This research follows `component-library-foundations-research-report.md`, which established a hybrid, native-first, category-specific direction. The report identified semantic durability as a high-value unresolved assumption:

- CSS can radically alter presentation but cannot repair missing or incorrect semantics.
- Visual reordering may conflict with reading and focus order.
- A component boundary based on visual similarity may be unstable.
- Contextual layout should generally belong to the parent.
- Accessibility is shared between library and consumer.

This package is the first focused validation cycle beneath that report.

Recommended repository placement:

```text
research/
  packages/
    RP-CLF-002-semantic-durability.md
  journals/
    JR-CLF-002-*.md
  evidence/
    EV-CLF-*.md
  hypotheses/
    HY-CLF-*.md
  experiments/
    EX-CLF-001-semantic-transformations/
      README.md
      content-inventory.md
      context-models.md
      test-matrix.md
      results.md
```

------------------------------------------------------------------------

# Current Understanding

## Observation OBS-CLF-001

### Observation

WCAG requires content whose sequence affects meaning to retain a programmatically determinable correct reading sequence. W3C technique G57 demonstrates that CSS may position elements freely when the underlying sequence remains meaningful. Failure F1 identifies CSS positioning that changes meaning as a failure of WCAG 1.3.2.

### Interpretation

CSS rearrangement is not inherently inaccessible. It becomes unsafe when visual placement implies a relationship or sequence that differs from the DOM, or when keyboard focus no longer follows a logical interaction sequence.

### Confidence

High.

## Observation OBS-CLF-002

### Observation

WCAG focus-order guidance states that focus order need not exactly match visual layout, but it must remain logical and preserve the meaning and operation implied by the visual presentation.

### Interpretation

A component can tolerate some visual rearrangement, but not arbitrary reordering of interactive regions. A design transformation that promotes a secondary action ahead of the primary proposition may require semantic or structural change, not merely CSS order.

### Confidence

High.

## Observation OBS-CLF-003

### Observation

Open UI studies component anatomies before standardizing behavior, states, and events. Its working process treats anatomy as the foundation from which behavior is defined, and its card research shows broad disagreement among systems about what a card contains.

### Interpretation

Component anatomy is not a neutral implementation detail. A premature anatomy can encode assumptions that later constrain behavior and redesign. The diversity of card anatomies weakens the idea that “card” itself is a stable semantic object.

### Confidence

Moderate to high.

## Observation OBS-CLF-004

### Observation

Carbon distinguishes productive and expressive typography strategies and allows them to be blended according to context. It also warns that accessible components do not guarantee an accessible product because content-owner changes can affect compliance.

### Interpretation

Mature systems explicitly support contextual presentation differences while retaining shared foundations, but they do not claim that the component alone controls all semantic or accessibility outcomes.

### Confidence

Moderate.

## Observation OBS-CLF-005

### Observation

The HTML standard allows autonomous custom elements to contain broadly author-defined content, while semantics supplied by the custom element author are not equivalent to the built-in semantics of native elements.

### Interpretation

A custom-element boundary does not validate the content model. The semantic structure must be designed independently of whether it later receives a custom-element wrapper.

### Confidence

High.

------------------------------------------------------------------------

# Key Discoveries

## KD-CLF-001: Stable markup is a constrained optimization target

The correct goal is not immutable DOM. It is minimizing structural change **without sacrificing meaning, operation, or accessibility**.

A redesign requiring markup changes is evidence of one of four conditions:

1. The original markup encoded presentation rather than meaning.
2. The new design introduces a genuinely different interaction model.
3. The visual design conflicts with a meaningful sequence and should be rejected or revised.
4. The domain contains multiple semantic objects that were incorrectly merged.

Only the first represents a clear architectural failure. The others may justify change.

## KD-CLF-002: A semantic core may be more durable than a complete anatomy

Identity, proposition, status, confidence, and provenance may remain invariant while metadata placement, supporting detail, actions, and relationship navigation vary by context.

This suggests distinguishing:

- **semantic invariants** — relationships that must survive every representation;
- **contextual content** — information required only for a particular task;
- **presentation choices** — emphasis, grouping, density, alignment, and decoration;
- **interaction transformations** — disclosures, navigation, selection, editing, or comparison.

## KD-CLF-003: Information priority and information sequence are related but not identical

A title can become visually less prominent without moving in the DOM. Conversely, moving provenance ahead of a finding may alter interpretation in a scientific report even when all content remains present. Visual hierarchy can often change safely; explanatory sequence sometimes cannot.

## KD-CLF-004: The durable unit is likely a domain record, not a card

A card is commonly a visual grouping mechanism. Editorial prose, registry rows, print blocks, and mobile disclosures may all represent the same evidence record without all being cards. The library may eventually need a domain-oriented structure plus separate presentation compositions rather than a universal card component.

## KD-CLF-005: Reuse must be measured at more than one layer

The same data can be reused while markup differs. The same semantic core can be reused while contextual wrappers differ. The same behavior can be reused without sharing the entire visual component. Therefore, “markup reuse” is only one kind of reuse and should not be maximized at the expense of clarity.

------------------------------------------------------------------------

# Hypothesis Registry

## HY-CLF-001: Universal Semantic Record

**Statement:** One canonical semantic sequence for an evidence record can serve all six contexts without changing the relative order of required regions.

**Rationale:** Durable meaning should permit presentation changes through CSS and parent composition.

**Supporting evidence:** WCAG allows CSS positioning when the programmatic sequence remains meaningful; editorial and print views often share a narrative sequence.

**Contradicting evidence:** Dense registries prioritize scanning; mobile views may require progressive disclosure; action-oriented contexts may need controls earlier; scientific interpretation may require provenance before conclusions.

**Status:** Testing.

**Confidence:** Low to moderate.

**Next falsification attempt:** Model the six contexts with one sequence and identify any context where visual order, focus order, or task flow becomes misleading.

## HY-CLF-002: Core-Plus-Context Model

**Statement:** A small invariant semantic core can remain stable while supplementary regions and interaction wrappers vary by context.

**Rationale:** Domain meaning may be stable even when task-specific details and controls differ.

**Supporting evidence:** Mature systems separate foundations from patterns; accessibility is shared with consumers; Open UI separates anatomy, states, and behaviors.

**Contradicting evidence:** Too small a core may provide little practical reuse; contextual regions may become undocumented escape hatches.

**Status:** Testing.

**Confidence:** Moderate.

**Next falsification attempt:** Define the minimum core before transformations, then test whether every context can use it without duplicating or contradicting information.

## HY-CLF-003: Specialized Semantic Models

**Statement:** Editorial, registry, and action-oriented contexts require separate semantic structures even when they share underlying data.

**Rationale:** Task and reading sequence may change enough that one anatomy becomes artificial.

**Supporting evidence:** Visual grouping labels such as card span many incompatible anatomies; focus and reading order must preserve task meaning.

**Contradicting evidence:** Separate models may duplicate markup and accessibility logic and increase migration burden.

**Status:** Testing.

**Confidence:** Moderate.

**Next falsification attempt:** Identify whether differences are genuinely semantic or can be expressed as parent composition and optional contextual content.

## HY-CLF-004: CSS-Only Hierarchy Transformation

**Statement:** Typography, spacing, geometry, grouping, and responsive behavior can create all six visual hierarchies without changing semantic region order.

**Rationale:** CSS is designed to control rendering across media.

**Supporting evidence:** Modern CSS supports grid, flex, logical properties, container queries, media queries, and print styling.

**Contradicting evidence:** CSS cannot create missing semantics or safely resolve every order conflict.

**Status:** Testing.

**Confidence:** Moderate within non-interactive contexts; low across interaction changes.

**Next falsification attempt:** Require a mobile action-first flow and a provenance-first print flow while preserving the same DOM order.

## HY-CLF-005: Visual Card Is Not a Durable Component Boundary

**Statement:** A generic card abstraction will accumulate presentation modes because it groups unrelated semantic objects by appearance.

**Rationale:** Open UI card research shows wide anatomical variation; cards are used for navigation, summaries, commerce, media, status, and actions.

**Supporting evidence:** Existing design systems document many card types and anatomies.

**Contradicting evidence:** A deliberately minimal surface/container abstraction may remain useful if it claims no domain semantics.

**Status:** Provisionally supported.

**Confidence:** Moderate.

**Next falsification attempt:** Compare a purely visual surface composition with a domain evidence record and determine which public obligations each would need.

## HY-CLF-006: DOM Order Can Remain Task-Neutral

**Statement:** A single DOM sequence can remain logical for reading, keyboard navigation, and comprehension across all six contexts.

**Rationale:** A strong semantic sequence may outlive presentation changes.

**Supporting evidence:** Meaningful sequence can remain stable while CSS changes placement.

**Contradicting evidence:** Tasks differ between reading, scanning, comparing, navigating, and acting.

**Status:** Testing.

**Confidence:** Low.

**Next falsification attempt:** Conduct task walkthroughs and screen-reader linearization for every context.

------------------------------------------------------------------------

# Experimental Program

## EX-CLF-001: Semantic Transformation Matrix

### Research question

Which relationships in an evidence record remain invariant across editorial, registry, expressive, mobile, low-vision, and print contexts?

### Inputs

Create a content corpus with at least twelve evidence records exhibiting:

- short and very long titles;
- no summary and multi-paragraph summaries;
- low, moderate, and high confidence;
- supported, challenged, and superseded status;
- zero, one, and many sources;
- supporting and contradicting relationships;
- missing optional metadata;
- long translated labels;
- right-to-left text;
- actionable and non-actionable records;
- asynchronous status updates;
- and malformed or incomplete imported data.

### Predefined semantic candidates

Before visual modeling, inventory candidate relationships without assigning markup:

- record identity;
- proposition heading;
- explanatory body;
- confidence qualifier;
- lifecycle status;
- provenance/source relation;
- support relation;
- contradiction relation;
- limitation/caveat;
- action set;
- collection membership;
- chronology.

For each relationship, classify it as:

- invariant;
- context-required;
- optional;
- derived;
- presentation-only;
- or unresolved.

### Competing models

#### Model M1 — Universal record

One complete semantic sequence is used in every context. CSS and parent composition perform all transformations.

#### Model M2 — Core plus contextual regions

A stable core is preserved; task-specific supplementary content and controls are supplied by contextual compositions.

#### Model M3 — Specialized models

Separate structures are used for narrative evidence, registry evidence, and actionable evidence, sharing only data contracts and lower-level behaviors.

### Context transformations

#### C1 Minimal editorial

Primary task: understand an argument in narrative flow.

Pressure applied:

- prose integration;
- narrow measure;
- low visual chrome;
- source citations near claims;
- optional actions visually quiet.

#### C2 Dense analytical registry

Primary task: scan, sort, compare, and inspect many records.

Pressure applied:

- high density;
- repeated columns or aligned fields;
- truncated summaries;
- status and confidence visible at a glance;
- batch selection may be present.

#### C3 Expressive overview

Primary task: orient and persuade without losing research integrity.

Pressure applied:

- dramatic scale differences;
- selective metadata;
- imagery or illustration adjacency;
- asymmetrical composition;
- limited initial detail.

#### C4 Mobile inspection flow

Primary task: review one record and take an action in a narrow viewport.

Pressure applied:

- progressive disclosure;
- persistent or prominent actions;
- long touch targets;
- uncertain network and delayed JavaScript;
- one-column reading sequence.

#### C5 Low-vision presentation

Primary task: read and understand with enlarged text, strong contrast, and reduced visual complexity.

Pressure applied:

- 200% text size;
- user text-spacing overrides;
- strong focus indication;
- no information encoded only by color;
- minimal motion;
- content reflow without two-dimensional scrolling except where essential.

#### C6 Print research report

Primary task: preserve argument, provenance, and stable references on paper or PDF.

Pressure applied:

- no interactive disclosure;
- visible URLs or reference identifiers where required;
- pagination;
- orphan/widow pressure;
- grayscale legibility;
- repeated contextual headings.

### Measurements

For each model and context, record:

1. Required semantic relationships retained
2. Required relationship changes
3. Region-order changes
4. Interactive-order changes
5. Duplicated information
6. Omitted information
7. Context-specific wrappers
8. Presentation-specific fields or switches
9. CSS visual reordering operations
10. Cases where visual and DOM sequence diverge
11. Screen-reader linearization defects
12. Keyboard focus-order defects
13. No-JavaScript comprehension failures
14. Localization or RTL defects
15. Print-only structural changes
16. Author explanation steps required
17. Number of exceptions to the model

### Failure thresholds

A model is weakened when any of the following occurs:

- more than two contexts require a different meaningful sequence;
- visual reordering creates a conflict with reading or focus order;
- more than two presentation-specific switches are required to make the anatomy usable;
- a context needs duplicate hidden content to preserve accessibility;
- consumers must know undocumented internal ordering assumptions;
- optional regions create contradictory or nonsensical combinations;
- no-JavaScript output becomes materially incomplete;
- the same field has different semantic meaning across contexts;
- or more than 20% of records require one-off exceptions.

A model is falsified for universal use when:

- a required context cannot preserve correct meaning and operation without structural change;
- or preserving the model requires an accessibility failure.

### Success criteria

A model is provisionally supported when:

- all invariant relationships remain programmatically available;
- no context produces a meaningful-sequence or focus-order conflict;
- presentation changes do not require hidden duplicate content;
- context-specific additions are explicit and bounded;
- no more than one semantic structure change is required across six contexts;
- and authors can explain the model without knowledge of implementation internals.

### Manual evaluation

- Linear reading review with styles disabled
- Keyboard-only walkthrough
- Screen-reader review in at least VoiceOver/Safari and NVDA/Firefox or Chrome
- 200% browser zoom
- WCAG text-spacing override
- Forced-colors mode
- Print preview and generated PDF inspection
- Right-to-left review
- Translation expansion review
- No-JavaScript review

### Automated evaluation

- HTML validation
- Accessibility scanning
- heading and landmark structure assertions
- focusable-element order extraction
- duplicate-ID detection
- DOM sequence snapshots
- content-completeness assertions
- generated model-combination checks
- print overflow checks where tooling permits

### Output

- `content-inventory.md`
- `semantic-invariants.md`
- `context-models.md`
- `transformation-matrix.csv`
- `accessibility-results.md`
- `exceptions.md`
- `decision-record.md`
- updated evidence and hypothesis registries

------------------------------------------------------------------------

# Evidence Registry

## EV-CLF-001: Meaningful sequence permits styling but constrains order

**Date:** 2026-07-21  
**Experiment:** Standards review  
**Observation:** WCAG technique G57 permits CSS positioning when the underlying sequence remains meaningful.  
**Measurement:** Normative accessibility requirement supported by W3C guidance.  
**Relevant hypotheses:** HY-CLF-001, HY-CLF-004, HY-CLF-006  
**Effect:** Supports bounded semantic stability; contradicts arbitrary visual reordering.  
**Confidence:** High  
**Limitations:** Does not determine the best sequence for this project’s domain records.  
**Reproduction:** Review WCAG 2.2 technique G57 and compare the DOM sequence with visual positioning.  
**Source:** https://www.w3.org/WAI/WCAG22/Techniques/general/G57

## EV-CLF-002: CSS positioning can fail meaningful sequence

**Date:** 2026-07-21  
**Experiment:** Standards counterexample review  
**Observation:** W3C failure F1 identifies content whose meaning changes because CSS positioning differs from programmatic order.  
**Measurement:** Explicit documented WCAG failure.  
**Relevant hypotheses:** HY-CLF-004, HY-CLF-006  
**Effect:** Weakens CSS-only transformation as a universal strategy.  
**Confidence:** High  
**Limitations:** Requires project-specific judgment about when meaning changes.  
**Reproduction:** Review failure examples and linearize proposed context models.  
**Source:** https://www.w3.org/WAI/WCAG22/Techniques/failures/F1

## EV-CLF-003: Focus order must preserve visual meaning and operation

**Date:** 2026-07-21  
**Experiment:** Accessibility standards review  
**Observation:** Focus order may differ from visual layout but must remain logical and preserve the meaning and operation conveyed by the visual presentation.  
**Measurement:** WCAG 2.4.3 understanding guidance.  
**Relevant hypotheses:** HY-CLF-001, HY-CLF-006  
**Effect:** Establishes a hard constraint on action and control rearrangement.  
**Confidence:** High  
**Limitations:** Logical order still requires human evaluation.  
**Reproduction:** Tab through each model and compare focus progression with visual and semantic hierarchy.  
**Source:** https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html

## EV-CLF-004: Component anatomy precedes behavior standardization

**Date:** 2026-07-21  
**Experiment:** Open UI process review  
**Observation:** Open UI treats anatomy as the foundation for defining behavior, states, and events.  
**Measurement:** Repeated process guidance across Open UI documentation.  
**Relevant hypotheses:** HY-CLF-001, HY-CLF-002, HY-CLF-003  
**Effect:** Supports researching semantic structure before API or behavior design.  
**Confidence:** Moderate to high  
**Limitations:** Open UI focuses primarily on common controls, not all domain composites.  
**Reproduction:** Review Open UI working mode, glossary, and contribution guidance.  
**Sources:** https://open-ui.org/working-mode/ ; https://open-ui.org/get-involved/ ; https://open-ui.org/glossary/

## EV-CLF-005: Card anatomy is inconsistent across design systems

**Date:** 2026-07-21  
**Experiment:** Cross-system anatomy review  
**Observation:** Open UI’s card research catalogs divergent card concepts and parts, including basic, media, image, illustration, metadata, and overlay forms.  
**Measurement:** Multiple independent design systems use the same name for different anatomical and behavioral concepts.  
**Relevant hypothesis:** HY-CLF-005  
**Effect:** Supports treating card as a visual pattern rather than assuming a universal domain component.  
**Confidence:** Moderate  
**Limitations:** Divergence does not prove a minimal surface abstraction is useless.  
**Reproduction:** Compare the systems listed in Open UI card research.  
**Source:** https://open-ui.org/components/card.research/

## EV-CLF-006: Accessible components do not guarantee accessible products

**Date:** 2026-07-21  
**Experiment:** Mature-system guidance review  
**Observation:** Carbon states that individually accessible components are only part of building accessible products, and content-owner changes can affect compliance.  
**Measurement:** Explicit architecture and governance guidance from a mature production system.  
**Relevant hypotheses:** HY-CLF-002, HY-CLF-003  
**Effect:** Supports a shared accessibility contract and contextual evaluation.  
**Confidence:** Moderate  
**Limitations:** Carbon guidance is not a browser standard.  
**Reproduction:** Review Carbon accessibility overview and component accessibility guidance.  
**Sources:** https://carbondesignsystem.com/guidelines/accessibility/overview/ ; https://v10.carbondesignsystem.com/components/list/accessibility/

## EV-CLF-007: User text overrides are a structural stressor

**Date:** 2026-07-21  
**Experiment:** Accessibility adaptability review  
**Observation:** WCAG text-spacing guidance requires content to adapt when users override line, word, letter, and paragraph spacing.  
**Measurement:** WCAG 1.4.12 understanding guidance.  
**Relevant hypotheses:** HY-CLF-001, HY-CLF-004  
**Effect:** Requires models to survive content expansion and user formatting, not only design-system CSS.  
**Confidence:** High  
**Limitations:** Does not directly settle semantic anatomy.  
**Reproduction:** Apply the WCAG text-spacing values to each context model.  
**Source:** https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html

------------------------------------------------------------------------

# Failed Assumptions

## FA-CLF-001: Zero markup change is the success criterion

**Why it seemed reasonable:** Markup stability appears to minimize redesign cost and improve reuse.

**Why it fails:** It rewards preserving a structure even when interaction, reading sequence, or meaning has changed. It can encourage CSS reordering, duplicate hidden content, and overloaded variants.

**Replacement:** Minimize semantic-model churn while allowing evidence-backed structural change.

## FA-CLF-002: A visually repeated container is necessarily a reusable component

**Why it seemed reasonable:** Cards and panels recur throughout interfaces and appear to offer easy standardization.

**Why it fails:** Similar surfaces may represent navigation, evidence, commerce, status, selection, or actions. Their semantics and accessibility obligations differ.

**Replacement:** Separate surface composition from domain semantics and behavior.

## FA-CLF-003: CSS can absorb every hierarchy change

**Why it seemed reasonable:** Modern CSS can alter layout, typography, density, and responsive behavior extensively.

**Why it fails:** CSS cannot safely manufacture missing semantics or repair a meaningful-sequence conflict. Interactive order remains constrained.

**Replacement:** CSS owns presentation until a transformation changes meaning or operation.

------------------------------------------------------------------------

# Architectural Comparisons

## Comparison 1: Universal anatomy versus core-plus-context

| Dimension | Universal anatomy | Core plus context |
|---|---|---|
| Markup reuse | Highest initially | High for invariant core |
| Semantic clarity | Strong if sequence is truly universal | Strong if contextual boundaries are explicit |
| Variant pressure | High when contexts diverge | Moderate |
| Authoring complexity | Low at first, rises with exceptions | Moderate but more explicit |
| Accessibility risk | Reordering and hidden duplication | Misuse of optional contextual regions |
| Replaceability | Lower if consumers depend on complete anatomy | Higher if core contract remains small |
| Likely fit | Narrowly similar contexts | Broad but related contexts |

**Preliminary judgment:** Core-plus-context is the leading candidate, but must be protected from becoming an unbounded slot or escape-hatch system.

## Comparison 2: Shared markup versus shared data

| Approach | Benefit | Risk |
|---|---|---|
| Shared markup | Fewer templates; consistent semantics | Artificial universality and variants |
| Shared data model | Context-specific semantics possible | Multiple renderers and duplicated accessibility work |
| Shared semantic core plus specialized renderers | Balanced reuse | More governance and explicit boundaries required |

**Preliminary judgment:** The architecture should permit reuse at data, semantic-core, behavior, and presentation layers independently.

## Comparison 3: Generic card versus domain record

| Dimension | Generic card | Domain record |
|---|---|---|
| Meaning | Usually unspecified | Explicit |
| Reuse breadth | Visually broad | Domain-bounded |
| API pressure | Presentation switches | Domain states and relationships |
| Styling freedom | High if purely presentational | High if content remains open |
| Accessibility contract | Depends on contents | Can document required relationships |
| Failure mode | Becomes giant variant container | Becomes too domain-specific |

**Preliminary judgment:** Retain “surface/card” only as a composition concept unless later evidence demonstrates stable behavior. Use domain records when the domain relationship itself is reusable.

------------------------------------------------------------------------

# Theory Impact Assessment

## Affected theory records

No canonical theory registry exists yet. This package proposes the following candidates.

## New principle candidates

### TH-CLF-001: Semantic Stability Boundary

A structure should remain stable only while its meaning, required reading sequence, and interaction model remain stable.

**Prediction:** Redesigns that alter only typography, spacing, geometry, and grouping can retain semantic structure; redesigns that alter task sequence or information relationships will require contextual composition or structural change.

### TH-CLF-002: Layered Reuse Principle

Reuse should be evaluated independently at the data, semantic, behavioral, compositional, and visual layers.

**Prediction:** Systems that demand whole-component reuse will accumulate more variants than systems that permit reuse at narrower layers.

### TH-CLF-003: Visual Container Non-Equivalence

Repeated visual containment is insufficient evidence that contained objects share a component boundary.

**Prediction:** Generic card APIs will accumulate domain and presentation modes unless restricted to a minimal surface role.

## Deprecated principles

- Immutable markup as an architectural objective.
- Visual recurrence as sufficient evidence for componentization.

## Confidence changes

- Semantic stability: Moderate → Moderate with narrower scope.
- CSS redesignability: High for presentation → unchanged.
- Universal card abstraction: Uncertain → weakened.

## Predictions created

1. At least one of the six contexts will require a different interaction sequence.
2. A universal complete anatomy will produce more exceptions than a core-plus-context model.
3. The invariant semantic core will contain fewer regions than the first proposed evidence component.
4. Print and dense registry contexts will expose the most significant sequence tension.

## Predictions invalidated

None yet; empirical execution is pending.

## Required theory registry updates

Create TH-CLF-001 through TH-CLF-003 as candidate records, not accepted theory.

------------------------------------------------------------------------

# Decision Log

## DF-CLF-001: Test a domain record before a generic card

**Context:** A generic card is visually familiar but semantically ambiguous.

**Options considered:** Generic card first; native article/section examples; evidence record; multiple unrelated components.

**Evidence:** EV-CLF-004 and EV-CLF-005 show that anatomy matters and card definitions vary widely.

**Decision:** Use a complex evidence record as the primary semantic-durability test object. Include a minimal surface/card abstraction only as a comparison.

**Tradeoffs:** Domain specificity may underrepresent other products, but it exposes richer semantic pressure than a decorative container.

**Risks:** Findings may not generalize to controls or commerce objects.

**Reversal condition:** If the evidence record’s relationships are too unique to expose general component-boundary principles, repeat with a resource or actionable task record.

## DF-CLF-002: Compare three models rather than defend one

**Context:** The foundational report tentatively favored stable semantic markup.

**Options considered:** Validate one canonical structure; compare universal and specialized models; compare universal, core-plus-context, and specialized models.

**Evidence:** Current standards establish constraints but do not select the correct domain model.

**Decision:** Compare all three serious models.

**Tradeoffs:** More evaluation work, but substantially better falsification value.

**Risks:** Evaluators may unintentionally make one model weaker through poor modeling.

**Reversal condition:** None; competing implementation is part of the scientific method for this research stream.

## DF-CLF-003: Treat accessibility conflicts as falsification

**Context:** Stable markup could be preserved through visual reordering even when sequence becomes confusing.

**Evidence:** EV-CLF-001 through EV-CLF-003.

**Decision:** Any model requiring an accessibility regression to remain universal is falsified for universal use.

**Tradeoffs:** Reduces superficial markup reuse.

**Risks:** Human judgments of logical sequence may differ.

**Reversal condition:** Only stronger accessibility evidence showing the flagged sequence is logical and correctly conveyed.

------------------------------------------------------------------------

# Open Questions

1. Which evidence-record relationships are truly invariant rather than merely common?
2. Does confidence semantically qualify the proposition, the source base, or the overall record?
3. Is status part of identity, metadata, or task state?
4. Must provenance precede interpretation in research contexts?
5. Can actions remain after descriptive content in every interactive context?
6. Does progressive disclosure preserve enough meaning without JavaScript?
7. When is a collection a semantic list, table, feed, or set of independent articles?
8. Should dense comparison use a fundamentally different semantic model from narrative reading?
9. What information must print reveal that interactive interfaces may defer?
10. How should contextual additions be constrained so M2 does not become arbitrary slots?
11. Which relationships should be represented in visible content versus machine-readable metadata?
12. Can a domain record remain useful outside the research repository, or is it intentionally domain-specific?

------------------------------------------------------------------------

# Recommended Next Research

## Priority 1 — Execute EX-CLF-001

**Information gain:** Very high  
**Architectural risk addressed:** Incorrect semantic foundation  
**Effort:** Moderate  
**Urgency:** Immediate

## Priority 2 — Component taxonomy based on discovered invariants

Classify candidate library entries only after EX-CLF-001 distinguishes:

- native semantics;
- styling conventions;
- behavioral enhancements;
- semantic wrappers;
- domain composites;
- contextual compositions;
- and rejected visual abstractions.

**Information gain:** High  
**Risk:** Component-boundary error  
**Effort:** Moderate

## Priority 3 — Encapsulation experiment using the winning semantic model

Compare light DOM, Shadow DOM with slots/parts, and behavior-only enhancement after anatomy is understood.

**Information gain:** High  
**Risk:** Styling and accessibility coupling  
**Effort:** Moderate

## Priority 4 — Native control substitution criteria

Build a decision framework for when native elements may be enhanced or replaced, drawing from Open UI and accessibility evidence.

**Information gain:** High  
**Risk:** Rebuilding inaccessible controls  
**Effort:** Moderate

------------------------------------------------------------------------

# Research Backlog

| Rank | Research item | Expected information gain | Risk addressed | Effort |
|---:|---|---|---|---|
| 1 | Semantic transformation matrix | Very high | Wrong content model | Medium |
| 2 | Light DOM vs Shadow DOM by category | High | Encapsulation lock-in | Medium |
| 3 | Native controls decision framework | High | Accessibility and behavior debt | Medium |
| 4 | Token dependency and override model | High | Theme coupling | Medium-high |
| 5 | Parent-owned vs intrinsic layout study | High | Variant explosion | Medium |
| 6 | Server rendering and upgrade timing | Medium-high | Progressive enhancement | Medium |
| 7 | Cross-framework authoring ergonomics | Medium | Integration friction | Medium-high |
| 8 | Long-term design-system migration cases | Medium | Governance debt | High |

------------------------------------------------------------------------

# Suggested Specialized Research Agents

## Agent SRA-CLF-SEM

**Specialty:** Information architecture and semantic HTML  
**Task:** Execute content inventory, semantic invariants, and model comparison.

## Agent SRA-CLF-A11Y

**Specialty:** Accessibility engineering  
**Task:** Evaluate meaningful sequence, focus order, screen-reader linearization, zoom, text spacing, forced colors, and no-JavaScript behavior.

## Agent SRA-CLF-SYS

**Specialty:** Design-system comparative analysis  
**Task:** Compare how mature systems model cards, structured lists, data rows, status, and metadata.

## Agent SRA-CLF-I18N

**Specialty:** Internationalization  
**Task:** Stress test translated content, bidirectional text, logical properties, and culturally variable reading conventions.

------------------------------------------------------------------------

# Parallel Research Opportunities

The following can proceed without contaminating EX-CLF-001:

- catalog native HTML capabilities relevant to the first component slice;
- document browser support and platform trajectory for custom elements, declarative Shadow DOM, popover, dialog, and form-associated custom elements;
- analyze token migration histories in Material, Carbon, Spectrum, and FAST;
- define research repository schemas and automated evidence traceability.

Do not design component APIs in these parallel streams.

------------------------------------------------------------------------

# Risks

## R-CLF-001: Domain overfitting

The evidence record may be too specialized. Mitigation: extract general laws cautiously and repeat later with one action-oriented domain object.

## R-CLF-002: Visual design bias

A weak transformation may falsely support universal markup. Mitigation: require six structurally contrasting contexts and independent review.

## R-CLF-003: Retrofitted criteria

Researchers may move failure thresholds after seeing results. Mitigation: preserve this package and record every threshold change with rationale.

## R-CLF-004: Accessibility reduced to automation

Automated tools cannot judge meaningful sequence reliably. Mitigation: require manual linearization, keyboard, and screen-reader evaluation.

## R-CLF-005: Core-plus-context becomes slot sprawl

The leading model could absorb every difference through arbitrary extension points. Mitigation: count contextual regions and require a semantic reason for each.

## R-CLF-006: Confusing data reuse with component reuse

A shared schema may be mistaken for proof of shared markup. Mitigation: report reuse independently by layer.

------------------------------------------------------------------------

# Cross-Discipline Opportunities

## Information architecture

Provides methods for identifying entities, relationships, hierarchy, sequence, and task-dependent views.

## Cognitive psychology

Can test whether altered sequence changes comprehension, confidence judgments, or recall.

## Typography

Can determine how much visual hierarchy can change without changing semantic sequence.

## Gestalt psychology

Can identify when proximity and enclosure imply relationships absent from the DOM.

## Human factors

Can evaluate scanning, action placement, error likelihood, and low-vision adaptation.

## Scientific communication

Can determine when provenance, uncertainty, and counterevidence must appear relative to claims.

------------------------------------------------------------------------

# Knowledge Relationships

```text
TH-CLF-001 Semantic Stability Boundary
  supported by EV-CLF-001, EV-CLF-002, EV-CLF-003
  tested by EX-CLF-001
  constrains future component anatomy decisions

TH-CLF-002 Layered Reuse Principle
  supported by KD-CLF-002, KD-CLF-005
  tested by M1/M2/M3 comparison
  affects library taxonomy and migration strategy

TH-CLF-003 Visual Container Non-Equivalence
  supported by EV-CLF-004, EV-CLF-005
  tested by generic-card vs evidence-record comparison
  affects whether card becomes component or composition
```

------------------------------------------------------------------------

# Repository Updates

Add this package as the active research handoff. Create empty registries only if the repository does not already contain canonical ones. Do not duplicate existing registries.

Required updates after execution:

- append new EV records rather than renumbering;
- update HY status and confidence;
- create the experiment result document;
- create decision records for accepted and rejected semantic models;
- link the foundational report to this REP;
- record any new assumptions discovered during modeling.

------------------------------------------------------------------------

# Website Updates

When the research website exists, expose:

- package metadata;
- current hypotheses and confidence;
- transformation matrix;
- evidence relationships;
- failed models;
- remaining unknowns;
- reproduction instructions.

Do not publish preliminary conclusions as settled architectural guidance.

------------------------------------------------------------------------

# AI Consumption Notes

An agent continuing this work should interpret “stable markup” as a hypothesis with accessibility boundaries, not as a command to preserve DOM at all costs.

Important distinctions:

- Data model is not markup model.
- Visual container is not semantic component.
- Presentation hierarchy is not always reading sequence.
- Contextual composition is not necessarily component variation.
- Structural change is not automatically architectural failure.
- Accessibility regression is a hard failure, not a tradeoff to hide.

Before adding any region to a model, the agent must state:

1. the semantic relationship represented;
2. whether it is invariant or contextual;
3. the evidence for its position;
4. what happens when it is absent;
5. and whether it affects focus or reading order.

------------------------------------------------------------------------

# Handoff Instructions

The next agent should:

1. Read `component-library-foundations-research-report.md` in full.
2. Read this package in full.
3. Create the twelve-record stress corpus before proposing markup.
4. Inventory semantic relationships without using component names such as card, header, footer, or sidebar.
5. Freeze the initial success and failure criteria.
6. Model M1, M2, and M3 seriously.
7. Transform each model into all six contexts.
8. Run manual accessibility and content-sequence reviews.
9. Record exceptions and failures, including those that undermine the preferred model.
10. Update evidence, hypotheses, theory candidates, and decision records.
11. Produce RP-CLF-003 with results and the next highest-value research question.

The next agent must not:

- design production APIs;
- adopt a custom element merely to make the prototype feel realistic;
- use CSS visual order to conceal an invalid sequence;
- declare M2 successful because it is the current leading hypothesis;
- or collapse different semantic models solely to maximize reuse.

------------------------------------------------------------------------

# Research Journal

## JR-CLF-002-001 — 2026-07-21

### Question

What is the highest-risk unresolved assumption after the foundation report?

### Observation

Token, encapsulation, and API decisions all depend on having a defensible semantic structure. If the content model is wrong, later mechanisms merely stabilize the wrong boundary.

### Interpretation

Semantic durability should be tested before detailed Shadow DOM or token experiments.

### Decision

Promote semantic durability to the next critical research stream.

### Confidence

High.

## JR-CLF-002-002 — 2026-07-21

### Question

Should the first subject be a generic card?

### Observation

Card anatomy varies substantially across design systems, and the term often identifies a surface rather than a stable semantic entity.

### Interpretation

A generic card could produce misleadingly shallow evidence.

### Decision

Use a domain evidence record and retain a minimal card/surface only as a competing abstraction.

### Confidence

Moderate to high.

## JR-CLF-002-003 — 2026-07-21

### Question

What would falsify stable markup?

### Observation

Standards permit visual positioning but reject sequence changes that alter meaning; focus order must preserve operation and implied relationships.

### Interpretation

An accessibility conflict is not merely a weakness. It falsifies that semantic model for universal use.

### Decision

Make meaningful-sequence and focus-order conflicts hard failure criteria.

### Confidence

High.

------------------------------------------------------------------------

# Research Quality Metrics

| Metric | Current value |
|---|---:|
| Primary standards sources | 4 |
| Mature-system sources | 2 |
| Independent source organizations | 4 |
| Counterexamples reviewed | 3 |
| Competing viewpoints/models defined | 3 |
| Hypotheses active | 6 |
| Failed assumptions documented | 3 |
| Empirical experiments completed | 0 |
| Research completeness | 45% |
| Confidence gain | Moderate narrowing, no empirical confirmation |
| Open questions reduced | 2 broad questions converted into 12 testable questions |

------------------------------------------------------------------------

# Research Debt

## Missing evidence

- empirical transformation results;
- screen-reader observations;
- authoring usability results;
- real product content beyond research records;
- long-term maintenance evidence.

## Missing experiments

- M1/M2/M3 implementation as throwaway semantic models;
- nested contextual composition;
- dynamic updates;
- removal and replacement test;
- cross-framework rendering, deferred until later.

## Missing disciplines

- professional information architecture review;
- localization review;
- low-vision user evaluation;
- scientific communication review.

## Replication needed

Repeat semantic-durability testing later with an action-oriented object such as a task, notification, or approval request.

## Tool limitations

Automated accessibility scanners cannot determine whether content order preserves meaning. Manual review is mandatory.

## Assumptions awaiting evidence

- M2 is better than M1 and M3;
- evidence record is representative enough;
- one semantic core can remain useful across product families;
- contextual composition can remain bounded.

------------------------------------------------------------------------

# Appendix A — Source Register

## Standards and platform research

1. W3C, “G57: Ordering the content in a meaningful sequence.”  
   https://www.w3.org/WAI/WCAG22/Techniques/general/G57

2. W3C, “F1: Failure of Success Criterion 1.3.2 due to changing the meaning of content by positioning information with CSS.”  
   https://www.w3.org/WAI/WCAG22/Techniques/failures/F1

3. W3C, “Understanding Success Criterion 2.4.3: Focus Order.”  
   https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html

4. W3C, “Understanding Success Criterion 1.4.12: Text Spacing.”  
   https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html

5. WHATWG, “HTML Living Standard.”  
   https://html.spec.whatwg.org/

6. Open UI, “Working Mode.”  
   https://open-ui.org/working-mode/

7. Open UI, “Getting Involved.”  
   https://open-ui.org/get-involved/

8. Open UI, “Glossary.”  
   https://open-ui.org/glossary/

9. Open UI, “Card Research.”  
   https://open-ui.org/components/card.research/

## Mature design-system evidence

10. IBM Carbon Design System, “Accessibility Overview.”  
    https://carbondesignsystem.com/guidelines/accessibility/overview/

11. IBM Carbon Design System, “Typography Style Strategies.”  
    https://carbondesignsystem.com/elements/typography/style-strategies/

------------------------------------------------------------------------

# Appendix B — Completion Checklist

- [x] Identifier and required metadata
- [x] Research state snapshot
- [x] Executive summary
- [x] Original objective
- [x] Scope
- [x] Repository context
- [x] Current understanding
- [x] Key discoveries
- [x] Evidence registry
- [x] Hypothesis registry
- [x] Failed assumptions
- [x] Architectural comparisons
- [x] Open questions
- [x] Recommended next research
- [x] Research backlog
- [x] Suggested specialized agents
- [x] Parallel research opportunities
- [x] Risks
- [x] Cross-discipline opportunities
- [x] Knowledge relationships
- [x] Repository updates
- [x] Website updates
- [x] AI consumption notes
- [x] Handoff instructions
- [x] Research journal
- [x] Theory impact assessment
- [x] Research quality metrics
- [x] Research debt
- [x] Appendix
- [ ] Empirical experiment executed
- [ ] Hypotheses revised from results
- [ ] Final semantic architecture recommendation issued

------------------------------------------------------------------------

# Revision History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0 | 2026-07-21 | OpenAI Autonomous Engineering Research Agent | Created executable semantic-durability research package and defined the next foundational experiment. |
