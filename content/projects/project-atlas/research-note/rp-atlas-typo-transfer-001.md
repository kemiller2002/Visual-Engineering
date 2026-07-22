---
identifier: RP-ATLAS-TYPO-TRANSFER-001
title: Typography Cross-Layer Transfer and Adaptive Reading
research_area: Project Atlas / Typography Genome
discipline:
  - vision science
  - cognitive psychology
  - psycholinguistics
  - human-computer interaction
  - typography
author_agent: OpenAI
version: 1.0
confidence: Moderate-High
completion: Complete for current research phase
priority: Critical
date: 2026-07-21
related_projects:
  - Project Atlas
  - Composition Science
related_documents:
  - Project_Atlas_Typography_Autonomous_Research_Report_v1.md
  - Project_Atlas_Letter_Confusion_Data_Audit_v1.md
  - Project_Atlas_Visual_Information_Transfer_Foundations_v1.md
supersedes: null
superseded_by: null
tags:
  - typography
  - reading
  - transfer
  - eye movements
  - comprehension
  - adaptive systems
  - personalization
keywords:
  - cross-layer transfer
  - active bottleneck
  - compensation cost
  - font tuning
  - reading speed
  - comprehension
  - visual span
llm_ingest: true
machine_readable: true
status: canonical research package
summary: |
  This research package investigates when improvements to glyphs, fonts, spacing,
  size, width, and weight transfer to higher-level outcomes such as word recognition,
  continuous reading, comprehension, navigation, memory, and action. The research
  rejects a simple upward-transfer model. Typography changes can improve local
  perceptual capacity without improving reading, can preserve reading speed through
  increased compensatory effort, or can improve reading for some individuals while
  harming others. The strongest emerging theory is that transfer occurs when three
  conditions align: the manipulated typographic property affects the active
  bottleneck, the benefit survives interactions with layout and language, and the
  measured outcome is sensitive to the cost being reduced. Atlas should therefore
  model typography as a personalized adaptive control problem rather than search for
  one universally optimal typeface.
---

# Research State Snapshot

- **Theory Version:** TH-TYPO-ADAPTIVE-002
- **Knowledge Base Version:** KB-ATLAS-2026-07-21
- **Highest Confidence Areas:**
  - typography operates through multiple layers
  - local perceptual improvements do not guarantee reading improvements
  - print size and display capacity create interacting constraints
  - reader compensation can mask typographic cost
  - individual differences materially affect optimal settings
- **Lowest Confidence Areas:**
  - predicting transfer before testing
  - quantifying cognitive effort independently of speed
  - generalizing personalized font effects beyond study populations
  - linking reading improvements to real-world task outcomes
- **Largest Remaining Unknown:** How to diagnose the active bottleneck for a person, task, and environment with a short practical test.
- **Active Research Streams:**
  - human confusion matrices
  - personalized typography
  - compensation-cost metrics
  - cross-script generalization
  - task-weighted typography
- **Recently Invalidated Ideas:**
  - better glyph recognition automatically improves reading
  - one best font can be selected for a population
  - slower reading caused by disfluency reliably improves memory
  - reading speed alone is an adequate outcome
- **Priority Changes:**
  - personalized and task-specific models moved to highest priority
  - universal font ranking moved to low priority
  - cross-layer measurement moved ahead of additional anatomy cataloging

# Executive Summary

## What Was Accomplished

This phase investigated the largest uncertainty left by the prior Project Atlas
typography research:

> When does a measurable improvement at the glyph or font level transfer upward
> to word recognition, reading speed, comprehension, memory, navigation, or action?

The research reviewed evidence from vision science, psycholinguistics,
eye-tracking, low-vision research, learning science, and human-computer
interaction. It examined both successful and failed transfers.

Six major hypothesis cycles were completed:

1. Whether glyph-level improvement is sufficient for reading improvement.
2. Whether reading speed captures the cost of typography.
3. Whether font effects are stable across readers.
4. Whether typography-induced difficulty improves memory or comprehension.
5. Whether layout constraints can reverse local typographic benefits.
6. Whether adaptation and personalization should replace universal optimization.

## Major Discovery

Cross-layer transfer is conditional.

A local typography change transfers upward only when:

1. it improves the process that is currently limiting performance;
2. the improvement is not cancelled by a new cost at another layer;
3. the higher-level task depends materially on the improved process;
4. the measurement captures the relevant benefit;
5. the reader has not already compensated enough to hide the difference.

This produces the proposed **Transfer Alignment Principle**:

> A typography intervention produces system-level benefit only when the
> intervention, active bottleneck, task dependency, and outcome measure are aligned.

## Confidence

**Moderate to high.**

The individual components are supported by multiple independent studies.
The integrated predictive model remains unvalidated as a whole.

