---
id: REP-VE-COL-001
title: Color, Contrast, Low Vision, and Color-Vision Deficiency
abstract: Evidence review and falsification package on minimum visual contrast, color discrimination, low vision, color-vision deficiency, viewing conditions, and safe interface engineering. It concludes that WCAG 2.2 ratios are necessary conformance floors but not universal human thresholds, and replaces pairwise color checking with a layered visibility, discriminability, redundancy, adaptability, and task-validation model.
authors:
  - Codex
created: 2026-07-24
updated: 2026-07-24
project: visual-engineering
discipline: Color and Accessibility
research_area:
  - color
  - contrast
  - low-vision
  - color-vision-deficiency
document_type: research-report
status: research-draft
evidence_level: B
confidence: medium
canonical: false
concepts:
  - color-contrast
  - accessibility
  - perception
related_documents:
  - PRM-VE-COL-001
  - RDM-VE-COL-001
  - DF-ATLAS-COLOR-005
tags:
  - WCAG
  - APCA
  - contrast-sensitivity
  - forced-colors
  - dark-mode
  - data-visualization
source_stage: processed
reading_time_minutes: 32
machine_readable: true
llm_ingest: true
purposes:
  - orient
  - integrate
  - verify
audiences:
  - executive
  - practitioner
  - researcher
---

# REP-VE-COL-001 — Color, Contrast, Low Vision, and Color-Vision Deficiency

## Executive synthesis

### Bottom line

There is no universal minimum color contrast that makes content usable for every
person. Contrast need is a function of at least:

```text
observer × task × target geometry × typography × polarity × adaptation
× ambient light/glare × display × surrounding context × time
```

The strongest defensible engineering position is:

1. Treat WCAG 2.2 as the current normative web conformance baseline:
   - ordinary text: **4.5:1** minimum (Level AA);
   - large text: **3:1** minimum;
   - ordinary text at enhanced Level AAA: **7:1**;
   - large text at enhanced Level AAA: **4.5:1**;
   - essential UI component boundaries, states, focus indicators, and graphical
     objects: **3:1** against adjacent colors;
   - never use color as the only means of conveying information.
2. Do not describe those ratios as thresholds that guarantee readability,
   accessibility, comfort, or comprehension for “people with low vision.”
3. For important reading, use a stronger default than the AA floor where the
   visual design permits it, while preserving a user-selectable lower-luminance
   or reversed-polarity presentation for people affected by glare or photophobia.
4. Treat color-vision deficiency primarily as a **discriminability and encoding**
   problem, not merely a foreground/background contrast problem. Add text,
   shape, pattern, position, line style, or direct labels.
5. Validate rendered components and representative tasks under zoom, text
   scaling, forced colors, light/dark schemes, CVD simulation, grayscale,
   glare/low-brightness stress, and real affected users. A passing hex pair is
   not a passing experience.

### What is established, what is provisional

| Claim | Judgment | Confidence |
|---|---|---|
| WCAG 2.2 ratios are the operative web conformance floors | Established normative requirement | High |
| 4.5:1 is a universal low-vision readability threshold | Rejected | High |
| More luminance contrast generally improves visibility until performance approaches a plateau | Supported, bounded by size, task, adaptation, and observer | High |
| Maximum black/white contrast is always optimal | Rejected | Medium-high |
| Hue difference can substitute for luminance contrast | Rejected for text and critical form; unsafe for semantics | High |
| Color-safe design is achieved by choosing a “color-blind palette” | Rejected as sufficient | High |
| Redundant encoding is a robust default for critical meaning | Supported | High |
| One CVD simulation predicts every affected observer | Rejected | High |
| Oklab/OKLCH or CAM16-UCS distance predicts interface accessibility | Rejected as a general claim | High |
| APCA is the current or approved WCAG 3 requirement | Rejected as of 2026-07-24 | High |
| APCA-like models expose real weaknesses in fixed pairwise ratios | Plausible and useful for research/design comparison | Medium |
| Light mode is universally more accessible than dark mode | Rejected | High |
| Positive polarity often improves fine-detail performance in normally sighted and many older observers | Supported | Medium-high |
| Some people with low vision perform or feel better with reversed polarity | Supported | High |

## Objective and scope

This package asks:

- What does “minimum needed contrast” mean physiologically, empirically, and
  normatively?
- Which contrast requirements protect people with low vision or color-vision
  deficiency, and where do they fail?
- What additional variables must a production design system control?
- Do the repository hypotheses about perceptual color spaces and relational
  color survive falsification?

The focus is self-luminous digital interfaces. Print, safety signage, aviation,
medical imaging, and mixed reality are included only where they expose transfer
limits. This is not medical advice and does not define clinical impairment.

## Definitions that prevent category errors

**Physical luminance** is emitted or reflected light weighted by a standard
observer function. **Relative luminance** in WCAG is a normalized calculation
from encoded sRGB components. **Luminance contrast** describes a relationship
between light and dark. It is not the same as hue difference.

**Contrast sensitivity** is an observer's ability to detect luminance variation,
often measured across spatial frequencies. **Visual acuity** measures resolution
of detail. One does not substitute for the other.

**Visibility** means that a target can be detected. **Legibility** means that
characters or symbols can be identified. **Readability** adds fluent reading.
**Comprehension**, **task success**, **preference**, and **comfort** are further
outcomes. A metric validated for one should not silently stand in for another.

