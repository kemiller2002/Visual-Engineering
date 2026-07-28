---
identifier: RP-ATLAS-COLOR-004
title: "Albert Munsell vs. Modern Perceptual Color Spaces"
research_area: "Project Atlas / Perceptual Measurement"
discipline:
  - Color Science
  - Psychophysics
  - Design Systems
author_agent: "GPT-5.6 Thinking"
version: 1.0
date: 2026-07-21
confidence: "High on architectural conclusions; moderate on comparative performance outside tested datasets"
completion: 0.88
priority: Critical
status: "Research Execution Package"
related_projects:
  - Project Atlas
  - Composition Science
related_documents:
  - CLR-MMS-001 Chevreul
  - CLR-MMS-002 Albers
  - CLR-MMS-003 Itten
tags:
  - Munsell
  - CIELAB
  - CAM16-UCS
  - Oklab
  - OKLCH
  - color-difference
  - color-appearance
  - design-tokens
keywords:
  - perceptual uniformity
  - hue
  - value
  - chroma
  - adaptation
  - gamut
llm_ingest: true
machine_readable: true
project: project-atlas
purposes:
  - integrate
  - verify
audiences:
  - executive
  - practitioner
  - researcher
---

# Executive Summary

Albert H. Munsell's enduring contribution was not a perfect color solid. It was
the decision to separate color description into three ordered attributes:

- hue
- value
- chroma

and to space physical samples by visual judgment rather than by geometric or
pigment theory alone.

That move survives in nearly every later perceptual color system.

The investigation produced five major conclusions.

1. **Munsell's conceptual decomposition survives.** Modern spaces still
   separate a lightness-like coordinate from two chromatic dimensions, often
   exposed cylindrically as lightness, chroma, and hue.

2. **The irregular color solid is a discovery, not a defect.** Different hues
   and lightness levels support different attainable chroma. Any neat cylinder
   that hides this is describing coordinates, not the realizable color gamut.

3. **Perceptual uniformity is local, conditional, and task-bound.** No evaluated
   space is uniformly best for every observer, gamut, viewing condition,
   difference scale, interpolation problem, or rendering task.

4. **Color appearance and color difference are separate problems.** CIELAB and
   Oklab are convenient coordinate spaces. CAM16 models viewing-condition
   effects and CAM16-UCS adds a more uniform difference space. These should not
   be treated as interchangeable.

5. **Atlas should not select one universal color space.** It should maintain a
   canonical physical representation and derive task-specific perceptual views.

The strongest architectural recommendation is:

```text
Measured stimulus
    ↓
canonical tristimulus / spectral record
    ↓
viewing-condition model
    ↓
task-specific perceptual space
    ↓
decision metric
    ↓
validated design use
```

For web design, Oklab/OKLCH is an excellent authoring and interpolation layer and
is standardized in CSS Color 4. It should not be promoted as the sole scientific
distance metric. CAM16-UCS currently has stronger evidence for general
color-difference prediction across diverse and wide-gamut datasets, but is more
complex and depends on explicit viewing conditions. CIELAB remains important
for interoperability and standards, though its nonuniformities are well known.

---

# Original Objective

Determine which parts of Munsell survived modern color science and build the
first Atlas Perceptual Measurement Layer.

---

# Research State Snapshot

## Theory Version

Atlas Color Theory 0.4

## Highest Confidence Areas

- color appearance is relational
- hue, lightness/value, and chroma are useful separable descriptors
- no color coordinate is fully meaningful without a reference white and viewing
  assumptions
- numerical distance depends on the chosen space and metric
- area and context cannot be inferred from a color coordinate alone

## Lowest Confidence Areas

- comparative performance of spaces for interface-scale suprathreshold
  differences
- dark-mode appearance prediction
- wide-gamut accent weighting
- color-area influence
- observer-specific corrections

## Largest Remaining Unknown

Which measurement stack best predicts functional UI outcomes rather than
laboratory color-pair judgments?

## Recently Invalidated Ideas

- one perceptual space can serve every Atlas purpose
- cylindrical coordinates imply a cylindrical realizable gamut
- equal chroma values are guaranteed to look equally colorful across spaces and
  conditions
