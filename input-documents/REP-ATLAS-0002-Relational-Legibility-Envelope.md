---
title: ATLAS-0002 Relational Legibility Envelope
id: REP-ATLAS-0002
document_type: research_execution_package
project: Composition Science
version: 1.0
status: working
date: 2026-07-21
authors:
  - Kevin Miller
  - OpenAI autonomous research agent
confidence: Moderate
llm_ingest: true
machine_readable: true
purpose: |
  Convert the qualitative Relational Legibility concept into a bounded,
  testable model integrating grouping, discrimination, visual search,
  spatial stability, accessibility, and consequence without asserting a
  universal pixel spacing rule.
references:
  - Project_Atlas_Autonomous_Research_Report_001_Relational_Legibility.md
  - Composition_Science_Markdown_Template_v1.md
  - Composition_Science_Ontology_v1.md
  - Composition_Science_Repository_Governance_Specification_v1.md
  - Composition_Science_Research_Library_v0.4.md
---

# ATLAS-0002: Relational Legibility Envelope

## Purpose

This package advances the Relational Legibility model from a conceptual statement to a research-ready predictive framework.

The target is not a universal spacing scale. The target is a conditional model that can answer:

- When will related elements be perceived as a group?
- When will nearby elements become difficult to identify?
- When will increasing separation weaken rather than improve composition?
- Which cues compensate for weak spacing?
- Which transformations preserve compositional identity?
- When does a small weakness become unacceptable because consequences are high?

The package follows Composition Science requirements to preserve contradictions, use stable identifiers, distinguish observation from interpretation, and avoid claims stronger than the evidence.

------------------------------------------------------------------------

# Executive Summary

## What was accomplished

Six research cycles continued the prior Atlas work. This pass:

1. formalized the Relational Legibility Envelope;
2. separated grouping, identification, search, action, and stability;
3. replaced a single spacing variable with normalized perceptual variables;
4. proposed candidate metrics and laws;
5. tested whether the model could be reduced to one score;
6. documented failure conditions and the next evidence package.

## Major discoveries

### The envelope is not one curve

Relational legibility is a feasible region created by several partially independent constraints:

```text
group coherence
individual discriminability
search efficiency
interaction accuracy
semantic correctness
spatial stability
accessibility robustness
consequence-adjusted safety
```

A composition can satisfy one and fail another.

### Center separation and edge gap are not interchangeable

Crowding research frequently uses center-to-center spacing. Interface implementation usually uses edge-to-edge gaps. Atlas must record both plus element dimensions.

### Visual angle is necessary but insufficient

Visual angle supports comparison across devices and viewing distances, but does not encode similarity, orientation, common region, semantic grouping, familiarity, input method, or time pressure.

### Group organization can reduce crowding

Research shows that flankers grouped with one another can interfere less with a target even when target distance is unchanged. Reorganization may sometimes substitute for more whitespace.

### Stable emphasis is often safer than adaptive relocation

Spatial-memory research and recent adaptive-menu work support changing emphasis before changing item position.

### One aggregate score would hide failure modes

Excellent grouping cannot compensate for an inaccessible focus order. Fast selection cannot compensate for catastrophic rare errors. Atlas should use a profile with hard gates, not one quality number.

## Confidence

- **High:** the model must be conditional and multidimensional.
- **High:** crowding is not a fixed pixel rule.
- **High:** accessibility requires agreement across visual and operational structure.
- **Moderate-high:** stable spatial organization supports learned performance.
- **Moderate:** the proposed variables cover the most important mechanisms.
- **Low-to-moderate:** exact weights and cross-domain thresholds.

## Largest remaining uncertainty

How should cue strength and task importance be calibrated so that the model predicts measured human performance rather than merely organizing expert judgment?

------------------------------------------------------------------------

# Prior State Reviewed