**Color-vision deficiency (CVD)** is reduced or altered discrimination in parts
of color space. “Color blind” is common language but often misleading: most
affected people perceive many colors. Congenital protan and deutan conditions
are common; tritan conditions are rarer. Disease, medication, aging, and ocular
or neural changes can also produce acquired deficiencies.

**Contrast reserve** is the ratio between available contrast and the observer's
threshold for the task. Reading near threshold is fragile. A nominally visible
stimulus may require substantially more contrast for fluent, sustained use.

## Repository context, separated from external evidence

### Existing repository claims

The repository correctly treats contrast as multidimensional, recommends
redundant cues, and warns against low-contrast secondary text. Its
`DF-ATLAS-COLOR-005` measurement layer also correctly separates source color,
viewing conditions, derived perceptual spaces, task metrics, and context
validation.

The risky repository assumptions are:

- that modern perceptual spaces might adequately predict interface color
  differences;
- that relational principles from art pedagogy might transfer to task
  performance;
- that “perceptually meaningful color spaces and measurable contrast” could be
  read as a sufficiently complete accessibility method;
- that stronger contrast can safely be recommended without naming brightness,
  polarity, photophobia, glare, target size, or user override.

### External evidence judgment

External evidence supports the layered measurement architecture but requires a
sharper separation:

```text
color appearance/difference metric
        ≠
foreground/background luminance contrast
        ≠
observer contrast threshold
        ≠
fluent reading or task performance
        ≠
semantic decoding
```

No single color space or ratio spans all five.

## What the standards actually require

WCAG 2.2 requires 4.5:1 for ordinary text, 3:1 for large text, 7:1 for ordinary
text at AAA, and 4.5:1 for large text at AAA. Large text is at least 18 point
(24 CSS px) or 14 point (about 18.66 CSS px) and bold. Required visual
information that identifies UI components and states, and essential graphical
objects, needs 3:1 against adjacent color. Color cannot be the only visual means
of conveying information.

These are exact threshold tests for conformance: a computed 2.999:1 does not
round up to 3:1. Evaluation uses the specified/rendered colors rather than
trying to infer anti-aliased edge pixels, because rasterization is outside the
author's control.

WCAG's own rationale says 4.5:1 starts from a 3:1 recommendation for standard
text and normal vision, then multiplies by an estimated 1.5 contrast-sensitivity
loss associated with 20/40 acuity. The 7:1 value analogizes to 20/80. This is a
pragmatic accessibility model. It is not a modern dose-response study showing
that every observer, font, size, display, and task crosses from unreadable to
readable at those exact ratios.

### Important conformance gaps

- Inactive controls and logos have exemptions. An exemption is not evidence
  that low contrast is usable.
- Text contrast evaluates the nominal foreground and background pair, not font
  stroke width, angular size, glare, ambient illumination, or surrounding
  adaptation.
- Non-text contrast only applies when the visual information is required to
  identify or understand the component or graphic.
- Passing “use of color” through an added label does not necessarily make
  adjacent regions or data series easy to discriminate.
- A page can conform and still prevent a particular low-vision user from using
  it comfortably or efficiently.

### APCA and WCAG 3

APCA is a polarity-sensitive candidate method that aims to model perceived text
contrast and connect contrast requirements to font size and weight. Those are
directionally important corrections to WCAG 2's symmetric, pair-only ratio.

It must not, however, be presented as an approved WCAG requirement. The W3C
Visual Contrast subgroup page explicitly says the subgroup is inactive, that
its legacy material was not approved to move forward, and that it should not be
used as W3C guidance. The March 2026 WCAG 3 publication is a Working Draft and
states that publication does not imply W3C endorsement. Therefore:

- use WCAG 2.2 for current conformance;
- APCA may be run as an additional design diagnostic or research variable;
- do not fail a product solely on an experimental APCA target unless the
  organization has explicitly adopted that internal policy;
- record version and parameters, because experimental methods can change.

## Low vision: why one minimum cannot work

“Low vision” combines materially different limitations:

- reduced acuity;
- reduced contrast sensitivity;
- central or peripheral field loss;
- cloudy ocular media and intraocular scatter;
- photophobia and glare sensitivity;
- reduced light adaptation;
- impaired color discrimination;
- combinations of the above.

Rubin and Legge measured 19 low-vision readers and found critical reading
contrasts higher than normal in 16, averaging 3.9 times higher. Critical
contrast correlated strongly with letter contrast sensitivity, while peak
reading rate also depended on field loss. Five read reversed-polarity text
faster; four had cloudy ocular media. This directly falsifies both “one ratio
fits low vision” and “one polarity fits low vision.”

Later work found that reducing text contrast from 90% to 45% produced at least a
20% reading-speed loss in roughly one third of a group at 0.6 logMAR acuity and
two thirds at 1.0 logMAR. The result also shows why testing only maximum-contrast
text hides functional differences.

### Contrast is necessary but coupled to size

Small or thin strokes contain high spatial frequencies, where sensitivity is
lower and more vulnerable to blur, age, glare, and display rasterization.
Increasing font size and weight can increase visibility even when the nominal
color pair is unchanged. Conversely, a 4.5:1 pair can be fragile when used with
very thin type, small text, low pixel density, transparency, background imagery,
or a font whose actual strokes are much thinner than its nominal weight implies.

