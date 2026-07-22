---
identifier: DF-ATLAS-COLOR-005
title: "Atlas Perceptual Measurement Layer"
project: "Project Atlas"
artifact_type: "Architecture and Decision Framework"
version: 0.1
date: 2026-07-21
status: "Proposed Canonical Foundation"
confidence: "High for layered architecture; moderate for default metric choices"
related_research_package: RP-ATLAS-COLOR-004
llm_ingest: true
machine_readable: true
---

# Purpose

Define how Project Atlas records, transforms, compares, validates, and
communicates color measurements without pretending that one color space solves
every problem.

The layer is designed to support:

- design tokens
- web components
- visual research
- accessibility
- material and architectural color
- image and display workflows
- future predictive composition models

---

# Foundational Rule

> Preserve the least-derived reliable source representation, then generate
> task-specific perceptual views with explicit assumptions.

No derived coordinate becomes the sole permanent truth.

---

# Architecture

```text
┌──────────────────────────────────────────────────────┐
│  1. Source Record                                    │
│  spectrum, XYZ, measured Lab, encoded RGB, material  │
└──────────────────────────┬───────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────┐
│  2. Physical / Colorimetric Normalization            │
│  illuminant, observer, white point, luminance, alpha │
└──────────────────────────┬───────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────┐
│  3. Viewing-Condition Profile                        │
│  surround, adapting luminance, background, medium    │
└──────────────────────────┬───────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────┐
│  4. Derived Perceptual Views                         │
│  Munsell, Lab/LCh, CAM16, CAM16-UCS, Oklab/OKLCH    │
└──────────────────────────┬───────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────┐
│  5. Task Metrics                                     │
│  ΔE, interpolation, luminance contrast, gamut loss   │
└──────────────────────────┬───────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────┐
│  6. Context Validation                               │
│  adjacency, area, hierarchy, semantics, observer     │
└──────────────────────────┬───────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────┐
│  7. Decision Record                                  │
│  accepted use, limits, failures, confidence          │
└──────────────────────────────────────────────────────┘
```

---

# Layer Definitions

## 1. Source Record

Preferred source order:

1. spectral reflectance or emission data
2. measured XYZ with measurement metadata
3. measured CIELAB with illuminant and observer
4. encoded device-independent color
5. encoded RGB with complete profile
6. unprofiled hex value

Unprofiled hex is accepted only as a low-confidence web input.

## 2. Colorimetric Normalization

Required fields when applicable:

```yaml
color_space:
transfer_function:
primaries:
white_point:
observer:
illuminant:
luminance_cd_m2:
measurement_geometry:
measurement_device:
bit_depth:
alpha:
```

## 3. Viewing-Condition Profile

```yaml
viewing_profile_id:
medium: emissive | reflective | transmissive
adapting_luminance:
background_luminance:
surround: dark | dim | average | custom
discounting_illuminant:
reference_white:
ambient_illuminance:
display_peak_luminance:
display_black_luminance:
```

Unknown values must be marked unknown, not silently defaulted.

## 4. Derived Perceptual Views

### Munsell

Use for:

- historical comparison
- material and soil references
- human-facing hue/value/chroma ordering
- comparison to classical theories

Do not use as the primary computational interchange format.

### CIELAB / CIELCh

Use for:

- standards interoperability
- legacy measurement systems
- material and print workflows
- CIEDE2000 calculations

Do not assume Euclidean Lab distance is uniformly perceptual.

### CAM16

Use for:

- appearance prediction
- adapting between viewing conditions
- explicit brightness, lightness, chroma, colorfulness, saturation, and hue
  correlates

Do not use without recording input viewing assumptions.

### CAM16-UCS

Use for:

- research-grade color-difference analysis
- wide-gamut comparison
- datasets where CAM16-UCS has demonstrated fit

Do not assume superiority for every attribute or UI task.

### Oklab / OKLCH

Use for:

- CSS authoring
- palette generation
- design-token manipulation
- gradients and interpolation
- intuitive lightness/chroma/hue controls

Do not use raw Euclidean Oklab distance as the sole validation metric for
critical color matching.

---

# Default Operation Matrix

| Operation | Default | Secondary validation |
|---|---|---|
| Web token authoring | OKLCH | gamut and context validation |
| CSS interpolation | Oklab or OKLCH, path-dependent | rendered gradient review |
| Material difference | CIELAB + CIEDE2000 | instrument and illuminant record |
| Viewing-condition change | CAM16 | representative observer test |
| General perceptual difference research | CAM16-UCS | compare against CIEDE2000 |
| Text accessibility | applicable luminance-based standard | real component testing |
| Categorical palette spacing | OKLCH initial construction | CAM16-UCS and CVD simulation |
| Historical palette reconstruction | Munsell where available | spectral or XYZ conversion |
| Cross-device identity | profile-managed XYZ/Lab pipeline | rendered device measurements |
| Gamut mapping | explicit algorithm in perceptual space | before/after difference record |

---

# Canonical Color Record

```yaml
color_id: CLR-EXAMPLE-001
name: example-accent

source:
  type: encoded-rgb
  value: "#E5484D"
  color_space: srgb
  transfer_function: srgb
  white_point: D65
  confidence: medium

derived:
  oklch:
    value: [null, null, null]
    method_version:
  cielab:
    value: [null, null, null]
    illuminant: D65
    observer: 2deg
    method_version:
  cam16:
    viewing_profile_id:
    J:
    C:
    h:
    Q:
    M:
    s:
  cam16_ucs:
    J_prime:
    a_prime:
    b_prime:

gamut:
  source_gamut: srgb
  target_gamuts:
    srgb: in-gamut
    display-p3: in-gamut

functional_roles:
  - accent

validated_contexts: []
failed_contexts: []

provenance:
  created_by:
  created_at:
  source_document:
  conversion_library:
  conversion_version:
```

---

# Color Relationship Record

A color is not validated alone.

```yaml
relationship_id: REL-COLOR-001
foreground_color_id:
background_color_id:
adjacent_color_ids: []
viewing_profile_id:
component_type:
area_ratio:
boundary:
spatial_frequency:
semantic_roles:
metrics:
  relative_luminance_ratio:
  delta_e_2000:
  delta_e_cam16_ucs:
  delta_e_oklab:
  gamut_mapping_loss:
observer_profiles:
  - standard
outcomes:
  legibility:
  discriminability:
  hierarchy:
  identity_preservation:
  aesthetic_fit:
confidence:
evidence_ids: []
```

---

# Metric Rules

## Rule PM-001

Never report “Delta E” without naming the formula and reference conditions.

## Rule PM-002

Never report “contrast” without naming the dimension and functional outcome.

## Rule PM-003

Never compare chroma values from different spaces as though they share a unit.

## Rule PM-004

Never compare hue angles from different spaces without conversion and
validation.

## Rule PM-005

Never use a color-difference score as a proxy for preference, harmony, or
meaning.

## Rule PM-006

Record gamut mapping before measuring the delivered color.

## Rule PM-007

Accessibility validation is a separate decision path from perceptual-uniformity
validation.

## Rule PM-008

Contextual appearance tests override isolated-coordinate confidence when the
final use is compositional.

---

# Confidence Model

```yaml
measurement_confidence:
  high: spectral or calibrated instrument record
  medium: profiled numerical source
  low: unprofiled encoded value

appearance_confidence:
  high: explicit viewing conditions and validated model
  medium: representative profile
  low: assumed or unknown context

functional_confidence:
  high: tested in representative component and observer conditions
  medium: metric-supported but not field-tested
  low: inferred from coordinates alone
```

The final confidence is never higher than the weakest critical layer.

---

# Gamut Policy

Every transformation must classify the color as:

- in gamut
- near boundary
- out of gamut
- mapped
- clipped
- unknown

For mapped colors record:

```yaml
mapping:
  source_space:
  target_gamut:
  algorithm:
  intent:
  pre_mapping_coordinates:
  post_mapping_coordinates:
  perceptual_difference_metric:
  perceptual_difference:
  hue_shift:
  lightness_shift:
  chroma_loss:
```

---

# Implementation Sequence

## Phase 1 — Metadata and Conversion

- define canonical YAML schemas
- retain source color profile
- add Oklab/OKLCH, Lab/LCh, XYZ conversions
- record library and version
- add gamut status

## Phase 2 — Measurement

- add named Delta E metrics
- add relative luminance calculations
- add CAM16 and CAM16-UCS with viewing profiles
- add round-trip and edge-case tests

## Phase 3 — Context

- add color relationship records
- add area and boundary metadata
- add component screenshots or references
- add color-vision-deficiency simulations
- record validated and failed contexts

## Phase 4 — Research Validation

- construct UI-native color-pair dataset
- compare metric predictions with observer judgments
- calibrate dark-mode and wide-gamut profiles
- publish evidence-backed decision thresholds

---

# Required Tests

## Conversion tests

- neutral axis remains neutral
- white and black endpoints
- known reference colors
- round-trip error
- adaptation round trips
- NaN and undefined hue handling
- out-of-gamut values
- high-chroma blue and yellow
- near-black behavior

## Decision tests

- same token on light and dark surfaces
- equal OKLCH spacing compared with CAM16-UCS
- gamut-mapped brand color
- status colors under color-vision deficiencies
- small icon versus large surface area
- ambient and display luminance variation

---

# Non-Goals

The measurement layer does not by itself predict:

- harmony
- beauty
- emotion
- cultural meaning
- brand suitability
- narrative role
- visual balance
- attention in complex scenes

It supplies controlled variables and evidence for those later models.

---

# Candidate Laws

## TH-ATLAS-COLOR-017 — Weakest-Layer Confidence

The reliability of a color decision cannot exceed the least reliable critical
layer in its measurement-to-context pipeline.

## TH-ATLAS-COLOR-018 — Derived-View Non-Authority

No derived perceptual coordinate should overwrite the canonical source record.

## TH-ATLAS-COLOR-019 — Operation-Specific Representation

The correct representation of color is determined by the operation, not by a
universal preferred space.

## TH-ATLAS-COLOR-020 — Delivered-Color Priority

Design validation must measure or estimate the delivered, gamut-mapped color,
not only the authored coordinate.

---

# Open Questions

1. Which metric best predicts UI-level suprathreshold discrimination?
2. How should viewing profiles be estimated on uncontrolled consumer devices?
3. Should Atlas store spectral approximations for branded material colors?
4. How should area alter color-difference interpretation?
5. What confidence penalty applies to unprofiled screenshots?
6. How should HDR and wide-gamut tokens be represented?
7. How should individual observer variation be stored?
8. Which gamut-mapping method best preserves identity and hierarchy?
9. Can a common context schema serve screens, print, paint, and architecture?
10. Which parts should become web-component tooling?

---

# Immediate Repository Actions

```text
/color/
  /research/
    RP-ATLAS-COLOR-004-Munsell-Modern-Spaces.md
  /frameworks/
    DF-ATLAS-COLOR-005-Perceptual-Measurement-Layer.md
  /schemas/
    color-record.schema.yaml
    color-relationship.schema.yaml
    viewing-profile.schema.yaml
  /registries/
    color-evidence-registry.md
    color-theory-registry.md
```

---

# Agent Handoff

Future agents must:

1. preserve source metadata
2. identify the task before selecting a space
3. name every metric
4. record viewing assumptions
5. distinguish authored from delivered color
6. validate relationships rather than isolated swatches
7. preserve failed contexts
8. never strengthen “perceptual” into “universally perceptual”