The previous report established that proximity affects grouping; grouping is multi-cue and competitive; crowding limits identification; progressive disclosure redistributes complexity; spatial stability supports learning; and visual hierarchy alone is insufficient for accessibility. fileciteturn1file0L1-L83

The project template requires stable IDs, explicit confidence, contradictory evidence, and measurable variables. fileciteturn1file5L1-L90

The ontology places this work primarily under GN-100 Perception, GN-200 Cognition, GN-300 Action, GN-510 Spatial Organization, GN-520 Hierarchy, GN-540 Structure, GN-550 Navigation, and GN-560 Interaction. fileciteturn2file14L1-L49

------------------------------------------------------------------------

# Research Log

## Cycle 1 — Is This Mainly a Spacing Model?

### Objective

Determine whether spacing can remain the primary independent variable.

### Hypothesis

**HY-ATLAS-002-001:** Relational legibility can be modeled mainly through within-group and between-group spacing.

### Evidence Found

Proximity is a strong grouping cue. Crowding research finds systematic effects of target-flanker separation, especially as eccentricity increases. Design systems repeatedly distinguish within-group from between-group spacing.

### Evidence Against

Grouping can change without changing target distance. Sayim and colleagues found that flankers grouped with one another reduced crowding independently of their distance from the target. Similarity, common region, connectedness, alignment, and semantics can override proximity. citeturn430190search2

### Analysis

Spacing is important but not sufficient. The model must represent geometry, cue agreement, target similarity, semantics, task, and learned structure.

### Conclusion

**Rejected.** The envelope is a multi-constraint composition model, not a spacing model.

### Confidence

High.

### Next Step

Determine the minimum independent outcome dimensions.

------------------------------------------------------------------------

## Cycle 2 — Can One Performance Measure Summarize Legibility?

### Objective

Find a single dependent variable suitable for comparing compositions.

### Hypothesis

**HY-ATLAS-002-002:** Task completion time can serve as the primary summary.

### Evidence Found

Reaction time is widely used in visual search, menu selection, target acquisition, and classification.

### Evidence Against

Fast performance can coexist with high error rates, poor comprehension, inaccessible structure, unsafe shortcuts, poor learning, and failure in rare states. Experts can execute poor but practiced mappings quickly.

### Analysis

Required outcome families include grouping accuracy, identification, search latency, hierarchy reconstruction, location retention, selection error, recovery cost, cross-modal structural agreement, and consequence-weighted errors.

### Conclusion

**Rejected.** Time is useful but cannot be the sole outcome.

### Confidence

High.

### Next Step

Define a profile with gates and optimization metrics.

------------------------------------------------------------------------

## Cycle 3 — Can Visual Angle Normalize Devices?

### Objective

Determine whether visual angle can replace pixels as the base spatial unit.

### Hypothesis

**HY-ATLAS-002-003:** Expressing size and separation in visual angle makes findings transferable across devices.

### Evidence Found

Vision science represents size, eccentricity, and critical spacing in angular units. A 50-observer crowding study reported that a two-parameter Bouma model explained 82% of variance; adding meridian, orientation, target kind, and observer increased explained variance to 94%. The project evidence registry already preserves these modifiers and warns against turning them into CSS rules. fileciteturn2file8L19-L78

Letter-identification research distinguishes acuity, overlap masking, and crowding as separate size or spacing constraints. citeturn430190search17

### Evidence Against

Equal angular geometry does not normalize contrast, luminance, rendering, glare, motion, target similarity, semantics, or input method.

### Analysis

Visual angle is a required normalization layer, not a complete predictor.

```text
angular size = 2 × atan(physical size / (2 × viewing distance))
angular separation = 2 × atan(physical separation / (2 × viewing distance))
```

### Conclusion

**Partially confirmed.** Necessary but insufficient.

### Confidence

High.

### Next Step

Define spatial metrics without claiming universal thresholds.

------------------------------------------------------------------------

## Cycle 4 — Are Grouping and Crowding Monotonic Opposites?

### Objective

