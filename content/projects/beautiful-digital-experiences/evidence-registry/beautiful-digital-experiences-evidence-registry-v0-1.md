---
id: EVREG-BDE-001
title: Beautiful Digital Experiences Evidence Registry
abstract: Initial evidence registry for aesthetic quality, perceived usability, processing fluency, prototypicality, repeated use, credibility, and accessibility.
authors:
  - Kevin Miller
  - OpenAI Codex
created: 2026-07-26
updated: 2026-07-26
project: beautiful-digital-experiences
document_type: evidence-registry
status: active
evidence_level: C
confidence: low
canonical: false
concepts:
  - perception
  - cognition
  - product-design
  - research-methodology
related_documents:
  - ../research-execution-package/rep-bde-0001-territory-and-evidence-foundation.md
  - ../hypothesis-registry/beautiful-digital-experiences-hypothesis-registry-v0-1.md
tags:
  - evidence
  - aesthetics
  - usability
machine_readable: true
llm_ingest: true
purposes:
  - verify
  - reference
audiences:
  - researcher
---

# Beautiful Digital Experiences Evidence Registry v0.1

## Registry rules

- A record describes what a source can support, not everything it mentions.
- Observation and interpretation remain separate.
- `support` means relevant evidence, not proof of the whole hypothesis.
- Population, stimulus, task, duration, and measurement boundaries travel with a claim.
- Current evidence strength is a claim-relative appraisal, not a journal ranking.

## Evidence records

### EV-BDE-001 — Apparent usability versus inherent usability

- **Source:** Kurosu, M., & Kashimura, K. (1995). *Apparent usability vs.
  inherent usability*. CHI '95 Conference Companion.
  <https://doi.org/10.1145/223355.223680>
- **Type:** short conference experiment.
- **Direct observation:** apparent-usability ratings for ATM layouts were more strongly
  related to aesthetic aspects than to the study's inherent-usability measure.
- **Interpretation permitted:** visual appearance can bias or inform perceived-usability
  judgments before actual use.
- **Not permitted:** aesthetic quality improves objective task performance.
- **Boundaries:** short paper, ATM-layout stimuli, historical interface context.
- **Related hypotheses:** HY-BEAUTY-001, HY-BEAUTY-013.
- **Confidence:** low-to-medium.

### EV-BDE-002 — What is beautiful is usable

- **Source:** Tractinsky, N., Katz, A. S., & Ikar, D. (2000). *What is
  beautiful is usable*. Interacting with Computers, 13(2), 127–145.
  <https://doi.org/10.1016/S0953-5438(00)00031-X>
- **Type:** controlled experiment using an ATM surrogate.
- **Direct observation:** perceived aesthetics and perceived usability were strongly
  related before and after use; aesthetics influenced post-use perceptions.
- **Interpretation permitted:** aesthetic impressions persist into post-use subjective
  evaluation and can contribute to a usability halo.
- **Not permitted:** perceived beauty and actual usability are interchangeable.
- **Boundaries:** single task family and interface genre.
- **Related hypotheses:** HY-BEAUTY-001, HY-BEAUTY-014.
- **Confidence:** medium.

### EV-BDE-003 — Design aesthetics in usability testing

- **Source:** Sonderegger, A., & Sauer, J. (2010). *The influence of design
  aesthetics in usability testing: Effects on user performance and perceived
  usability*. Applied Ergonomics, 41(3), 403–410.
  <https://doi.org/10.1016/j.apergo.2009.09.002>
- **Type:** controlled experiment; 60 adolescents; functionally identical phone
  simulations with appealing versus unappealing appearance.
- **Direct observation:** appealing appearance increased perceived usability despite no
  difference in objective usability quality.
- **Interpretation permitted:** visual appeal more reliably shifts subjective usability
  than functional quality in this experiment.
- **Not permitted:** universal population or product transfer.
- **Related hypotheses:** HY-BEAUTY-001, HY-BEAUTY-008.
- **Confidence:** medium within scope.

### EV-BDE-004 — Aesthetics and usability over time

- **Source:** Sonderegger, A., Zbinden, G., Uebelbacher, A., & Sauer, J. (2012).
  *The influence of product aesthetics and usability over the course of time: a
  longitudinal field experiment*. Ergonomics, 55(7), 713–730.
  <https://doi.org/10.1080/00140139.2012.672658>