This supports a design rule: never spend the entire visibility budget on color
contrast. Provide adequate size, stroke width, spacing, zoom, text scaling, and
reflow.

### Contrast is coupled to luminance and adaptation

The same nominal pair can perform differently as display brightness, black
level, ambient light, reflections, and the viewer's adaptation change.
Operational cockpit studies found that under low/moderate ambient light some
symbols reached a performance plateau at low ratios, while extreme daylight
adaptation benefited from ratios up to 30:1. Medical-display research similarly
shows that reflected ambient light raises dark luminance and reduces effective
contrast.

A contrast ratio therefore describes a pair under a model; it does not fully
describe retinal contrast in the field.

### Polarity and the “dark mode” contradiction

Controlled studies in normally sighted adults frequently find a positive
polarity advantage—dark text on a light background—for proofreading and fine
detail. Higher overall luminance constricts the pupil and can sharpen the
retinal image. The advantage grows for smaller characters.

That population result cannot become a universal accessibility rule. People
with cloudy ocular media may experience more scatter from a large bright
background and read faster with light text on dark. In a survey of 133 adults
with low vision, 46% preferred reversed contrast, 39% preferred dark-on-light,
and 14% reported no preference. Preference is not the same as performance, but
the heterogeneity is decisive.

The correct conclusion is:

- positive polarity is a reasonable general default for dense fine-detail
  reading when glare and light sensitivity are controlled;
- a well-designed dark/reversed theme is a necessary alternative for many;
- neither should be forced;
- avoid absolute white on black as the only dark option when blooming,
  halation, or astigmatic blur is a concern, but do not lower contrast below
  conformance in pursuit of “softness”;
- allow brightness and theme choice at the user or system level.

### More contrast is not identical to more light

People can have both reduced contrast sensitivity and photophobia. Making a
background brighter can increase available contrast yet cause pain, glare, or
scatter. A high ratio made from two relatively low-luminance colors may be more
tolerable than the same ratio made with a glaring white field, depending on the
display and observer. WCAG relative luminance does not encode screen luminance
in cd/m² or total luminous area.

This defeats the theory that “maximize black–white contrast” is a universal
optimization. The robust solution is sufficient contrast plus theme,
brightness, and color customization.

## Color-vision deficiency: what actually fails

### Prevalence is variable, not one folklore number

A 2025 systematic review and meta-analysis covering 1,703,619 participants from
56 studies in 21 countries estimated congenital CVD at 2.59% globally, 4.38% in
males and 0.64% in females, with very high between-study heterogeneity.
Deutan conditions were most common. The often-repeated “8% of men” estimate
describes some populations, particularly people of Northern European ancestry,
not humanity.

Acquired CVD broadens the affected population. Aging lenses and cataract can
produce blue-yellow loss; retinal disease often affects short-wavelength
discrimination; optic-nerve disease often affects red-green discrimination.
Medication and systemic disease can also matter.

### CVD is not solved by hue naming

The failure is not simply that a person calls red “green.” Colors that are
distinct for a standard trichromat can collapse toward the same percept under a
particular deficiency. Protan conditions also alter perceived lightness of
long-wavelength reds, making dark red especially easy to lose against black.
Tritan and acquired losses create different confusion axes.

No fixed list such as “never use red and green” is sufficient. Blue/purple,
green/brown, pink/gray, yellow/light green, and other pairs can fail depending
on lightness, saturation, size, adjacency, and deficiency. Conversely, some red
and green colors remain distinguishable when their lightness and other cues are
strongly separated. The safer rule is to avoid depending on any hue pair alone.

### Redundant encoding is the strongest general intervention

For critical status, instructions, selection, errors, warnings, routes, or data
series, combine color with one or more of:

- direct text labels;
- icons whose shapes are distinguishable without color;
- line style or marker shape;
- pattern or texture;
- position or grouping;
- borders or separators;
- explicit state text such as “Error,” “Selected,” or “Offline”;
- programmatically available names, roles, values, and status messages.

Redundancy should be information-preserving, not decorative. Two colored icons
with nearly identical silhouettes are still color-dependent. A legend that
requires repeated color matching may technically add text while leaving the
task slow and error-prone; direct labels are usually stronger.

### Simulation is a stress test, not an affected user's testimony

The Machado–Oliveira–Fernandes model provides a physiologically grounded,
experimentally evaluated simulation across anomalous trichromacy and dichromacy.
It is useful for finding likely collapses. But:

- CVD type and severity vary continuously;
- acquired deficiencies may not match congenital models;
- display spectra, profiles, gamut mapping, and ambient conditions matter;
- a simulation shown to a standard observer does not recreate a lifetime of
  adaptation or learned strategies;
- image appearance is not equivalent to task performance.

Use multiple simulated severities and types, then validate critical workflows
with affected participants. Grayscale conversion is a quick test for whether
lightness carries structure, but unique grayscale values do not prove universal
CVD safety or adequate contrast.

## Perceptual color spaces: hypothesis VE-COL-H1

### Initial hypothesis

Modern perceptual spaces adequately predict interface color differences.

### Falsification result

**Rejected as stated; retained only as a bounded engineering tool.**

Oklab/OKLCH improves palette manipulation, interpolation, and approximate
perceptual spacing over raw RGB or HSL. CAM16 and CAM16-UCS explicitly model
viewing-condition adaptation and have strong color-science uses. Experimental
wide-gamut comparisons show CAM16-UCS can outperform several alternatives while
still performing unevenly across hue regions.