- Euclidean distance in any “perceptual” space is automatically a reliable
  perceptual difference

---

# Research Log

## JR-ATLAS-COLOR-041 — What problem did Munsell solve?

### Objective

Reconstruct Munsell's actual contribution without importing claims from later
renotations.

### Hypothesis

Munsell created a mathematically uniform color space comparable to a modern
analytical color model.

### Evidence Found

Munsell's original work explicitly required hue, value, and chroma to specify a
color and used physical samples, visual comparison, photometric measurement,
and rotating mixture devices. His atlas represented attainable pigment colors
as an irregular tree rather than forcing all hues into equal radial limits.

### Evidence Against

The original physical atlas was not an analytically complete or perfectly
uniform space. The Optical Society of America later conducted large visual
spacing studies and published the 1943 Munsell renotation. Modern numerical use
usually refers to this later empirical reconstruction rather than Munsell's
first samples.

### Conclusion

Munsell established the architecture and experimental direction. Later
committees improved the coordinate realization.

### Confidence

High

---

## JR-ATLAS-COLOR-042 — Are hue, value, and chroma independent?

### Objective

Test whether the three attributes are independent in perception and production.

### Hypothesis

Each dimension can be changed freely while the others remain fixed.

### Evidence Found

The attributes are operationally separable. Constant-value and constant-chroma
sample series can be constructed over bounded regions.

### Evidence Against

The attainable range is conditional. Maximum chroma varies sharply with hue,
value, medium, illuminant, and device gamut. Perceived hue can also shift with
lightness or chroma, and appearance depends on adaptation and surround.

### Conclusion

The dimensions are useful coordinates, not independent physical generators.

### Confidence

High

---

## JR-ATLAS-COLOR-043 — Is perceptual uniformity globally possible?

### Objective

Determine whether equal coordinate distance can equal equal perceived
difference everywhere.

### Hypothesis

A single three-dimensional Euclidean space can be globally uniform.

### Evidence Found

Munsell renotation, CIELAB, CAM16-UCS, Oklab, and newer spaces all improve
uniformity over raw tristimulus coordinates for selected data and tasks.

### Evidence Against

Successive spaces and increasingly complex color-difference equations exist
because residual nonuniformities remain. Performance varies with:

- small versus large differences
- surface versus emissive color
- luminance level
- gamut
- hue region
- observer
- reference white
- adaptation
- dataset composition

Wide-gamut evaluations continue to find model-dependent errors. Recent studies
often favor CAM16-UCS or corrected variants for broad difference prediction,
while Oklab prioritizes simplicity, hue behavior, interpolation, and image or
design workflows.

### Conclusion

Global uniformity should be treated as an approximation target, not a solved
property.

### Confidence

High

---

## JR-ATLAS-COLOR-044 — CIELAB

### Objective

Determine CIELAB's proper role.

### Evidence Found

CIE L*a*b* is an international standard that provides lightness, chromatic
coordinates, cylindrical chroma and hue correlates, and standardized distance
methods. It remains widely used for materials, manufacturing, and exchange.

### Evidence Against

CIELAB is not uniformly perceptual across its full volume. Simple Euclidean
Delta E 1976 performs poorly in known regions, motivating CMC, CIE94, and
CIEDE2000. Hue linearity, especially in blue regions, and high-chroma behavior
remain problematic.

### Conclusion

Use CIELAB for standards compatibility and legacy measurement, not as Atlas's
universal perceptual truth.

### Confidence

High

---

## JR-ATLAS-COLOR-045 — CAM16 and CAM16-UCS

### Objective

Separate appearance modeling from uniform color-space use.

### Evidence Found

CAM16 predicts appearance correlates under explicit viewing conditions,
including adaptation-related inputs. CAM16-UCS transforms CAM16 correlates for
more uniform Euclidean difference estimates. Comparative studies report strong
overall performance, including wide-color-gamut conditions.

### Evidence Against

The model is more complex, depends on correctly specified viewing conditions,
and does not solve every attribute equally. Published work notes hue-linearity
issues, especially in blue, and ongoing HDR/WCG revisions show that no final
model exists.

