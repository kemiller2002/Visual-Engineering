---
identifier: DF-CS-ATLAS-001
title: Composition Science Atlas Research Framework
research_area: Composition Science
discipline: Cross-disciplinary research methodology
authors:
  - OpenAI Research Agent
author_agent: GPT-5.6 Thinking
confidence: Medium-High
completion: 100
priority: Critical
date: 2026-07-21
llm_ingest: true
machine_readable: true
project: composition-science
purpose: |
  Define the canonical method by which evidence from different disciplines is collected,
  evaluated, translated, compared, and incorporated into the Composition Science knowledge system.
references:
  - Composition_Science_Markdown_Template_v1(1).md
  - Research-Execution-Package-Specification-v2.md
related_projects:
  - Project Atlas
related_documents:
  - Composition Science Markdown Template v1
  - Research Execution Package Specification v2
supersedes: null
superseded_by: null
status: canonical-candidate
summary: |
  This framework turns Project Atlas from a collection of discipline reports into a governed
  evidence network. It defines common research questions, stable records, evidence evaluation,
  cross-disciplinary translation, contradiction handling, principle synthesis, and update rules.
  Its central safeguard is that apparent agreement across disciplines is not treated as independent
  confirmation until shared intellectual ancestry, duplicated evidence, and domain mismatch have
  been examined.
version: 1.0
tags:
  - atlas
  - cross-disciplinary research
  - evidence synthesis
  - composition science
  - knowledge graph
keywords:
  - principles
  - evidence independence
  - translation
  - contradiction
  - composition genome
  - research workflow
purposes:
  - orient
  - integrate
  - reference
audiences:
  - practitioner
  - researcher
  - contributor
---

# Composition Science Atlas Research Framework

## Purpose

This document defines how research from architecture, perception science, neuroscience, typography,
painting, film, music, cartography, industrial design, human factors, linguistics, biology, systems
engineering, and other disciplines enters the Composition Science knowledge system.

Its purpose is not merely to standardize reports. It is to make findings comparable without erasing
the differences between disciplines.

The framework must allow future research agents to determine:

1. What a discipline has learned.
2. What kind of evidence supports that knowledge.
3. Whether the evidence is independent or derivative.
4. Which underlying composition principles may be shared across domains.
5. Where translation between domains is valid, partial, or misleading.
6. What contradictions reveal about boundary conditions.
7. What should be promoted into the theory registry.
8. What remains uncertain and should be studied next.

------------------------------------------------------------------------

# Research State Snapshot

## Theory Version

Not yet assigned. The current body of work is pre-unification and should be treated as a collection
of candidate principles rather than a settled theory.

## Knowledge Base Version

Atlas Framework 1.0.

## Highest Confidence Areas

- Human perceptual limits constrain every visual composition system.
- Domain context changes the usefulness of otherwise valid principles.
- Stable identifiers and evidence traceability are necessary for cumulative research.
- Contradictions and failures carry as much scientific value as confirming evidence.

## Lowest Confidence Areas

- Whether a small set of universal composition laws exists.
- Whether principles can be quantitatively transferred between media.
- Whether a “composition genome” will prove analytically useful rather than merely descriptive.
- How confidence should be aggregated across heterogeneous evidence types.

## Largest Remaining Unknown

Can cross-disciplinary similarities be reduced to common causal mechanisms, or are many of them
only metaphorical similarities created by broad language such as hierarchy, rhythm, balance, and
flow?

## Active Research Streams

- Visual perception and attention
- Color science
- Typography
- Architecture and spatial cognition
- Product and industrial design
- Familiarity, convention, and intuitive interaction
- Web component foundations
- Artist and movement composition analysis

## Recently Invalidated Ideas

None formally registered. However, the assumption that convergence across multiple disciplines is
inherently strong evidence is rejected by this framework.

## Priority Changes

Cross-disciplinary synthesis should not wait until all discipline research is complete. Translation,
contradiction detection, and evidence lineage should be recorded from the beginning.

------------------------------------------------------------------------

# Key Findings

- Atlas should be organized as an evidence graph, not only as a folder hierarchy or encyclopedia.
- Every discipline should be studied through a common question set, but discipline-specific methods
  and vocabulary must be preserved.
- Cross-disciplinary agreement must be tested for shared ancestry before it counts as independent
  convergence.
- “Universal principles” should begin as hypotheses and earn promotion through causal explanation,
  boundary testing, prediction, and replication.
- Translation records are first-class research artifacts. They are not informal analogies.
- Contradictions should usually produce boundary conditions, subtypes, or rejected translations
  rather than being averaged away.
- The composition genome should initially be treated as an exploratory model, not a scientific law.

------------------------------------------------------------------------

# 1. Governing Model

Project Atlas contains six connected layers.