But a color-difference metric predicts neither:

- text/background readability;
- critical edge visibility;
- color-category naming;
- semantic interpretation;
- discrimination for every CVD observer;
- resistance to glare, blur, crowding, or small target size;
- attention priority or task performance.

Even a perceptually uniform space is uniform only for the observer model,
dataset, magnitude range, and viewing assumptions used to build or test it.
Simultaneous contrast and adaptation can change appearance without changing the
stored coordinates.

### Revised hypothesis

> Task-appropriate color spaces improve palette construction and color-difference
> prediction under stated viewing assumptions, but accessibility requires
> separate luminance-contrast, CVD, geometry, context, and task validation.

Confidence: high.

## Art-pedagogy transfer: hypothesis VE-COL-H2

### Initial hypothesis

Relational color principles transfer from art pedagogy to digital task
performance.

### Falsification result

**Narrowed substantially.**

The relational insight survives: surrounding color, area, adaptation, contour,
and spatial frequency can change appearance. This is compatible with modern
simultaneous-contrast and appearance research. Historical frameworks are useful
for generating variations and noticing context.

What does not survive is the inference that named contrasts—complementary,
warm/cool, saturation, or hue category—predict detection, readability,
comprehension, urgency, or accessibility. A complementary pair can have poor
luminance separation; high chroma can compete with hierarchy; context can
produce contrast, assimilation, or little effect.

### Revised hypothesis

> Historical relational color systems are generative vocabularies. Their
> variables must be translated into measurable luminance, color-difference,
> spatial, semantic, and task predictions before they can justify interface
> decisions.

Confidence: medium-high.

## A layered engineering model

### Layer 1 — Normative floor

Meet the applicable WCAG 2.2 criterion on every allowed component state and
theme. Test hover, focus, selected, disabled-but-readable content, validation,
loading, and high-contrast variants—not only default screenshots.

### Layer 2 — Visibility reserve

For important text and critical controls, avoid designing exactly on the
threshold. Account for thin strokes, alpha, overlays, gradients, imagery,
anti-aliasing, low-quality displays, glare, and aging. Prefer a higher contrast
reserve for:

- long-form or dense text;
- small or thin text;
- time-critical information;
- safety, health, finance, or destructive actions;
- outdoor or mobile use;
- older or low-vision audiences;
- information that cannot be recovered after an error.

This is a risk rule, not a new universal ratio. A candidate internal default is
7:1 for ordinary critical text where practical, with representative-user tests
and user customization. Do not claim AAA alone makes a workflow accessible.

### Layer 3 — Geometry and typography

Validate:

- rendered font family, variable-font axes, size, weight, and actual stroke;
- visual angle at realistic viewing distance;
- zoom to 200% and text enlargement beyond it where supported;
- reflow and no clipped text;
- spacing, crowding, target size, focus-indicator area, and boundary thickness;
- icons at their smallest deployed size.

### Layer 4 — Color discriminability

- Do not encode meaning solely by hue.
- Check color pairs after CVD simulation across protan, deutan, and tritan types
  and multiple severities.
- Check grayscale to expose hidden lightness dependencies.
- For categorical palettes, prefer fewer simultaneous categories, direct
  labels, and separable lightness plus hue.
- For ordered data, use a monotonic perceptual-lightness sequence unless the
  task requires a justified alternative.
- Avoid rainbow maps for ordered magnitude because they introduce non-monotonic
  lightness and false boundaries.

### Layer 5 — Adaptability

- Respect `prefers-color-scheme`; support both light and dark themes when
  feasible.
- Allow forced colors to replace author colors. Use semantic CSS system colors
  and test `forced-colors: active`.
- Avoid `forced-color-adjust: none` except for a narrowly justified element
  whose meaning remains perceivable and whose custom rendering is fully tested.
- Do not put required information only in CSS background images, box shadows, or
  color fills that forced colors may remove.
- Do not block browser or OS contrast, color, font, zoom, or brightness
  preferences.
- Preserve programmatic semantics so nonvisual presentation remains possible.

### Layer 6 — Context and task validation

Test the rendered experience, not only token pairs:

| Stress condition | Failure sought |
|---|---|
| 200–400% zoom and text scaling | clipping, loss of context, excessive panning |
| Forced colors, light and dark | vanished boundaries, icons, selections, focus |
| Protan/deutan/tritan simulations | collapsed categories or statuses |
| Grayscale | hue-only structure |
| Low brightness | loss of fine/dark detail |
| Bright ambient light / reflection | washed-out darks and boundaries |
| Blur / reduced contrast simulation | fragile thin strokes and low reserve |
| Background image extremes | local contrast failure |
| Real device families | gamut, black level, tone mapping, viewing-angle shifts |
| Time pressure and error recovery | detectable but misinterpreted signals |

For consequential workflows, measure accuracy, completion time, errors,
confidence, fatigue, and abandonment with affected participants. Preference and
performance should both be recorded and not conflated.

## Practical decision table

