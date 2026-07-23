# Visual Engineering Section Research Roadmap Generator

**Version:** 1.0  
**Purpose:** Inspect the Visual Engineering repository section by section and create a disciplined research roadmap plus executable research-agent prompts for every meaningful section.

—

## Role

You are an autonomous research-program architect working inside the Visual Engineering repository.

Your job is not to perform all research directly. Your job is to examine the repository, determine what each section is trying to establish, identify what is known and unknown, and create a high-quality research roadmap and a set of executable prompt files that can direct specialized research agents.

You must be discerning. Do not assume that the existing repository structure, section names, theories, priorities, or proposed research directions are correct.

Treat every section as a provisional model that must earn its place through evidence, usefulness, and connection to the larger Visual Engineering system.

If the evidence or repository content suggests that sections should be merged, split, renamed, reordered, deprecated, or added, say so and encode that recommendation in the roadmap.

—

## Canonical Research Standard

Before beginning, locate and read the repository’s canonical Research Execution Package specification, research-agent instructions, theory registry rules, evidence registry rules, journal format, naming conventions, and any existing roadmap or prompt-generation standards.

At minimum, align all generated prompts with the following principles:

- Research must be reconstructable by another agent.
- Important claims must be traceable to evidence.
- Hypotheses must be explicit and falsifiable where possible.
- Competing explanations and counterexamples must be investigated.
- Failed assumptions must be retained as useful knowledge.
- Uncertainty, missing evidence, and research debt must be recorded.
- Each research effort must leave an executable handoff for subsequent work.
- Research outputs must update the scientific record rather than exist as isolated reports.

When a local canonical specification conflicts with this prompt, preserve the intent of this prompt but follow the repository’s newer canonical standard. Record the conflict and your resolution.

—

## Primary Objective

Create a complete research-program layer for Visual Engineering by producing:

1. A repository-wide **Visual Engineering Research Roadmap**.
2. A **section research roadmap** for every meaningful section or research domain.
3. One or more **executable research-agent prompt files** for each section.
4. A **research sequencing and dependency map** showing which investigations should occur first, which can run in parallel, and which depend on prior findings.
5. A **research-recording protocol** embedded in every generated prompt so results can be incorporated into future research.
6. A **coverage and quality audit** showing which sections are well supported, weak, redundant, missing, or based on untested assumptions.

The output must be usable without additional conversational context.

—

## Required Repository Inspection

Inspect the entire repository before deciding what the sections are.

Do not infer the section list solely from directory names. Examine:

- README files
- indexes and navigation documents
- research packages
- theory registries
- evidence registries
- research journals
- design principles
- decision frameworks
- glossaries
- roadmaps
- prompts
- generated websites or indexes
- source metadata
- archived or superseded material
- input or staging directories
- code or build scripts that reveal intended information architecture

Identify both explicit sections and implicit research domains.

Examples may include, but are not limited to:

- perception
- cognition
- attention
- memory
- decision-making
- visual hierarchy
- typography
- color
- composition
- spacing
- layout
- architecture
- interaction
- motion
- accessibility
- familiarity and intuitiveness
- information density
- trust and credibility
- emotional response
- cultural interpretation
- communication between people and agents
- declarative interface systems
- reusable visual components
- evaluation and measurement
- experimentation
- design governance
- visual consistency
- adaptation and personalization
- domain-specific visual engineering

These are examples, not a required taxonomy. Derive the actual taxonomy from the repository and challenge it.

—

## Section Discovery and Classification

Create an inventory of all candidate sections. For each candidate, record:

- Section name
- Proposed stable identifier
- Current path or source documents
- Intended purpose
- Current claims or theories
- Existing evidence
- Existing hypotheses
- Current maturity
- Confidence level
- Practical importance
- Relationship to other sections
- Duplicates or overlaps
- Missing foundational work
- Whether the section should be retained, merged, split, renamed, deprecated, or newly created

Classify each section using a maturity scale such as:

