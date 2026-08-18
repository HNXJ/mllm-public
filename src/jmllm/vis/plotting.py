import os
import sys
import re
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
from itertools import combinations
try:
    from scipy.cluster import hierarchy
    HAS_SCIENTIFIC = True
except ImportError:
    HAS_SCIENTIFIC = False

# =============================================================================
# CONFIGURATION & CONSTANTS
# =============================================================================
REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CSV_PATH = str(REPO_ROOT / "content" / "202608_temp" / "hpc_table_final.csv")
DEFAULT_REPORTS_DIR = str(REPO_ROOT / "content" / "202608_temp" / "reports" / "manuscript_figures")

HYPOTHESES = ["H1", "H2", "H3"]
CONTEXTS = ["LO", "GO"]
HYPOTHESIS_LABELS = {
    "H1": "Subtractive predictions (H1)",
    "H2": "Feedforward prediction errors (H2)",
    "H3": "Ubiquitous predictions (H3)",
}
TYPE_COLORS = {
    "empirical": "#27ae60",
    "theoretical": "#2980b9",
    "computational": "#2980b9",
    "this work": "#c0392b",
    "other": "#95a5a6",
    "unknown": "#95a5a6",
}
LO_COLOR = "#EF553B"
GO_COLOR = "#636EFA"
AUTUMN_ENHANCED = [[0.0, 'rgb(255, 0, 0)'], [0.8, 'rgb(255, 165, 0)'], [1.0, 'rgb(255, 255, 0)']]

# =============================================================================
# DATA PREPARATION & SCHEMAS
# =============================================================================

def convert_scores_to_hpc_table(scores_csv_path: str, output_csv_path: str = None) -> pd.DataFrame:
    """Converts a raw scores.csv (long format) into the canonical 90-column hpc_table_final.csv schema."""
    glossary_path = REPO_ROOT / "ontology" / "glossary" / "HPC" / "hpc-36-reference.md"
    factor_to_id = {}
    factor_to_h = {}
    current_h = "H1"
    
    if glossary_path.exists():
        lines = glossary_path.read_text(encoding="utf-8").splitlines()
        for l in lines:
            if "## H1:" in l: current_h = "H1"
            elif "## H2:" in l: current_h = "H2"
            elif "## H3:" in l: current_h = "H3"
            elif l.strip().startswith("|") and "Factor Name" not in l and "----" not in l and "Total" not in l:
                parts = [p.strip() for p in l.split("|")]
                if len(parts) >= 4 and parts[1].isdigit():
                    fid = int(parts[1])
                    fname = parts[2]
                    factor_to_id[fname] = fid
                    factor_to_h[fname] = current_h

    scores_df = pd.read_csv(scores_csv_path)
    scores_df["score_num"] = pd.to_numeric(scores_df["score"], errors="coerce")
    scores_df["Hypothesis"] = scores_df["factor"].map(factor_to_h)
    scores_df["factor_id"] = scores_df["factor"].map(factor_to_id)
    
    studies = sorted(scores_df["paper_id"].unique())
    models = sorted(scores_df["scientific_model"].unique())
    
    rows = []
    for s in studies:
        m_year = re.search(r"\d{4}", s)
        year = float(m_year.group(0)) if m_year else 2020.0
        stype = "this work" if "Westerberg" in s else "empirical"
        
        for m in models:
            sub = scores_df[(scores_df["paper_id"] == s) & (scores_df["scientific_model"] == m)]
            if sub.empty:
                continue
                
            row = {
                "study_name": s,
                "agent_": m,
                "year_": year,
                "type_": stype,
            }
            
            for ctx in ["LO", "GO"]:
                ctx_sub = sub[sub["context"] == ctx]
                row[f"{ctx}-count"] = ctx_sub["score_num"].count()
                for h in ["H1", "H2", "H3"]:
                    h_vals = ctx_sub[ctx_sub["Hypothesis"] == h]["score_num"].dropna()
                    row[f"{ctx}-{h}-avg"] = round(h_vals.mean(), 3) if not h_vals.empty else np.nan
                    row[f"{ctx}-{h}-std"] = round(h_vals.std(), 3) if len(h_vals) > 1 else (0.0 if len(h_vals)==1 else np.nan)
                    
                for fid in range(1, 37):
                    fname = [k for k, v in factor_to_id.items() if v == fid]
                    if fname:
                        f_vals = ctx_sub[ctx_sub["factor"] == fname[0]]["score_num"].dropna()
                        row[f"{ctx}-F{fid:02d}"] = round(f_vals.mean(), 3) if not f_vals.empty else np.nan

            rows.append(row)
            
    out_df = pd.DataFrame(rows)
    if output_csv_path:
        Path(output_csv_path).parent.mkdir(parents=True, exist_ok=True)
        out_df.to_csv(output_csv_path, index=False)
        print(f"[*] Generated canonical table: {output_csv_path} ({len(out_df)} study-agent entries)")
    return out_df

