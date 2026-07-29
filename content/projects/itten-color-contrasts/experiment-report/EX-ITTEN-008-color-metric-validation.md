---
id: EX-ITTEN-008
title: Color-Difference Metric Validation
document_type: experiment_report
project: itten-color-contrasts
status: computational-stress-test-complete-ground-truth-study-pending
created: 2026-07-28
updated: 2026-07-28
purposes: [verify, reproduce]
audiences: [researcher, contributor]
---

# EX-ITTEN-008 — Color-difference metric validation

## Question and falsifier

Which metric predicts task-specific discrimination across modern wide-gamut and HDR
displays? A universal-metric claim fails if rankings or calibration vary materially by
regime, task, observer, or device.

## Work completed

Three thousand fixed-seed random sRGB pairs were compared with Euclidean Lab and Oklab
before and after a simple gamut-compression transform. Rank stability and relation to
luminance difference were recorded.

## Pilot results

Rank stability after the mild compression was `.9990` for Lab and `.9987` for Oklab.
Cross-metric rank correlation was only `.7824`. Correlation with luminance difference
was `.3675` for Lab and `.7417` for Oklab in this generated corpus.

The stress transform was too mild to separate within-metric robustness, but the
cross-metric disagreement justifies empirical comparison. There is no perceptual
ground truth here, and ΔE00, CAM16-UCS, Jzazbz, and HDR viewing conditions remain to be
implemented.

## Validation experiment ready to run

- Build a stratified pair corpus spanning hue, lightness, chroma, near-threshold and
  suprathreshold distances, gamut edges, skin/medical/status colors, and SDR/HDR.
- Measure actual display spectra and luminance; record adaptation and surround.
- Tasks: forced-choice discrimination, suprathreshold difference scaling, appearance
  matching, and real interface state identification.
- Metrics: ΔE76 baseline, ΔE00, CAM16-UCS, Oklab, Jzazbz and current refinements,
  cone-contrast, and luminance contrast.
- Evaluate held-out predictive likelihood, calibration error, rank correlation, and
  worst-group error rather than selecting by pooled correlation alone.
- Publish raw trials, transformations, calibration files, exclusions, and code.

## Current position / continuation

**Stage:** reproducible baseline stress test complete; metric validation not achieved.
**Next action:** add reference ΔE00/CAM16-UCS/Jzazbz implementations with unit tests,
then construct a physically measurable stimulus corpus and preregister validation.
**Data:** `../experiments/data/ex-itten-008.json`.