Create a relationship between group coherence and individual discrimination.

### Hypothesis

**HY-ATLAS-002-004:** Grouping decreases and discriminability increases monotonically as spacing grows.

### Evidence Found

At a coarse level, proximity strengthens grouping and additional separation can reduce crowding.

### Evidence Against

Grouping is reinforced by common region, connectedness, similarity, labels, and alignment. Grouped flankers can reduce crowding without added target separation. Excessive spacing can increase search distance, scrolling, and label-control separation.

### Analysis

The model needs separate functions:

```text
G = grouping confidence
D = discriminability
Q = search efficiency
A = action efficiency
M = spatial-memory support
T = transformation preservation
X = cross-modal agreement
E = consequence-weighted error
```

### Conclusion

**Rejected in monotonic form.**

### Confidence

High.

### Next Step

Define the envelope as constraint intersection.

------------------------------------------------------------------------

## Cycle 5 — Should Adaptive Interfaces Move Important Items?

### Objective

Refine the Spatial Stability Hierarchy.

### Hypothesis

**HY-ATLAS-002-005:** The best adaptive interface moves high-value commands toward the user.

### Evidence Found

Adaptive interfaces can prioritize expected commands and reduce visible search.

### Evidence Against

Moving commands damages location memory. Spatial-memory research notes that interfaces often undermine users by moving or rearranging items. citeturn430190search3 Recent Fractal Adaptive Menu research reports better selection through attentional guidance without moving item positions. citeturn430190search11 Landmarks also aid spatial memory and expertise development. citeturn430190search33

### Analysis

Classify adaptation by disruption:

```yaml
level_0: no change
level_1: emphasis only
level_2: local detail or density
level_3: predictable collapse
level_4: explicit context replacement
level_5: opaque relocation
```

The burden of proof should increase with disruption.

### Conclusion

**Rejected.** Prefer adaptive emphasis over adaptive relocation.

### Confidence

Moderate-high.

### Next Step

Add stability as an independent dimension.

------------------------------------------------------------------------

## Cycle 6 — Can the Envelope Produce One Design Score?

### Objective

Determine the output format for Atlas analysis.

### Hypothesis

**HY-ATLAS-002-006:** All dimensions can be combined into a weighted score.

### Evidence Found

A weighted score would be convenient for rankings, automated generation, and dashboards.

### Evidence Against

Compensatory scoring allows unacceptable trades. Excellent grouping could offset invisible focus; fast selection could offset catastrophic errors; visual hierarchy could offset semantic-order conflict. Weights would encode value judgments about users and consequence.

### Analysis

Use a **profile with gates**:

```yaml
gates:
  semantic_structure: pass
  focus_order: pass
  minimum_identification: pass
  consequence_adjusted_error: pass
profile:
  grouping_confidence: 0.84
  discrimination_accuracy: 0.91
  search_slope_ms_per_item: 18
  selection_error_rate: 0.02
  spatial_retention: 0.73
  transformation_preservation: 0.88
```

### Conclusion

**Rejected.** Optimization begins only after mandatory gates pass.

### Confidence

High.

------------------------------------------------------------------------

# Confirmed Findings

## CF-ATLAS-002-001 — Relational legibility is multidimensional

Grouping, identification, search, action, semantics, accessibility, and stability are not interchangeable.

**Confidence:** High.

## CF-ATLAS-002-002 — Spacing must be recorded in several forms

Record edge gap, center separation, element dimensions, and visual angle where viewing geometry matters.

**Confidence:** High.

## CF-ATLAS-002-003 — Critical spacing is conditional

Eccentricity is important, while orientation, field location, target type, and observer explain additional variance.

**Confidence:** High.

## CF-ATLAS-002-004 — Group organization can alter crowding independently of distance

**Confidence:** Moderate-high.

## CF-ATLAS-002-005 — Stable landmarks support learning

**Confidence:** Moderate-high.

## CF-ATLAS-002-006 — Accessibility variables are structural variables