def _safe_write_plot(fig, output_dir=None, stem=None, write_html=True, write_svg=False, show=False):
    if output_dir is not None and stem is not None:
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        if write_html:
            fig.write_html(str(out_path / f"{stem}.html"))
        if write_svg:
            try:
                fig.write_image(str(out_path / f"{stem}.svg"))
            except Exception as exc:
                print(f"  [!] SVG export skipped for {stem}: {exc}")
    if show:
        fig.show()
    return fig

def load_hpc_long_table(csv_path, excludes=None):
    df = pd.read_csv(csv_path)
    if "ignore_row" in df.columns:
        df = df[df["ignore_row"].fillna(False).astype(bool) == False]
    for pattern in (excludes or []):
        df = df[~df["study_name"].astype(str).str.contains(pattern, case=False, na=False)]
        
    records = []
    for _, row in df.iterrows():
        for ctx in CONTEXTS:
            records.append({
                "Base Study ID": row["study_name"],
                "Context": ctx,
                "Model Name": row.get("agent_", "unknown"),
                "Study Type": str(row.get("type_", "unknown")).lower(),
                "Year": row.get("year_", 2020),
                "H1": pd.to_numeric(row.get(f"{ctx}-H1-avg"), errors="coerce"),
                "H2": pd.to_numeric(row.get(f"{ctx}-H2-avg"), errors="coerce"),
                "H3": pd.to_numeric(row.get(f"{ctx}-H3-avg"), errors="coerce"),
            })
    return pd.DataFrame(records)

def study_level_scores(csv_path, excludes=None, include_std=True, drop_empty=True):
    df = pd.read_csv(csv_path)
    if "ignore_row" in df.columns:
        df = df[df["ignore_row"].fillna(False).astype(bool) == False]
    for pattern in (excludes or []):
        df = df[~df["study_name"].astype(str).str.contains(pattern, case=False, na=False)]
        
    agg = {"type_": "first"}
    if "year_" in df.columns:
        agg["year_"] = "first"
    cols = [f"{ctx}-{h}-avg" for ctx in CONTEXTS for h in HYPOTHESES]
    if include_std:
        cols.extend([f"{ctx}-{h}-std" for ctx in CONTEXTS for h in HYPOTHESES])
    for col in cols:
        if col in df.columns:
            agg[col] = "mean"
            
    grouped = df.groupby("study_name", dropna=False).agg(agg).reset_index()
    if drop_empty:
        avg_cols = [c for c in grouped.columns if c.endswith("-avg")]
        grouped = grouped.dropna(subset=avg_cols, how="all")
    return grouped.sort_values("study_name").reset_index(drop=True)

def study_labels(grouped):
    names = grouped["study_name"].tolist()
    labels = [str(i + 1) for i in range(len(names))]
    hover = [f"{labels[i]}: {names[i]}" for i in range(len(names))]
    types = grouped["type_"].fillna("unknown").tolist() if "type_" in grouped.columns else ["unknown"] * len(names)
    return names, labels, hover, types

def _hpc_axis_3d(title_text, font_size=10):
    return dict(
        title=dict(text=title_text, font=dict(size=font_size)),
        range=[-1, 1],
        tickvals=[-1, 1],
        ticktext=["Disagree", "Agree"],
        tickfont=dict(size=8, color="#2c3e50"),
        showbackground=False,
        showgrid=True,
        gridcolor="lightgray",
        zeroline=True,
        zerolinecolor="black",
        zerolinewidth=2,
    )

def _study_legend_annotations(labels, names, y=-0.16, cols=5, font_size=10):
    annotations = []
    n = len(labels)
    rows = int(np.ceil(n / cols))
    col_width = 1.0 / cols
    for i, (label, name) in enumerate(zip(labels, names)):
        r = i % rows
        c = i // rows
        x_pos = c * col_width
        y_pos = y - r * 0.03
        annotations.append(dict(
            text=f"<b>{label}:</b> {name}",
            x=x_pos, y=y_pos,
            xref="paper", yref="paper",
            showarrow=False,
            font=dict(size=font_size, color="#2c3e50"),
            align="left", xanchor="left"
        ))
    return annotations

