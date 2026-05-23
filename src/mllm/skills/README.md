# MLLM Skills: Ontology-Constrained Evidence Mapping

## Skill Categories

### 1. Glossaries (`glossary/`)
These skills provide the foundational ontology for evaluation. 
- **HPC-36**: A 36-factor neurophysiological glossary organizing predictive coding findings into H1 (Suppression), H2 (Error), and H3 (Ubiquity).
- **HPC-Ontogram**: A high-fidelity 3D visualization of the glossary's structure and logical relationships (created March 28, 2026).

### 2. Instructions (`instructions/`)
Guidelines for structured scoring, context separation, and output validation.
- **Scoring Methodology**: Mandatory guidelines for evidence-based factor scoring, requiring specific figure/text evidence for non-null scores.
- **Multi-Agent Consensus**: Protocol for calculating mean-square-distance references and council-level agreement metrics.

### 3. Prompts (`prompts/`)
Prompt templates and system messages for model-council evaluation.

## Manuscript Alignment
- **HPC-36 ontology**: Maintains the three hypothesis families used in the manuscript: predictive suppression, feedforward error propagation, and ubiquity.
- **Local/global context separation**: Preserves separate scoring for local oddball and global oddball evidence.
- **Council analysis**: Supports downstream Agent Consistency, Literature Consistency, Literature-Agent Consistency, and hypothesis-space geometry analyses.