```text
Disciplines
    ↓
Source Evidence
    ↓
Domain Findings
    ↓
Cross-Discipline Translations
    ↓
Candidate Principles and Boundary Conditions
    ↓
Theory, Predictions, Experiments, and Applications
```

Each layer answers a different question.

| Layer | Question |
|---|---|
| Discipline | Where did the knowledge originate? |
| Source evidence | What was actually observed, measured, argued, or demonstrated? |
| Domain finding | What does the evidence support inside its original field? |
| Translation | What corresponding structure may exist in another field? |
| Candidate principle | What deeper mechanism could explain multiple findings? |
| Theory and application | What can now be predicted, tested, or used? |

No layer may silently substitute for another. A respected design tradition is not empirical evidence.
A correlation is not a mechanism. A metaphor is not a validated translation. A useful heuristic is
not automatically a universal principle.

------------------------------------------------------------------------

# 2. Canonical Record Types and Stable Identifiers

The REP stable identifier system remains authoritative. Atlas adds subtypes without replacing it.

| Record | Prefix | Purpose |
|---|---|---|
| Research package | RP- | Completed research handoff |
| Journal entry | JR- | Chronological scientific record |
| Evidence | EV- | Source, observation, dataset, experiment, artifact, or documented practice |
| Hypothesis | HY- | Testable claim not yet accepted into theory |
| Theory | TH- | Governed explanatory model |
| Experiment | EX- | Planned or completed empirical test |
| Decision framework | DF- | Operational method for making research or design decisions |
| Concept | CN- | Defined term or construct |
| Glossary entry | GL- | Canonical vocabulary definition |

Recommended Atlas concept subtypes:

| Concept subtype | Example ID | Purpose |
|---|---|---|
| Discipline profile | CN-DISC-ARCH-001 | Defines the field, goals, constraints, and methods |
| Domain finding | CN-FIND-ARCH-014 | A supported conclusion within one discipline |
| Candidate principle | HY-PRIN-007 | Proposed cross-domain principle |
| Translation | HY-TRAN-ARCH-UI-003 | Proposed mapping between two domains |
| Boundary condition | CN-BOUND-019 | Condition under which a claim changes or fails |
| Genome node | CN-GENE-011 | Exploratory compositional trait |
| Measurement definition | CN-METRIC-006 | Operational definition of a measurable variable |

The older `OBS-`, `EVD-`, and `LAW-` labels in the Composition Science template should be normalized in
future revisions:

- Observation records should be journal entries or evidence records.
- `EVD-` should become `EV-`.
- A proposed law should begin as `HY-PRIN-` and may become `TH-` only after governance review.

------------------------------------------------------------------------

# 3. Discipline Research Protocol

Every discipline study must answer the same core questions. These questions make comparison possible,
but researchers may add domain-specific questions where necessary.

## 3.1 Discipline Definition

- What does this discipline study?
- What practical or theoretical problems is it trying to solve?
- What counts as success inside the discipline?
- Which schools, subfields, or traditions disagree about its purpose?

## 3.2 Native Constraints

- What physical constraints shape the discipline?
- What biological and perceptual constraints apply?
- What technological constraints apply?
- What social, cultural, economic, legal, or institutional constraints apply?
- Which constraints are permanent, and which are historically contingent?

## 3.3 Native Units and Variables

- What does the discipline measure?
- Which variables are directly measurable?
- Which constructs are inferred?
- Which terms lack stable operational definitions?
- At what spatial, temporal, or organizational scale does it operate?

## 3.4 Foundational Principles

- Which principles are repeatedly treated as fundamental?
- Which are supported by experiments?
- Which emerged from craft tradition or expert practice?
- Which may be stylistic conventions presented as laws?
- Which have known counterexamples?

## 3.5 Mechanisms

- Why is each principle believed to work?
- Is the proposed mechanism perceptual, cognitive, physical, social, cultural, economic, or technical?
- Does the evidence establish causation, correlation, prediction, or only description?
- What alternative explanations remain plausible?

## 3.6 Failure and Boundary Conditions

- Where does the principle fail?
- What populations, cultures, tasks, media, environments, or expertise levels change the result?
- Is failure caused by the principle being wrong, or by applying it outside its native scope?
- Are there nonlinear thresholds, reversals, or tradeoffs?

## 3.7 Historical Lineage

- Where did the idea originate?
- Which later disciplines borrowed it?
- Are multiple sources truly independent, or do they descend from one original claim?
- Has the idea changed meaning during transmission?

## 3.8 Composition Relevance

- What aspects of organization, attention, sequence, relationship, meaning, or action does the field
  illuminate?
- Which Atlas concepts might it support or challenge?
- What is lost when its ideas are translated into visual or interface design?

------------------------------------------------------------------------

# 4. Evidence Evaluation Model

A single star score is too crude for Atlas. Evidence must be evaluated across separate dimensions.

## 4.1 Evidence Dimensions

Each evidence record should include:

| Dimension | Question |
|---|---|
| Source quality | Is the source primary, methodologically credible, and inspectable? |
| Directness | Does it directly test the claim or merely resemble it? |
| Replication | Has the finding been independently reproduced? |
| Independence | Do supporting sources have distinct evidence and intellectual ancestry? |
| Ecological validity | Does the evidence apply to real-world conditions relevant to the claim? |
| Population coverage | Which users, cultures, abilities, and expertise levels were studied? |
| Domain transfer | Is the evidence native to the application domain or translated from elsewhere? |
| Mechanistic support | Is there evidence explaining why the effect occurs? |
| Effect magnitude | Is the effect large enough to matter in practice? |
| Boundary knowledge | Are failure conditions and exceptions understood? |
| Recency and durability | Is the evidence current where recency matters, and stable where it should be? |
| Contradictory evidence | How much credible evidence points in another direction? |

Each dimension should be rated separately as:

- Strong
- Moderate
- Weak
- Unknown
- Not applicable

A final confidence judgment may be assigned, but the dimensional profile must remain visible.

## 4.2 Evidence Type Classification

Evidence records must identify their type:

- Controlled experiment
- Field experiment
- Observational study
- Meta-analysis or systematic review
- Formal model or proof
- Engineering test
- Standards or regulatory evidence
- Historical artifact
- Long-running professional practice
- Expert testimony
- Case study
- Failure report
- Ethnographic observation
- Qualitative interview
- Simulation
- Derived analysis
- Secondary synthesis

Different evidence types answer different questions. Controlled experiments may establish causal
relationships but lack ecological validity. Historical practice may establish durability but not
causation. Expert consensus may identify useful hypotheses but can preserve inherited error.

## 4.3 Independence Test

Before citing cross-disciplinary convergence, researchers must check:

1. Did the disciplines rely on the same original researcher or theory?
2. Did one discipline explicitly borrow the principle from another?
3. Are the sources analyzing the same dataset or examples?
4. Are they using the same broad term for different mechanisms?
5. Are apparent replications actually repeated citations of one finding?
6. Did similar practical constraints independently produce the same solution?

Convergence is strongest when distinct disciplines reach compatible findings through different
methods, datasets, histories, and practical pressures.

------------------------------------------------------------------------

# 5. Universal Principle Lifecycle

No principle begins as a law.

## Stage 0 — Repeated Observation

Similar patterns appear in one or more disciplines.

## Stage 1 — Candidate Concept

The pattern receives a provisional definition. Ambiguous umbrella terms should be split where
possible. For example, “hierarchy” may contain perceptual salience, semantic importance,
organizational rank, and action priority.

## Stage 2 — Cross-Discipline Hypothesis

A testable claim proposes a shared mechanism.

Example:

> HY-PRIN-007: Increasing perceptual differentiation between task-relevant classes reduces visual
> search time until added differentiation begins producing competing salience.

This is more useful than “contrast improves hierarchy” because it identifies variables, outcomes,
and a likely boundary.

## Stage 3 — Translation Testing

The mechanism is examined across multiple domains. Researchers record what remains invariant and
what must change.

## Stage 4 — Boundary Mapping

Known failures, reversals, tradeoffs, user differences, and context dependencies are documented.

## Stage 5 — Predictive Validation

The principle makes predictions not already contained in its source evidence. Those predictions are
tested through experiments, cases, or prospective observation.

## Stage 6 — Theory Candidate

The principle may be proposed for inclusion in the theory registry when it has:

- A stable operational definition
- Multiple credible evidence records
- At least one independent line of confirmation
- Documented counterevidence
- Known boundary conditions
- A plausible mechanism
- At least one successful prediction or falsification attempt
- Clear distinction from neighboring principles

## Stage 7 — Governed Theory Record

Only research governance may promote the principle to `TH-` status. Theory records remain revisable.

------------------------------------------------------------------------

# 6. Translation Framework

Cross-disciplinary translation is the core scientific activity of Atlas, but also its greatest source
of false confidence.

## 6.1 Translation Record

Every translation must document:

- Source discipline and concept
- Target discipline and concept
- Shared abstract structure
- Source mechanism
- Proposed target mechanism
- Variables preserved
- Variables transformed
- Variables lost
- Scale differences
- Temporal differences
- Human task differences
- Evidence supporting the mapping
- Evidence challenging the mapping
- Known limits
- Testable predictions
- Translation confidence

## 6.2 Translation Classes

| Class | Meaning |
|---|---|
| Mechanistic equivalence | The same causal mechanism appears to operate in both domains |
| Structural analogy | Relationships are similar, but mechanisms may differ |
| Functional equivalence | Different structures solve the same human problem |
| Historical transfer | One discipline directly borrowed the concept from another |
| Metaphorical resemblance | The mapping is evocative but not evidentially established |
| Invalid translation | Similar language hides materially different constructs |