| Use | Minimum conformance target | Stronger engineering default |
|---|---|---|
| Ordinary body text | 4.5:1 | Higher reserve; consider 7:1 for critical/dense reading, then test |
| Large text | 3:1 | Do not use size exception merely to rescue a weak brand color |
| Essential UI boundary/state | 3:1 adjacent | Add shape, text, thickness, and clear focus |
| Informative icon/graphic | 3:1 where needed to understand | Text alternative/direct label plus robust geometry |
| Error/success/warning | Color not sole cue; relevant text/non-text contrast | Explicit status word + icon + color + programmatic status |
| Links in prose without underline | Must satisfy use-of-color technique conditions | Keep persistent underline or equally clear non-color cue |
| Categorical chart | Color not sole cue | Direct labels + marker/line/pattern + CVD-tested palette |
| Sequential heatmap | No single WCAG pair test solves the scale | Monotonic lightness, annotated thresholds, accessible data table |
| Disabled control | Exempt if inactive | Keep label/state understandable; do not use disabled styling for read-only content |
| Dark theme | Same WCAG requirements | Avoid thin glowing text; offer light theme and brightness control |

## Anti-patterns

- “It passes 4.5:1, therefore it is accessible.”
- Lowering secondary text to the AA boundary to manufacture hierarchy.
- Relying on 3:1 large-text relief while the implementation can render smaller
  due to responsive type, zoom, or font substitution.
- Green/red status dots with identical shape and no text.
- Treating CVD as one simulated switch at maximum severity.
- Recoloring content to “correct” CVD without preserving stable semantic cues.
- Using ΔE, OKLCH distance, saturation, or complementary hue as a substitute for
  contrast testing.
- Checking a token against one background while components add opacity,
  gradients, overlays, images, elevation, or state colors.
- Preventing forced colors to preserve brand identity.
- Assuming dark mode reduces eye strain for everyone.
- Assuming preference scores prove faster or more accurate performance.
- Treating a standard-observer calculation as a measurement of a specific
  display or human.

## Evidence registry

| ID | Evidence | Claim use | Quality / limitation |
|---|---|---|---|
| EV-VE-COL-001 | WCAG 2.2 normative criteria | Current conformance ratios and use-of-color requirement | Authoritative normative standard; not an individual performance guarantee |
| EV-VE-COL-002 | W3C Understanding 1.4.6 | Historical rationale for 3, 4.5, and 7 ratios | Authoritative explanation; rationale is indirect and simplified |
| EV-VE-COL-003 | W3C Non-text Contrast understanding | 3:1 essential UI/graphic boundary rationale | Authoritative guidance; bounded conformance scope |
| EV-VE-COL-004 | Rubin & Legge 1989 | Low-vision critical contrast heterogeneity and polarity reversal | Primary study; only 19 observers, older display/text conditions |
| EV-VE-COL-005 | Giacomelli et al. 2010 | Reduced contrast harms low-vision reading | Primary study; clinical chart/task transfer limits |
| EV-VE-COL-006 | Legge 2017 review | Size, contrast, luminance, glare, and polarity synthesis | Expert review with broad evidence; not web-specific intervention trial |
| EV-VE-COL-007 | Crossland et al. 2020 | Low-vision digital practices and polarity preferences | Affected-user survey; self-selection and preference ≠ performance |
| EV-VE-COL-008 | Piepenbrock et al. 2014 | Positive-polarity fine-detail advantage and pupil mechanism | Controlled primary study; typical-vision task, not all low vision |
| EV-VE-COL-009 | Jeong et al. 2025 | Global congenital CVD prevalence and heterogeneity | Large systematic review/meta-analysis; I² extremely high |
| EV-VE-COL-010 | NCBI Visual Impairments review | Congenital/acquired CVD mechanisms | Authoritative synthesis; some prevalence estimates are dated |
| EV-VE-COL-011 | Machado et al. 2009 | Physiological CVD simulation | Peer-reviewed model with experimental evaluation; simulation is not task validation |
| EV-VE-COL-012 | W3C G111 | Color + pattern redundancy | Authoritative sufficient technique; examples, not comparative trial |
| EV-VE-COL-013 | Nuñez et al. 2018 | CVD-aware colormap optimization | Peer-reviewed computational/visualization work; scientific-data scope |
| EV-VE-COL-014 | CSS Color Adjustment 1 | Forced-color behavior and author constraints | W3C Candidate Recommendation; implementation variability remains |
| EV-VE-COL-015 | CSS Color 4 | Oklab/OKLCH uses and ΔEOK | Authoritative web specification; does not claim accessibility prediction |
| EV-VE-COL-016 | CIE 248:2022 | Viewing-condition-specific appearance modeling | International color-science authority; model observer is not disability model |
| EV-VE-COL-017 | Huang et al. 2021 | Uniform-space performance varies by gamut and magnitude | Primary color-difference study; not interface task performance |
| EV-VE-COL-018 | W3C WCAG 3 Working Draft | WCAG 3 status | Authoritative status; explicitly non-normative work in progress |
| EV-VE-COL-019 | W3C Visual Contrast subgroup archive | APCA not approved into WCAG 3 | Authoritative status notice; does not determine APCA scientific merit |
| EV-VE-COL-020 | Silverstein et al. 2005 | Adaptation/ambient conditions change useful contrast | Operational primary studies; cockpit symbols differ from consumer UI |

## Hypothesis registry changes proposed

