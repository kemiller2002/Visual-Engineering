---
id: EX-ITTEN-006
title: OLED and LCD Appearance Equivalence
document_type: experiment_report
project: itten-color-contrasts
status: parameter-sweep-complete-device-study-pending
created: 2026-07-28
updated: 2026-07-28
purposes: [verify, reproduce]
audiences: [researcher, contributor]
---

# EX-ITTEN-006 — OLED/LCD appearance equivalence

## Question and falsifier

When emitted colorimetry is matched, which spectral, black-level, reflection,
off-axis, temporal, and local-dimming variables change appearance or performance?
The class-label account fails if within-class device variance rivals or exceeds the
OLED-versus-LCD mean.

## Work completed

A transparent engineering parameter sweep crossed two illustrative device profiles,
four ambient levels, and three white luminances (24 conditions). Effective black was
modeled as emitted black plus Lambertian ambient reflection.

## Pilot results

At 300-nit white, modeled effective contrast changed from 600,000:1 to 79.5:1 for the
illustrative OLED profile between 0 and 1,000 lux, and from 3,750:1 to 38.3:1 for the
LCD profile. The values are parameter consequences, not measurements of named products.
They demonstrate that emitted matching cannot establish viewed equivalence.

## Device experiment ready to run

- Minimum sample: three OLED and three LCD models, with multiple units if feasible.
- Instruments: spectroradiometer, imaging photometer, lux meter, temporal light meter,
  and goniometric/off-axis fixture.
- Match center-screen XYZ and luminance, then measure spectra, black, flare/reflection,
  viewing angle, temporal modulation, ABL, local dimming, and tone/gamut mapping.
- Human tasks: dark-detail detection, color matching, small-text reading, halo/local
  contrast judgment, and discomfort under 0/50/200/1000 lux.
- Analysis: multilevel model with device technology and unit/model random effects.
  Attribute effects to measured variables, not the marketing class.

## Current position / continuation

**Stage:** apparatus equations and condition matrix complete; no devices measured.
**Next action:** inventory available displays/instruments, record exact model/firmware,
warm up and calibrate, then run repeatability measurements before participant viewing.
**Data:** `../experiments/data/ex-itten-006.json`.