Visual, semantic, focus, and announcement order must be evaluated together.

**Confidence:** High.

## CF-ATLAS-002-007 — Consequence changes acceptance thresholds

**Confidence:** High as a human-factors principle; thresholds remain domain-specific.

------------------------------------------------------------------------

# Rejected Hypotheses

- **RH-ATLAS-002-001:** Relational legibility is mainly a spacing problem.
- **RH-ATLAS-002-002:** Task completion time is sufficient.
- **RH-ATLAS-002-003:** Visual angle makes findings universally transferable.
- **RH-ATLAS-002-004:** Grouping and discrimination are monotonic opposites.
- **RH-ATLAS-002-005:** Adaptive relocation is the best prioritization mechanism.
- **RH-ATLAS-002-006:** One weighted total score is safe.

------------------------------------------------------------------------

# Observations

## OBS-ATLAS-002-001

### Observation

Project documents often use “spacing” without distinguishing edge gap, center distance, and visual angle.

### Interpretation

This can create false comparisons across elements of different sizes.

### Confidence

High.

## OBS-ATLAS-002-002

### Observation

Design-system token scales primarily provide implementation consistency.

### Interpretation

Token regularity should not be presented as perceptual threshold evidence.

### Confidence

High.

## OBS-ATLAS-002-003

### Observation

The strongest quantitative perceptual evidence is conditional and parameterized.

### Interpretation

Atlas should preserve modifier variables rather than average them away.

### Confidence

High.

------------------------------------------------------------------------

# Proposed Model

## MODEL-ATLAS-002-001 — Relational Legibility Envelope

A composition is relationally legible for a specified user, task, environment, and consequence when every mandatory structural and operational constraint is satisfied and optional performance measures remain within acceptable ranges.

```text
RLE(context) is acceptable iff:

G >= G_min(context)
D >= D_min(context)
A_error <= A_max(context)
X passes mandatory structural checks
E <= E_max(context)

and Q, M, and T are optimized without violating the gates.
```

Where:

- `G` = grouping confidence
- `D` = individual discriminability
- `Q` = search efficiency
- `A` = action accuracy and cost
- `M` = spatial-memory support
- `T` = transformation preservation
- `X` = cross-modal structural agreement
- `E` = consequence-weighted error risk

Different compositions may succeed through different cue combinations. A weak proximity cue may be repaired by common region and labels; a dense command space may remain learnable through stable landmarks; hidden content may remain usable through a clear reveal path.

### Assumptions

1. User population is specified.
2. Task is specified.
3. Viewing and interaction conditions are specified.
4. Important errors and consequences are specified.
5. Measurements are revalidated after material context changes.
6. Accessibility and safety gates are noncompensatory.

------------------------------------------------------------------------

# Candidate Laws

## LAW-ATLAS-002-001 — Relational Group Evidence Law

### Hypothesis

Perceived grouping is determined by accumulated agreement among spatial, visual, semantic, and behavioral cues rather than proximity alone.

### Prediction

Holding spacing constant, adding an agreeing common-region, connectedness, or semantic-label cue will improve grouping judgments. Conflicting cues will reduce agreement or increase latency.

### Confidence

Moderate-high.

## LAW-ATLAS-002-002 — Conditional Peripheral Separation Law

### Hypothesis

The separation needed for reliable identification grows with eccentricity but is moderated by direction, target type, similarity, grouping, and observer.

### Prediction

A model with eccentricity and modifiers will outperform fixed-pixel and fixed-ratio models.

### Confidence

High in crowding tasks; moderate for interface transfer.

## LAW-ATLAS-002-003 — Grouped-Flanker Relief Law

### Hypothesis

Distractors forming a strong group separate from the target can interfere less than equally distant ungrouped distractors.

### Confidence

Moderate.

## LAW-ATLAS-002-004 — Learned Location Stability Law

### Hypothesis