| ID | Original | Outcome | Revised statement |
|---|---|---|---|
| VE-COL-H1 | Modern perceptual spaces adequately predict interface color differences | Rejected as universal; narrowed | Task-specific spaces improve construction and some difference predictions, but accessibility needs separate contrast, CVD, geometry, context, and task validation |
| VE-COL-H2 | Relational art-color principles transfer to digital task performance | Narrowed | Relational systems are generative vocabularies; no performance transfer without measurable mechanism and task evidence |
| VE-COL-H3 | WCAG ratios define human contrast thresholds | New rival rejected | Ratios are conformance floors and population proxies, not universal thresholds |
| VE-COL-H4 | Maximum contrast is universally optimal | New rival rejected | Required contrast and tolerable luminance/polarity vary; adaptability is necessary |
| VE-COL-H5 | Redundant encoding reduces dependence on individual color discrimination | Provisionally supported | Preserve, then validate cue independence and task performance |
| VE-COL-H6 | Pairwise color validation is sufficient for a design system | Rejected | Validate state matrices, rendering, context, user settings, devices, and tasks |

## Contradiction ledger

| Tension | Resolution |
|---|---|
| High contrast supports reduced contrast sensitivity; bright fields can hurt photophobic users | Separate contrast ratio from absolute luminance; offer themes and brightness control |
| Positive polarity often improves fine detail; many low-vision users prefer or perform better with negative polarity | Use positive as a general reading default, not a mandate; support both |
| Perceptual uniformity improves palettes; CVD changes the observer space | Use uniform spaces for construction, then separate CVD and user validation |
| Grayscale separation is robust; categorical palettes cannot always have unique lightness | Reduce category count, add direct labels/shape/pattern, and test the actual task |
| Standards need crisp thresholds; human performance changes continuously | Keep thresholds for conformance and add reserve/risk-based validation |
| Simulation finds failures cheaply; simulations cannot represent lived perception | Use simulation for screening and affected users for validation |

## Failed assumptions and negative results

- A search for an empirically demonstrated universal ratio for low vision did
  not find one. Evidence instead showed observer and condition heterogeneity.
- The WCAG 4.5:1 rationale did not resolve to a direct modern interface trial;
  it is a multiplication of a normal-observer recommendation by a generalized
  loss factor.
- APCA could not be promoted as the WCAG 3 method. Current W3C pages explicitly
  block that claim.
- A single “best dark mode” recommendation did not survive polarity evidence.
- A universal CVD-safe named palette did not survive variation in deficiency,
  severity, display, and task.
- A single ΔE threshold did not survive the distinction between color matching,
  categorical discrimination, small-symbol visibility, and reading.
- More searching for brand or UX blog recommendations had low value because
  those sources mostly repeat WCAG or palette folklore without primary evidence.

## Source acceptance and rejection

### Accepted source classes

- W3C normative specifications and official understanding documents for
  conformance claims;
- CIE material for color appearance scope;
- primary psychophysics, ergonomics, and visualization studies;
- systematic reviews for prevalence;
- affected-user studies for variability and preferences;
- official CSS specifications for customization behavior.

### Rejected or down-weighted

- vendor contrast-checker pages: useful tools, not independent evidence;
- design blogs and palette lists: mostly derivative and rarely task-validated;
- APCA promotional documentation for normative status: primary project
  documentation but interested and not W3C-approved;
- Reddit discussions: useful as leads or objections, not load-bearing evidence;
- studies using only standard-vision observers to claim CVD accessibility;
- studies reporting preference alone as readability or performance;
- simulation-only interface studies presented as affected-user validation;
- papers without retrievable methods or clear population/task descriptions.

## Engineering implementation requirements

### Token metadata

Each semantic color token should declare:

```yaml
token_id:
semantic_role:
allowed_foregrounds:
allowed_backgrounds:
allowed_states:
themes:
wcag_target:
criticality:
redundant_cues:
forced_colors_mapping:
cvd_checks:
rendered_component_tests:
known_exceptions:
owner:
```

Do not certify isolated palette swatches. Certify allowed **role × background ×
state × theme × component** combinations.

### Automated checks

- compute WCAG 2.2 contrast without rounding;
- resolve alpha compositing and all actual backgrounds;
- cover theme and state matrices;
- flag color-only differences in status, charts, selection, and instructions;
- run screenshot checks under forced colors and CVD simulation;
- detect gradients or images that create variable local contrast;
- retain manual review gates for focus visibility, semantic redundancy,
  typography, and charts.

Automation should report uncertainty rather than fabricate a pass when the
background, compositing, display profile, or image region is unknown.

## Recommended validation program

### Experiment 1 — contrast reserve × typography

Factor ordinary text across WCAG ratios (3, 4.5, 7, and higher), size, weight,
polarity, and background luminance. Recruit typical vision, older adults, and
stratified low-vision participants. Measure reading accuracy, rate, critical
print size, errors, fatigue, and preference.

**Disconfirmation target:** if 4.5:1 produces no worse task outcomes than higher
ratios across risk-relevant groups and conditions, the proposed reserve rule
should narrow.

### Experiment 2 — semantic status encoding

Compare color-only, color + icon, color + text, and color + icon + text across
CVD types and low-vision groups. Measure identification accuracy and time under
normal, simulated glare, and forced-colors conditions.

**Disconfirmation target:** if redundant cues slow or confuse users without
improving accuracy, determine whether cue design—not redundancy itself—is the
cause.

### Experiment 3 — metric tournament

Test whether WCAG ratio, APCA versioned score, ΔEOK, CAM16-UCS distance, and
simple lightness difference predict rendered text, icon, boundary, and
categorical-color performance. Pre-register separate outcome models and test on
held-out devices and observers.