# =============================================================================
# MANUSCRIPT VISUALIZATION SUITE (FIGURES 3, 4, 5, 6, 7, 8)
# =============================================================================

def plot_3d_hpc_spaces(csv_path, excludes=None, output_dir=None, show=False, write_svg=False):
    """Figure 7: 3D Local Oddball (LO) and Global Oddball (GO) HPC Spaces."""
    grouped = study_level_scores(csv_path, excludes=excludes, include_std=True)
    display_names, numeric_labels, hover_labels, study_types = study_labels(grouped)
    figs = {}
    for ctx in CONTEXTS:
        h1 = grouped[f"{ctx}-H1-avg"].to_numpy(dtype=float)
        h2 = grouped[f"{ctx}-H2-avg"].to_numpy(dtype=float)
        h3 = grouped[f"{ctx}-H3-avg"].to_numpy(dtype=float)
        
        fig = go.Figure()
        for i in range(len(grouped)):
            color = TYPE_COLORS.get(study_types[i], TYPE_COLORS["unknown"])
            fig.add_trace(go.Scatter3d(
                x=[h1[i]], y=[h3[i]], z=[h2[i]],
                mode="markers+text",
                marker=dict(size=4, color=color, symbol="circle"),
                text=[numeric_labels[i]],
                textposition="top center",
                textfont=dict(size=12, color=color),
                showlegend=False,
                hovertemplate=f"<b>{hover_labels[i]}</b><br>H1: {h1[i]:.2f}<br>H2: {h2[i]:.2f}<br>H3: {h3[i]:.2f}<extra></extra>",
            ))
            
            # Error bars
            s1 = grouped.loc[i, f"{ctx}-H1-std"]
            s2 = grouped.loc[i, f"{ctx}-H2-std"]
            s3 = grouped.loc[i, f"{ctx}-H3-std"]
            if pd.notna(s1) and s1 > 0:
                fig.add_trace(go.Scatter3d(x=[h1[i] - s1, h1[i] + s1], y=[h3[i], h3[i]], z=[h2[i], h2[i]], mode="lines", line=dict(color=color, width=1, dash="dot"), showlegend=False, hoverinfo="none"))
            if pd.notna(s3) and s3 > 0:
                fig.add_trace(go.Scatter3d(x=[h1[i], h1[i]], y=[h3[i] - s3, h3[i] + s3], z=[h2[i], h2[i]], mode="lines", line=dict(color=color, width=1, dash="dot"), showlegend=False, hoverinfo="none"))
            if pd.notna(s2) and s2 > 0:
                fig.add_trace(go.Scatter3d(x=[h1[i], h1[i]], y=[h3[i], h3[i]], z=[h2[i] - s2, h2[i] + s2], mode="lines", line=dict(color=color, width=1, dash="dot"), showlegend=False, hoverinfo="none"))

        fig.update_layout(
            title=dict(text=f"{ctx} HPC Hypothesis Space", x=0.5, font=dict(size=20)),
            scene=dict(
                xaxis=_hpc_axis_3d("SUBTRACTIVE PREDICTIONS (H1)"),
                yaxis=_hpc_axis_3d("UBIQUITOUS PREDICTIONS (H3)"),
                zaxis=_hpc_axis_3d("FEEDFORWARD PREDICTION ERRORS (H2)"),
                aspectmode="cube",
                camera=dict(eye=dict(x=-1.0, y=-1.0, z=1.0)),
            ),
            margin=dict(l=0, r=260, b=0, t=50),
            paper_bgcolor="white",
        )
        stem = f"01_lo_3d_hpc_space" if ctx == "LO" else "02_go_3d_hpc_space"
        _safe_write_plot(fig, output_dir, stem, show=show, write_svg=write_svg)
        figs[ctx.lower()] = fig
    return figs