### Conclusion

CAM16 is the preferred Atlas layer when viewing-condition changes matter.
CAM16-UCS is the strongest current default candidate for general research-grade
difference analysis, subject to dataset and condition checks.

### Confidence

Moderate to high

---

## JR-ATLAS-COLOR-046 — Oklab and OKLCH

### Objective

Determine whether Oklab should become the Atlas design-system space.

### Evidence Found

Oklab was designed as a simple, numerically stable perceptual space with good
lightness, chroma, and hue behavior. Its fit used modern appearance data,
including CAM16-derived relationships. Oklab and OKLCH are included in CSS Color
4, making them directly useful for web authoring, interpolation, palette
generation, and gamut-aware tokens.

### Evidence Against

Oklab is not an appearance model and has no explicit surround or adaptation
parameters. Its published validation is less comprehensive than major
color-difference standards. Current research continues to propose corrections,
and recent comparative work reports weaker raw Oklab distance prediction than
CIEDE2000 or CAM16-UCS on some suprathreshold datasets.

### Conclusion

Use OKLCH as the default web-authoring coordinate, not as the only validation
metric.

### Confidence

High for workflow suitability; moderate for general perceptual-distance claims

---

## JR-ATLAS-COLOR-047 — Does Atlas need one canonical space?

### Objective

Choose a single color space for Atlas.

### Hypothesis

One space can simplify the system without materially reducing validity.

### Evidence Against

Different operations require incompatible properties:

- measurement requires device-independent physical reference
- appearance prediction requires viewing conditions
- color difference requires empirical uniformity
- interpolation requires smooth paths and stable hue
- accessibility requires luminance and task-specific thresholds
- rendering requires a target gamut and transfer function
- material matching may require spectra and illuminant analysis

### Conclusion

Hypothesis rejected.

Atlas requires a layered measurement architecture.

### Confidence

High

---

# Key Discoveries

## KD-001 — Munsell's surviving contribution is dimensional discipline

The lasting principle is not the exact sample coordinates. It is the rule that
color descriptions must separate hue, lightness/value, and chromatic strength.

## KD-002 — Uniformity is a declared optimization

A space should never be called perceptually uniform without naming:

- the dataset
- difference magnitude
- viewing conditions
- observer assumptions
- metric
- medium
- gamut

## KD-003 — A color space is not a color appearance model

Coordinate organization and viewing-condition prediction are separate
capabilities.

## KD-004 — A cylindrical interface does not imply a cylindrical gamut

OKLCH, LCh, and Munsell notation are useful interfaces, but realizable chroma
limits remain irregular.

## KD-005 — The best space depends on the decision

| Decision | Preferred starting point |
|---|---|
| Web authoring and interpolation | OKLCH / Oklab |
| Standards exchange and material workflows | CIELAB plus appropriate Delta E |
| Viewing-condition transformation | CAM16 |
| General research-grade difference | CAM16-UCS, validated for the condition |
| Accessibility text contrast | Relative luminance plus applicable standard |
| Spectral metamerism or illuminant change | Spectral data, not three coordinates |
| Historical visual ordering | Munsell renotation |

---

# Evidence Registry

## EV-ATLAS-COLOR-101

**Source:** Albert H. Munsell, *Atlas of the Munsell Color System*.

**Finding:** Munsell required hue, value, and chroma and explicitly represented
unequal attainable chroma across the color solid.

**Supports:** TH-ATLAS-COLOR-011, TH-ATLAS-COLOR-012

**Grade:** Historical primary source

## EV-ATLAS-COLOR-102

**Source:** Newhall, Nickerson, and Judd, OSA Munsell renotation work.

**Finding:** Later visual experiments revised the spacing and numerical
coordinates of the Munsell system.

**Supports:** TH-ATLAS-COLOR-013

**Grade:** Primary psychophysical research

## EV-ATLAS-COLOR-103

**Source:** CIE, Colorimetry Part 4: CIE 1976 L*a*b*.

**Finding:** CIELAB formally specifies lightness, chroma, hue correlates, and
distance procedures.