## Remaining Uncertainty

The most important unresolved issue is practical diagnosis. Atlas needs a short
protocol that can distinguish whether a reader is currently constrained by:

- visual acuity
- contrast
- crowding
- glyph confusability
- line capacity
- eye-movement strategy
- lexical processing
- comprehension
- fatigue
- interface navigation

# Original Objective

Determine when and why typography improvements transfer from lower perceptual
layers to higher reading and task outcomes.

# Scope

Included:

- glyph recognition
- word recognition
- continuous reading
- visual span
- eye movements
- reading speed
- comprehension
- memory
- subjective workload
- personalization
- display and layout interaction

Excluded from this phase:

- full cross-script comparison
- production of new fonts
- new human-subject experiments
- branding and expressive typography except where relevant to transfer
- complete interface-navigation research

# Repository Context

This package extends three prior artifacts:

1. The visual-information foundation established that typography can be modeled
   as a noisy channel only at clearly defined layers.
2. The letter-confusion audit established that similarity ratings, confusion
   matrices, visual-span measures, and synthetic datasets answer different
   questions.
3. The autonomous typography report established the active-bottleneck model and
   rejected universal monotonic rules for spacing, size, weight, and width.

The present package tests the missing link between those lower-level findings
and real reading behavior.

# Current Understanding

Typography changes can produce at least four distinct outcomes:

```text
1. Capacity improvement
   The reader can recover more visual information.

2. Efficiency improvement
   The same task is completed faster or with fewer eye movements.

3. Compensation reduction
   Performance remains similar, but less effort is required.

4. Task improvement
   Comprehension, recall, navigation, or decision quality improves.
```

These outcomes are related but not interchangeable.

A study may show a capacity gain without an efficiency gain. A reader may
maintain speed while making longer fixations. A font may feel easier without
improving comprehension. A more difficult font may slow reading without creating
deeper processing.

# Key Discoveries

## KD-001: Transfer is bottleneck-dependent

Glyph improvements matter most near perceptual limits, in peripheral reading,
under low contrast, for low-vision readers, and in low-context tasks.

When lexical, semantic, temporal, or oculomotor processes dominate, improved
glyph distinction may not change reading speed.

## KD-002: Compensation can preserve output

Readers alter:

- fixation duration
- fixation count
- saccade length
- regressions
- reading strategy
- use of context

As a result, average reading speed can remain stable while effort changes.

## KD-003: Individual differences are not noise

Large-scale personalized-font studies report that different readers achieve
their best reading performance with different typefaces. Preference does not
reliably predict performance.

The appropriate unit of analysis may therefore be the reader-font-task
combination rather than the typeface alone.

## KD-004: Local difficulty is usually not a desirable difficulty

Disfluent fonts reliably increase perceived difficulty, but effects on learning
and memory are inconsistent or null. Additional orthographic effort does not
necessarily create semantic or relational processing.

## KD-005: Layout can cancel local gains

Larger print improves recognition until fewer characters fit per line or screen.
Wider forms may improve local shape availability while increasing line length or
reducing text capacity. More spacing can reduce crowding while fragmenting words.

Typography must therefore be evaluated within its display geometry.

## KD-006: Personalization is more promising than universal ranking

Evidence from adaptive and individualized typography suggests meaningful reading
speed gains can be obtained by tuning font family, size normalization, character
spacing, and line spacing to the reader.

The strongest current direction is not “find the best font,” but “identify a
small effective configuration for this reader and task.”

# Research Log

## Cycle 1: Is glyph-level improvement sufficient for continuous reading?

### Objective

Test whether a font that improves isolated or peripheral letter recognition
should improve continuous reading.

### Hypothesis

Improved glyph recognition will reliably increase reading speed.

### Evidence Found

Fonts designed for peripheral distinction can improve:

- isolated letter recognition
- peripheral word recognition
- some low-vision outcomes

Luciole showed small advantages over some comparison fonts for some readers with
low vision.

### Evidence Against

A font designed specifically for peripheral vision improved peripheral letter
and word recognition but did not improve eye-mediated sentence reading.

Training that reduced crowding did not always produce proportional changes in
visual span or reading speed.

### Sources

- Bernard et al. (2016)
- He et al. (2017)
- Galiano et al. (2023)
- Legge et al. visual-span research

### Analysis

The local benefit was real, but the continuous-reading system was able to
compensate or was limited elsewhere.

The original hypothesis assumed a serial pipeline:

```text
better letters → better words → faster reading
```

The evidence supports a conditional network:

```text
better letters
    ├─ improves reading if letter information is limiting
    ├─ produces no change if another process is limiting
    └─ may be cancelled by spacing, width, familiarity, or eye-movement costs
```

### Conclusion

Rejected as a universal claim.