def plot_3d_shift_vectors(csv_path, excludes=None, output_dir=None, show=False, write_svg=False):
    """Figure 8: 3D LO-to-GO displacement vectors by study plus average displacement."""
    grouped = study_level_scores(csv_path, excludes=excludes, include_std=False).dropna(subset=[f"{ctx}-{h}-avg" for ctx in CONTEXTS for h in HYPOTHESES]).reset_index(drop=True)
    display_names, numeric_labels, _, study_types = study_labels(grouped)
    fig = go.Figure()
    
    for i, row in grouped.iterrows():
        color = TYPE_COLORS.get(study_types[i], TYPE_COLORS["unknown"])
        lo = np.array([row["LO-H1-avg"], row["LO-H3-avg"], row["LO-H2-avg"]], dtype=float)
        go_pt = np.array([row["GO-H1-avg"], row["GO-H3-avg"], row["GO-H2-avg"]], dtype=float)
        v = go_pt - lo
        fig.add_trace(go.Scatter3d(x=[lo[0], go_pt[0]], y=[lo[1], go_pt[1]], z=[lo[2], go_pt[2]], mode="lines", line=dict(color=color, width=2), showlegend=False, hoverinfo="none"))
        fig.add_trace(go.Cone(x=[go_pt[0]], y=[go_pt[1]], z=[go_pt[2]], u=[v[0]], v=[v[1]], w=[v[2]], sizemode="absolute", sizeref=0.08, anchor="tip", colorscale=[[0, color], [1, color]], showscale=False, hoverinfo="none"))
        fig.add_trace(go.Scatter3d(x=[lo[0]], y=[lo[1]], z=[lo[2]], mode="markers", marker=dict(size=2, color=color, symbol="circle", opacity=0.5), showlegend=False, hovertemplate=f"<b>{numeric_labels[i]}: {display_names[i]} LO</b><extra></extra>"))
        fig.add_trace(go.Scatter3d(x=[go_pt[0]], y=[go_pt[1]], z=[go_pt[2]], mode="markers+text", marker=dict(size=4, color=color, symbol="diamond"), text=[numeric_labels[i]], textposition="bottom center", textfont=dict(size=13, color=color), showlegend=False, hovertemplate=f"<b>{numeric_labels[i]}: {display_names[i]} GO</b><extra></extra>"))
        
    lo_avg = np.array([grouped["LO-H1-avg"].mean(), grouped["LO-H3-avg"].mean(), grouped["LO-H2-avg"].mean()])
    go_avg = np.array([grouped["GO-H1-avg"].mean(), grouped["GO-H3-avg"].mean(), grouped["GO-H2-avg"].mean()])
    fig.add_trace(go.Scatter3d(x=[lo_avg[0], go_avg[0]], y=[lo_avg[1], go_avg[1]], z=[lo_avg[2], go_avg[2]], mode="lines+markers+text", line=dict(color="black", width=8), marker=dict(size=[6, 8], color="black"), text=["AVG LO", "AVG GO"], textposition="top center", name="Average shift", showlegend=True))
    
    fig.update_layout(
        title=dict(text="LO to GO Shift Vectors", x=0.5, font=dict(size=20)),
        scene=dict(xaxis=_hpc_axis_3d("SUBTRACTIVE PREDICTIONS (H1)"), yaxis=_hpc_axis_3d("UBIQUITOUS PREDICTIONS (H3)"), zaxis=_hpc_axis_3d("FEEDFORWARD PREDICTION ERRORS (H2)"), aspectmode="cube", camera=dict(eye=dict(x=-1.0, y=-1.0, z=1.0))),
        margin=dict(l=0, r=260, b=0, t=50),
        paper_bgcolor="white",
    )
    return _safe_write_plot(fig, output_dir, "04_3d_shift_vectors", show=show, write_svg=write_svg)

def plot_context_score_distribution(df_long, output_dir=None, show=False, write_svg=False):
    """Figure 3: Distribution of context-hypothesis scores."""
    columns = [f"{ctx}-{h}" for ctx in CONTEXTS for h in HYPOTHESES]
    fig = go.Figure()
    for col_name in columns:
        ctx, h = col_name.split("-")
        vals = df_long[df_long["Context"] == ctx][h].dropna()
        mean_v = float(vals.mean()) if not vals.empty else 0.0
        med_v = float(vals.median()) if not vals.empty else 0.0
        fig.add_trace(go.Box(
            y=vals, x=[col_name] * len(vals),
            name=col_name,
            boxpoints="all", jitter=0.55, pointpos=0,
            fillcolor="rgba(255,255,255,0)", line=dict(color="rgba(255,255,255,0)"),
            marker=dict(size=4, color="#1f77b4", opacity=0.45),
            showlegend=False
        ))
        fig.add_trace(go.Scatter(x=[col_name], y=[med_v], mode="markers", marker=dict(size=12, color="#8e1b9d", symbol="square", line=dict(width=0.7, color="black")), name="Median", showlegend=(col_name == columns[0])))
        fig.add_trace(go.Scatter(x=[col_name], y=[mean_v], mode="markers", marker=dict(size=14, color="#ff0000", symbol="diamond", line=dict(width=0.7, color="black")), name="Mean", showlegend=(col_name == columns[0])))
        
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    fig.update_layout(
        title=dict(text="Distribution of context-hypothesis scores", x=0.5, font=dict(size=20)),
        yaxis=dict(title="Score : -1 (disagree) ; +1 (agree)", range=[-1.1, 1.1]),
        template="plotly_white", height=600
    )
    return _safe_write_plot(fig, output_dir, "08_context_score_distribution", show=show, write_svg=write_svg)

