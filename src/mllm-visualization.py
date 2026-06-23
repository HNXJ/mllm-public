import os
import sys
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
# CONFIGURATION & PATHS
# =============================================================================
REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = str(REPO_ROOT / "examples" / "hpc_table_final.csv")
REPORTS_DIR = str(REPO_ROOT / "examples" / "reports") + "/"
os.makedirs(REPORTS_DIR, exist_ok=True)

# Aesthetics
AUTUMN_ENHANCED = [[0.0, 'rgb(255, 0, 0)'], [0.8, 'rgb(255, 165, 0)'], [1.0, 'rgb(255, 255, 0)']]
BENCHMARKS = {"Ground LAC": 0.07, "Hypothesis-Shuffle": 0.5, "Random-Shuffle": 0.67}

# =============================================================================
# DATA LOADING & UTILITIES
# =============================================================================

def _safe_write_plot(fig, output_html=None, output_svg=None):
    if output_html:
        Path(output_html).parent.mkdir(parents=True, exist_ok=True)
        fig.write_html(output_html)
    if output_svg:
        try:
            fig.write_image(output_svg)
        except Exception as e:
            print(f"  [!] SVG export failed (ensure kaleido is installed): {e}")

def prepare_hpc_plot_data(csv_path):
    df_full = pd.read_csv(csv_path)
    # Filter data rows, excluding summary/std rows
    df = df_full[~df_full['study_name'].str.contains('-std', na=False)].dropna(subset=['study_name', 'agent_'])
    
    records = []
    for _, row in df.iterrows():
        # Map canonical 90-col schema to plot-ready melted format
        # LO Context
        records.append({
            "Base Study ID": row["study_name"],
            "Context": "LO",
            "Model Name": row["agent_"],
            "H1": pd.to_numeric(row["LO-H1-avg"], errors='coerce'),
            "H2": pd.to_numeric(row["LO-H2-avg"], errors='coerce'),
            "H3": pd.to_numeric(row["LO-H3-avg"], errors='coerce'),
            "Type": row["type_"]
        })
        # GO Context
        records.append({
            "Base Study ID": row["study_name"],
            "Context": "GO",
            "Model Name": row["agent_"],
            "H1": pd.to_numeric(row["GO-H1-avg"], errors='coerce'),
            "H2": pd.to_numeric(row["GO-H2-avg"], errors='coerce'),
            "H3": pd.to_numeric(row["GO-H3-avg"], errors='coerce'),
            "Type": row["type_"]
        })
    return pd.DataFrame.from_records(records)

# =============================================================================
# CORE VISUALIZATION FUNCTIONS
# =============================================================================

def plot_3d_scatter(df_melted, context="LO", output_base="hpc_3d"):
    df_ctx = df_melted[df_melted["Context"] == context].groupby("Base Study ID").agg({
        "H1": "mean", "H2": "mean", "H3": "mean", "Type": "first"
    }).reset_index()
    
    fig = go.Figure(data=[go.Scatter3d(
        x=df_ctx["H1"], y=df_ctx["H2"], z=df_ctx["H3"],
        mode='markers',
        text=df_ctx["Base Study ID"],
        marker=dict(size=8, color=df_ctx["H1"], colorscale='Viridis', opacity=0.8)
    )])
    
    fig.update_layout(
        title=f"HPC Hypothesis Space ({context} Context)",
        scene=dict(xaxis_title='H1', yaxis_title='H2', zaxis_title='H3'),
        paper_bgcolor='rgba(0,0,0,0)', font=dict(color="black")
    )
    _safe_write_plot(fig, f"{output_base}_{context.lower()}.html", f"{output_base}_{context.lower()}.svg")

