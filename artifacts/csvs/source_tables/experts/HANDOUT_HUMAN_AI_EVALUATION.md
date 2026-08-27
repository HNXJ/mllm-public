# Handout: Bidirectional Human+AI Expert Evaluation Protocol (`hpchai_01` & `hpchai_02`)

This document is a self-contained instruction handout to paste into a new agent chat to execute the dual-pass **Human+AI literature evaluation** across the 31 canonical predictive-processing papers.

---

## 📋 Mission Overview & Scientific Role

You are acting as a **Senior Computational Neuroscientist & Biophysicist Expert Reviewer (Human+AI Evaluation Panel)**.

Your objective is to evaluate all **31 canonical scientific papers** against the **HPC-36 ontology** across two experimental contexts:
- **LO**: Local Oddball paradigm
- **GO**: Global Oddball paradigm

To ensure order-fairness and capture both initial-context and cumulative-synthesis effects, you will execute **two independent passes**:
1. **`hpchai_01` (Try 1 - Forward Pass)**: Evaluate papers in order **$1 \longrightarrow 31$**.
2. **`hpchai_02` (Try 2 - Reverse Pass)**: Evaluate papers in order **$31 \longrightarrow 1$**.

---

## 🛠️ Canonical Ground Truth & Resources

- **Ontology Glossary**: [`ontology/glossary/HPC/hpc-36-reference.md`](file:///Users/hamednejat/workspace/main/mllm-public/ontology/glossary/HPC/hpc-36-reference.md)
  - **H1 (IDs 1–12)**: Predictive Suppression
  - **H2 (IDs 13–24)**: Feedforward Error Propagation
  - **H3 (IDs 25–36)**: Hierarchical Ubiquity
- **Evaluation Prompt Rubric**: [`ontology/instructions/hpc_eval_prompt.md`](file:///Users/hamednejat/workspace/main/mllm-public/ontology/instructions/hpc_eval_prompt.md)
- **Scoring Scale**: Floating point in $[-1.0, +1.0]$, or `null` if the paper does not address the factor:
  - `+1.0`: Strong quantitative evidence SUPPORTS
  - `+0.6`: Moderate evidence SUPPORTS
  - `+0.2`: Weak evidence SUPPORTS
  - `0.0`: Neutral / no evidence
  - `-0.2`: Weak evidence AGAINST
  - `-0.6`: Moderate evidence AGAINST
  - `-1.0`: Strong quantitative evidence CONTRADICTS
  - `null`: Factor unaddressed (*prefer null over 0.0 for unmentioned mechanisms*)

---

## 📚 Canonical 31-Paper List (Ordered 1 to 31)

Located in `content/markdowns/*-vllm-deepread_compressed.md`:

```text
 1. Attinger2017           11. Hertag2020            21. Rao&Ballard1999      31. Yamins2014
 2. Bakhtiari2021          12. Jiang&Rao2024         22. Rao2024
 3. Bastos2012             13. Keller2012            23. Sacramento2018
 4. Bastos2020             14. Keller2018            24. Spratling2008
 5. Bekinschtein2009       15. Kiebel2008            25. Spratling2010
 6. Chao2018               16. LaoRodriguez2023      26. Srinivasan1982
 7. Friston2010            17. LeeMejias2025         27. VanDerveer2021
 8. Furutachi2024          18. Mikulasch2023         28. Wacongne2011
 9. Garret2020             19. Nejad2025             29. Wacongne2012
10. Greedy2022             20. Payeur2021            30. Westerberg&Xiong2025
```

---

## 📝 Required Output Format & Table Schema

Output must be formatted as a 90-column CSV matching `examples/hpc_table_final.csv`:

```text
study_name,agent_,year_,type_,LO-count,GO-count,LO-H1-avg,LO-H1-std,LO-H2-avg,LO-H2-std,LO-H3-avg,LO-H3-std,GO-H1-avg,GO-H1-std,GO-H2-avg,GO-H2-std,GO-H3-avg,GO-H3-std,LO-F01..LO-F36,GO-F01..GO-F36
```

### Destination Files:
- **Forward Pass ($1 \to 31$)**: Write to [`content/tables/experts/human_ai/hpchai_01.csv`](file:///Users/hamednejat/workspace/main/mllm-public/content/tables/experts/human_ai/hpchai_01.csv) (`agent_ = 'hpchai_01'`)
- **Reverse Pass ($31 \to 1$)**: Write to [`content/tables/experts/human_ai/hpchai_02.csv`](file:///Users/hamednejat/workspace/main/mllm-public/content/tables/experts/human_ai/hpchai_02.csv) (`agent_ = 'hpchai_02'`)
- **Combined Panel**: Concatenate both into [`content/tables/experts/human_ai/hpchai_all.csv`](file:///Users/hamednejat/workspace/main/mllm-public/content/tables/experts/human_ai/hpchai_all.csv) (62 rows $\times$ 90 cols).

---

## 🚀 Prompt to Paste into New Agent Chat

```text
You are a Senior Computational Neuroscientist and Biophysicist performing the official Human+AI expert evaluations for the Scientific Reports revision.

Follow the protocol in content/tables/experts/HANDOUT_HUMAN_AI_EVALUATION.md:

1. Perform Pass 1 (Forward, 1 -> 31):
   - Read each of the 31 papers in content/markdowns/*-vllm-deepread_compressed.md in order 1 to 31.
   - Score all 36 HPC ontology factors from ontology/glossary/HPC/hpc-36-reference.md for both LO and GO contexts following ontology/instructions/hpc_eval_prompt.md.
   - Save the resulting 31-row, 90-column CSV to content/tables/experts/human_ai/hpchai_01.csv with agent_='hpchai_01'.

2. Perform Pass 2 (Reverse, 31 -> 1):
   - Re-evaluate all 31 papers in reverse order (31 down to 1), applying cumulative contextual synthesis.
   - Save the resulting 31-row, 90-column CSV to content/tables/experts/human_ai/hpchai_02.csv with agent_='hpchai_02'.

3. Combine both passes into content/tables/experts/human_ai/hpchai_all.csv (62 rows).

4. Compute the deviance (MSD, MAE, Pearson r, sign agreement) between hpchai_01 and hpchai_02 to measure human+AI re-test reliability across evaluation order.
```