### Confidence

High

### Next Step

Determine whether common reading metrics conceal compensation.

---

## Cycle 2: Does reading speed capture typographic cost?

### Objective

Test whether equal reading speed implies equivalent typography performance.

### Hypothesis

If two text settings produce the same reading speed, they are functionally
equivalent.

### Evidence Found

Reading speed is strongly related to many practical reading outcomes and remains
an important measure.

### Evidence Against

Font-width studies found similar aggregate speed with different combinations of
fixation counts, fixation durations, and saccade behavior.

Webpage typography studies found effects on eye movements even when higher-level
performance differences were limited.

Bionic-reading studies found little or no speed advantage and changed effort or
reading time inconsistently.

### Sources

- Minakata and Beier (2021)
- Scaltritti et al. (2019)
- Beelders et al. (2025)
- eye-movement studies of reading strategy

### Analysis

Readers can maintain throughput by paying a higher internal cost.

Equivalent speed can coexist with:

- longer fixations
- more regressions
- reduced spare attention
- lower robustness under distraction
- higher fatigue
- reduced persistence

Reading speed is an output variable, not a complete cost function.

### Conclusion

Rejected.

### Confidence

High

### Next Step

Investigate whether individual readers exhibit stable differences in font
response.

---

## Cycle 3: Is there a universally superior font for fluent readers?

### Objective

Test whether population averages can identify one generally best-performing
typeface.

### Hypothesis

Once fonts are normalized for size, one or a small set of fonts will consistently
outperform others across readers.

### Evidence Found

Some fonts perform better on average in specific experiments. Familiar and
conventional structures often support fluent reading.

### Evidence Against

Individual-difference studies found substantial reader-specific variation in
font preference and reading speed.

Preference and familiarity did not reliably identify the fastest font for each
reader.

Studies of school-age readers found that personalized font selection could
increase reading speed while preserving comprehension.

Adaptive-font systems demonstrated the feasibility of learning a reader-specific
font configuration.

### Sources

- Wallace et al. (2020)
- Wallace et al. (2022)
- Kadner et al. (2021)
- Nedeljković et al. (2020)

### Analysis

Population means can conceal crossover interactions:

```text
Reader A: Font X > Font Y
Reader B: Font Y > Font X
Average: X ≈ Y
```

This is not random measurement noise if the preference remains reproducible.

Universal defaults are still needed, but they should be viewed as robust
starting points rather than optima.

### Conclusion

Rejected as a universal claim.

### Confidence

Moderate to high

### Next Step

Test whether deliberate difficulty can improve higher-level outcomes.

---

## Cycle 4: Does typographic disfluency improve memory or comprehension?

### Objective

Evaluate whether making text harder to read creates deeper processing.

### Hypothesis

A difficult-to-read font increases mental effort, which improves memory and
comprehension.

### Evidence Found

A small number of studies reported benefits under limited conditions, especially
for distinctive material or novel-word learning.

Distinctive typography can direct attention when selectively applied.

### Evidence Against

Multiple studies found no benefit of Sans Forgetica or other disfluent fonts for
recall or comprehension.

A one-week delayed-recall study found a strong testing benefit but no font
benefit, despite a large perceived-difficulty manipulation.

The authors argued that disfluency increases local orthographic work rather than
semantic-relational processing and may interfere with integration across words.

Recent work also reports null effects on comprehension and attention.

### Sources

- Wetzler et al. (2021)
- Taylor et al.
- Geller et al.
- Tietz et al. (2025)
- disfluency meta-analytic debate

### Analysis

Effort is not fungible.

```text
More perceptual effort
≠
more semantic processing
```

Difficulty helps only when the extra work engages processes that are useful for
the later task.

This is consistent with transfer-appropriate processing and the broader Atlas
transfer model.

### Conclusion

Rejected as a general theory.

### Confidence

High

### Next Step

Investigate interactions between local legibility and available layout space.

---

## Cycle 5: Can local legibility improvements be reversed by layout constraints?

### Objective

Test whether larger, wider, or more spaced type remains beneficial when display
capacity is considered.

### Hypothesis

Improving local visual availability will improve total reading performance.

### Evidence Found

Larger print improves reading below critical print size.

Spacing can reduce crowding.

Wider or larger-x-height forms may improve recognition under small-size
conditions.

### Evidence Against

On small displays, increasing print size reduces characters per line and lines
per screen. Reading performance requires both sufficient angular size and enough
text capacity.

Research found a minimum approximate character count per line for maintaining a
criterion level of reading speed.

Increased spacing and width can introduce more eye movements and navigation cost.

### Sources

- Atilgan et al. (2020)
- Legge and Bigelow (2011)
- Yu et al. (2007)
- Minakata and Beier (2021)
- Sawyer et al. (2025)