def plot_context_comparison(df_long, output_dir=None, show=False, write_svg=False):
    """Figure 11: Three-panel empirical LO-vs-GO context comparison."""
    pivot = df_long.groupby(["Base Study ID", "Context"])[HYPOTHESES].mean().unstack("Context")
    if ("H1", "LO") in pivot.columns:
        pivot = pivot.sort_values(by=("H1", "LO"), ascending=True)
    studies = pivot.index.tolist()
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.08, subplot_titles=[f"Hypothesis {h}" for h in HYPOTHESES])
    for i, h in enumerate(HYPOTHESES, start=1):
        for ctx, color, symbol in [("LO", LO_COLOR, "circle"), ("GO", GO_COLOR, "square")]:
            y = pivot[(h, ctx)] if (h, ctx) in pivot.columns else [np.nan] * len(studies)
            fig.add_trace(go.Scatter(x=studies, y=y, mode="markers", marker=dict(color=color, size=10, symbol=symbol, line=dict(width=0.5, color="black")), name=ctx, showlegend=(i == 1)), row=i, col=1)
        fig.update_yaxes(title="score", range=[-1, 1], dtick=0.2, zeroline=True, zerolinecolor="black", row=i, col=1)
    fig.update_xaxes(tickangle=45, tickfont=dict(size=10), row=3, col=1)
    fig.update_layout(title=dict(text="HPC Context Comparison: LO vs GO", x=0.5, font=dict(size=20)), height=950, template="plotly_white")
    return _safe_write_plot(fig, output_dir, "11_context_comparison", show=show, write_svg=write_svg)

# =============================================================================
# MAIN ORCHESTRATOR
# =============================================================================

def run_all_visualizations(csv_path=None, scores_path=None, reports_dir=None):
    """Runs the complete suite of manuscript visualizations.
    Accepts either an existing 90-column hpc_table_final.csv OR raw scores.csv.
    """
    if reports_dir is None:
        reports_dir = DEFAULT_REPORTS_DIR
    os.makedirs(reports_dir, exist_ok=True)
    
    # If scores.csv provided (or present), convert to 90-col table first
    if scores_path and os.path.exists(scores_path):
        target_csv = os.path.join(reports_dir, "hpc_table_final.csv")
        convert_scores_to_hpc_table(scores_path, target_csv)
        csv_path = target_csv
    elif csv_path is None:
        if os.path.exists(DEFAULT_CSV_PATH):
            csv_path = DEFAULT_CSV_PATH
        else:
            default_scores = REPO_ROOT / "content" / "202608_temp" / "scores.csv"
            if default_scores.exists():
                convert_scores_to_hpc_table(str(default_scores), DEFAULT_CSV_PATH)
                csv_path = DEFAULT_CSV_PATH
            else:
                csv_path = str(REPO_ROOT / "examples" / "hpc_table_final.csv")

    print(f"[*] Generating full manuscript visualization suite from: {csv_path}")
    print(f"[*] Target output directory: {reports_dir}")
    
    # 1. 3D HPC Spaces (Figure 7 LO & GO)
    plot_3d_hpc_spaces(csv_path, output_dir=reports_dir, show=False, write_svg=True)
    
    # 2. 3D Shift Vectors (Figure 8)
    plot_3d_shift_vectors(csv_path, output_dir=reports_dir, show=False, write_svg=True)
    
    # 3. Score distribution & context comparison
    df_long = load_hpc_long_table(csv_path)
    plot_context_score_distribution(df_long, output_dir=reports_dir, show=False, write_svg=True)
    plot_context_comparison(df_long, output_dir=reports_dir, show=False, write_svg=True)
    
    print(f"\n[+] Success: All exact manuscript figures generated and saved in: {reports_dir}")

if __name__ == "__main__":
    run_all_visualizations()
