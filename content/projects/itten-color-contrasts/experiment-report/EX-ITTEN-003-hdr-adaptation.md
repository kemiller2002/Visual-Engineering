---
id: EX-ITTEN-003
title: HDR Interface Adaptation and Recovery
document_type: experiment_report
project: itten-color-contrasts
status: model-simulation-complete-instrumented-study-pending
created: 2026-07-28
updated: 2026-07-28
purposes: [verify, reproduce]
audiences: [researcher, contributor]
---

# EX-ITTEN-003 — HDR interface adaptation and recovery

## Question and falsifier

How do peak luminance, bright-field area, and ambient illumination change post-highlight
search, legibility, discomfort, and recovery? A field-size/adaptation account fails if
recovery is invariant across physically verified exposure conditions.

## Work completed

A parameter sweep crossed peak luminance `200/600/1000/2000 cd/m²`, bright-field area
`1/10/40%`, and ambient `0/50/200/1000 lux` (48 conditions). An exponential recovery
proxy generated initial sensitivity loss and time to 90% recovery.

## Pilot results

Predicted 90% recovery time had median `9.1656 s`, 95th percentile `14.2672 s`, and
maximum `16.0654 s`. Predicted initial sensitivity loss had median `.1849` and maximum
`.3864`. These numbers are model outputs and must not become design thresholds.

## Instrumented experiment ready to run

- Hardware: HDR reference or characterized consumer display, spot photometer or
  spectroradiometer, lux meter, chinrest, and response box.
- Exposure: neutral field followed by controlled white highlight; verify emitted
  luminance, area, duration, and surround for every trial.
- Tasks: pre/post contrast threshold staircase, low-contrast target search, reading,
  discomfort rating, and pupil diameter if available.
- Timing: dense sampling at 0.25, 0.5, 1, 2, 4, 8, 16, and 30 seconds.
- Safety: conservative luminance/duration review, breaks, withdrawal rule, and
  exclusion for photosensitivity or relevant ocular conditions under ethics guidance.
- Analysis: hierarchical recovery curves; peak × area × ambient interactions; report
  both threshold elevation and task error.

## Current position / continuation

**Stage:** simulation and parameter grid complete; no light was shown to participants.
**Next action:** name and characterize the physical display and measuring instrument;
then replace proxy parameters with a five-participant apparatus pilot.
**Data:** `../experiments/data/ex-itten-003.json`.