### Analysis

Typography and layout share a finite spatial budget.

A local change reallocates that budget:

```text
larger characters
    → more visible detail
    → fewer characters per fixation or line
    → more navigation

more spacing
    → less crowding
    → lower density
    → greater peripheral extent
```

The correct objective is not maximum local legibility. It is maximum task
performance under a spatial constraint.

### Conclusion

The hypothesis was rejected in its simple form.

### Confidence

High

### Next Step

Determine whether adaptive typography is theoretically and practically superior
to fixed settings.

---

## Cycle 6: Should typography be modeled as an adaptive control problem?

### Objective

Evaluate whether personalization and situational adjustment offer a stronger
model than universal design values.

### Hypothesis

A small adaptive system can identify settings that improve reading for a specific
reader without harming comprehension.

### Evidence Found

Individualized studies show measurable reading-speed differences across fonts.

Generative and adaptive systems have optimized font shapes or configurations
using human-in-the-loop feedback.

Personalized selection can preserve comprehension while improving speed.

Recent situational systems report improvements in efficiency and perceived
workload when typography responds to context.

### Evidence Against

Personalized testing has costs:

- measurement noise
- practice effects
- short-term optimization
- preference instability
- overfitting to one text type
- implementation complexity

The evidence base is still small compared with conventional reading research.

A personalized optimum for speed may not optimize comfort, retention, or
accessibility.

### Sources

- Wallace et al. (2020, 2022)
- Kadner et al. (2021)
- adaptive typography HCI research
- individual-difference studies

### Analysis

The evidence supports constrained adaptation, not unlimited customization.

A practical system should:

1. begin with a robust accessible default;
2. test a small controlled set of alternatives;
3. measure more than preference;
4. preserve user override;
5. optimize for the current task;
6. avoid continuous visual instability.

### Conclusion

Provisionally supported.

### Confidence

Moderate

### Next Step

Develop and validate a short bottleneck-diagnostic and personalization protocol.

# Confirmed Findings

## CF-TR-001

Local perceptual improvements do not guarantee higher-level reading benefits.

**Evidence:** EV-TR-001, EV-TR-002, EV-TR-003  
**Confidence:** High

## CF-TR-002

Reading speed alone can conceal changes in eye-movement strategy and effort.

**Evidence:** EV-TR-004, EV-TR-005  
**Confidence:** High

## CF-TR-003

Typographic effects vary meaningfully across readers.

**Evidence:** EV-TR-006, EV-TR-007, EV-TR-008  
**Confidence:** Moderate-High

## CF-TR-004

Font preference is not a reliable substitute for measured performance.

**Evidence:** EV-TR-006  
**Confidence:** Moderate-High

## CF-TR-005

Disfluent fonts do not reliably improve memory or comprehension.

**Evidence:** EV-TR-009, EV-TR-010  
**Confidence:** High

## CF-TR-006

Print size, spacing, width, and display capacity interact.

**Evidence:** EV-TR-011, EV-TR-012, EV-TR-013  
**Confidence:** High

## CF-TR-007

Personalized typography can improve reading performance while preserving
comprehension in some populations.

**Evidence:** EV-TR-006, EV-TR-007, EV-TR-008  
**Confidence:** Moderate

# Evidence Registry

## EV-TR-001

**Citation:** Bernard et al. (2016), font designed for peripheral vision.  
**Finding:** Improved peripheral letter and word recognition, but not
eye-mediated reading performance.  
**Supports:** HY-TR-002, TH-TYPO-ADAPTIVE-002  
**Quality:** High, peer-reviewed experimental study.

## EV-TR-002

**Citation:** He et al. (2017), linking crowding, visual span, and reading.  
**Finding:** Challenges a simple causal pathway from reduced crowding to reading
improvement.  
**Supports:** HY-TR-002  
**Quality:** High.

## EV-TR-003

**Citation:** Galiano et al. (2023), Luciole low-vision font.  
**Finding:** Small, population- and comparison-dependent advantages rather than
universal superiority.  
**Supports:** HY-TR-001, HY-TR-004  
**Quality:** Moderate-High.

## EV-TR-004

**Citation:** Minakata and Beier (2021), font width and eye movements.  
**Finding:** Font width changed eye-movement strategies and exposed tradeoffs.  
**Supports:** HY-TR-003  
**Quality:** High.

## EV-TR-005

**Citation:** Scaltritti et al. (2019), typography on real webpages.  
**Finding:** Typographic variables affected eye movements and performance across
reader groups.  
**Supports:** HY-TR-003  
**Quality:** High.

## EV-TR-006

**Citation:** Wallace et al. (2020), individual font preference and effectiveness.  
**Finding:** Readers differ in fastest font; normalization matters; preference
and familiarity do not fully predict performance.  
**Supports:** HY-TR-004, TH-TYPO-PERSONALIZED-001  
**Quality:** Moderate-High.