def agent_compare_summary_ordered(df_melted, title="Model Pairwise Agreement (MSD)", output_html=None, output_svg=None):
    df_long = df_melted.melt(id_vars=['Base Study ID', 'Context', 'Model Name'], value_vars=['H1', 'H2', 'H3'], var_name='Hyp', value_name='Score')
    df_long['Key'] = df_long['Base Study ID'] + '_' + df_long['Context'] + '_' + df_long['Hyp']
    pivot = df_long.pivot_table(index='Key', columns='Model Name', values='Score')
    models = sorted(pivot.columns.tolist())
    
    dist_mat = pd.DataFrame(index=models, columns=models, dtype=float)
    for m1 in models:
        for m2 in models:
            if m1 == m2: dist_mat.loc[m1, m2] = 0.0
            else:
                common = pivot[[m1, m2]].dropna()
                dist_mat.loc[m1, m2] = np.mean((common[m1] - common[m2])**2) if not common.empty else np.nan

    avg_msd = np.nanmean(dist_mat.values[np.triu_indices(len(models), k=1)])
    
    fig = make_subplots(rows=2, cols=2, horizontal_spacing=0.15, vertical_spacing=0.2,
                        subplot_titles=(title, 'H1 Consistency', 'H2 Consistency', 'H3 Consistency'))

    fig.add_trace(go.Heatmap(
        z=dist_mat.values, x=[m[:8] for m in models], y=models,
        colorscale=AUTUMN_ENHANCED, zmin=0, zmax=1.0,
        colorbar=dict(title='MSD', x=0.45, y=0.75, len=0.4, tickvals=[0, 0.07, 0.5, 0.67, 1.0], 
                      ticktext=["0", "0.07", "0.5", "0.67", "1.0"])
    ), row=1, col=1)

    h_types = ['H1', 'H2', 'H3']
    pos = [(1,2), (2,1), (2,2)]
    for i, h_type in enumerate(h_types):
        for ctx, color in [('LO', 'red'), ('GO', 'blue')]:
            sub_pivot = df_melted[df_melted["Context"] == ctx].pivot_table(index='Base Study ID', columns='Model Name', values=h_type)
            msds = []
            for m in models:
                if m in sub_pivot.columns:
                    diffs = [np.mean((sub_pivot[m] - sub_pivot[o]).dropna()**2) for o in models if m!=o and o in sub_pivot.columns]
                    msds.append(np.mean(diffs) if diffs else np.nan)
                else: msds.append(np.nan)
            fig.add_trace(go.Bar(x=[m[:8] for m in models], y=msds, name=f"{ctx} {h_type}", marker_color=color, showlegend=(i==0)), row=pos[i][0], col=pos[i][1])
        fig.update_yaxes(title_text="Avg MSD", range=[0, 1.2], row=pos[i][0], col=pos[i][1])

    fig.update_layout(height=1000, width=1400, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="black"))
    _safe_write_plot(fig, output_html, output_svg)
    return avg_msd

def study_compare_summary_ordered(df_melted, title="Study-Study Distance (MSD)", output_html=None, output_svg=None):
    pivot = df_melted.pivot_table(index=["Model Name", "Context"], columns="Base Study ID", values=["H1", "H2", "H3"])
    studies = sorted(pivot.columns.get_level_values(1).unique())
    
    msd_mat = []
    for s1 in studies:
        row = []
        s1_data = pivot.xs(s1, axis=1, level=1).values.flatten()
        for s2 in studies:
            if s1 == s2: row.append(0.0)
            else:
                s2_data = pivot.xs(s2, axis=1, level=1).values.flatten()
                mask = ~np.isnan(s1_data) & ~np.isnan(s2_data)
                row.append(np.mean((s1_data[mask] - s2_data[mask])**2) if np.sum(mask) > 0 else np.nan)
        msd_mat.append(row)
    
    msd_mat = np.array(msd_mat)
    if HAS_SCIENTIFIC and len(studies) > 2:
        try:
            perm = hierarchy.leaves_list(hierarchy.linkage(np.nan_to_num(msd_mat, nan=1.0), method='ward'))
            studies = [studies[i] for i in perm]
            msd_mat = msd_mat[perm, :][:, perm]
        except: pass

    fig = go.Figure(data=go.Heatmap(
        z=msd_mat, x=studies, y=studies, colorscale=AUTUMN_ENHANCED, zmin=0, zmax=1.0,
        colorbar=dict(title="MSD", tickvals=[0, 0.07, 0.5, 0.67, 1.0])
    ))
    fig.update_layout(title=title, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="black"), xaxis=dict(tickangle=-45))
    _safe_write_plot(fig, output_html, output_svg)
    return msd_mat