Only mechanistic and well-tested functional equivalence should materially strengthen a universal
principle. Structural analogy is valuable for hypothesis generation. Metaphorical resemblance should
never be counted as confirmation.

## 6.3 Example Translation Record

```yaml
identifier: HY-TRAN-ARCH-UI-001
source_concept: architectural circulation
target_concept: interface navigation
translation_class: functional_equivalence
shared_problem: enabling purposeful movement through a structured environment
preserved_variables:
  - destination visibility
  - route choice
  - landmarks
  - transition points
transformed_variables:
  - physical distance becomes interaction cost
  - rooms become information states
lost_variables:
  - bodily locomotion
  - gravity
  - full-scale spatial memory
confidence: medium
status: active hypothesis
```

The translation is promising, but not literal. Navigation interfaces may inherit some wayfinding
mechanisms while differing substantially in embodiment, scale, persistence, and reversibility.

------------------------------------------------------------------------

# 7. Contradiction Resolution Protocol

Contradictions must not be averaged into a vague compromise.

When two credible findings disagree, classify the disagreement.

| Contradiction type | Meaning |
|---|---|
| Population difference | Results vary by age, ability, culture, expertise, or other user factor |
| Task difference | The studies optimize different goals |
| Scale difference | The principle changes across spatial or temporal scales |
| Medium difference | The physical or digital medium changes the mechanism |
| Measurement difference | Different operational definitions produced different results |
| Context difference | Environmental conditions explain the disagreement |
| Tradeoff | Improving one outcome worsens another |
| Threshold effect | The relationship changes after a limit is crossed |
| Historical change | Technology or convention altered the effect |
| Genuine theoretical conflict | Competing explanations cannot both be true as stated |
| Evidence quality conflict | One conclusion rests on weaker methods or unsupported inference |

For every contradiction:

1. Preserve both claims and their evidence IDs.
2. Identify whether the terms and outcome variables are equivalent.
3. Test for hidden boundary conditions.
4. Generate competing hypotheses.
5. Specify evidence that would discriminate between them.
6. Update confidence without deleting the losing claim.
7. Record whether the contradiction narrows, splits, or invalidates a principle.

------------------------------------------------------------------------

# 8. Universal Principle Registry

The registry is the governed index of candidate and accepted principles.

Each entry must include:

```yaml
identifier: HY-PRIN-XXX
title: null
canonical_definition: null
status: proposed | active | contested | theory-candidate | deprecated
mechanism: null
independent_evidence_lines: []
disciplines: []
supporting_evidence: []
challenging_evidence: []
translations: []
boundary_conditions: []
predictions: []
experiments: []
applications: []
confusable_concepts: []
confidence_profile: {}
last_reviewed: YYYY-MM-DD
```

## Initial Candidate Families

These are research territories, not accepted laws:

- Differentiation and contrast
- Grouping and segmentation
- Hierarchy and priority signaling
- Rhythm and recurrence
- Balance and distribution
- Flow, sequence, and path
- Scale and proportion
- Affordance and action possibility
- Feedback and state visibility
- Familiarity and learned convention
- Predictability and expectation
- Coherence and consistency
- Variety and novelty
- Tension and release
- Density and compression
- Redundancy and error tolerance
- Progressive disclosure
- Landmarking and orientation
- Figure-ground organization
- Information scent and anticipatory cues

Researchers should be willing to split, merge, rename, or reject these families.

------------------------------------------------------------------------

# 9. Translation Matrix

The translation matrix is a view generated from translation records, not an independent source of
truth.

| Candidate principle | Architecture | Typography | Film | Music | Human factors | Biology |
|---|---|---|---|---|---|---|
| Rhythm | Repeated bays and spatial intervals | Leading, measure, recurring text structures | Editing cadence and shot duration | Pulse, meter, recurrence | Repeated action sequences | Cycles and oscillations |
| Hierarchy | Spatial prominence and access | Scale, weight, placement | Shot scale, framing, narrative emphasis | Melodic and dynamic prominence | Priority encoding | Salience and signaling |
| Flow | Circulation and transitions | Reading order | Temporal sequencing | Harmonic and rhythmic progression | Task sequence | Movement and information pathways |
| Contrast | Material, light, form | Value, weight, size | Lighting, framing, motion | Dynamics, register, timbre | Alarm differentiation | Signal detection |

Every cell must eventually link to one or more translation IDs. Blank cells are useful: they reveal
missing research or concepts that may not transfer.

------------------------------------------------------------------------

# 10. Composition Genome

The composition genome is an exploratory representation of how principles combine in a work, style,
discipline, or system.

It should not imply that composition traits are biologically inherited, fixed, independent, or
reducible to a single scalar value.

## 10.1 Genome Node Requirements

Each node must specify:

- Operational definition
- Observable indicators
- Measurement method
- Scale and unit
- Context
- Interactions with other nodes
- Evidence basis
- Known confounds
- Reliability
- Validity

## 10.2 Possible Node Categories

- Attention distribution
- Salience concentration
- Repetition interval
- Variation rate
- Spatial density
- Temporal density
- Symmetry
- directional bias
- segmentation strength
- transition abruptness
- hierarchy depth
- information redundancy
- novelty frequency
- predictability
- path constraint
- recovery support

## 10.3 Prohibited Early Uses

Until validated, genome scores should not be used to:

- Rank artistic quality
- Claim universal aesthetic superiority
- Diagnose user experience from appearance alone
- Compare incomparable media without normalization
- Produce false numerical precision
- Replace direct usability or perception testing

The first goal is descriptive and hypothesis-generating. Predictive use must be earned empirically.

------------------------------------------------------------------------

# 11. Scientific Workflow

```text
Select discipline or uncertainty
        ↓
Review existing Atlas records and prior REPs
        ↓
Create discipline profile
        ↓
Collect source evidence and historical lineage
        ↓
Separate observations from interpretations
        ↓
Extract domain-native findings
        ↓
Identify mechanisms and boundary conditions
        ↓
Create or update translation records
        ↓
Test evidence independence
        ↓
Map support and contradictions to candidate principles
        ↓
Generate falsifiable predictions and experiments
        ↓
Update registries, website views, and research backlog
        ↓
Produce REP and handoff instructions
```

## 11.1 Intake Rule

No new report is considered incorporated merely because it exists in the repository. Incorporation
requires:

- Valid metadata
- Stable identifiers
- Evidence records
- Explicit confidence
- Mappings to existing concepts or proposed new concepts
- Open questions
- Recommended registry changes
- A completed REP or documented reason why research remains active

## 11.2 Synthesis Rule

Research agents may propose but may not silently alter canonical theory. They must state:

- What should change
- Why
- Which evidence supports the change
- What existing records are affected
- What uncertainty remains

## 11.3 Revision Rule

All changes must preserve:

- Prior identifiers
- Contradictory evidence
- Deprecated interpretations
- Revision history
- Supersession links

------------------------------------------------------------------------

# 12. Prioritizing New Disciplines

Disciplines should not be selected only because they are interesting. Use a portfolio strategy.

## 12.1 Priority Dimensions

- Foundational relevance to perception, cognition, action, or organization
- Methodological rigor
- Independence from disciplines already studied
- Ability to challenge current assumptions
- Availability of primary evidence
- Potential for measurable variables
- Applicability across media
- Neglected populations or contexts
- Value to current engineering or design decisions

## 12.2 Recommended Research Waves

### Wave 1 — Human constraints and causal foundations

- Vision science
- Auditory perception
- Cognitive psychology
- Attention research
- Memory and learning
- Motor control
- Human factors and ergonomics
- Psychophysics

### Wave 2 — Disciplines with mature composition practice

- Architecture
- Typography
- Cartography
- Information visualization
- Industrial design
- Film editing and cinematography
- Music theory and perception
- Painting and graphic composition

### Wave 3 — Meaning, culture, and coordination

- Linguistics and pragmatics
- Semiotics
- Anthropology
- Sociology
- Behavioral economics
- Rhetoric
- Narrative theory
- Organizational design

### Wave 4 — Complex adaptive and engineered systems

- Systems engineering
- Control theory
- Information theory
- Network science
- Ecology
- Evolutionary biology
- Safety engineering
- Resilience engineering

The waves may run in parallel. Their purpose is to maintain balance between biological constraints,
craft knowledge, cultural meaning, and formal systems.

------------------------------------------------------------------------

# 13. Repository and Website Structure

A file hierarchy remains useful for stewardship, while the website should expose graph relationships.

```text
/composition-science
  /governance
  /disciplines
  /evidence
  /hypotheses
  /theory
  /translations
  /boundaries
  /experiments
  /genome
  /registries
  /research-journal
  /research-packages
  /generated
```

Recommended generated website views:

- Discipline explorer
- Principle registry
- Evidence graph
- Translation matrix
- Contradiction map
- Boundary-condition explorer
- Research confidence dashboard
- Open-question queue
- Genome explorer
- Theory change history

Markdown files remain canonical. Website pages should be generated from them and must not become an
independent editable knowledge source.

------------------------------------------------------------------------

# 14. Quality Gates

A discipline study is not complete until it passes these gates.

## Evidence Gate

- Primary sources were sought.
- Important claims link to evidence IDs.
- Counterexamples and competing viewpoints were reviewed.
- Source lineage and independence were examined.

## Concept Gate

- Native terminology is defined.
- Broad concepts are operationalized or marked ambiguous.
- Observation, interpretation, hypothesis, and theory remain distinct.

## Translation Gate

