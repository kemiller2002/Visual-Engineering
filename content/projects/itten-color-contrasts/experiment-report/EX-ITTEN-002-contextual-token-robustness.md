---
id: EX-ITTEN-002
title: Contextual Color-Token Robustness
document_type: experiment_report
project: itten-color-contrasts
status: computational-pilot-complete-human-study-pending
created: 2026-07-28
updated: 2026-07-28
purposes: [verify, reproduce]
audiences: [researcher, contributor]
---

# EX-ITTEN-002 — Contextual color-token robustness

## Question and falsifier

Which metric best predicts color discrimination in real component surrounds? Any claim
that one isolated metric is sufficient fails if a context-aware or spatial model
materially improves held-out human judgments.

## Work completed

Twelve interface colors were crossed with six backgrounds (72 pairs). The pipeline
computed WCAG luminance contrast, Euclidean CIELAB difference, Euclidean Oklab
difference, and an explicitly labeled toy induction stress value (8% displacement away
from the surround in Lab).

## Pilot results

Rank correlation was `.6357` for WCAG versus Lab, `.9398` for WCAG versus Oklab, and
`.6791` for Lab versus Oklab. Of 72 pairs, 31 passed 4.5:1 and 47 passed 3:1. The toy
induction shift had median `6.1736` and maximum `9.2009` ΔE76.

The result establishes metric disagreement in this sample, not perceptual superiority.
WCAG contrast, Lab distance, and Oklab distance describe different constructs. The
induction magnitude is generated, not observed.

## Human experiment ready to run

- Render complete controls in six surrounds at fixed angular sizes, including thin
  strokes, text, fills, disabled states, and alerts.
- Use a calibrated wide-gamut monitor with recorded primaries, transfer function,
  white, black, and ambient illumination.
- Tasks: same/different discrimination, state identification, visual search, and
  appearance matching to an adjustable isolated patch.
- Compare ΔE00, CAM16-UCS, Oklab, WCAG contrast, and at least one spatial appearance
  model against held-out accuracy and matching error.
- Stratify by normal color vision, protan/deutan class, and older adults. Record visual
  acuity and display viewing angle.
- Primary analysis: cross-validated mixed-effects logistic model; report calibration,
  not only rank correlation.

## Current position / continuation

**Stage:** code and metric baseline complete; no appearance judgments collected.
**Next action:** add CAM16-UCS/ΔE00 reference implementations and generate calibrated
rendered stimuli before preregistration.
**Data:** `../experiments/data/ex-itten-002.json`.
