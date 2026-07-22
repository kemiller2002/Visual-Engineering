# Migration Plan

Generated: 2026-07-21T15:32:33+00:00

## Principles

- No big-bang rewrite
- Preserve original filenames in intake history
- Promote canonical artifacts first
- Generate indexes before moving large volumes of files

## Phase A: Stabilize Intake

- Freeze `input-documents` as an intake area.
- Generate repository manifest and quality reports on every run.
- Add metadata to files currently missing front matter.

## Phase B: Establish Canonical Layer

- Promote governance, ontology, genome, methodology, and library documents into `content/projects/*/canonical`.
- Create concept pages for the highest-frequency concepts first.

## Phase C: Resolve Duplicates And Lineage

- Merge exact duplicates:
- Composition_Science_Research_Library_v0.2 2.md
- Composition_Science_Research_Library_v0.2.md
- Project_Atlas_Visual_Information_Transfer_Foundations_v1 2.md
- Project_Atlas_Visual_Information_Transfer_Foundations_v1.md

## Phase D: Move Derived Research

- Move derived reports and case studies into project collections:
- Composition_Science_Architecture_Human_Scale_and_Proportion_Research.md
- Composition_Science_Phase_2_Visual_Hierarchy_and_Wayfinding.md
- Composition_Science_Phase_3_Evidence_Review_Attention_Wayfinding.md
- Composition_Science_Research_Library_v0.1.md
- Composition_Science_Research_Library_v0.4.md
- Project_Atlas_Applied_Case_Study_001_Account_Settings_Form.md
- Project_Atlas_Autonomous_Research_Itten_Seven_Contrasts_v0.1.md
- Project_Atlas_Autonomous_Research_Report_001_Relational_Legibility.md
- Project_Atlas_Color_Vocabulary_and_Mechanism_Taxonomy.md
- Project_Atlas_Evidence_Gallery_v0.1.md
- Project_Atlas_Foundation_Research_Plan.md
- Project_Atlas_Letter_Confusion_Data_Audit_v1.md
- Project_Atlas_Masters_vs_Modern_Science_02_Josef_Albers_v0.1.md
- Project_Atlas_Perceptual_Color_Genome.md
- Project_Atlas_Project_Charter_v0.1.md
- Project_Atlas_Research_Methodology_v0.2.md

## Phase E: Normalize Names

- Rename inconsistent intake files into slug and ID-backed forms:
- ATLAS-0001_Proximity_and_Relative_Separation_v0.1.md
- Architecture_as_a_Foundation_for_Composition_Science.md
- Composition_Science_Markdown_Template_v1.md
- Composition_Science_Visual_Density_Crowding_and_Perceptual_Separation.md
- GN-100_Perception_Autonomous_Research_Report_v1.md
- Product_Genome_Autonomous_Research_Run_01.md
- Project_Atlas_Color_Evidence_Registry_v0.1.md
- Project_Atlas_Comparative_Color_Framework_v0.1.md
- Project_Atlas_Foundational_Documents_and_Ribbon_Evidence_Collection_001.md
- Project_Atlas_Masters_vs_Modern_Science_01_Chevreul_v0.1.md
- Project_Atlas_Rosetta_Stone_Cross_System_Design_Mechanism_Map_v0.1.md

## Phase F: Generate Registries And Site

- Build evidence, hypothesis, experiment, and decision registries from metadata and document sections.
- Publish the generated website only after validation gates pass.

## Exit Condition

The repository exits migration mode when canonical concepts, registries, and search indexes are generated automatically and intake documents can be promoted without manual navigation edits.
