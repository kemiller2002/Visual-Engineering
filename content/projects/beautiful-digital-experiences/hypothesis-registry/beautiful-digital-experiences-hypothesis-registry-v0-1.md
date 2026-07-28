---
id: HYREG-BDE-001
title: Beautiful Digital Experiences Hypothesis Registry
abstract: Initial registry for the 15 required beauty hypotheses, with mechanisms, predictions, evidence, alternatives, boundaries, and falsification status.
authors:
  - Kevin Miller
  - OpenAI Codex
created: 2026-07-26
updated: 2026-07-26
project: beautiful-digital-experiences
document_type: hypothesis-registry
status: active
evidence_level: C
confidence: low
canonical: false
concepts:
  - product-design
  - perception
  - cognition
  - composition
  - research-methodology
related_documents:
  - ../evidence-registry/beautiful-digital-experiences-evidence-registry-v0-1.md
  - ../research-execution-package/rep-bde-0001-territory-and-evidence-foundation.md
tags:
  - hypotheses
  - aesthetics
  - falsification
machine_readable: true
llm_ingest: true
purposes:
  - verify
  - reference
audiences:
  - researcher
---

# Beautiful Digital Experiences Hypothesis Registry v0.1

## Status vocabulary

- **Initialized:** claim is specified but not adequately tested.
- **Provisional support:** evidence bears on the predicted mechanism, with important
  transfer limits.
- **Mixed:** supporting and contradicting evidence or boundary reversals are known.
- **Narrowed:** the original form was too broad and a scoped revision is active.
- **Rejected:** current claim form is contradicted; history is preserved.

## Required hypotheses

### HY-BEAUTY-001

- **Claim:** Aesthetic quality improves perceived usability more reliably than measured
  task performance.
- **Mechanism:** halo/affect-as-information changes expectations and post-use appraisal;
  it does not necessarily change interaction structure.
- **Prediction:** appearance manipulation produces a larger and more consistent effect
  on perceived-usability measures than on completion, error, or time.
- **Support:** EV-BDE-001, EV-BDE-002, EV-BDE-003.
- **Contradiction:** some task and goal conditions show performance effects, including
  slower completion, so “no performance effect” is not the claim.
- **Boundary conditions:** task stakes, goal orientation, exposure, age, domain,
  usability severity, and brand/content cues.
- **Alternatives:** experiment-demand effects; perceived craftsmanship signals actual
  engineering quality; positive emotion changes persistence.
- **Test status:** provisional support; **confidence: medium**.
- **Falsifier:** robust, larger objective-performance effects across preregistered,
  repeated, multi-domain studies.

### HY-BEAUTY-002

- **Claim:** People prefer category-recognizable designs containing limited controlled
  novelty.
- **Mechanism:** prototypicality supports prediction and fluency; novelty supports
  interest, identity, and informational reward.
- **Prediction:** category-fit and beauty form a conditional inverted-U across novelty,
  with the optimum varying by audience and task.
- **Support:** EV-BDE-005, EV-BDE-006, EV-BDE-007, EV-BDE-008, EV-BDE-009.
- **Contradiction:** EV-BDE-008 favored high prototypicality and low complexity in rapid
  screenshots; it did not demonstrate a novelty optimum.
- **Boundary conditions:** expertise, epistemic motivation, repeated use, product risk,
  category maturity, and cultural model.
- **Alternatives:** novelty is merely production-value or prestige signaling.
- **Test status:** initialized; **confidence: low**.
- **Falsifier:** monotonic preference for prototypicality or novelty after controlling
  execution quality and familiarity.

### HY-BEAUTY-003

- **Claim:** Beautiful interfaces use consistency of relationships rather than identical
  repetition.
- **Mechanism:** invariant spatial, typographic, and semantic relations support
  prediction while controlled surface variation preserves information and rhythm.
- **Prediction:** relationally consistent variants outperform identical repetition on
  coherence and interest without harming task performance.
- **Support:** indirect only: EV-BDE-009, EV-BDE-010 and existing Composition Science
  relational-legibility work.
- **Contradiction:** none directly tested; component sameness may improve learning in
  dense applications.
- **Boundary conditions:** frequency of use, system scale, safety, localization.
- **Alternatives:** quality comes from simple component consistency, not relations.
- **Test status:** initialized; **confidence: low**.

### HY-BEAUTY-004

- **Claim:** Art direction contributes more to perceived website quality than decorative
  interface styling.
- **Mechanism:** imagery supplies high-area, semantically rich signals of specificity,
  material quality, atmosphere, and budget.
- **Prediction:** changing imagery quality and coherence while holding layout constant
  produces larger effects than changing ornamental UI styling while imagery is fixed.
- **Support:** no direct causal evidence registered.
- **Contradiction:** application-like products with little imagery can be highly admired.
- **Boundary conditions:** image-led versus task-led category, viewport, content volume.
- **Alternatives:** imagery operates as brand or production-budget signal.
- **Test status:** initialized; **confidence: very low**.