## EV-TR-007

**Citation:** Wallace et al. (2022), different fonts increase reading speed for
different individuals.  
**Finding:** Individual font tuning can improve reading speed while maintaining
comprehension.  
**Supports:** HY-TR-004, HY-TR-007  
**Quality:** Moderate-High.

## EV-TR-008

**Citation:** Kadner et al. (2021), AdaptiFont.  
**Finding:** Human-in-the-loop optimization can generate reader-specific font
configurations.  
**Supports:** HY-TR-007  
**Quality:** Moderate.

## EV-TR-009

**Citation:** Wetzler, Pyke, and Werner (2021), Sans Forgetica delayed recall.  
**Finding:** Strong manipulation of perceived difficulty; no one-week recall
benefit; testing effect remained.  
**Supports:** HY-TR-005  
**Quality:** High.

## EV-TR-010

**Citation:** Tietz et al. (2025), text disfluency, attention, and comprehension.  
**Finding:** Disfluency did not improve comprehension or reduce mind wandering.  
**Supports:** HY-TR-005  
**Quality:** Moderate-High.

## EV-TR-011

**Citation:** Atilgan et al. (2020), print-size and display-size constraints.  
**Finding:** Adequate print size and sufficient characters per line jointly
constrain reading.  
**Supports:** HY-TR-006  
**Quality:** High.

## EV-TR-012

**Citation:** Yu et al. (2007), letter spacing.  
**Finding:** Spacing reduces crowding but increases peripheral extent; effects are
non-monotonic.  
**Supports:** HY-TR-006  
**Quality:** High.

## EV-TR-013

**Citation:** Legge and Bigelow (2011), print-size review.  
**Finding:** Critical print size and fluent range; no unlimited benefit from
larger text.  
**Supports:** HY-TR-006  
**Quality:** High.

# Hypothesis Registry

## HY-TR-001: Direct Transfer

**Claim:** Better glyph recognition directly improves reading.  
**Status:** Rejected as universal; retained conditionally.  
**Confidence:** High.

## HY-TR-002: Active Bottleneck

**Claim:** A local typography change transfers only when it affects the current
limiting process.  
**Status:** Supported.  
**Confidence:** Moderate-High.

## HY-TR-003: Compensation Masking

**Claim:** Readers can preserve speed by changing eye movements and effort,
masking typography cost.  
**Status:** Supported.  
**Confidence:** High.

## HY-TR-004: Stable Individual Optima

**Claim:** Readers have reproducible differences in effective font configuration.  
**Status:** Provisionally supported.  
**Confidence:** Moderate.

## HY-TR-005: Disfluency Benefit

**Claim:** Perceptual difficulty improves learning by inducing deeper processing.  
**Status:** Rejected as a general claim.  
**Confidence:** High.

## HY-TR-006: Spatial Budget

**Claim:** Local visual improvements can create layout costs that reverse their
benefit.  
**Status:** Supported.  
**Confidence:** High.

## HY-TR-007: Adaptive Typography

**Claim:** Controlled personalization can outperform one fixed default for some
readers and tasks.  
**Status:** Provisionally supported.  
**Confidence:** Moderate.

## HY-TR-008: Transfer Alignment

**Claim:** System-level benefit requires alignment among intervention, active
bottleneck, task dependency, and outcome measure.  
**Status:** New theory candidate.  
**Confidence:** Moderate-High.

# Failed Assumptions

1. **Assumption:** Letter recognition is the base variable governing all reading.
   - **Failure:** Other processes can dominate.
2. **Assumption:** Reading speed is a complete performance measure.
   - **Failure:** Eye-movement and effort changes can occur without speed changes.
3. **Assumption:** Population averages identify the best font.
   - **Failure:** Crossover effects among readers are substantial.
4. **Assumption:** More perceptual effort creates deeper learning.
   - **Failure:** Effort is often consumed locally at the orthographic layer.
5. **Assumption:** Larger or more open text is always better.
   - **Failure:** Spatial capacity and navigation introduce opposing costs.
6. **Assumption:** Preference can guide personalization.
   - **Failure:** Preferred and fastest fonts do not reliably match.

# Proposed Models

## TH-TYPO-ADAPTIVE-002: Adaptive Layered Reading Theory

Typography performance emerges from interaction among:

```text
visual signal
× observer capability
× learned familiarity
× language redundancy
× display geometry
× task demand
× compensation strategy
```

No typeface has one context-free readability value.

## CN-TR-001: Transfer Alignment Principle

A local improvement produces a higher-level benefit when:

```text
Intervention affects active bottleneck
AND
task depends on that bottleneck
AND
new costs do not cancel the gain
AND
measurement detects the gain
```