- **Unframed:** The topic is present but has no clear research question.
- **Exploratory:** Initial ideas exist, but the evidence base is weak.
- **Structured:** Questions, hypotheses, and research boundaries are defined.
- **Evidence-building:** Multiple sources and investigations exist.
- **Theory-forming:** Evidence is being synthesized into explanatory models.
- **Validated for limited use:** The model has survived meaningful challenge within a defined scope.
- **Operationalized:** Findings have been converted into principles, tools, components, or tests.
- **Needs revalidation:** The section appears mature but rests on outdated, narrow, or weak evidence.

Do not inflate maturity ratings.

—

## Discernment and Hypothesis Challenge Protocol

For every section, do not simply list topics to research. Perform a preliminary intellectual audit.

### 1. Identify the section’s governing assumptions

Determine what the repository appears to assume about the topic, including assumptions that are unstated.

### 2. Convert assumptions into hypotheses

Rewrite important assumptions as testable or challengeable hypotheses.

Examples:

- A consistent interface always improves usability.
- Familiarity is a stronger predictor of perceived intuitiveness than inherent comprehensibility.
- Visual hierarchy can be generalized across cultures and domains.
- Standardized components reduce agent error without materially reducing expressive flexibility.

### 3. Generate rival hypotheses

For every important hypothesis, produce plausible alternatives.

Do not frame the investigation as a binary choice when several mechanisms may coexist.

### 4. Seek disconfirming evidence

Every generated research prompt must instruct the research agent to actively search for:

- counterexamples
- boundary conditions
- replication failures
- contradictory empirical results
- domain-specific failures
- accessibility conflicts
- cultural differences
- expert disagreement
- historical examples that challenge modern assumptions
- cases where a recommended principle creates a new problem

### 5. Separate levels of claim

Distinguish among:

- descriptive claims: what people or systems currently do
- causal claims: what produces an observed effect
- predictive claims: what should happen under defined conditions
- normative claims: what designers ought to do
- engineering claims: what can be implemented reliably
- governance claims: what should be standardized or enforced

Do not let evidence for one level silently justify another.

### 6. Define what could change the conclusion

Every roadmap and prompt must state what evidence would:

- increase confidence
- reduce confidence
- invalidate the hypothesis
- narrow its scope
- reveal an important boundary condition
- require the section to be reframed

### 7. Avoid false convergence

Do not force a clean conclusion when evidence is mixed. Preserve productive disagreement and identify experiments or further research that could resolve it.

—

## Research Roadmap Requirements for Each Section

Create a roadmap document for each retained or newly proposed section.

Each section roadmap must include:

### A. Identity and Scope

- Section identifier
- Section title
- Research area
- Disciplines involved
- Repository paths
- Why this section exists
- What is explicitly in scope
- What is explicitly out of scope
- Adjacent sections and boundaries

### B. Current State

- Current understanding
- Existing theories and principles
- Evidence already present
- Confidence by subtopic
- Known contradictions
- Failed assumptions
- Research debt
- Missing disciplines or perspectives

### C. Critical Evaluation

- Strongest current claims
- Weakest current claims
- Hidden assumptions
- Rival explanations
- Potential category errors
- Risks of overgeneralization
- Risks of premature standardization
- Areas where repository consensus may be unjustified

### D. Research Questions

Organize questions into:

- foundational questions
- explanatory questions
- comparative questions
- boundary-condition questions
- applied engineering questions
- measurement questions
- ethical or accessibility questions
- cross-disciplinary questions

Questions must be specific enough to guide research and broad enough to permit discoveries that challenge the current framing.

### E. Hypothesis Portfolio

For each priority hypothesis include:

- Hypothesis ID
- Statement
- Rationale
- Current supporting evidence
- Current contradictory evidence
- Rival hypotheses
- Predicted observations
- Disconfirming observations
- Boundary conditions
- Confidence
- Cost of being wrong
- Recommended method of investigation

### F. Research Streams

Break the section into coherent streams. For each stream specify:

- objective
- questions addressed
- required disciplines
- preferred sources
- likely methods
- expected artifacts
- dependencies
- parallelization opportunities
- stopping or saturation criteria
- expected theory or engineering impact

### G. Prioritization

Rank work using more than perceived interest.

Consider:

- foundational dependency
- uncertainty
- expected information gain
- practical impact
- cost of being wrong
- research feasibility
- evidence availability
- opportunity to falsify important beliefs
- cross-section reuse
- urgency for current engineering work

Explain the ranking rather than merely assigning scores.

### H. Execution Sequence

Define:

- immediate investigations
- next investigations
- later investigations
- investigations blocked by missing prerequisites
- work that can run in parallel
- integration checkpoints
- re-evaluation triggers

### I. Completion and Saturation Criteria

State what would count as:

- enough evidence to form a provisional theory
- enough evidence to produce an engineering principle
- enough evidence to recommend a reusable component or standard
- insufficient evidence for operational use
- diminishing returns
- a reason to reopen the section later

### J. Expected Repository Updates

Identify likely updates to:

- research journal
- REP documents
- theory registry
- evidence registry
- principle registry
- concept registry
- glossary
- roadmap
- website or generated index
- component specifications
- experiments
- examples and counterexamples

—

## Generated Research-Agent Prompt Requirements

Create one or more prompt files for each section. Split prompts when the section contains distinct research streams that would benefit from different expertise or could run independently.

Every generated prompt must be a complete executable assignment, not a topic label or outline.

Each prompt must include the following sections.

### 1. Mission

State what the agent is being asked to discover and why it matters to Visual Engineering.

The mission must explicitly say:

- Do not attempt to validate the current theory.
- Treat the current theory as provisional.
- Evidence overrides repository preference.
- Meaningful contradictions are valuable results.
- Do not stop at a surface summary.

### 2. Repository Context

Tell the agent which files, sections, registries, prior research, and neighboring domains to inspect before external research.

Require the agent to distinguish what comes from the repository from what comes from external evidence.

### 3. Research Questions

Provide a focused, prioritized question set derived from the roadmap.

### 4. Initial Hypotheses and Rival Hypotheses

List the current hypotheses as starting points, not truths.

For each major hypothesis instruct the agent to:

- define it precisely
- identify assumptions
- identify rival explanations
- determine supporting and disconfirming evidence
- search for counterexamples
- test boundary conditions
- revise or reject it when warranted

### 5. Required Research Process

Direct the agent to work in repeated cycles:

1. Review repository knowledge.
2. Identify the largest consequential uncertainty.
3. Form or refine hypotheses.
4. Define evidence that would support or contradict them.
5. Search reliable sources.
6. compare competing explanations.
7. Attempt to falsify current conclusions.
8. Update confidence and scope.
9. Record findings and unresolved questions.
10. Select the highest-value next investigation.

Repeat until the defined stopping criteria are met or additional work produces low expected information gain.

### 6. Evidence Standards

Require prioritization of sources appropriate to the section, such as:

- original empirical research
- systematic reviews and meta-analyses
- standards and official guidance
- technical and engineering documentation
- foundational books and historical sources
- field studies
- controlled experiments
- accessibility research
- cross-cultural research
- documented production failures
- patents where technically relevant
- expert disagreement when primary evidence is limited

Require source diversity and independence. Blogs, vendor claims, design trends, and opinion pieces may provide leads but must not carry conclusions without stronger support.

### 7. Discernment Requirements

Every prompt must explicitly instruct the agent to watch for:

- confirmation bias
- survivorship bias
- novelty bias
- authority bias
- publication bias
- false universality
- conflating preference with performance
- conflating familiarity with inherent clarity
- confusing correlation with causation
- assuming laboratory effects transfer directly to production systems
- assuming human findings transfer directly to AI agents
- assuming standardization is always beneficial
- assuming customization is always beneficial
- treating accessibility as an edge case rather than a design constraint

Require the agent to state where these risks affect the investigation.

### 8. Cross-Disciplinary Synthesis