### HY-BEAUTY-005

- **Claim:** Perceived polish is cumulatively produced by many resolved details.
- **Mechanism:** each mismatch is weak evidence of incomplete control; repeated matches
  increase inferred craftsmanship and reduce prediction errors.
- **Prediction:** incremental detail repair yields monotonic or thresholded gains in
  craftsmanship ratings with macro-composition held constant.
- **Support:** EV-BDE-010 identifies craftsmanship as a separable perceived facet.
- **Contradiction:** a dominant art-directed feature may overwhelm small defects at first
  exposure.
- **Boundary conditions:** exposure duration, defect salience, expertise, task pressure.
- **Alternatives:** one global latent impression causes detail ratings.
- **Test status:** initialized; **confidence: low**.

### HY-BEAUTY-006

- **Claim:** A design can violate surface conventions and remain usable when deeper
  perceptual and semantic structure is preserved.
- **Mechanism:** grouping, hierarchy, labels, mappings, feedback, and state continuity
  carry action meaning below conventional styling.
- **Prediction:** convention-breaking variants with preserved deep structure retain
  comprehension and recovery while increasing expressive-aesthetic ratings.
- **Support:** EV-BDE-009 distinguishes expressive aesthetics; EV-BDE-007 makes fluency
  expectation-dependent.
- **Contradiction:** unfamiliar controls can impose learning and accessibility costs.
- **Boundary conditions:** novice/expert status, risk, frequency, assistive technology.
- **Alternatives:** users transfer conventions that experimenters failed to identify.
- **Test status:** initialized; **confidence: low**.

### HY-BEAUTY-007

- **Claim:** Beauty judgments stabilize differently when based on complete experiences
  rather than static screenshots.
- **Mechanism:** interaction reveals temporal coherence, content resilience, friction,
  state completeness, and performance.
- **Prediction:** screenshot–experience agreement falls as task/state diversity grows;
  repeated-session ratings show lower halo and greater sensitivity to craft and friction.
- **Support:** EV-BDE-004 and the scope boundary in EV-BDE-008.
- **Contradiction:** rapid appeal ratings can be internally stable across short exposure
  durations.
- **Boundary conditions:** site type, interaction depth, media weight, exposure interval.
- **Alternatives:** rating change is mere exposure rather than better evidence.
- **Test status:** provisional support; **confidence: low-to-medium**.

### HY-BEAUTY-008

- **Claim:** Designers and general users differ in admired features but overlap on
  coherence, intentionality, legibility, and execution quality.
- **Mechanism:** expertise changes learned categories, attention, and novelty reward;
  common perceptual constraints preserve partial agreement.
- **Prediction:** experts weight originality and detail more; both groups penalize severe
  incoherence and illegibility.
- **Support:** EV-BDE-009 and EV-BDE-010 provide candidate shared dimensions but do not
  test audience groups.
- **Contradiction:** no direct registered evidence.
- **Boundary conditions:** design education, domain expertise, culture, status signaling.
- **Alternatives:** apparent expertise effects are vocabulary or response-style effects.
- **Test status:** initialized; **confidence: very low**.

### HY-BEAUTY-009

- **Claim:** Visual trends succeed partly because they satisfy recurring psychological
  or cultural needs, not only imitation.
- **Mechanism:** trends package needs for novelty, nostalgia, status, tactility, clarity,
  optimism, or technical demonstration into recognizable forms.
- **Prediction:** adoption explanations and preference effects cluster by need, and useful
  mechanisms survive after surface motifs decline.
- **Support:** EV-BDE-005, EV-BDE-006, EV-BDE-007 provide possible psychological routes.
- **Contradiction:** diffusion can occur through platform defaults and mimetic pressure
  without preference.
- **Boundary conditions:** professional networks, tooling, economic cycle, medium.
- **Alternatives:** availability, vendor promotion, and portfolio incentives.
- **Test status:** initialized; **confidence: very low**.

### HY-BEAUTY-010

- **Claim:** Durable digital designs combine stable compositional principles with
  replaceable stylistic layers.
- **Mechanism:** perceptual and semantic relationships age more slowly than culturally
  coded surface motifs.
- **Prediction:** blinded historical evaluations retain coherence/craft ratings better
  than trend-forwardness ratings; surface restyling can preserve task structure.
- **Support:** indirect Composition Science evidence only.
- **Contradiction:** interaction conventions and compositional norms also age.
- **Boundary conditions:** platform change, content category, brand heritage.
- **Alternatives:** durability is mainly repeated exposure or prestige.
- **Test status:** initialized; **confidence: low**.

### HY-BEAUTY-011

- **Claim:** Minimalism succeeds aesthetically only when reduction increases emphasis,
  coherence, or perceived material quality.