Repeated functions become faster to find when identity, approximate location, and landmarks remain stable.

### Confidence

Moderate-high.

## LAW-ATLAS-002-005 — Adaptive Emphasis Precedence Law

### Hypothesis

When relevance changes but identity does not, altering emphasis preserves learned performance better than altering position.

### Confidence

Moderate.

## LAW-ATLAS-002-006 — Cross-Modal Structural Agreement Law

### Hypothesis

A composition is more robust when visual order, semantic order, focus order, and announced grouping communicate compatible relationships.

### Confidence

High for agreement; moderate for literal equivalence.

## LAW-ATLAS-002-007 — Consequence-Adjusted Margin Law

### Hypothesis

Required separation, salience, redundancy, verification, and error tolerance increase with failure consequence, time pressure, workload, and irreversibility.

### Confidence

High as a principle; low for universal weights.

------------------------------------------------------------------------

# Metrics

## MET-ATLAS-002-001 — Edge Gap

Minimum edge-to-edge distance between rendered elements.

## MET-ATLAS-002-002 — Center Separation

Distance between target centers.

## MET-ATLAS-002-003 — Angular Separation

```text
2 × atan(center separation / (2 × viewing distance))
```

Record degrees, viewing distance, eccentricity, and radial/tangential orientation.

## MET-ATLAS-002-004 — Relative Separation Ratio

```text
between-group gap / within-group gap
```

Use descriptively or experimentally, not as a universal threshold.

## MET-ATLAS-002-005 — Cue Agreement Vector

```yaml
proximity: agree|neutral|conflict
similarity: agree|neutral|conflict
common_region: agree|neutral|conflict
connectedness: agree|neutral|conflict
alignment: agree|neutral|conflict
label_semantics: agree|neutral|conflict
behavior: agree|neutral|conflict
```

## MET-ATLAS-002-006 — Group Reconstruction Accuracy

Report accuracy, confusion matrix, response time, observer agreement, and uncertainty.

## MET-ATLAS-002-007 — Identification Under Clutter

Report target, distractor class, eccentricity, spacing, exposure, and population.

## MET-ATLAS-002-008 — Search Slope

Change in reaction time divided by change in set size.

## MET-ATLAS-002-009 — Spatial Retention

After training and delay, measure location recall, command-selection time, fixation distance, and relocation errors.

## MET-ATLAS-002-010 — Transformation Preservation

```yaml
identity_preserved:
group_preserved:
order_preserved:
prominence_preserved:
label_association_preserved:
focus_sequence_preserved:
task_path_preserved:
```

Test narrow viewport, zoom, reflow, touch scale, localization, RTL, dark mode, and disclosure states.

## MET-ATLAS-002-011 — Complexity Redistribution Ledger

```yaml
visible_search_cost:
reveal_cost:
navigation_cost:
memory_cost:
state_tracking_cost:
overview_loss:
spatial_instability:
recovery_cost:
```

## MET-ATLAS-002-012 — Consequence-Weighted Error Record

```yaml
error_type:
probability:
severity:
detectability:
recoverability:
time_to_harm:
affected_population:
```

Do not collapse this into one universal equation.

------------------------------------------------------------------------

# Proposed Experiments

Existing literature must be exhausted first, consistent with the project methodology. fileciteturn2file10L1-L73

## EXP-ATLAS-002-001 — Grouping–Discrimination Boundary

Manipulate within-group spacing, between-group spacing, common region, similarity, eccentricity, and target-flanker similarity. Measure grouping reconstruction, target identification, response time, and confidence.

## EXP-ATLAS-002-002 — Adaptive Emphasis Versus Relocation

Compare stable baseline, adaptive emphasis, predictable collapse, and adaptive relocation among novice, trained, and expert users.

## EXP-ATLAS-002-003 — Cross-Modal Structure Audit

Compare screenshot grouping, DOM landmarks, heading structure, keyboard traversal, screen-reader announcements, and reflow state.