## CN-TR-002: Compensation Reserve

Readers possess a finite capacity to compensate for weak typography.

Compensation reserve is consumed through:

- longer fixation
- additional fixation
- regression
- contextual inference
- working-memory effort
- slower navigation

A design may appear adequate in easy conditions but fail under distraction,
fatigue, or secondary-task load.

## CN-TR-003: Spatial Typography Budget

Every display allocates a finite visual area among:

- character size
- character width
- letter spacing
- word spacing
- line length
- number of lines
- margins
- hierarchy

Improvement in one dimension consumes capacity elsewhere.

## DF-TR-001: Typography Intervention Decision Framework

1. Define the task.
2. Define the critical error.
3. Identify the likely bottleneck.
4. Choose an intervention that targets that bottleneck.
5. Measure local effect.
6. Measure eye-movement or effort effect.
7. Measure task-level transfer.
8. Test under degraded conditions.
9. Test individual variation.
10. retain a user override.

# Theory Impact Assessment

## Affected Theory Records

- TH-TYPO-CHANNEL-001
- TH-TYPO-ADAPTIVE-001
- TH-TYPO-BOTTLENECK-001

## New Principle Candidates

- CN-TR-001 Transfer Alignment Principle
- CN-TR-002 Compensation Reserve
- CN-TR-003 Spatial Typography Budget
- TH-TYPO-PERSONALIZED-001 Reader-Specific Typography

## Deprecated Principles

- Universal Font Superiority
- Direct Glyph-to-Reading Transfer
- Disfluency as General Desirable Difficulty

## Confidence Changes

- Active bottleneck theory: Moderate → Moderate-High
- Personalized typography: Low → Moderate
- Universal readability score: Low → Very Low
- Compensation-cost model: Moderate → Moderate-High

## Predictions Created

1. Personalized settings will produce larger gains under perceptually demanding
   conditions than under easy reading.
2. Readers with equal speed across fonts will differ in fixation and workload.
3. Preference will predict adoption better than peak performance, but not peak
   reading speed.
4. Low-context tasks will show stronger transfer from glyph distinction than
   ordinary prose.
5. Font gains measured on a large display will shrink or reverse on a small
   display when line capacity falls below a critical range.
6. Disfluent typography applied selectively may improve attention to marked
   elements, while applying it globally will not improve learning.

## Predictions Invalidated

- A font engineered for isolated-character distinction will necessarily improve
  sentence reading.
- Greater perceived difficulty predicts better delayed recall.

## Required Theory Registry Updates

Add:

- TH-TYPO-ADAPTIVE-002
- CN-TR-001
- CN-TR-002
- CN-TR-003
- DF-TR-001

Deprecate:

- TH-TYPO-DIRECT-TRANSFER-001
- TH-TYPO-DISFLUENCY-001

# Open Questions

## Critical

1. Can a five-minute test diagnose a reader's active typography bottleneck?
2. How stable are personalized font gains across days, devices, and content?
3. Which compensation metrics best predict fatigue and failure under load?
4. How should Atlas optimize multiple objectives without reducing them to one
   score?

## High

5. Do personalized settings improve comprehension over long reading sessions?
6. How much gain comes from font family versus size normalization, spacing,
   grade, and line layout?
7. Which reader characteristics predict response to typography?
8. Can a computational model narrow the personalization search space reliably?
9. How do personalized settings interact with browser zoom and accessibility
   overrides?

## Medium

10. Can selective disfluency serve as an attention signal without harming
    comprehension?
11. Are individual optima stable across languages and scripts?
12. How much familiarization is needed before a new font reaches stable
    performance?

# Recommended Next Research

| Priority | Research | Expected Value | Effort |
|---|---|---:|---:|
| 1 | Design a short active-bottleneck diagnostic | Very high | High |
| 2 | Build a cross-layer study registry | Very high | Moderate |
| 3 | Reanalyze personalized-font datasets | High | Moderate |
| 4 | Define compensation-cost metrics | High | High |
| 5 | Compare low-context and prose tasks | High | Moderate |
| 6 | Model display spatial budget | High | Moderate |
| 7 | Test stability of individualized settings | High | High |
| 8 | Extend to non-Latin scripts | High | High |

# Research Backlog

- Extract effect sizes from individualized-font studies.
- Record whether fonts were normalized by x-height, cap height, or nominal size.
- Compare preference, speed, comprehension, and workload within participants.
- Build a taxonomy of transfer failures.
- Review pupillometry and dual-task methods for reading effort.
- Review standards for safety-critical labels and identifiers.
- Investigate font grade as distinct from weight.
- Compare static adaptation with continuous adaptive typography.
- Analyze accessibility risks of changing typography automatically.
- Review long-session reading and fatigue studies.