def one_to_other_summary_plot(df_melted, paper_selected="Westerberg&Xiong2025", avg_msd_line=None):
    df_agg = df_melted.groupby(['Base Study ID', 'Context']).agg({'H1':'mean', 'H2':'mean', 'H3':'mean'}).reset_index()
    df_pivot = df_agg.pivot(index='Base Study ID', columns='Context', values=['H1', 'H2', 'H3'])
    
    metrics = [f"{c}-{h}" for h in ['H1', 'H2', 'H3'] for c in ['LO', 'GO']]
    fig = make_subplots(rows=2, cols=1, subplot_titles=('Global Pairwise Differences', f'Differences vs {paper_selected}'))
    
    colors = {'LO': 'red', 'GO': 'blue'}
    for i, m in enumerate(metrics):
        ctx, h = m.split('-')
        vals = df_agg[df_agg["Context"] == ctx].set_index("Base Study ID")[h].dropna()
        if len(vals) >= 2:
            pairs = list(combinations(vals.index, 2))
            diffs = [(vals[p1] - vals[p2])**2 for p1, p2 in pairs if p1 != paper_selected and p2 != paper_selected]
            fig.add_trace(go.Scatter(x=[m]*len(diffs), y=diffs, mode='markers', marker=dict(color=colors[ctx], size=5, opacity=0.3), showlegend=(i==0)), row=1, col=1)
        
        if paper_selected in vals.index:
            ref = vals[paper_selected]
            s_diffs = (vals.drop(paper_selected) - ref)**2
            fig.add_trace(go.Scatter(x=[m]*len(s_diffs), y=s_diffs, mode='markers', marker=dict(color=colors[ctx], size=7, opacity=0.7), showlegend=False), row=2, col=1)

    for r in [1, 2]:
        if avg_msd_line: fig.add_hline(y=avg_msd_line, line_dash='dash', line_color='purple', row=r, col=1, annotation_text=f"LAC: {avg_msd_line:.2f}")
        fig.update_yaxes(title="MSE", range=[0, 1.2], row=r, col=1)
    
    fig.update_layout(height=900, title=f"Literature Consensus vs {paper_selected}", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="black"))
    _safe_write_plot(fig, os.path.join(REPORTS_DIR, "literature_consensus_comparison.html"), os.path.join(REPORTS_DIR, "literature_consensus_comparison.svg"))

def plot_2d_h_comparison(df_melted):
    df_agg = df_melted.groupby(['Base Study ID', 'Context']).agg({'H1':'mean', 'H2':'mean', 'H3':'mean'}).reset_index()
    fig = make_subplots(rows=3, cols=1, subplot_titles=("H1", "H2", "H3"), shared_yaxes=True, vertical_spacing=0.1)
    
    for i, h in enumerate(['H1', 'H2', 'H3']):
        lo_s = df_agg[df_agg["Context"]=="LO"].set_index("Base Study ID")[h]
        go_s = df_agg[df_agg["Context"]=="GO"].set_index("Base Study ID")[h].sort_values()
        common = go_s.index.intersection(lo_s.index)
        
        # Plot LO points
        fig.add_trace(go.Scatter(
            x=common, y=lo_s[common].values, 
            mode='markers', name='LO', 
            marker=dict(color='red'), showlegend=(i==0)
        ), row=i+1, col=1)
        
        # Plot GO points
        fig.add_trace(go.Scatter(
            x=common, y=go_s[common].values, 
            mode='markers', name='GO', 
            marker=dict(color='blue'), showlegend=(i==0)
        ), row=i+1, col=1)
        
        fig.update_yaxes(range=[-1.1, 1.1], row=i+1, col=1)
        fig.update_xaxes(tickangle=-45, row=i+1, col=1)

    fig.update_layout(height=1000, title="Averaged Hypothesis Comparison (LO vs GO)", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="black"))
    _safe_write_plot(fig, os.path.join(REPORTS_DIR, "hpc_h2h_comparison.html"), os.path.join(REPORTS_DIR, "hpc_h2h_comparison.svg"))

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def run_all():
    print(f"[*] Loading data from {CSV_PATH}...")
    if not os.path.exists(CSV_PATH):
        print(f"[!] Error: {CSV_PATH} not found.")
        return

    df_melted = prepare_hpc_plot_data(CSV_PATH)
    print(f"[*] Data prepared: {len(df_melted)} context-agent evaluations.")

    print("[*] Generating Agent-Agent Comparison...")
    avg_model_diff = agent_compare_summary_ordered(df_melted, output_html=os.path.join(REPORTS_DIR, "agent_agent_compare.html"), output_svg=os.path.join(REPORTS_DIR, "agent_agent_compare.svg"))

    print("[*] Generating Study-Study Distance...")
    lc_matrix = study_compare_summary_ordered(df_melted, output_html=os.path.join(REPORTS_DIR, "study_study_compare.html"), output_svg=os.path.join(REPORTS_DIR, "study_study_compare.svg"))

    print("[*] Generating Literature Consensus Analysis...")
    one_to_other_summary_plot(df_melted, paper_selected="Westerberg&Xiong2025", avg_msd_line=avg_model_diff)

    print("[*] Generating 2D Hypothesis Overlays...")
    plot_2d_h_comparison(df_melted)

    print("[*] Generating 3D Context Figures...")
    plot_3d_scatter(df_melted, context="LO", output_base=os.path.join(REPORTS_DIR, "hpc_3d"))
    plot_3d_scatter(df_melted, context="GO", output_base=os.path.join(REPORTS_DIR, "hpc_3d"))

    print(f"\n[+] Success: All reports saved to {REPORTS_DIR}")

if __name__ == "__main__":
    run_all()
