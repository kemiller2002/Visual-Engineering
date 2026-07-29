---
id: EX-ITTEN-001
title: Extension Ratios, Area, and Salience
document_type: experiment_report
project: itten-color-contrasts
status: computational-pilot-complete-human-study-pending
created: 2026-07-28
updated: 2026-07-28
purposes: [verify, reproduce]
audiences: [researcher, contributor]
---

# EX-ITTEN-001 — Extension ratios, area, and salience

## Question and falsifier

Do fixed color-area ratios predict perceived balance after luminance, chroma, position,
and semantic priority are controlled? The fixed-ratio account fails if those variables
explain balance and attention better than complementary area ratio, or if the preferred
ratio changes materially by task or observer.

## Work completed

A deterministic full-factorial pipeline test crossed four area fractions, four
luminance differences, three chroma differences, three positions, and two semantic
priority levels: 288 modeled conditions. The proxy was intentionally explicit:

`area^0.62 × hypot(3.2ΔL, 1.7ΔC) × center-bias × semantic-priority`.

This tests design, data shape, reproducibility, and analysis sensitivity—not people.

## Pilot results

Proxy-score correlations were area `r=.5161`, luminance difference `r=.7096`, chroma
difference `r=.0704`, and semantic priority `r=.2286`; score range was
`0.0152–1.2586`. Because the generating model assigned those weights, these are
successful pipeline-recovery results, not support for the coefficients. The run
demonstrates why area alone cannot identify “visual weight.”

## Human experiment ready to run

- Design: within-participant 4 × 4 × 3 × 3 factorial subset selected with
  D-optimal balancing; include Itten ratios plus logarithmically spaced alternatives.
- Stimuli: calibrated, texture-free pairs and complete interface compositions; match
  or independently manipulate CAM16 lightness and chroma.
- Outcomes kept separate: two-alternative balance judgment, adjustment-to-balance,
  first fixation, dwell distribution, target-search accuracy, and preference.
- Participants: initial 60 normal trichromats plus 30 participants with diagnosed
  red–green CVD; expand after pilot variance and reliability estimates.
- Analysis: mixed-effects psychometric model with participant and stimulus random
  effects; compare area-only, feature, and feature-plus-semantic models by held-out
  likelihood. Do not treat gaze as balance.
- Controls: randomized side, gaze-calibrated center fixation, equal exposure, reading
  direction, visual acuity, age, color-vision assessment, and device calibration.

## Current position / continuation

**Stage:** computational pipeline complete; human evidence absent.
**Next action:** create calibrated stimulus set, preregister model comparison, obtain
ethics/participant consent as locally required, and collect the first 15-participant
reliability pilot.
**Data:** `../experiments/data/ex-itten-001.json`.
**Code:** `scripts/itten-color/run-computational-pilots.mjs`.
