# Universal Scoring Methodology

## Scoring Scale
The default scoring scale ranges from -1.0 to +1.0 with `np.nan` for unaddressed factors.

| Score | Meaning |
|-------|---------|
| +1.0  | Strong quantitative evidence SUPPORTS the factor |
| +0.6  | Moderate evidence SUPPORTS the factor |
| +0.2  | Weak evidence SUPPORTS the factor |
| 0.0   | No evidence found, or neutral/contradictory result |
| -0.2  | Weak evidence AGAINST the factor |
| -0.6  | Moderate evidence AGAINST the factor |
| -1.0  | Strong quantitative evidence CONTRADICTS the factor |
| np.nan| Factor is NOT mentioned or cannot be evaluated |

**Granularity**: Use intermediate floats (e.g., 0.8, -0.3) for precision.

## Key Rules
1. **0.0 vs np.nan**: 
   - `0.0`: The study addresses the factor but finds no evidence or a neutral result.
   - `np.nan`: The study does not mention or address the factor at all.
   - *When in doubt, prefer `np.nan` over `0.0` to avoid false negatives.*

2. **Evidence Priority**:
   - Direct quantitative results (figures, tables, statistics) — highest weight.
   - Qualitative descriptions — acceptable when quantitative data unavailable.
   - Methodological observations — for “Methodological” tagged factors.

3. **Context Independence**:
   - Each context (LO vs GO) must be scored independently.
   - Do not average or conflate scores across contexts.

4. **Reasoning Log**:
   - For non-`np.nan` scores: Cite specific sections, figures, or tables. Justify magnitude.
   - For `np.nan` scores on expected factors: Explain why it was marked missing.
   - For `0.0` scores: What evidence was considered and why it was neutral.
   - For non-zero scores: Explain the reason or evidence clearly.
