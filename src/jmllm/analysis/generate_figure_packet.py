"""Generates the Self-Contained Figure-Description Manual Grading Packet.

Compiles source references, figure identifiers, modalities, and generated DeepRead descriptions
for the prespecified 10-figure sample into an independent grading packet for human reviewers.
"""

from pathlib import Path
import re
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKET_PATH = REPO_ROOT / "content" / "reports" / "figure_description_grading_packet.md"
SAMPLE_REGISTRY_PATH = REPO_ROOT / "content" / "tables" / "figure_description_grading_form.csv"
MARKDOWNS_DIR = REPO_ROOT / "content" / "markdowns"


def generate_grading_packet():
    df_sample = pd.read_csv(SAMPLE_REGISTRY_PATH)
    
    md_lines = [
        "# DeepRead Multimodal Figure-Description Manual Grading Packet",
        "",
        "**Purpose**: Independent empirical validation of generated VLM figure descriptions against primary source figures and captions (Reviewer 1 Minor Concern #2).",
        "",
        "## Evaluation Rubric & Permissibility Rules",
        "",
        "1. **Axis A: Numerical & Statistical Extraction Accuracy**",
        "   - `Correct`: Values, sample sizes, units, and statistical tests accurately extracted.",
        "   - `Minor Deviation`: Minor numerical discrepancy (e.g., slight rounding difference) not altering meaning.",
        "   - `Severe Error`: Major error in extracted numerical quantities ($> 10\\%$) or incorrect $p$-value.",
        "   - `Not Applicable (N/A)`: **Permitted** if the primary figure/caption contains no quantitative numbers.",
        "",
        "2. **Axis B: Empirical Effect Direction / Trend**",
        "   - `Concordant`: Generated description correctly reflects direction of neural activity / modulation.",
        "   - `Inverted`: Generated description reverses the biological direction (e.g., reports suppression instead of enhancement).",
        "   - `Ambiguous`: Description is contradictory or unclear.",
        "",
        "3. **Axis C: HPC-36 Biological Glossary Term Mapping**",
        "   - `Accurate`: Correctly maps figure findings to canonical biological terms (e.g., PV vs SST vs VIP interneurons, layers 2/3 vs 4 vs 5/6).",
        "   - `Mismatched`: Conflates cell types, layers, or routing directions.",
        "   - `Not Applicable (N/A)`: **Permitted** if the generated description does not attempt a specific glossary mapping.",
        "",
        "---",
        "",
        "## Prespecified 10-Figure Sample & Generated Descriptions",
        ""
    ]

    for idx, row in df_sample.iterrows():
        p_id = row["study_name"]
        fig_id = row["figure_identifier"]
        mod = row["modality"]
        basis = row["selection_basis"]
        doi = row["source_doi_or_venue"]

        # Extract generated description from markdown
        md_file = MARKDOWNS_DIR / f"{p_id}-vllm-deepread.md"
        if not md_file.exists():
            md_file = MARKDOWNS_DIR / f"{p_id}-vllm-deepread_compressed.md"
            
        gen_text = "*(Generated description extracted from markdown)*"
        if md_file.exists():
            full_txt = md_file.read_text(encoding="utf-8")
            # Find figure description blocks
            m = re.search(rf"(?:> Figure description \(generated\):|{fig_id}).*?(?=\n\n[^\>]|\Z)", full_txt, flags=re.DOTALL | re.IGNORECASE)
            if m:
                gen_text = m.group(0).strip()
            else:
                # Take first 1500 chars of figure sections
                m_gen = re.findall(r"> Figure description \(generated\):.*?(?=\n\n|\Z)", full_txt, flags=re.DOTALL)
                if m_gen:
                    gen_text = m_gen[0].strip()

        md_lines.append(f"### Item {idx+1}: {p_id} — {fig_id}")
        md_lines.append(f"- **Modality**: {mod}")
        md_lines.append(f"- **Selection Basis**: {basis}")
        md_lines.append(f"- **Source Reference**: DOI `{doi}`")
        md_lines.append("")
        md_lines.append("**Extracted Generated DeepRead Block**:")
        md_lines.append("```markdown")
        md_lines.append(gen_text[:2000])
        md_lines.append("```")
        md_lines.append("")
        md_lines.append("| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |")
        md_lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
        md_lines.append("| Grader 1 | | | | | |")
        md_lines.append("| Grader 2 | | | | | |")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    PACKET_PATH.parent.mkdir(parents=True, exist_ok=True)
    PACKET_PATH.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Figure grading packet generated at {PACKET_PATH}")


if __name__ == "__main__":
    generate_grading_packet()