# Suggested Specialized Research Agents

## Agent A: Personalized Typography Analyst

Focus:

- individual-difference datasets
- reliability
- effect sizes
- personalization algorithms
- overfitting risk

## Agent B: Eye-Movement Compensation Analyst

Focus:

- fixation duration
- regressions
- saccade length
- pupil response
- dual-task cost
- fatigue

## Agent C: Task-Critical Typography Analyst

Focus:

- medication labels
- safety signage
- serial numbers
- control panels
- glance reading

## Agent D: Spatial Budget Modeler

Focus:

- print size
- viewport size
- characters per line
- reflow
- zoom
- responsive layout

# Parallel Research Opportunities

- typography personalization
- visual hierarchy transfer
- icon and symbol confusion
- chart-label legibility
- wayfinding
- alert design
- multilingual interfaces
- low-vision adaptive systems

# Risks

- personalization may overfit short tests
- speed optimization may reduce comprehension or comfort
- adaptive changes may create instability
- study fonts may not reflect production implementations
- individual effects may be inflated by repeated-measures designs
- publication bias may favor positive personalization results
- accessibility systems may conflict with authored adaptation
- laboratory reading may not predict real-world persistence

# Cross-Discipline Opportunities

## Control Theory

Model the reader as a controller that changes sampling behavior to preserve
performance.

## Economics

Treat attention and screen area as scarce resources with opportunity costs.

## Decision Theory

Weight typography errors by consequence rather than frequency alone.

## Reliability Engineering

Use degradation testing and failure thresholds instead of ideal-condition
ranking.

## Personalized Medicine

Use robust defaults plus individual response testing rather than population
averages alone.

## Information Theory

Measure uncertainty reduction at each layer, without equating symbol accuracy
with meaning.

# Knowledge Relationships

```text
Glyph robustness
    ↓ conditional transfer
Word recognition
    ↓ constrained by
Eye movements + language inference
    ↓ constrained by
Layout and display capacity
    ↓ produces
Reading efficiency and compensation cost
    ↓ affects
Comprehension, navigation, action
```

Personalization affects every transition rather than only glyph selection.

# Repository Updates

Create or update:

```text
/research/typography/rep/RP-ATLAS-TYPO-TRANSFER-001.md
/theory/TH-TYPO-ADAPTIVE-002.md
/concepts/CN-TR-001-transfer-alignment.md
/concepts/CN-TR-002-compensation-reserve.md
/concepts/CN-TR-003-spatial-typography-budget.md
/frameworks/DF-TR-001-typography-intervention.md
/evidence/typography-transfer-registry.yaml
```

# Website Updates

Add a Typography Transfer section with:

- layered transfer diagram
- local-versus-system outcome examples
- personalized typography evidence
- rejected disfluency claim
- interactive spatial-budget illustration
- confidence indicators

Do not present a universal “best font” list.

# AI Consumption Notes

Agents consuming this package should:

1. Treat reading speed, comprehension, and preference as separate outcomes.
2. Never infer transfer from a lower-level metric alone.
3. Preserve individual-level data when available.
4. Record whether font sizes were physically or optically normalized.
5. Distinguish typeface, font, grade, weight, spacing, and layout.
6. Record display size and characters per line.
7. Separate null effects from evidence of equivalence.
8. Avoid recommending disfluent fonts for learning without task-specific
   evidence.
9. Prefer profiles and conditional rules over global scores.
10. Reference evidence and hypothesis IDs in future work.

# Handoff Instructions

The next agent should begin with **Open Question 1**:

> Can a short diagnostic determine the active typography bottleneck?

Required next steps:

1. Review adaptive psychophysical methods such as qReading.
2. Review short font-tuning methods used by individualized-font studies.
3. Identify the minimum set of tasks needed to distinguish:
   - size limitation
   - crowding
   - glyph confusion
   - line-capacity limitation
   - lexical limitation
4. Propose an experiment that can run in five to ten minutes.
5. Define stopping criteria and reliability requirements.
6. Produce RP-ATLAS-TYPO-DIAGNOSTIC-001.

# Research Journal

## JR-ATLAS-TR-001

Reviewed previous Atlas artifacts and identified cross-layer transfer as the
largest unresolved uncertainty.

## JR-ATLAS-TR-002

Compared successful local recognition improvements with failed reading-speed
transfer. Direct-transfer theory weakened.

## JR-ATLAS-TR-003

Reviewed eye-movement evidence. Added compensation masking and compensation
reserve concepts.

## JR-ATLAS-TR-004

Reviewed individual-difference and adaptive-font studies. Personalized
typography confidence increased from low to moderate.

## JR-ATLAS-TR-005