- Mappings identify what is preserved, transformed, and lost.
- Metaphors are labeled as metaphors.
- Domain transfer confidence is explicit.

## Falsification Gate

- The strongest conclusion has at least one stated failure condition.
- Evidence that would disprove or narrow the claim is specified.
- Negative findings are retained.

## Handoff Gate

- A new agent can reconstruct the research.
- Registry updates are explicit.
- Open questions and next actions are prioritized.
- The REP completion checklist is satisfied.

------------------------------------------------------------------------

# 15. Initial Hypotheses Created by This Framework

## HY-PRIN-001 — Cross-Domain Constraint Convergence

### Hypothesis

When independent disciplines face the same underlying human perceptual or cognitive constraint, they
will tend to evolve structurally similar solutions even without direct intellectual transfer.

### Predictions

- Similar solutions will appear in historically disconnected traditions.
- The strongest commonalities will correspond to stable human constraints.
- Differences will correlate with medium, task, culture, technology, or scale.

### Supporting Evidence

Not yet registered.

### Counter Evidence

Possible widespread convergence caused by shared cultural transmission rather than common constraint.

### Confidence

Low. High-value research hypothesis.

## HY-PRIN-002 — Translation Loss

### Hypothesis

Every cross-disciplinary translation loses or transforms variables, and unrecorded translation loss
is a major source of false universal principles.

### Prediction

Translations that explicitly document lost variables will make more accurate domain predictions than
translations based only on shared vocabulary.

### Confidence

Medium.

## HY-PRIN-003 — Boundary-First Generalization

### Hypothesis

A principle becomes more transferable when its boundary conditions are known, even if documenting
those limits lowers its apparent universality.

### Prediction

Boundary-rich principles will outperform broad heuristics in prospective design decisions.

### Confidence

Medium.

## HY-PRIN-004 — Principle Interaction Dominance

### Hypothesis

Composition outcomes are often governed more by interactions among principles than by the isolated
strength of any one principle.

### Prediction

Genome models containing interaction terms will predict perception and task outcomes better than
independent trait scores.

### Confidence

Low-Medium.

------------------------------------------------------------------------

# 16. Observations

## JR-OBS-001

### Observation

Many disciplines use recurring terms such as hierarchy, rhythm, balance, contrast, and flow.

### Interpretation

These terms may indicate shared compositional structures, but their breadth creates a high risk of
false equivalence.

### Confidence

High for the observation; Medium for the interpretation.

## JR-OBS-002

### Observation

The current Composition Science template and REP specification use partially different identifier
systems.

### Interpretation

Identifier divergence will create duplicate records and weaken traceability unless normalized.

### Confidence

High.

## JR-OBS-003

### Observation

A simple evidence-level score combines source quality, replication, transferability, and mechanism
into one number.

### Interpretation

A single score hides important weaknesses and can produce unjustified confidence.

### Confidence

High.

------------------------------------------------------------------------

# 17. Evidence

## EV-CS-001

### Citation

Composition Science Markdown Template v1.

### Summary

Defines standard Composition Science metadata, observations, evidence, candidate laws, open questions,
next actions, revision history, and agent instructions.

### Supports

- DF-CS-ATLAS-001
- HY-PRIN-002

### Challenges

- The template's `EVD-` and `LAW-` labels conflict with the REP canonical identifier model.

## EV-CS-002

### Citation

Research Execution Package Specification v2.

### Summary

Defines the REP as the canonical research handoff and establishes identifiers, metadata, mandatory
sections, theory impact, evidence traceability, quality metrics, research debt, and completion criteria.

### Supports

- DF-CS-ATLAS-001
- The requirement for stable, traceable, executable research artifacts

### Challenges

- The REP does not yet define detailed cross-disciplinary translation or evidence-independence rules.

------------------------------------------------------------------------

# 18. Open Questions

1. What operational definition should distinguish a principle, mechanism, pattern, heuristic, and law?
2. How should evidence confidence be aggregated without producing false precision?
3. What graph schema best represents evidence lineage, translation, contradiction, and supersession?
4. Which initial principle family should be used to test the complete workflow?
5. How can cultural variation be incorporated without treating culture as noise?
6. What methods can measure composition traits consistently across static, interactive, spatial, and
   temporal media?
7. Which existing research streams have already generated findings ready for registry extraction?
8. Should the Composition Science base template be revised to adopt REP identifiers directly?
9. What governance process promotes `HY-PRIN-` records into `TH-` records?
10. Which confidence dimensions should be required versus optional for different evidence types?

------------------------------------------------------------------------

# 19. Recommended Next Research

## Highest-Value Next Step

Run a pilot synthesis on one candidate principle across three methodologically distinct disciplines.

Recommended pilot:

**Differentiation for perceptual search and priority signaling** across:

1. Vision science and psychophysics
2. Typography or information visualization
3. Aviation or medical human factors

