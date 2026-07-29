---
id: EX-ITTEN-007
title: Peripheral Chromatic Interface Cues
document_type: experiment_report
project: itten-color-contrasts
status: model-simulation-complete-gaze-study-pending
created: 2026-07-28
updated: 2026-07-28
purposes: [verify, reproduce]
audiences: [researcher, contributor]
---

# EX-ITTEN-007 — Peripheral chromatic interface cues

## Question and falsifier

What cue size and contrast are needed for alerts under divided attention and realistic
motion? The hue-fragility prediction fails if hue-only detection remains invariant with
eccentricity after retinal size and luminance are controlled.

## Work completed

A proxy crossed eccentricity `0/5/10/20/30°`, size `.1/.25/.5/1/2°`, and four chroma
levels (100 conditions). It estimated the minimum tested size passing an arbitrary
sensitivity criterion.

## Pilot results

At the lowest modeled chroma, the minimum was `.25°` foveally, `.5°` at 5°, `2°` at
10°, and no tested size passed at 20° or 30°. At 20°, only the two highest chroma levels
passed, both at `1°`; no condition passed at 30°. These are model predictions, not
thresholds.

## Gaze-contingent experiment ready to run

- Apparatus: calibrated display, chinrest, high-rate eye tracker, gaze-contingent
  presentation, and controlled ambient light.
- Factors: eccentricity, angular size, hue direction, luminance contrast, chroma,
  duration, motion, cue redundancy, and central-task load.
- Use cone-contrast coordinates and verify rendered output; include protan/deutan
  observers and older adults after the initial normal-trichromat pilot.
- Outcomes: detection sensitivity (d′), criterion, localization error, response time,
  fixation break, and central-task cost.
- Staircases estimate 75%-correct thresholds; trials with broken fixation are repeated,
  not silently included.

## Current position / continuation

**Stage:** condition grid and analysis target complete; no gaze data collected.
**Next action:** implement gaze-contingent stimulus timing and validate end-to-end
latency before preregistering the 12-participant threshold pilot.
**Data:** `../experiments/data/ex-itten-007.json`.