- **Type:** two-week mixed-design field experiment; 60 mobile-phone users.
- **Direct observation:** the positive effect of appeal on perceived usability waned
  with exposure.
- **Interpretation permitted:** first-impression halo is not necessarily durable.
- **Not permitted:** all aesthetic appreciation declines with familiarity.
- **Related hypotheses:** HY-BEAUTY-007, HY-BEAUTY-014, HY-BEAUTY-015.
- **Confidence:** low-to-medium pending full-text extraction.

### EV-BDE-005 — Processing fluency theory

- **Source:** Reber, R., Schwarz, N., & Winkielman, P. (2004). *Processing
  fluency and aesthetic pleasure: Is beauty in the perceiver's processing
  experience?* Personality and Social Psychology Review, 8(4), 364–382.
  <https://doi.org/10.1207/S15327957PSPR0804_3>
- **Type:** theoretical review.
- **Direct observation:** the review integrates effects of contrast, repetition,
  symmetry, and prototypicality through processing fluency.
- **Interpretation permitted:** felt processing ease is a plausible contributor to
  aesthetic pleasure.
- **Not permitted:** fluency completely defines beauty or predicts contextual fit.
- **Related hypotheses:** HY-BEAUTY-002, HY-BEAUTY-009, HY-BEAUTY-013,
  HY-BEAUTY-014.
- **Confidence:** medium as a mechanism family; low as a complete theory.

### EV-BDE-006 — Pleasure–Interest model

- **Source:** Graf, L. K., & Landwehr, J. R. (2015). *A dual-process
  perspective on fluency-based aesthetics: The pleasure-interest model of
  aesthetic liking*. Personality and Social Psychology Review, 19(4), 395–410.
  <https://doi.org/10.1177/1088868315574978>
- **Type:** theoretical synthesis.
- **Direct observation:** the model distinguishes immediate fluent pleasure from
  elaborated interest and models boredom and confusion as separate outcomes.
- **Interpretation permitted:** some controlled complexity or difficulty can be
  aesthetically rewarding when processing motivation and affordance support mastery.
- **Not permitted:** novelty or complexity is intrinsically better.
- **Related hypotheses:** HY-BEAUTY-002, HY-BEAUTY-009, HY-BEAUTY-011,
  HY-BEAUTY-014.
- **Confidence:** medium as a competing explanatory model.

### EV-BDE-007 — Fluency, prediction, and motivation

- **Source:** Yoo, J., Jasko, K., & Winkielman, P. (2024). *Fluency,
  prediction and motivation: how processing dynamics, expectations and epistemic
  goals shape aesthetic judgements*. Philosophical Transactions of the Royal
  Society B, 379, 20230326.
  <https://doi.org/10.1098/rstb.2023.0326>
- **Type:** peer-reviewed theoretical review.
- **Direct observation:** the authors extend fluency theory using expectations,
  predictive processing, and epistemic motivation while recording conceptual and
  empirical challenges to the simple account.
- **Interpretation permitted:** fluency is relative to internal models and goals.
- **Not permitted:** category expectations have been causally demonstrated for all
  website genres.
- **Related hypotheses:** HY-BEAUTY-002, HY-BEAUTY-006, HY-BEAUTY-013.
- **Confidence:** medium for theory framing.

### EV-BDE-008 — Website complexity, prototypicality, and first impression

- **Source:** Tuch, A. N., Presslaber, E. E., Stöcklin, M., Opwis, K., &
  Bargas-Avila, J. A. (2012). *The role of visual complexity and
  prototypicality regarding first impression of websites*. International
  Journal of Human-Computer Studies, 70(11), 794–811.
  <https://doi.org/10.1016/j.ijhcs.2012.06.003>
- **Type:** two screenshot-rating studies; first used 119 real-site screenshots.
- **Direct observation:** visual complexity and prototypicality affected ratings at very
  short exposures; low complexity and high prototypicality were favored in the tested
  set.
- **Interpretation permitted:** rapid aesthetic judgment uses coarse complexity and
  category-form cues.
- **Not permitted:** low complexity/high prototypicality maximizes complete-experience
  quality, memorability, or repeated-use preference.
- **Related hypotheses:** HY-BEAUTY-002, HY-BEAUTY-007, HY-BEAUTY-013,
  HY-BEAUTY-015.