------------------------------------------------------------------------

# Failure and Boundary Conditions

The model should not be used to claim universal beauty, emotional response, cultural meaning, brand fit, one ideal density, one spacing ratio, safety certification, or usability without human evaluation.

The model is weakest when the task is exploratory or expressive, novelty is deliberately valuable, users construct rather than retrieve meaning, social interpretation dominates, or movement and time define the composition.

------------------------------------------------------------------------

# Emerging Patterns

## EP-ATLAS-002-001 — Constraint Intersection

Good composition is often the intersection of minimum conditions, not optimization of one variable.

## EP-ATLAS-002-002 — Reorganization Can Substitute for Separation

Interference may be reduced through grouping, differentiation, or landmarks rather than additional whitespace.

## EP-ATLAS-002-003 — Normalization Is Layered

Pixels normalize implementation. Visual angle normalizes viewing geometry. Neither normalizes meaning, task, or consequence.

## EP-ATLAS-002-004 — Stability Is Stored User Capital

Learned locations and landmarks represent accumulated investment. Relocation liquidates part of it.

## EP-ATLAS-002-005 — Noncompensatory Requirements Matter

Accessibility and safety failures should act as gates, not weak weighted penalties.

------------------------------------------------------------------------

# Open Questions

1. How should cue agreement be quantified?
2. Which crowding results transfer from letters to icons, controls, and charts?
3. What minimum user tasks should every Atlas audit test?
4. Can transformation preservation be predicted statically?
5. How do aging, low vision, amblyopia, and field loss alter the envelope?
6. Can adaptive emphasis scale to large command sets without excessive salience competition?
7. How should consequence gates connect to established safety-engineering methods?

------------------------------------------------------------------------

# Repository Update Proposal

No permanent registry change should occur without review of this REP, consistent with repository governance. fileciteturn2file0L1-L45

## Hypothesis Registry

Add HY-ATLAS-002-001 through HY-ATLAS-002-006 with their documented dispositions.

## Candidate Law Registry

Propose LAW-ATLAS-002-001 through LAW-ATLAS-002-007. None should be promoted beyond candidate law.

## Evidence Registry

Add evidence records for crowding modifiers, grouped-flanker relief, spatial-memory stability, adaptive emphasis, FAA clutter guidance, and WCAG structural requirements.

## Metrics Registry

Add MET-ATLAS-002-001 through MET-ATLAS-002-012.

## Genome Links

```yaml
GN-511_Proximity:
  - LAW-ATLAS-002-001
  - LAW-ATLAS-002-003
GN-512_Separation:
  - LAW-ATLAS-002-002
  - MET-ATLAS-002-001
  - MET-ATLAS-002-002
  - MET-ATLAS-002-003
  - MET-ATLAS-002-004
GN-513_Density:
  - MET-ATLAS-002-011
GN-515_Enclosure:
  - LAW-ATLAS-002-001
GN-516_Connectedness:
  - LAW-ATLAS-002-001
GN-520_Hierarchy:
  - MODEL-ATLAS-002-001
GN-540_Structure:
  - LAW-ATLAS-002-006
  - MET-ATLAS-002-010
GN-550_Navigation:
  - LAW-ATLAS-002-004
  - LAW-ATLAS-002-005
GN-560_Interaction:
  - MET-ATLAS-002-009
  - MET-ATLAS-002-011
```

------------------------------------------------------------------------

# Recommendations

| Priority | Action | Expected value | Effort |
|---|---|---:|---:|
| 1 | Build a quantitative evidence table for crowding studies | Very high | Medium |
| 2 | Extract studies on grouping-dependent crowding | Very high | Medium |
| 3 | Build a visual-angle normalization utility | High | Low |
| 4 | Create a rendered audit fixture for grouping, focus, reflow, and localization | Very high | Medium |
| 5 | Synthesize adaptive emphasis versus relocation | High | Medium |
| 6 | Add aging and low-vision modifiers | Very high | High |
| 7 | Connect consequence gates to FAA, NASA, and FDA methods | High | High |
| 8 | Do not publish a universal spacing recommendation | Very high | None |