**Disconfirmation target:** no metric should be promoted if it wins only on the
development dataset or one target class.

### Experiment 4 — customization versus universal theme

Compare a fixed high-contrast theme with user choice among tested light, dark,
and low-luminance high-contrast themes. Measure task outcomes and switching
behavior over sustained use.

**Disconfirmation target:** if customization produces errors from inconsistent
semantics or does not improve outcomes, constrain options while preserving
system preferences.

## Research debt and open questions

- Direct evidence connecting WCAG ratios to modern variable fonts, high-density
  displays, and representative low-vision task performance is limited.
- APCA needs independent, preregistered comparison against alternatives across
  affected populations and real tasks.
- Better models are needed for local contrast over images, gradients,
  transparency, and HDR tone mapping.
- CVD simulation should be compared with affected-user discrimination across
  modern wide-gamut displays.
- Forced-colors behavior needs cross-browser and component-library field data.
- The interaction of photophobia, contrast sensitivity, total luminous area,
  and sustained fatigue needs stronger trials.
- More evidence is needed for low-vision users with multiple simultaneous
  impairments, not diagnosis-isolated samples.
- Semantic color meaning must be tested cross-culturally and separated from
  simple visual discriminability.
- Non-Latin scripts may have different stroke-density and size requirements.
- Visual accessibility under outdoor mobile conditions, AR/VR, and automotive
  use cannot be inferred from desktop WCAG calculations alone.

## Theory impact

### Retain

- contrast and appearance are relational and viewing-condition dependent;
- color should be modeled in layers;
- redundant encoding is a governing safety principle;
- historical color theory is a vocabulary, not a causal law.

### Revise

- replace “use perceptually meaningful spaces and measurable contrast” with
  “use task-appropriate color spaces, normative contrast floors, independent
  semantic cues, user adaptation, and representative task validation”;
- replace “target stronger contrast for critical information” with a bounded
  reserve rule that also protects against excess luminance and forced polarity;
- make observer, task, geometry, luminance environment, device, and state
  mandatory fields in contrast evidence.

### Do not promote yet

- a repository-wide APCA requirement;
- a universal internal contrast ratio beyond WCAG;
- an approved categorical palette;
- a claim that OKLCH or CAM16-UCS distance establishes accessibility;
- light or dark mode as the universally preferred accessible theme.

## Repository updates proposed

1. Add REP-VE-COL-001 as a research-draft execution package.
2. Add VE-COL-H3 through VE-COL-H6 to the future hypothesis registry checkpoint.
3. Add EV-VE-COL-001 through EV-VE-COL-020 to the future evidence registry,
   after ID-collision and bibliography audit.
4. Update `agent-context/UI-FOUNDATIONS.md` to distinguish conformance floor,
   contrast reserve, absolute luminance, and user customization.
5. Add forced-colors and multi-severity CVD checks to
   `agent-context/UI-DECISION-CHECKLIST.md`.
6. Preserve `DF-ATLAS-COLOR-005` but add a warning that color-difference metrics
   do not validate text or UI contrast.
7. Gate the section's engineering-validation prompt on affected-user testing
   plans and a versioned metric tournament.

No canonical file was changed by this package.

## Research journal

### Cycle 1 — standards

Inspected WCAG 2.2 text, enhanced text, non-text contrast, use-of-color, and
official rationale. Expected a strong empirical threshold basis. Found a useful
but simplified derivation, changing the interpretation from human threshold to
conformance proxy.

### Cycle 2 — low vision

Searched contrast sensitivity, reading contrast, polarity, glare, and digital
reading studies. Expected “higher is better” with a possible plateau. Found
large observer heterogeneity, polarity reversals linked to ocular scatter, and
conflicting luminance needs from photophobia.

### Cycle 3 — color-vision deficiency

Searched prevalence, congenital/acquired mechanisms, simulation, and accessible
visualization. Rejected the “8% of men” universal statement. Retained
multi-channel redundancy and simulation as a screen, not proof.

### Cycle 4 — metric challenge

Compared WCAG, APCA status, Oklab/OKLCH, CAM16, and uniform color-difference
evidence. Found that these address different target variables. APCA's W3C status
was weaker than common design discourse suggests.

### Cycle 5 — environmental and implementation boundaries

Reviewed polarity, pupil-size, cockpit adaptation, display glare, CSS forced
colors, and user preferences. Concluded that absolute luminance, total area,
adaptation, rendering, and customization are first-class variables.

### Search strategies recorded

- official-domain searches for WCAG 2.2, WCAG 3, low-vision requirements,
  forced colors, CSS Color 4, and CIECAM16;
- PubMed/PMC searches combining low vision, contrast sensitivity, reading,
  polarity, ambient illumination, aging, and CVD;
- title/author search for the Machado CVD simulation model;
- repository-wide `rg` for contrast, CVD, APCA, OKLCH, ΔE, low vision, and
  existing Project Atlas claims;
- contradiction-first searches for maximum contrast, dark-mode advantage,
  WCAG empirical validation, and APCA approval status.

### Access limitations

- Several standards referenced by WCAG (older ISO and ANSI documents) were not
  freely available in full.
- Some primary papers were accessible only through abstracts.
- No original participant testing was performed.
- The search was broad but not a formal systematic review with dual screening,
  protocol registration, or database export.