- **Confidence:** medium for rapid screenshot impressions; low beyond them.

### EV-BDE-009 — Classical and expressive aesthetics

- **Source:** Lavie, T., & Tractinsky, N. (2004). *Assessing dimensions of
  perceived visual aesthetics of web sites*. International Journal of
  Human-Computer Studies, 60(3), 269–298.
  <https://doi.org/10.1016/j.ijhcs.2003.09.002>
- **Type:** four-study scale-development program.
- **Direct observation:** perceived website aesthetics separated into classical and
  expressive dimensions with reported reliability and validity evidence.
- **Interpretation permitted:** orderly clarity and convention-breaking expression are
  distinguishable aesthetic routes.
- **Not permitted:** two dimensions exhaust beauty or transfer unchanged across cultures
  and contemporary interfaces.
- **Related hypotheses:** HY-BEAUTY-002, HY-BEAUTY-003, HY-BEAUTY-006,
  HY-BEAUTY-008.
- **Confidence:** medium.

### EV-BDE-010 — Visual Aesthetics of Websites Inventory

- **Source:** Moshagen, M., & Thielsch, M. T. (2010). *Facets of visual
  aesthetics*. International Journal of Human-Computer Studies, 68(10),
  689–709. <https://doi.org/10.1016/j.ijhcs.2010.05.006>
- **Type:** seven-study measurement development and validation.
- **Direct observation:** four interrelated facets—simplicity, diversity, colorfulness,
  and craftsmanship—were identified, with convergent, divergent, discriminative, and
  concurrent validity evidence reported.
- **Interpretation permitted:** perceived visual aesthetics requires a profile rather
  than a single liking item.
- **Not permitted:** the four facets measure functional usability, category fit, or
  cultural resonance.
- **Related hypotheses:** HY-BEAUTY-003, HY-BEAUTY-005, HY-BEAUTY-008,
  HY-BEAUTY-011.
- **Confidence:** medium.

### EV-BDE-011 — Website credibility prominence study

- **Source:** Fogg, B. J., Soohoo, C., Danielson, D. R., Marable, L.,
  Stanford, J., & Tauber, E. R. (2003). *How Do Users Evaluate the Credibility
  of Web Sites?* Stanford Persuasive Technology Lab / Consumer WebWatch.
  <https://credibility.stanford.edu/pdf/How_Do_People_Evaluate_a_Web_Site%27s_Credibility_v37.pdf>
- **Type:** large online comparative-comment study; report, not a controlled causal
  experiment.
- **Direct observation:** “design look” appeared in 46.1% of coded credibility comments
  in the reported sample.
- **Interpretation permitted:** visual presentation is a salient cue in credibility
  judgment.
- **Not permitted:** polished design makes an organization trustworthy, or the 46.1%
  estimate transfers to current sites.
- **Related hypotheses:** HY-BEAUTY-001, HY-BEAUTY-013.
- **Confidence:** low-to-medium; historically important but dated and noncausal.

### EV-BDE-012 — WCAG 2.2

- **Source:** W3C Web Accessibility Initiative (2024). *Web Content
  Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation.
  <https://www.w3.org/TR/WCAG22/>
- **Type:** normative technical standard.
- **Direct observation:** defines testable requirements including text and non-text
  contrast, reflow, focus, motion/flashing, input, target size, and predictable
  interaction.
- **Interpretation permitted:** complete-experience evaluation must include accessible
  states and interaction constraints.
- **Not permitted:** conformance is sufficient evidence of beauty, usability, or
  desirability.
- **Related hypotheses:** HY-BEAUTY-012, HY-BEAUTY-015.
- **Confidence:** high for conformance requirements; not aesthetic evidence.

## Evidence gaps

1. Cross-cultural measurement invariance for beauty, expressiveness, and category fit.
2. Full-experience replications of screenshot prototypicality findings.
3. Factorial isolation of art direction from interface styling.
4. Expert-versus-general-audience preference with representative stimuli.
5. Detail accumulation experiments.
6. Accessibility interventions measured for both use and aesthetic response.
7. Longitudinal studies beyond two weeks and beyond phone/ATM task families.
8. Evidence connecting visual polish to retention, conversion, and calibrated trust
   without brand or content confounds.

## Revision history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-07-26 | Added 12 bounded evidence records and the initial evidence-gap register. |