- **Mechanism:** removal decreases competition and increases signal contrast, but beyond
  a point it removes identity, cues, and informational reward.
- **Prediction:** reduced variants improve ratings only while hierarchy and specificity
  remain; sterile and ambiguous variants lose warmth, interest, or usability.
- **Support:** EV-BDE-006, EV-BDE-008, EV-BDE-010.
- **Contradiction:** low-complexity screenshots were preferred in EV-BDE-008, but
  minimalism was not independently manipulated.
- **Boundary conditions:** information density, art direction, brand familiarity, task.
- **Alternatives:** “minimal” ratings proxy fashion or luxury.
- **Test status:** initialized; **confidence: low**.

### HY-BEAUTY-012

- **Claim:** Accessibility constraints can increase beauty when they improve hierarchy,
  clarity, contrast, and feedback.
- **Mechanism:** perceptual robustness and explicit state communication can also create
  coherence and craft; constraint can focus expression.
- **Prediction:** well-art-directed accessible revisions improve inclusive performance
  without reducing, and sometimes increasing, aesthetic profiles.
- **Support:** EV-BDE-012 defines relevant constraints; no causal beauty evidence.
- **Contradiction:** some remediations may reduce a specific mood or brand expression.
- **Boundary conditions:** remediation quality, disability, display, context, original
  design.
- **Alternatives:** gains come from general redesign effort, not accessibility.
- **Test status:** initialized; **confidence: very low**.

### HY-BEAUTY-013

- **Claim:** Beauty depends partly on fulfillment or skillful revision of category
  expectations.
- **Mechanism:** internal category models establish priors for form, trust, information
  density, and interaction.
- **Prediction:** identical visual languages receive different beauty, trust, and
  appropriateness ratings when transferred across categories.
- **Support:** EV-BDE-005, EV-BDE-007, EV-BDE-008; EV-BDE-011 shows visual cues enter
  credibility judgments.
- **Contradiction:** strong brand or expressive authorship may establish a new category
  model.
- **Boundary conditions:** category knowledge, risk, culture, brand, novelty tolerance.
- **Alternatives:** ratings follow familiarity alone or inferred production budget.
- **Test status:** provisional mechanism support; **confidence: low**.

### HY-BEAUTY-014

- **Claim:** Repeated exposure can raise liking through familiarity but also reveal
  superficial novelty and unresolved details.
- **Mechanism:** fluency increases with exposure while task evidence updates the initial
  halo.
- **Prediction:** simple unfamiliar variants may rise, novelty-led variants may fall, and
  well-resolved variants remain stable; changes correlate differently with task evidence.
- **Support:** EV-BDE-004, EV-BDE-005, EV-BDE-006.
- **Contradiction:** registered longitudinal evidence mainly shows halo attenuation, not
  all proposed trajectories.
- **Boundary conditions:** exposure spacing, task variation, initial usability, mastery.
- **Alternatives:** regression to the mean and memory effects.
- **Test status:** mixed/initialized; **confidence: low**.

### HY-BEAUTY-015

- **Claim:** Visual quality cannot be evaluated accurately without realistic content,
  responsive and interaction states, and repeated-use scenarios.
- **Mechanism:** ideal screenshots omit stressors that reveal compositional resilience,
  state completeness, accessibility, and temporal craft.
- **Prediction:** rankings based on ideal heroes diverge from rankings after long content,
  errors, localization, mobile reflow, keyboard use, and repeated tasks.
- **Support:** EV-BDE-004, EV-BDE-008 boundary, EV-BDE-012.
- **Contradiction:** first-impression appeal is itself a valid, stable outcome for some
  contexts.
- **Boundary conditions:** claim type; static campaign pages may need less interaction
  evidence than tools.
- **Alternatives:** divergence reflects content quality rather than visual-system
  resilience.
- **Test status:** narrowed: accurate **complete-experience** quality requires these
  states; first-impression beauty does not. **Confidence: medium on construct logic,
  low empirically**.

## Additional hypotheses exposed by Cycle 1

### HY-BEAUTY-016

- **Claim:** Appropriateness moderates the conversion of coherence and expression into
  trust and desire.
- **Mechanism:** the same aesthetic cue can signal competence in one genre and
  irresponsibility in another.
- **Prediction:** category-transfer manipulations create beauty–trust dissociations.
- **Status:** initialized; **confidence: very low**.

### HY-BEAUTY-017

- **Claim:** First-impression beauty and durable beauty are related but distinct
  constructs.
- **Mechanism:** first impressions weight global visual statistics and priors; durable
  judgments incorporate temporal coherence, friction, content, and state completion.
- **Prediction:** they load on correlated but separable factors across repeated sessions.
- **Status:** initialized; **confidence: low**.

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-07-26 | Initialized required hypotheses 001–015 and added 016–017 from Cycle 1 uncertainty. |