This candidate is preferable to a broad concept such as “balance” because it can be operationalized
using measurable variables such as target-distractor similarity, search time, error rate, salience,
and signal detectability.

The pilot should produce:

- One discipline profile per field
- A minimum of ten strong evidence records
- A source-lineage map
- At least three domain findings
- Two or more translation records
- One candidate principle record
- Documented contradictions and boundaries
- At least one falsifiable experiment proposal
- A completed REP

------------------------------------------------------------------------

# 20. Research Backlog

## Critical

- Normalize identifiers between the Composition Science template and REP specification.
- Define machine-readable schemas for evidence, translation, principle, and boundary records.
- Select and execute the first cross-disciplinary pilot.
- Establish theory promotion governance.

## High

- Inventory existing project files and extract candidate principles and evidence.
- Build the discipline registry.
- Build the source-lineage model.
- Define confidence profiles by evidence type.
- Define contradiction and boundary-condition records.

## Medium

- Prototype generated website views.
- Explore graph storage options while retaining Markdown as canonical.
- Develop genome node measurement standards.
- Create linting and validation rules for metadata and IDs.

## Deferred

- Automated principle scoring
- Automated aesthetic quality prediction
- Full genome visualization
- Prescriptive design generation from principle records

------------------------------------------------------------------------

# 21. Suggested Specialized Research Agents

- Evidence Lineage Agent: traces intellectual ancestry and duplicated citations.
- Discipline Research Agent: conducts deep native-domain research.
- Translation Agent: proposes and challenges cross-domain mappings.
- Falsification Agent: searches for counterexamples and alternative explanations.
- Registry Curator: normalizes terminology, IDs, and relationships.
- Experimental Design Agent: converts candidate principles into measurable tests.
- Accessibility and Population Agent: identifies excluded users and population boundaries.
- Historical Methods Agent: distinguishes durable practice from inherited convention.

No agent should both propose and approve a theory change without independent review.

------------------------------------------------------------------------

# 22. Parallel Research Opportunities

The following can proceed independently:

- Discipline registry design
- Evidence schema design
- Translation schema design
- Pilot source collection
- Repository inventory
- Website information architecture
- Confidence-model research
- Governance model research

Their outputs should converge through a shared REP and stable identifier model.

------------------------------------------------------------------------

# 23. Risks

## False Universality

Broad terms may conceal different mechanisms.

## Citation Echo

Many apparent confirmations may trace back to one source.

## Prestige Bias

A respected discipline or expert tradition may be treated as stronger evidence than its methods
justify.

## Measurement Reductionism

Measurable variables may crowd out meaningful but difficult-to-measure phenomena.

## Cultural Flattening

Claims derived from narrow populations may be mislabeled as universal.

## Repository Entropy

Uncontrolled terminology and duplicate identifiers may make the knowledge base untrustworthy.

## Premature Automation

Automated scoring or synthesis may amplify flaws before schemas and governance mature.

## Genome Reification

Exploratory traits may be mistaken for objective natural categories.

------------------------------------------------------------------------

# 24. Cross-Discipline Opportunities

- Use psychophysics to operationalize concepts inherited from visual arts.
- Use human factors failure research to challenge aesthetic heuristics.
- Use architecture and cartography to enrich digital wayfinding models.
- Use music and film to study composition over time rather than only in static layouts.
- Use linguistics and semiotics to distinguish perception from meaning.
- Use information theory cautiously to model density, redundancy, and signal differentiation.
- Use ecology and systems engineering to study resilience, interaction effects, and adaptation.
- Use anthropology to test whether proposed universals are culturally situated conventions.

------------------------------------------------------------------------

# 25. Knowledge Relationships

```text
EV-CS-001 ─supports─> DF-CS-ATLAS-001
EV-CS-002 ─supports─> DF-CS-ATLAS-001
DF-CS-ATLAS-001 ─creates─> HY-PRIN-001
DF-CS-ATLAS-001 ─creates─> HY-PRIN-002
DF-CS-ATLAS-001 ─creates─> HY-PRIN-003
DF-CS-ATLAS-001 ─creates─> HY-PRIN-004
HY-TRAN-* ─supports/challenges─> HY-PRIN-*
CN-BOUND-* ─constrains─> HY-PRIN-* or TH-*
EX-* ─tests─> HY-* or TH-*
RP-* ─proposes updates to─> registries
```

------------------------------------------------------------------------

# 26. Repository Updates

Recommended additions:

- Add this document to `/governance` or `/frameworks`.
- Create empty canonical registries for disciplines, principles, evidence, translations, boundaries,
  and experiments.
- Add schema examples and validation rules.
- Revise the Composition Science Markdown Template to use REP-compatible identifiers.
- Add a project index linking current research streams to the new record types.

------------------------------------------------------------------------

# 27. Website Updates

Generate an Atlas landing page that answers:

- What is Composition Science?
- Which disciplines are represented?
- Which principles are currently proposed?
- What evidence supports each principle?
- Where do disciplines agree or disagree?
- What remains uncertain?
- What research should happen next?

The site should visibly distinguish:

- Observation
- Evidence
- Hypothesis
- Theory
- Translation
- Application

------------------------------------------------------------------------

# 28. AI Consumption Notes

Agents consuming this framework must:

1. Treat all initial principle families as hypotheses.
2. Inspect source lineage before claiming independent convergence.
3. Preserve native disciplinary meaning before translating terms.
4. State what is lost or transformed in every translation.
5. Keep confidence multidimensional.
6. Never infer universality from frequency of citation alone.
7. Prefer causal and predictive claims over purely metaphorical resemblance.
8. Record counterevidence and boundary conditions in the same artifact as supporting evidence.
9. Propose registry changes explicitly rather than modifying theory silently.
10. Produce a REP when a research cycle reaches a meaningful stopping point.

------------------------------------------------------------------------

# 29. Handoff Instructions

The next agent should:

1. Read this framework, the Composition Science template, and REP v2.
2. Create initial registry files using the schemas defined here.
3. Select the differentiation/search pilot.
4. Conduct research in vision science, information visualization or typography, and high-stakes human
   factors.
5. Trace the lineage of overlapping principles.
6. Create evidence, finding, translation, boundary, and hypothesis records.
7. Attempt to falsify the shared principle.
8. Produce the first pilot REP.
9. Recommend changes to this framework based on actual execution friction.

------------------------------------------------------------------------

# 30. Research Journal

## JR-2026-07-21-001

### Objective

Convert the proposed Atlas model into an executable cross-disciplinary research framework.

### Work Completed

- Reviewed the Composition Science Markdown Template v1.
- Reviewed the Research Execution Package Specification v2.
- Reconciled the two artifact models.
- Defined discipline intake, evidence evaluation, translation, contradiction, principle lifecycle,
  genome safeguards, workflow, quality gates, and research priorities.

### Major Decision

Cross-disciplinary convergence will not count as independent evidence until source lineage and shared
ancestry have been examined.

### Remaining Uncertainty

The framework has not yet been tested against a complete research pilot.

### Next Decision Point

After the first pilot REP, revise the framework based on observed failures, unnecessary complexity,
and missing record types.

------------------------------------------------------------------------

# 31. Appendix A — Minimum Discipline Report Skeleton

```markdown
---
identifier: RP-[AREA]-[NUMBER]
title: [Discipline] Composition Research Package
research_area: Composition Science
discipline: [Discipline]
author_agent: [Agent]
version: 1.0
confidence: [Rating]
completion: [Percent]
priority: [Priority]
status: draft
---

# Executive Summary
# Original Objective
# Scope
# Discipline Definition
# Native Constraints
# Native Variables and Measures
# Foundational Principles
# Mechanisms
# Evidence Registry
# Domain Findings
# Historical Lineage
# Counterevidence and Failures
# Boundary Conditions
# Cross-Discipline Translations
# Candidate Principle Impacts
# Hypothesis Registry
# Failed Assumptions
# Open Questions
# Recommended Next Research
# Repository Updates
# AI Consumption Notes
# Handoff Instructions
# Research Journal
# Completion Checklist
```

------------------------------------------------------------------------

# 32. Completion Checklist

- [x] Purpose and scope defined
- [x] REP metadata included
- [x] Research state snapshot included
- [x] Canonical record types defined
- [x] Discipline protocol defined
- [x] Evidence evaluation defined
- [x] Evidence independence addressed
- [x] Translation protocol defined
- [x] Contradiction protocol defined
- [x] Principle lifecycle defined
- [x] Genome safeguards defined
- [x] Workflow defined
- [x] Quality gates defined
- [x] Initial hypotheses recorded
- [x] Open questions recorded
- [x] Research backlog prioritized
- [x] Risks documented
- [x] Repository and website impacts documented
- [x] Handoff instructions included
- [x] Revision history included

------------------------------------------------------------------------

# Revision History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0 | 2026-07-21 | OpenAI Research Agent | Initial canonical-candidate framework |

------------------------------------------------------------------------

# Agent Instructions

When creating or modifying this document:

1. Separate observation from interpretation.
2. Never strengthen a conclusion beyond the available evidence.
3. Preserve contradictory findings.
4. Prefer measurable variables over subjective descriptions.
5. Reference hypotheses, evidence, theory records, translations, and genome nodes whenever possible.
6. Use REP-compatible stable IDs.
7. Record assumptions and confidence explicitly.
8. Inspect evidence ancestry before claiming independent support.
9. Keep the YAML header valid.
10. Do not delete revision history; append to it.
11. Treat metaphors as hypothesis generators, not validation.
12. Revise this framework after real research pilots expose weaknesses.