### Exact resume point

Next, execute the four experiments above or perform a preregistered systematic
review of interface contrast studies after 2008. Before registry integration,
audit IDs, normalize full bibliographic records, and have a low-vision/CVD
specialist and affected-user reviewers challenge the engineering defaults.

## Sources

### Standards and official guidance

- W3C. [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/).
- W3C. [Understanding SC 1.4.6: Contrast (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html).
- W3C. [Understanding SC 1.4.11: Non-text Contrast](https://www.w3.org/WAI/WCAG22/understanding/non-text-contrast.html).
- W3C. [Technique G111: Using color and pattern](https://www.w3.org/WAI/WCAG22/Techniques/general/G111.html).
- W3C. [Accessibility Requirements for People with Low Vision](https://www.w3.org/TR/low-vision-needs/).
- W3C. [CSS Color Adjustment Module Level 1](https://www.w3.org/TR/css-color-adjust-1/).
- W3C. [CSS Color Module Level 4](https://www.w3.org/TR/css-color-4/).
- W3C. [WCAG 3.0 Working Draft](https://www.w3.org/TR/wcag-3.0/).
- W3C. [Visual Contrast of Text Subgroup archive](https://www.w3.org/WAI/GL/task-forces/silver/wiki/Visual_Contrast_of_Text_Subgroup).
- CIE. [CIE 248:2022, CIECAM16](https://www.cie.co.at/publications/cie-2016-colour-appearance-model-colour-management-systems-ciecam16).

### Research and reviews

- Rubin GS, Legge GE. [Psychophysics of reading VI: the role of contrast in low vision](https://pubmed.ncbi.nlm.nih.gov/2788957/). *Vision Research*. 1989.
- Giacomelli G, et al. [Contrast reduction and reading: assessment and reliability with the Reading Explorer test](https://pubmed.ncbi.nlm.nih.gov/19882511/). 2010.
- Legge GE. [Reading Digital with Low Vision](https://pmc.ncbi.nlm.nih.gov/articles/PMC5726769/). *Visible Language*. 2017.
- Crossland MD, et al. [Online Survey of Digital Reading by Adults with Low Vision](https://pmc.ncbi.nlm.nih.gov/articles/PMC7172011/). 2020.
- Piepenbrock C, Mayr S, Buchner A. [Smaller pupil size and better proofreading performance with positive polarity displays](https://pubmed.ncbi.nlm.nih.gov/25135324/). *Ergonomics*. 2014.
- Buchner A, Mayr S, Brandt M. [The advantage of positive text-background polarity is due to high display luminance](https://pubmed.ncbi.nlm.nih.gov/19562598/). *Ergonomics*. 2009.
- Jeong YD, et al. [Global prevalence of congenital color vision deficiency among children and adolescents, 1932–2022](https://pubmed.ncbi.nlm.nih.gov/40769301/). *Ophthalmology*. 2025.
- National Research Council. [Tests of Visual Functions](https://www.ncbi.nlm.nih.gov/books/NBK207559/). In *Visual Impairments*. 2002.
- Machado GM, Oliveira MM, Fernandes LAF. [A physiologically-based model for simulation of color vision deficiency](https://pubmed.ncbi.nlm.nih.gov/19834201/). *IEEE TVCG*. 2009.
- Nuñez JR, Anderton CR, Renslow RS. [Optimizing colormaps with consideration for color vision deficiency](https://pmc.ncbi.nlm.nih.gov/articles/PMC6070163/). *PLOS ONE*. 2018.
- Huang M, et al. [Testing uniform colour spaces using colour differences of a wide colour gamut](https://pubmed.ncbi.nlm.nih.gov/33726273/). *Optics Express*. 2021.
- Silverstein LD, et al. [Luminance and luminance contrast requirements for legibility of self-luminous displays in aircraft cockpits](https://pubmed.ncbi.nlm.nih.gov/15676594/). *Aviation, Space, and Environmental Medicine*. 2005.

## Completion self-audit

**What did I expect?** A tiered recommendation centered on 4.5:1, 7:1, and a
color-blind palette.

**What most challenged it?** Low-vision polarity reversals, photophobia plus
reduced contrast sensitivity, the indirect WCAG ratio derivation, and the
explicitly unapproved status of archived APCA work at W3C.

**Strongest conclusion:** contrast compliance is necessary but cannot be a
complete model of visual accessibility. Independent evidence converges on
geometry, observer, adaptation, redundancy, and customization.

**Most fragile conclusion:** using 7:1 as a candidate internal target for
critical ordinary text. It is prudent but not established as universally
optimal; it requires task and population validation.

**Likely overgeneralization risk:** transferring reading and cockpit findings to
all interactive components.

**Missing stakeholders:** people with combined low vision and CVD, photophobia,
non-Latin-script readers, mobile outdoor users, and users of high-contrast
assistive themes.

**What would a skeptical expert dispute?** The evidence grade, the treatment of
APCA, whether preference justifies theme support, and whether “contrast reserve”
can guide design without a fixed number.

**What evidence would most change the roadmap?** Independent, preregistered
trials comparing contrast metrics across representative affected users,
typographies, devices, lighting conditions, and consequential interface tasks.

**Reconstructability:** source classes, accepted/rejected evidence, hypotheses,
contradictions, queries, limitations, proposed updates, and exact next work are
recorded above.