**Supports:** TH-ATLAS-COLOR-014

**Grade:** International standard

## EV-ATLAS-COLOR-104

**Source:** Li et al., “Comprehensive color solutions: CAM16, CAT16, and
CAM16-UCS.”

**Finding:** CAM16 offers appearance prediction and CAM16-UCS a corresponding
uniform space for difference evaluation.

**Supports:** TH-ATLAS-COLOR-015

**Grade:** Primary peer-reviewed research

## EV-ATLAS-COLOR-105

**Source:** Ottosson, “A perceptual color space for image processing.”

**Finding:** Oklab was optimized for simple and stable lightness, chroma, and
hue behavior and compared against Munsell and appearance-model data.

**Supports:** TH-ATLAS-COLOR-016

**Grade:** Original technical publication; not equivalent to a standard

## EV-ATLAS-COLOR-106

**Source:** W3C CSS Color Module Level 4.

**Finding:** CSS supports `oklab()` and `oklch()` as authoring formats.

**Supports:** DF-ATLAS-COLOR-004

**Grade:** Web standard

## EV-ATLAS-COLOR-107

**Source:** Basova et al., wide-gamut color-difference evaluation.

**Finding:** CAM16-UCS variants showed strong versatility under WCG and high
luminance conditions.

**Supports:** TH-ATLAS-COLOR-015

**Challenges:** universal Oklab-distance use

**Grade:** Peer-reviewed comparative research

---

# Hypothesis Registry

## HY-ATLAS-COLOR-031

**Hypothesis:** Munsell's three dimensions remain the most useful human-facing
decomposition.

**Status:** Supported with terminology and condition limits.

**Confidence:** High

## HY-ATLAS-COLOR-032

**Hypothesis:** One perceptually uniform space can support all Atlas decisions.

**Status:** Rejected.

**Confidence:** High

## HY-ATLAS-COLOR-033

**Hypothesis:** Oklab is the best default space for all design-system color
operations.

**Status:** Rejected in strong form.

**Revised:** Oklab/OKLCH is the preferred web-authoring view but should be
paired with other validation models.

**Confidence:** High

## HY-ATLAS-COLOR-034

**Hypothesis:** CAM16-UCS is currently the best general research default for
color-difference work.

**Status:** Provisionally supported.

**Limits:** Not universal; requires condition-appropriate validation.

**Confidence:** Moderate

## HY-ATLAS-COLOR-035

**Hypothesis:** Physical or colorimetric source data should be retained even
when authoring uses perceptual coordinates.

**Status:** Supported.

**Confidence:** High

---

# Failed Assumptions

1. “Perceptual” means uniformly perceptual everywhere.
2. Hue angle is stable across spaces.
3. Equal chroma values are comparable across spaces.
4. A design token can be permanently stored in only one derived space.
5. A color-difference metric predicts hierarchy, preference, or accessibility.
6. Display RGB values are adequate scientific source records.
7. Appearance under one white point transfers automatically to another.
8. Gamut clipping is only a technical rendering concern rather than a
   perceptual transformation.

---

# Proposed Theory Updates

## TH-ATLAS-COLOR-011 — Dimensional Color Description

A practical color description must separate lightness, chromatic direction, and
chromatic magnitude.

**Confidence:** High

## TH-ATLAS-COLOR-012 — Irregular Realizable Gamut

The maximum realizable chroma is conditional on hue, lightness, medium,
illuminant, and output device.

**Confidence:** High

## TH-ATLAS-COLOR-013 — Conditional Uniformity

Perceptual uniformity is always an approximation bounded by observer, stimulus,
task, gamut, viewing condition, and difference scale.

**Confidence:** High

## TH-ATLAS-COLOR-014 — Measurement-Appearance Separation

A device-independent colorimetric coordinate does not by itself predict color
appearance.

**Confidence:** High

## TH-ATLAS-COLOR-015 — Task-Specific Space Selection

Color spaces and metrics must be selected according to the decision being made.

**Confidence:** High

## TH-ATLAS-COLOR-016 — Canonical Source Preservation

Atlas should preserve the least-derived available source representation and
generate perceptual coordinates as reproducible views.