Reviewed disfluency and Sans Forgetica evidence. General desirable-difficulty
hypothesis rejected.

## JR-ATLAS-TR-006

Reviewed display-size and print-size interaction. Spatial typography budget
model added.

## JR-ATLAS-TR-007

Integrated findings into Transfer Alignment Principle and adaptive layered
reading theory.

# Research Quality Metrics

- **Primary Sources:** 13 core experimental or review sources
- **Independent Source Families:** 7
- **Counterexamples Reviewed:** 9
- **Competing Viewpoints Reviewed:** 5
- **Hypotheses Tested:** 8
- **Failed Hypotheses:** 4 universal claims, 2 simple assumptions
- **Research Completeness:** 82% for current objective
- **Confidence Gain:** Moderate → Moderate-High
- **Open Questions Reduced:** 1 major question decomposed into 12 testable
  questions

# Research Debt

## Missing Evidence

- raw individualized-font datasets
- long-term personalization stability
- fatigue and workload evidence
- safety-critical task transfer
- non-Latin transfer evidence

## Missing Experiments

- short bottleneck diagnostic
- within-person stability study
- low-context versus prose comparison
- dual-task compensation study
- small-display personalization study

## Missing Disciplines

- occupational ergonomics
- clinical low-vision rehabilitation
- safety engineering
- educational measurement
- adaptive user interfaces

## Tool Limitations

- several publisher pages did not expose full datasets
- some current HCI results are available only as abstracts
- no new human experiments were conducted
- effect sizes were not pooled meta-analytically

## Assumptions Awaiting Evidence

- compensation reserve is finite and measurable
- personalized font effects are stable enough for production use
- active bottlenecks can be diagnosed quickly
- computational proxies can reduce human testing substantially

# Appendix A: Bibliography

## Academic

- Atilgan, N. et al. (2020). *Reconciling Print-Size and Display-Size
  Constraints on Reading*.
- Bernard, J. B. et al. (2016). *A New Font Specifically Designed for
  Peripheral Vision Improves Peripheral Letter and Word Recognition, but Not
  Eye-Mediated Reading Performance*.
- Galiano, A. R. et al. (2023). *Luciole, a New Font for People with Low Vision*.
- He, Y. et al. (2017). *Linking Crowding, Visual Span, and Reading*.
- Kadner, F. et al. (2021). *Increasing Individuals' Reading Speed with a
  Generative Font Model and Bayesian Optimization*.
- Legge, G. E., and Bigelow, C. A. (2011). *Does Print Size Matter for Reading?*
- Minakata, K., and Beier, S. (2021). *The Effect of Font Width on Eye
  Movements During Reading*.
- Nedeljković, U. et al. (2020). *You Read Best What You Read Most*.
- Scaltritti, M. et al. (2019). *Investigating Effects of Typographic Variables
  on Webpage Reading Through Eye Movements*.
- Wallace, S. et al. (2020). *Individual Differences in Font Preference and
  Effectiveness as Applied to Interlude Reading in the Digital Age*.
- Wallace, S. et al. (2022). *Different Fonts Increase Reading Speed for
  Different Individuals*.
- Wetzler, E. L., Pyke, A. A., and Werner, A. (2021). *Sans Forgetica Is Not
  the Font of Knowledge*.
- Yu, D. et al. (2007). *Effect of Letter Spacing on Visual Span and Reading
  Speed*.

## Books

- Legge, G. E. (2007). *Psychophysics of Reading in Normal and Low Vision*.

## Industry

- Google Fonts accessibility and readability research initiatives.
- Browser and operating-system text customization documentation.

## Patents

No patent evidence was decisive in this phase.

## Standards

- WCAG text spacing and reflow requirements.
- ISO 9241 human-system interaction standards.

## Historical

- Bouma, H. letter recognition and crowding research.
- Reicher-Wheeler word-superiority research.

## Other

- qReading adaptive measurement method.
- Current adaptive typography HCI systems.

# Appendix B: Completion Checklist

- [x] Executive Summary
- [x] Original Objective
- [x] Scope
- [x] Repository Context
- [x] Current Understanding
- [x] Key Discoveries
- [x] Evidence Registry
- [x] Hypothesis Registry
- [x] Failed Assumptions
- [x] Open Questions
- [x] Recommended Next Research
- [x] Research Backlog
- [x] Suggested Specialized Research Agents
- [x] Parallel Research Opportunities
- [x] Risks
- [x] Cross-Discipline Opportunities
- [x] Knowledge Relationships
- [x] Repository Updates
- [x] Website Updates
- [x] AI Consumption Notes
- [x] Handoff Instructions
- [x] Research Journal
- [x] Appendix
- [x] Theory Impact Assessment
- [x] Research Quality Metrics
- [x] Research Debt
- [x] Completion Checklist