## Highest-value next package

**REP-ATLAS-0003: Quantitative Crowding and Grouping Evidence Matrix**

For every study, capture:

```yaml
participants:
population:
task:
stimulus:
target_size:
target_class:
flanker_class:
eccentricity:
spacing_measure:
orientation:
exposure:
grouping_manipulation:
dependent_variables:
effect_size:
model_fit:
limitations:
transfer_to_composition:
```

------------------------------------------------------------------------

# Bibliography

## Academic

- Ben-Av, M. B., and Sagi, D. (1995). *Perceptual Grouping by Similarity and Proximity*. https://pubmed.ncbi.nlm.nih.gov/7740775/
- Kurzawski, J. W., et al. (2023). *The Bouma Law Accounts for Crowding in 50 Observers*. https://doi.org/10.1167/jov.23.8.6
- Pelli, D. G., and Tillman, K. A. (2008). *The Uncrowded Window of Object Recognition*. https://pubmed.ncbi.nlm.nih.gov/18835355/
- Sayim, B., Westheimer, G., and Herzog, M. H. (2013). *Grouping and Crowding Affect Target Appearance over Different Spatial Scales*. https://pubmed.ncbi.nlm.nih.gov/23967164/
- Scarr, J., et al. (2013). *Supporting and Exploiting Spatial Memory in User Interfaces*. https://dl.acm.org/doi/10.1561/1100000046
- Song, S., Levi, D. M., and Pelli, D. G. (2014). *A Double Dissociation of the Acuity and Crowding Limits to Letter Identification*. https://pubmed.ncbi.nlm.nih.gov/24799622/
- Uddin, M. S., et al. (2021). *How People Use Landmarks to Develop Spatial Memory in Large Command Spaces*. https://dl.acm.org/doi/10.1145/3411764.3445050
- Wagemans, J., et al. (2012). *A Century of Gestalt Psychology in Visual Perception*. https://pubmed.ncbi.nlm.nih.gov/22845751/

## Industry and Engineering

- Sahraoui, A. E. A., et al. (2025). *Fractal Adaptive Menus*. https://dl.acm.org/doi/10.1145/3731406.3734978

## Standards and Government

- Federal Aviation Administration. *Human Factors Design Standard*. https://hf.tc.faa.gov/publications/2016-12-human-factors-design-standard/full_text.pdf
- Federal Aviation Administration. *Human Factors Design Guidelines for Multifunction Displays*. https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/0117.pdf
- NASA. *Human Systems Integration Handbook*. https://ntrs.nasa.gov/api/citations/20210010952/downloads/HSI%20Handbook%20v2.0%20092121_FINAL%20COPY.pdf
- W3C. *Web Content Accessibility Guidelines 2.2*. https://www.w3.org/TR/WCAG22/

## Books

No book was used as decisive evidence in this pass.

## Patents

No patent evidence was necessary for the questions resolved in this pass.

------------------------------------------------------------------------

# Revision History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0 | 2026-07-21 | Kevin Miller and OpenAI | Formalized the Relational Legibility Envelope, ran six falsification cycles, proposed seven candidate laws and twelve metrics, rejected aggregate scoring, and defined the quantitative evidence matrix as the next package. |

------------------------------------------------------------------------

# Agent Instructions

1. Separate observations from interpretations.
2. Preserve contradictory evidence.
3. Never convert crowding coefficients directly into CSS spacing rules.
4. Record target dimensions whenever recording gaps.
5. Record viewing geometry when making perceptual claims.
6. Treat accessibility and safety requirements as gates.
7. Do not collapse the profile into one score without governance approval.
8. Prefer existing studies before experiments.
9. Append revisions; do not erase rejected hypotheses.
10. Link future evidence to stable IDs.