**Confidence:** High

---

# Decision Framework

## DF-ATLAS-COLOR-004 — Color Representation Selection

Ask in order:

1. What is the medium?
2. Is the source spectral, reflective, emissive, or encoded?
3. What white point and luminance apply?
4. Are viewing conditions stable or changing?
5. Is the task matching, difference, interpolation, accessibility, appearance,
   rendering, or communication?
6. What gamut is available?
7. What observer assumptions apply?
8. Which metric has evidence for this exact problem?
9. What contextual validation remains necessary?

---

# Recommendations

## Critical

1. Adopt the Atlas Perceptual Measurement Layer defined in the companion
   document.
2. Store source RGB only with color space, transfer function, white point,
   bit depth, and alpha.
3. Store measured materials as spectra when illuminant sensitivity matters.
4. Use OKLCH for web authoring and controlled palette generation.
5. Validate important pair distances with an evidence-appropriate metric rather
   than raw OKLCH distance alone.
6. Use CAM16 when adapting between materially different viewing conditions.
7. Keep accessibility calculations separate from aesthetic color-difference
   calculations.

## High Value Research

1. Compare Oklab, CAM16-UCS, CIEDE2000, and current candidates on UI-specific
   datasets.
2. Build dark-mode and high-luminance viewing profiles.
3. Model gamut mapping as a documented perceptual operation.
4. Add observer variation and color-vision-deficiency profiles.
5. Link color coordinates to area, hierarchy, semantics, and context instead of
   treating color distance as communication distance.

---

# Research Debt

- No comprehensive UI-native psychophysical dataset was found.
- Most color-difference datasets use simplified patches rather than real
  layouts.
- Oklab's practical success exceeds the breadth of its formal validation.
- CAM16 input assumptions may be difficult to estimate in uncontrolled devices.
- Current HDR/WCG research is still evolving.
- Spectral storage is impractical for many design-system inputs.
- Color appearance models do not directly predict aesthetic harmony or
  compositional balance.

---

# Highest-Value Next Research

## RP Candidate: UI Color Difference and Functional Outcome

Collect and compare evidence for:

- perceived token spacing
- hierarchy discrimination
- status-color confusion
- dark-mode equivalence
- gamut-mapped identity
- repeated exposure
- component area
- color-vision variation

This should precede the use of any color space as a predictive design law.

---

# Bibliography

## Historical and Primary

- Munsell, Albert H. *A Color Notation*.
- Munsell, Albert H. *Atlas of the Munsell Color System*.
- Newhall, Sidney M.; Nickerson, Dorothy; Judd, Deane B. Munsell renotation
  research, 1943.

## Standards

- CIE. *Colorimetry — Part 4: CIE 1976 L*a*b* Colour Space*.
- CIE. *CIECAM16 / CAM16 colour appearance publications*.
- W3C. *CSS Color Module Level 4*.

## Academic and Technical

- Li, C. et al. “Comprehensive color solutions: CAM16, CAT16, and CAM16-UCS.”
- Safdar, M. et al. “Perceptually uniform color space for image signals
  including high dynamic range and wide gamut.”
- Basova, O. et al. “Evaluation of Color Difference Models for Wide Color
  Gamut.”
- Ottosson, Björn. “A perceptual color space for image processing.”
- Huang, Y. et al. “Towards perceptual uniformity and HDR-WCG image
  processing.”

---

# Handoff Instructions

The next agent should:

1. Treat this REP as the current Atlas measurement position.
2. Do not select a universal space without task evidence.
3. Extend rather than replace the evidence and hypothesis registries.
4. Preserve source color metadata.
5. Separate appearance, difference, rendering, accessibility, and communication
   outcomes.
6. Build the next REP around UI-native validation rather than another general
   color-space survey.

---

# Completion Checklist

- [x] Historical reconstruction
- [x] Competing spaces compared
- [x] Counterevidence reviewed
- [x] Failed assumptions documented
- [x] Theory updates proposed
- [x] Decision framework created
- [x] Research debt recorded
- [x] Executable next step defined
- [x] Companion implementation specification produced