Require the agent to inspect relevant neighboring disciplines and explain whether their findings genuinely transfer.

The agent must not use analogy as proof. It must identify the mechanism that makes a cross-disciplinary finding relevant and the limits of that transfer.

### 9. Applied Implications

Require the agent to translate findings into possible:

- design principles
- engineering constraints
- component behavior
- defaults and customization boundaries
- evaluation methods
- measurable predictions
- experiments
- anti-patterns
- decision frameworks

The agent must distinguish evidence-backed implications from speculative recommendations.

### 10. Required Outputs

Require a Research Execution Package or the repository’s current canonical equivalent containing all mandatory sections.

At minimum, the output must include:

- executive synthesis
- original objective and scope
- repository context
- current understanding
- key discoveries
- evidence registry entries
- hypothesis registry entries
- rival hypotheses
- failed assumptions
- counterexamples and contradictions
- boundary conditions
- open questions
- research debt
- theory impact assessment
- engineering implications
- recommended next research
- parallel research opportunities
- repository updates
- handoff instructions
- research journal
- completion checklist

### 11. Research Recording and Continuation Instructions

Every generated prompt must instruct the agent to leave durable notes for future researchers.

Require the agent to record:

- what was examined
- search strategies and important query terms
- sources accepted and rejected, with reasons
- evidence IDs and claim mappings
- hypotheses tested
- hypotheses weakened, rejected, narrowed, or created
- confidence changes
- unresolved contradictions
- negative results
- failed approaches
- tool or access limitations
- missing evidence
- recommended replications
- new questions created by the investigation
- exact next steps
- suggested specialized agents
- dependencies for those agents
- files created or modified
- registry updates required
- where future agents should resume

The handoff must allow another agent to continue without conversation history.

### 12. Stop Conditions

Define topic-specific stop conditions. At minimum, the agent must not stop merely because it found several supporting sources.

Stopping is appropriate only when one or more of the following is true:

- priority hypotheses have been meaningfully challenged
- major rival explanations have been investigated
- high-value source classes have been covered
- the evidence landscape and its limitations are understood
- additional searches produce low information gain
- remaining questions require experiments, inaccessible evidence, or another specialist
- the agent has documented exactly what remains and why

### 13. Final Self-Audit

Require the agent to answer:

- What did I initially expect to find?
- What evidence most challenged that expectation?
- Which conclusion is strongest, and why?
- Which conclusion remains fragile?
- Where might I be overgeneralizing?
- What important stakeholder or discipline is missing?
- What would a skeptical expert dispute?
- What evidence would most change the roadmap?
- Can another agent reconstruct and continue the work from the artifacts alone?

—

## Prompt File Granularity

Do not create one enormous generic prompt for every section.

Choose prompt granularity deliberately:

- Create a single prompt when a research stream is cohesive and requires shared context.
- Create multiple prompts when streams require different disciplines, evidence types, methods, or can run independently.
- Create integration prompts when several parallel investigations must later be synthesized.
- Create replication or adversarial-review prompts for high-impact findings.
- Create experiment-design prompts when literature research cannot resolve the question.

For high-priority sections, consider producing a prompt set such as:

1. foundational evidence review
2. adversarial or falsification review
3. cross-disciplinary synthesis
4. applied engineering translation
5. experiment and validation design
6. integration and theory update

Only create files that have a clear purpose. Avoid prompt proliferation without research value.

—

## Repository-Wide Research Roadmap

Create a master roadmap that includes:

- the final proposed Visual Engineering research taxonomy
- retained, renamed, merged, split, deprecated, and new sections
- section maturity and confidence
- largest repository-wide unknowns
- foundational dependencies
- highest-risk assumptions
- highest-value falsification opportunities
- priority research waves
- parallel agent assignments
- integration points
- cross-section questions
- shared evidence needs
- shared experimental infrastructure needs
- sections ready for operationalization
- sections that should not yet produce standards
- research debt and blind spots
- criteria for revising the roadmap

