---
id: EX-ITTEN-004
title: Color-Vision Deficiency, Aging, and Redundant Encoding
document_type: experiment_report
project: itten-color-contrasts
status: simulation-audit-complete-human-study-pending
created: 2026-07-28
updated: 2026-07-28
purposes: [verify, reproduce]
audiences: [researcher, contributor]
---

# EX-ITTEN-004 — CVD, aging, and redundant encoding

## Question and falsifier

Do redundant encodings preserve consequential task performance across aging and
congenital CVD better than color-only encodings? The redundancy principle fails if a
well-powered representative study finds no performance or error-resilience advantage.

## Work completed

All 66 pairs from a 12-color palette were transformed through typical, protan, deutan,
and tritan screening matrices at modeled ages 25, 65, and 80. A simple lens-yellowing
proxy and an Oklab `0.08` screening cutoff were applied: 792 observer-pair conditions.

## Pilot results

Modeled detectable-pair proportions declined from `1.000` to `.9848` for typical
vision, `.9697` to `.9394` for protan simulation, `.9242` to `.8788` for deutan
simulation, and remained `.9394` in the simplified tritan transform. The coded
shape-redundancy channel remained 1.0 by construction.

These are audit flags only. The cutoff, matrices, yellowing transform, and perfect
shape detection are assumptions. The result supports selecting difficult pairs for a
study; it does not estimate clinical detection rates.

## Human experiment ready to run

- Groups: younger typical, older typical, diagnosed protan, diagnosed deutan, and older
  CVD; confirm class/severity with a validated test rather than self-report.
- Conditions: color only, shape only, label only, color+shape, and color+label.
- Tasks: urgent-state search, legend decoding, trend comparison, and prospective-memory
  alert response under time pressure.
- Outcomes: miss/false-alarm rate, response time, confidence calibration, and subjective
  workload. Analyze speed and accuracy jointly.
- Accessibility: large-enough marks, correction lenses allowed, fatigue breaks, and
  accessible consent.
- Analysis: mixed-effects signal-detection model; test interaction of encoding,
  age, CVD class, mark size, and eccentricity.

## Current position / continuation

**Stage:** palette screening complete; representative user testing not started.
**Next action:** recruit through optometry/accessibility partners and run a
10-participant usability pilot before fixing the final stimulus set.
**Data:** `../experiments/data/ex-itten-004.json`.