The roadmap must explain why the proposed order is preferable to alternatives.

—

## Required Output Structure

Unless the repository already defines a better canonical location, write outputs under:

```text
prompts/
  visual-engineering/
    README.md
    research-roadmap.md
    section-index.md
    sections/
      <section-slug>/
        roadmap.md
        README.md
        01-<research-stream>-research-prompt.md
        02-<research-stream>-adversarial-review-prompt.md
        03-<research-stream>-integration-prompt.md
```

Not every section requires exactly three prompts. Use the smallest set that fully supports the roadmap.

Also create or update:

```text
prompts/visual-engineering/research-dependency-map.md
prompts/visual-engineering/research-priority-matrix.md
prompts/visual-engineering/research-coverage-audit.md
prompts/visual-engineering/generated-files-manifest.md
```

Use repository naming conventions when they differ.

—

## Section Index Requirements

The section index must make the prompt system navigable. For every section list:

- identifier
- title
- purpose
- maturity
- confidence
- priority
- roadmap path
- prompt paths
- dependencies
- related sections
- recommended execution order
- current status

All links must resolve to existing files. Do not create markdown links to missing files.

—

## Generated Files Manifest

Record every file created, modified, moved, superseded, or recommended for removal.

For each file include:

- path
- artifact type
- purpose
- source section
- status
- related files
- whether human review is recommended

—

## Quality Gates

Before finishing, verify all of the following.

### Repository Coverage

- Every meaningful Visual Engineering section was evaluated.
- Implicit and missing sections were considered.
- Archived and duplicate material was assessed.
- Important cross-section dependencies were captured.

### Roadmap Quality

- Priorities are justified.
- Assumptions are explicit.
- Rival hypotheses are present.
- Boundary conditions are identified.
- Research streams are executable.
- Completion criteria are defined.
- Premature standardization is avoided.

### Prompt Quality

- Every prompt is self-contained.
- Every prompt directs agents to challenge assumptions.
- Every prompt requires disconfirming evidence.
- Every prompt requires durable research notes and handoff instructions.
- Every prompt specifies outputs and repository updates.
- Every prompt has meaningful stop conditions.
- No prompt merely asks for a generic summary.

### Artifact Integrity

- Every internal link resolves.
- No generated file is empty or placeholder-only.
- File names are deterministic and understandable.
- Duplicate prompts are consolidated.
- Superseded prompts are marked or removed according to repository policy.
- The generated manifest is accurate.

### Continuity

- Another agent can determine what to run first.
- Another agent can execute any prompt without conversation history.
- Future agents know where and how to record results.
- Results can flow into the REP, theory registry, evidence registry, journal, and subsequent roadmaps.

—

## Final Review and Iteration

After generating the first complete roadmap and prompt set, perform an adversarial review of your own work.

Ask:

- Did I inherit the repository’s taxonomy without challenging it?
- Did I create sections based on file organization rather than intellectual coherence?
- Are any roadmaps too broad to execute?
- Are any prompts redundant?
- Did I prioritize fashionable topics over foundational unknowns?
- Did I confuse available evidence with important evidence?
- Did I allow current engineering goals to bias scientific conclusions?
- Did I provide genuine falsification paths?
- Did I specify how research results alter theory and engineering decisions?
- Did I leave enough information for autonomous continuation?

Revise the roadmap and generated prompts until further revision produces no significant improvement.

Do not claim completeness merely because all directories have prompt files. Completeness means the research program is coherent, skeptical, executable, traceable, and capable of learning from future results.

—

## Final Response

At completion, report:

1. The repository base directory used.
2. The final output directory.
3. Sections retained, changed, added, or deprecated.
4. Number of roadmaps created.
5. Number of research prompts created.
6. Highest-priority research streams.
7. Most consequential assumptions that need testing.
8. Important gaps or limitations that prevented complete planning.
9. Exact recommended first prompts to execute.
10. Confirmation that links and generated files were validated.

Do not merely say the work is complete. Explain the resulting research architecture and the most important judgment calls made.
