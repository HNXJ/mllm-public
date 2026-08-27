# Install static export support for Plotly in Colab.

# --- CELL ---


# Colab/runtime setup. Drive mount is optional; local/test CSV fallback is automatic.
try:
    from google.colab import drive
    drive.mount('/content/drive', force_remount=False)
except Exception:
    pass

from pathlib import Path

# Your Drive path remains the first candidate in Colab.
csv_path_to_file = 'data/hpc_table_final.csv'

# Outputs will be written here in Colab; locally this becomes ./hpc_figures.
OUTPUT_DIR = Path('/content/hpc_figures') if Path('/content').exists() else Path('hpc_figures')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Defaults for the one-shot run cell below.
EXCLUDES = []  # or STRICT_EXCLUDES after running the function cell
PLOT_STD = True
SHOW_FIGURES = True
WRITE_SVG = True

# --- CELL ---


import os
import re
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.stats as stats
import plotly.graph_objects as go
from plotly.subplots import make_subplots
try:
    from IPython.display import display
except Exception:
    display = print

try:
    import plotly.io as pio
    pio.renderers.default = "colab"
except Exception:
    pass

# -----------------------------
# Shared constants
# -----------------------------
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

DEFAULT_EXCLUDES = []
STRICT_EXCLUDES = ["Bakhtiari", "Garret", "Greedy", "Payeur", "Sacramento", "Yamins"]


def _as_path(path):
    return Path(path).expanduser().resolve() if path is not None else None


def _maybe_make_dir(output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def _safe_write_plot(fig, output_dir=None, stem=None, write_html=True, write_svg=False, show=True):
    """Save and/or display a Plotly figure without breaking the full run if SVG export fails."""
    if output_dir is not None and stem is not None:
        output_dir = _maybe_make_dir(output_dir)
        if write_html:
            fig.write_html(str(output_dir / f"{stem}.html"))
        if write_svg:
            try:
                fig.write_image(str(output_dir / f"{stem}.svg"))
            except Exception as exc:
                print(f"[warning] SVG export skipped for {stem}: {exc}")
    if show:
        fig.show()
    return fig


def _find_csv_path(preferred_path=None):
    """Resolve the CSV path in Colab, local notebooks, or this test sandbox."""
    candidates = []
    if preferred_path:
        candidates.append(preferred_path)
    candidates.extend([
        "data/hpc_table_final.csv",
        "/content/hpc_table_final.csv",
        "hpc_table_final.csv",
        "/mnt/data/hpc_table_final.csv",
    ])
    for candidate in candidates:
        p = Path(str(candidate)).expanduser()
        if p.exists():
            return str(p)
    checked = "\n".join(f"  - {c}" for c in candidates)
    raise FileNotFoundError(f"Could not find hpc_table_final.csv. Checked:\n{checked}")


def _filter_ignored_and_excluded(df, excludes=None):
    df = df.copy()
    if "ignore_row" in df.columns:
        mask = df["ignore_row"].fillna(False).astype(bool) == False
        df = df[mask].copy()
    for pattern in (excludes or []):
        df = df[~df["study_name"].astype(str).str.contains(pattern, case=False, na=False, regex=True)]
    return df


def load_raw_hpc_table(csv_path, excludes=None):
    """Load the original wide HPC table."""
    df = pd.read_csv(_find_csv_path(csv_path))
    df = _filter_ignored_and_excluded(df, excludes=excludes)
    if "type_" in df.columns:
        df["type_"] = df["type_"].fillna("unknown").astype(str).str.lower()
    return df


def _score_columns(include_std=False):
    cols = [f"{ctx}-{h}-avg" for ctx in CONTEXTS for h in HYPOTHESES]
    if include_std:
        cols.extend([f"{ctx}-{h}-std" for ctx in CONTEXTS for h in HYPOTHESES])
    return cols


def study_level_scores(csv_path, excludes=None, include_std=True, drop_empty=True):
    """Aggregate agent-level rows to one row per study."""
    df = load_raw_hpc_table(csv_path, excludes=excludes)
    agg = {"type_": "first"}
    if "year_" in df.columns:
        agg["year_"] = "first"
    for col in _score_columns(include_std=include_std):
        if col in df.columns:
            agg[col] = "mean"
    grouped = df.groupby("study_name", dropna=False).agg(agg).reset_index()
    if drop_empty:
        avg_cols = [c for c in grouped.columns if c.endswith("-avg")]
        grouped = grouped.dropna(subset=avg_cols, how="all")
    grouped = grouped.sort_values("study_name").reset_index(drop=True)
    return grouped


def _rename_this_work(study_name, study_type):
    name = str(study_name)
    t = str(study_type).lower()
    if "westerberg" in name.lower() or t == "this work":
        return "Westerberg&Xiong2025", "this work"
    return name, t


def study_labels(grouped):
    names = grouped["study_name"].astype(str).tolist()
    types = grouped["type_"].astype(str).str.lower().tolist()
    display_names = []
    clean_types = []
    for name, stype in zip(names, types):
        display_name, clean_type = _rename_this_work(name, stype)
        display_names.append(display_name)
        clean_types.append(clean_type)
    numeric_labels = [str(i + 1) for i in range(len(display_names))]
    hover_labels = [f"{i + 1}: {name}" for i, name in enumerate(display_names)]
    return display_names, numeric_labels, hover_labels, clean_types


def _hpc_axis_3d(title_text, font_size=10):
    return dict(
        title=dict(text=title_text, font=dict(size=font_size, color="black")),
        range=[-1.0, 1.0],
        tickmode="array",
        tickvals=[-1, 0, 1],
        ticktext=["-1", "0", "+1"],
        backgroundcolor="white",
        gridcolor="lightgrey",
        showgrid=True,
        zerolinecolor="black",
        zerolinewidth=2,
        linecolor="black",
    )


def _study_legend_annotations(labels, names, y=-0.16, cols=5, font_size=10):
    n = len(names)
    chunk = int(np.ceil(n / cols)) if n else 1
    annotations = []
    for i in range(cols):
        start = i * chunk
        end = min((i + 1) * chunk, n)
        if start >= n:
            break
        text = "<br>".join(f"<b>{num}</b>: {name}" for num, name in zip(labels[start:end], names[start:end]))
        annotations.append(dict(
            x=i * (1.0 / cols),
            y=y,
            xref="paper",
            yref="paper",
            xanchor="left",
            yanchor="top",
            text=("<b>Study legend:</b><br>" if i == 0 else "<br>") + text,
            showarrow=False,
            align="left",
            font=dict(size=font_size, color="black"),
            bgcolor="rgba(255,255,255,0.85)",
        ))
    return annotations


def _add_type_legend(fig, row=None, col=None):
    legend_types = [
        ("empirical", TYPE_COLORS["empirical"]),
        ("non-empirical", TYPE_COLORS["other"]),
        ("this work", TYPE_COLORS["this work"]),
    ]
    for label, color in legend_types:
        trace = go.Scatter(x=[None], y=[None], mode="markers", marker=dict(color=color, size=8), name=label)
        if row is None or col is None:
            fig.add_trace(trace)
        else:
            fig.add_trace(trace, row=row, col=col)


def _add_3d_error_bars(fig, grouped, ctx):
    required = [f"{ctx}-{h}-std" for h in HYPOTHESES]
    if not all(col in grouped.columns for col in required):
        return fig
    line_style = dict(color="rgba(50,50,50,0.55)", width=1.0)
    xs, ys, zs = grouped[f"{ctx}-H1-avg"], grouped[f"{ctx}-H3-avg"], grouped[f"{ctx}-H2-avg"]
    dxs, dys, dzs = grouped[f"{ctx}-H1-std"], grouped[f"{ctx}-H3-std"], grouped[f"{ctx}-H2-std"]
    ex_x, ex_y, ex_z, ey_x, ey_y, ey_z, ez_x, ez_y, ez_z = [], [], [], [], [], [], [], [], []
    for x, y, z, dx, dy, dz in zip(xs, ys, zs, dxs, dys, dzs):
        if pd.notna(x) and pd.notna(dx):
            ex_x.extend([x - dx / 2, x + dx / 2, None]); ex_y.extend([y, y, None]); ex_z.extend([z, z, None])
        if pd.notna(y) and pd.notna(dy):
            ey_x.extend([x, x, None]); ey_y.extend([y - dy / 2, y + dy / 2, None]); ey_z.extend([z, z, None])
        if pd.notna(z) and pd.notna(dz):
            ez_x.extend([x, x, None]); ez_y.extend([y, y, None]); ez_z.extend([z - dz / 2, z + dz / 2, None])
    if ex_x:
        fig.add_trace(go.Scatter3d(x=ex_x, y=ex_y, z=ex_z, mode="lines", line=line_style, showlegend=False, hoverinfo="none"))
    if ey_x:
        fig.add_trace(go.Scatter3d(x=ey_x, y=ey_y, z=ey_z, mode="lines", line=line_style, showlegend=False, hoverinfo="none"))
    if ez_x:
        fig.add_trace(go.Scatter3d(x=ez_x, y=ez_y, z=ez_z, mode="lines", line=line_style, showlegend=False, hoverinfo="none"))
    return fig


def _base_3d_scatter(labels, hover_labels, study_types, h1, h2, h3, title):
    fig = go.Figure()
    for label, hover, stype, x, z, y in zip(labels, hover_labels, study_types, h1, h2, h3):
        if pd.isna(x) or pd.isna(y) or pd.isna(z):
            continue
        color = TYPE_COLORS.get(stype, TYPE_COLORS["unknown"])
        fig.add_trace(go.Scatter3d(
            x=[x], y=[y], z=[z], mode="markers+text",
            marker=dict(size=4, color=color, symbol="circle", opacity=0.85),
            text=[label], textposition="middle center", textfont=dict(size=13, color=color),
            name=hover, showlegend=False,
            hovertemplate=f"<b>{hover}</b><br>Type: {stype}<extra></extra>",
        ))
    fig.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=20, color="black")),
        scene=dict(
            xaxis=_hpc_axis_3d("SUBTRACTIVE PREDICTIONS (H1)", 10),
            yaxis=_hpc_axis_3d("UBIQUITOUS PREDICTIONS (H3)", 10),
            zaxis=_hpc_axis_3d("FEEDFORWARD PREDICTION ERRORS (H2)", 10),
            aspectmode="cube",
            camera=dict(eye=dict(x=-1.0, y=-1.0, z=1.0), center=dict(x=0, y=0, z=0)),
        ),
        paper_bgcolor="white",
        margin=dict(l=0, r=260, b=0, t=50),
    )
    return fig


# -----------------------------
# Statistics and data reshaping
# -----------------------------
def load_hpc_long_table(csv_path, excludes=None):
    """Return one long row per original row x context with columns H1/H2/H3."""
    df = load_raw_hpc_table(csv_path, excludes=excludes)
    records = []
    for _, row in df.iterrows():
        study_name = str(row.get("study_name", "unknown-study")).strip()
        year = row.get("year_", np.nan)
        year_str = str(int(float(year))) if pd.notna(year) else "unknown-year"
        raw_type = str(row.get("type_", "unknown")).lower()
        raw_agent = str(row.get("agent_", "unknown-agent")).strip()
        display_study, study_type = _rename_this_work(study_name, raw_type)
        model_name, model_family = simplify_model_name(raw_agent)
        base_id = f"{display_study} ({year_str})"
        for ctx in CONTEXTS:
            records.append({
                "Base Study ID": base_id,
                "Study Name": display_study,
                "Year": year,
                "Study Type": study_type,
                "Context": ctx,
                "Model Name": model_name,
                "Model Family": model_family,
                "Agent Raw": raw_agent,
                "H1": pd.to_numeric(row.get(f"{ctx}-H1-avg"), errors="coerce"),
                "H2": pd.to_numeric(row.get(f"{ctx}-H2-avg"), errors="coerce"),
                "H3": pd.to_numeric(row.get(f"{ctx}-H3-avg"), errors="coerce"),
            })
    return pd.DataFrame.from_records(records)


def simplify_model_name(raw_agent):
    agent = str(raw_agent).lower()
    patterns = [
        (r"deepseek.*70b", "deepseek-r1-70b", "deepseek"),
        (r"gemma-3-27b", "gemma-3-27b", "google-gemma3"),
        (r"gemma-4-31b", "gemma-4-31b", "google-gemma4"),
        (r"phi-4", "phi-4-reasoning", "phi-4"),
        (r"mistral.*nemo", "mistral-nemo-12b", "mistral"),
        (r"olmo", "olmo-3-32b-think", "olmo"),
        (r"qwen3\.5.*opus", "qwen3.5-opus", "qwen"),
        (r"qwen3\.5.*claude", "qwen3.5-claude", "qwen"),
        (r"gpt-oss.*claude", "gpt-oss-claude", "gpt-oss"),
        (r"qwen3.*gemini", "qwen3-gemini", "qwen"),
    ]
    for pattern, model_name, family in patterns:
        if re.search(pattern, agent):
            return model_name, family
    return str(raw_agent), "unknown"


def calculate_msd_matrix(df_long, pivot_on="Model Name"):
    """Pairwise mean-square difference across shared study/context/hypothesis signatures."""
    other_axis = "Base Study ID" if pivot_on == "Model Name" else "Model Name"
    sub = df_long.dropna(subset=HYPOTHESES)
    melted = sub.melt(
        id_vars=[pivot_on, other_axis, "Context"],
        value_vars=HYPOTHESES,
        var_name="Hypothesis",
        value_name="Score",
    )
    pivot = melted.groupby([other_axis, "Context", "Hypothesis", pivot_on], observed=True)["Score"].mean().unstack(pivot_on)
    entities = sorted(pivot.columns.tolist())
    mat = pd.DataFrame(np.nan, index=entities, columns=entities)
    for i, e1 in enumerate(entities):
        for j, e2 in enumerate(entities[i:], start=i):
            v1 = pivot[e1].to_numpy(dtype=float)
            v2 = pivot[e2].to_numpy(dtype=float)
            mask = ~np.isnan(v1) & ~np.isnan(v2)
            if np.any(mask):
                mat.loc[e1, e2] = mat.loc[e2, e1] = np.mean((v1[mask] - v2[mask]) ** 2)
    for e in entities:
        mat.loc[e, e] = np.nan  # avoid np.fill_diagonal: pandas 2.x+ copy-on-write can make .values read-only
    return mat


def calculate_leave_one_out_influence(dist_mat):
    entities = dist_mat.index.tolist()
    all_vals = dist_mat.values[np.triu_indices(len(dist_mat), k=1)]
    total_mean = np.nanmean(all_vals) if len(all_vals) else np.nan
    influence = {}
    for entity in entities:
        sub = dist_mat.drop(index=entity, columns=entity)
        vals = sub.values[np.triu_indices(len(sub), k=1)]
        influence[entity] = np.nanmean(vals) - total_mean if len(vals) else np.nan
    return influence


def compute_our_vs_literature_stats(csv_path, excludes=None, print_results=True):
    """Compare this-work rows against literature rows for LO and GO/H1-H3."""
    df = load_raw_hpc_table(csv_path, excludes=excludes)
    is_this_work = (df["type_"].astype(str).str.lower() == "this work") | df["study_name"].astype(str).str.contains("Westerberg", case=False, na=False)
    our_df = df[is_this_work]
    lit_df = df[~df["study_name"].isin(our_df["study_name"].unique())]
    cols = [f"{ctx}-{h}-avg" for ctx in CONTEXTS for h in HYPOTHESES]
    our_scores = our_df[cols].dropna(how="all")
    lit_grouped = lit_df.groupby("study_name")[cols].mean().dropna(how="all")
    results = {"LO": {}, "GO": {}, "paired": {}}
    if print_results:
        print("=== This work vs literature tests ===")
    for ctx in CONTEXTS:
        if print_results:
            print(f"\n--- {ctx} ---")
        for h in HYPOTHESES:
            col = f"{ctx}-{h}-avg"
            our_vals = pd.to_numeric(our_scores[col], errors="coerce").dropna()
            lit_vals = pd.to_numeric(lit_grouped[col], errors="coerce").dropna()
            if len(our_vals) and len(lit_vals):
                t_stat, t_p = stats.ttest_ind(our_vals, lit_vals, equal_var=False, nan_policy="omit")
                w_stat, w_p = stats.ranksums(our_vals, lit_vals)
            else:
                t_stat = t_p = w_stat = w_p = np.nan
            results[ctx][h] = {
                "our_m": float(our_vals.mean()) if len(our_vals) else np.nan,
                "our_sd": float(our_vals.std()) if len(our_vals) else np.nan,
                "lit_m": float(lit_vals.mean()) if len(lit_vals) else np.nan,
                "lit_sd": float(lit_vals.std()) if len(lit_vals) else np.nan,
                "t_p": float(t_p),
                "w_p": float(w_p),
            }
            if print_results:
                r = results[ctx][h]
                print(f"{h}: this work M={r['our_m']:.3f}, literature M={r['lit_m']:.3f}, Wilcoxon p={r['w_p']:.4f}, t-test p={r['t_p']:.4f}")
    if print_results:
        print("\n=== LO vs GO paired Wilcoxon tests ===")
    for label, data in [("this_work", our_scores), ("literature", lit_grouped)]:
        results["paired"][label] = {}
        if print_results:
            print(f"\n--- {label.replace('_', ' ')} ---")
        for h in HYPOTHESES:
            pair = data[[f"LO-{h}-avg", f"GO-{h}-avg"]].dropna()
            if len(pair) > 0:
                try:
                    stat, p = stats.wilcoxon(pair[f"LO-{h}-avg"], pair[f"GO-{h}-avg"])
                except ValueError:
                    stat, p = np.nan, np.nan
                shift = pair[f"GO-{h}-avg"].mean() - pair[f"LO-{h}-avg"].mean()
            else:
                p = shift = np.nan
            results["paired"][label][h] = {"shift": float(shift), "w_p": float(p)}
            if print_results:
                print(f"{h}: shift={shift:.3f}, paired Wilcoxon p={p:.4f}")
    return results


def print_study_categories(csv_path, excludes=None):
    df = load_raw_hpc_table(csv_path, excludes=excludes)
    study_types = df[["study_name", "type_"]].drop_duplicates().sort_values("study_name")
    print("=== Empirical vs non-empirical studies ===\n")
    for _, row in study_types.iterrows():
        raw_type = str(row["type_"]).lower()
        study_name = str(row["study_name"])
        if raw_type == "empirical":
            category = "Empirical"
        elif "westerberg" in study_name.lower() or raw_type == "this work":
            category = "Empirical (this work)"
        else:
            category = f"Non-empirical ({raw_type})"
        print(f"- {study_name}: {category}")


def compute_shift_summary(csv_path, excludes=None, print_results=True):
    grouped = study_level_scores(csv_path, excludes=excludes, include_std=False).dropna(subset=[f"LO-{h}-avg" for h in HYPOTHESES] + [f"GO-{h}-avg" for h in HYPOTHESES])
    records = []
    for h in HYPOTHESES:
        shift = grouped[f"GO-{h}-avg"] - grouped[f"LO-{h}-avg"]
        stat, p = stats.ranksums(grouped[f"LO-{h}-avg"], grouped[f"GO-{h}-avg"])
        records.append({
            "Hypothesis": h,
            "Mean Shift (GO - LO)": float(shift.mean()),
            "Mean Abs Shift": float(shift.abs().mean()),
            "Rank-Sum P": float(p),
        })
    out = pd.DataFrame.from_records(records)
    if print_results:
        print("=== Shift summary across studies ===")
        display(out)
    return out


# -----------------------------
# Renamed, simplified visualization functions
# -----------------------------
def plot_3d_hpc_spaces(csv_path, excludes=None, plot_std=True, output_dir=None, show=True, write_svg=False):
    """3D LO and GO hypothesis-space scatter plots."""
    grouped = study_level_scores(csv_path, excludes=excludes, include_std=plot_std)
    display_names, numeric_labels, hover_labels, study_types = study_labels(grouped)
    figs = {}
    for ctx, title, stem in [
        ("LO", "LO HPC Hypothesis Space", "01_lo_3d_hpc_space"),
        ("GO", "GO HPC Hypothesis Space", "02_go_3d_hpc_space"),
    ]:
        fig = _base_3d_scatter(
            labels=numeric_labels,
            hover_labels=hover_labels,
            study_types=study_types,
            h1=grouped[f"{ctx}-H1-avg"],
            h2=grouped[f"{ctx}-H2-avg"],
            h3=grouped[f"{ctx}-H3-avg"],
            title=title,
        )
        if plot_std:
            _add_3d_error_bars(fig, grouped, ctx)
        fig.update_layout(annotations=_study_legend_annotations(numeric_labels, display_names, y=0.98, cols=2, font_size=9))
        figs[ctx.lower()] = _safe_write_plot(fig, output_dir, stem, show=show, write_svg=write_svg)
    return figs


def plot_2d_scatter_suite(csv_path, excludes=None, plot_std=True, test_stats=None, output_dir=None, show=True, write_svg=False):
    """Six 2D projections: LO and GO pairwise H1/H2/H3 scatter panels."""
    grouped = study_level_scores(csv_path, excludes=excludes, include_std=plot_std)
    display_names, numeric_labels, _, study_types = study_labels(grouped)
    pairs = [
        (1, 1, "LO", "H1", "H2"), (1, 2, "LO", "H1", "H3"), (1, 3, "LO", "H2", "H3"),
        (2, 1, "GO", "H1", "H2"), (2, 2, "GO", "H1", "H3"), (2, 3, "GO", "H2", "H3"),
    ]
    subplot_titles = [f"{ctx}: {x} vs {y}" for _, _, ctx, x, y in pairs]
    fig = make_subplots(rows=2, cols=3, subplot_titles=subplot_titles, vertical_spacing=0.15, horizontal_spacing=0.08)
    for i, row in grouped.iterrows():
        stype = study_types[i]
        color = TYPE_COLORS.get(stype, TYPE_COLORS["unknown"])
        for r, c, ctx, xh, yh in pairs:
            x_col = f"{ctx}-{xh}-avg"; y_col = f"{ctx}-{yh}-avg"
            x_val = row.get(x_col); y_val = row.get(y_col)
            if pd.isna(x_val) or pd.isna(y_val):
                continue
            err_x = err_y = None
            if plot_std:
                x_std = row.get(f"{ctx}-{xh}-std")
                y_std = row.get(f"{ctx}-{yh}-std")
                if pd.notna(x_std):
                    err_x = dict(type="data", array=[x_std / np.sqrt(10)], visible=True, color="rgba(50,50,50,0.4)", thickness=1)
                if pd.notna(y_std):
                    err_y = dict(type="data", array=[y_std / np.sqrt(10)], visible=True, color="rgba(50,50,50,0.4)", thickness=1)
            fig.add_trace(go.Scatter(
                x=[x_val], y=[y_val], mode="markers+text",
                marker=dict(color=color, size=6, line=dict(width=1, color="DarkSlateGrey")),
                text=[numeric_labels[i]], textposition="bottom center", textfont=dict(size=10, color=color),
                name=display_names[i], showlegend=False, error_x=err_x, error_y=err_y,
                hovertemplate=f"<b>{numeric_labels[i]}: {display_names[i]}</b><br>{ctx}-{xh}: %{{x:.3f}}<br>{ctx}-{yh}: %{{y:.3f}}<extra></extra>",
            ), row=r, col=c)
    for r, c, ctx, xh, yh in pairs:
        fig.update_xaxes(title_text=xh, range=[-1.1, 1.1], zeroline=True, zerolinecolor="black", gridcolor="lightgrey", row=r, col=c)
        fig.update_yaxes(title_text=yh, range=[-1.1, 1.1], zeroline=True, zerolinecolor="black", gridcolor="lightgrey", row=r, col=c)
        if test_stats and ctx in test_stats:
            txt = (
                f"<b>{xh} vs lit</b><br>Wilcoxon p: {test_stats[ctx][xh]['w_p']:.3f}<br>T-test p: {test_stats[ctx][xh]['t_p']:.3f}<br><br>"
                f"<b>{yh} vs lit</b><br>Wilcoxon p: {test_stats[ctx][yh]['w_p']:.3f}<br>T-test p: {test_stats[ctx][yh]['t_p']:.3f}"
            )
            fig.add_annotation(x=0.05, y=0.95, xref=f"x{c + (r - 1) * 3}", yref=f"y{c + (r - 1) * 3}", text=txt, showarrow=False, align="left", bgcolor="rgba(255,255,255,0.85)", bordercolor="black", borderwidth=1, font=dict(size=9))
    _add_type_legend(fig, row=1, col=1)
    fig.update_layout(
        height=1000, width=1250,
        title=dict(text="2D HPC Scatter Suite: LO vs GO", x=0.5, font=dict(size=20)),
        template="plotly_white",
        margin=dict(t=90, b=250, l=50, r=50),
        annotations=tuple(fig.layout.annotations) + tuple(_study_legend_annotations(numeric_labels, display_names)),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.03, xanchor="right", x=1),
    )
    stem = "03_2d_scatter_suite_with_stats" if test_stats else "03_2d_scatter_suite"
    return _safe_write_plot(fig, output_dir, stem, show=show, write_svg=write_svg)


def plot_3d_shift_vectors(csv_path, excludes=None, output_dir=None, show=True, write_svg=False):
    """3D LO-to-GO displacement vectors by study plus average displacement."""
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
        annotations=_study_legend_annotations(numeric_labels, display_names, y=0.98, cols=2, font_size=9),
        paper_bgcolor="white",
    )
    return _safe_write_plot(fig, output_dir, "04_3d_shift_vectors", show=show, write_svg=write_svg)


def plot_3d_trend_vectors(csv_path, excludes=None, output_dir=None, show=True, write_svg=False, trend_year=2040):
    """3D trend projection using linear year-to-score fits."""
    grouped = study_level_scores(csv_path, excludes=excludes, include_std=False).dropna(subset=["year_"] + [f"{ctx}-{h}-avg" for ctx in CONTEXTS for h in HYPOTHESES]).reset_index(drop=True)
    if len(grouped) < 2:
        raise ValueError("Need at least two dated studies for trend vectors.")

    def trend_points(subset):
        if len(subset) < 2:
            return None, None
        pred = {}
        for col in [f"{ctx}-{h}-avg" for ctx in CONTEXTS for h in HYPOTHESES]:
            m, b = np.polyfit(subset["year_"].to_numpy(dtype=float), subset[col].to_numpy(dtype=float), 1)
            pred[col] = m * trend_year + b
        return np.array([pred["LO-H1-avg"], pred["LO-H3-avg"], pred["LO-H2-avg"]]), np.array([pred["GO-H1-avg"], pred["GO-H3-avg"], pred["GO-H2-avg"]])

    t_lo_all, t_go_all = trend_points(grouped)
    no_w = grouped[~grouped["study_name"].astype(str).str.contains("Westerberg", case=False, na=False)]
    t_lo_no_w, t_go_no_w = trend_points(no_w)
    trend_vec = t_go_all - t_lo_all

    fig = go.Figure()
    aligned, divergent = [], []
    for i, row in grouped.reset_index(drop=True).iterrows():
        lo = np.array([row["LO-H1-avg"], row["LO-H3-avg"], row["LO-H2-avg"]], dtype=float)
        go_pt = np.array([row["GO-H1-avg"], row["GO-H3-avg"], row["GO-H2-avg"]], dtype=float)
        dot = float(np.dot(go_pt - lo, trend_vec))
        color = "blue" if dot > 0 else "red"
        name = "Aligned with trend" if dot > 0 else "Divergent from trend"
        if dot > 0:
            aligned.append(f"{i + 1}: {row['study_name']}")
        else:
            divergent.append(f"{i + 1}: {row['study_name']}")
        fig.add_trace(go.Scatter3d(x=[lo[0], go_pt[0]], y=[lo[1], go_pt[1]], z=[lo[2], go_pt[2]], mode="lines+markers+text", marker=dict(size=[3, 0], color=color), line=dict(color=color, width=1), text=["", str(i + 1)], textfont=dict(size=8, color=color), textposition="top center", name=name, showlegend=(name not in [tr.name for tr in fig.data]), hoverinfo="none"))

    for t_lo, t_go, color, dash, name in [
        (t_lo_all, t_go_all, "purple", "solid", f"Trend to {trend_year}: all"),
        (t_lo_no_w, t_go_no_w, "orange", "dash", f"Trend to {trend_year}: excl. Westerberg"),
    ]:
        if t_lo is None:
            continue
        v = t_go - t_lo
        fig.add_trace(go.Scatter3d(x=[t_lo[0], t_go[0]], y=[t_lo[1], t_go[1]], z=[t_lo[2], t_go[2]], mode="lines+markers", marker=dict(size=[9, 0], color=color), line=dict(color=color, width=10, dash=dash), name=name, showlegend=True))
        fig.add_trace(go.Cone(x=[t_go[0]], y=[t_go[1]], z=[t_go[2]], u=[v[0]], v=[v[1]], w=[v[2]], sizemode="absolute", sizeref=0.18, anchor="tip", colorscale=[[0, color], [1, color]], showscale=False, hoverinfo="none"))

    legend_text = "<b>Aligned studies:</b><br>" + "<br>".join(aligned) + "<br><br><b>Divergent studies:</b><br>" + "<br>".join(divergent)
    fig.update_layout(
        title=dict(text="Vector Trend Prediction", x=0.5, font=dict(size=20)),
        scene=dict(xaxis=_hpc_axis_3d("SUBTRACTIVE PREDICTIONS (H1)", 8), yaxis=_hpc_axis_3d("UBIQUITOUS PREDICTIONS (H3)", 8), zaxis=_hpc_axis_3d("FEEDFORWARD PREDICTION ERRORS (H2)", 8), aspectmode="cube"),
        annotations=[dict(x=1.02, y=0.90, xref="paper", yref="paper", text=legend_text, showarrow=False, align="left", font=dict(size=9), bgcolor="rgba(255,255,255,0.85)")],
        margin=dict(l=100, r=260, b=0, t=55),
        paper_bgcolor="white",
    )
    return _safe_write_plot(fig, output_dir, "05_3d_trend_vectors", show=show, write_svg=write_svg)


def plot_shift_magnitude_bar(csv_path, excludes=None, output_dir=None, show=True, write_svg=False):
    """Bar plot of mean absolute GO-LO shift by hypothesis."""
    summary = compute_shift_summary(csv_path, excludes=excludes, print_results=False)
    labels = [HYPOTHESIS_LABELS[h] for h in summary["Hypothesis"]]
    fig = go.Figure(go.Bar(x=labels, y=summary["Mean Abs Shift"], text=[f"{v:.4f}" for v in summary["Mean Abs Shift"]], textposition="auto"))
    fig.update_layout(title=dict(text="Average Shift Magnitude (|GO - LO|)", x=0.5), xaxis_title="Hypothesis", yaxis_title="Mean absolute shift", template="plotly_white")
    return _safe_write_plot(fig, output_dir, "06_shift_magnitude_bar", show=show, write_svg=write_svg)


def plot_model_agreement_dashboard(df_long, output_dir=None, show=True, write_svg=False):
    """Model agreement dashboard: pairwise model MSD plus per-hypothesis disagreement bars."""
    mat = calculate_msd_matrix(df_long, pivot_on="Model Name")
    order = list(mat.mean(axis=1).sort_values(ascending=False).index)
    short_names = [str(m).split("-")[0] if isinstance(m, str) else str(m) for m in order]
    fig = make_subplots(rows=2, cols=2, subplot_titles=["Pairwise model MSD", "H1 disagreement", "H2 disagreement", "H3 disagreement"], vertical_spacing=0.2, horizontal_spacing=0.15)
    fig.add_trace(go.Heatmap(z=mat.loc[order, order].values, x=short_names, y=order, colorscale="Viridis", colorbar=dict(title="MSD", x=0.46, y=0.8, len=0.35)), row=1, col=1)
    pivot = df_long.groupby(["Model Name", "Context", "Base Study ID"])[HYPOTHESES].mean().reset_index()
    pos = {"H1": (1, 2), "H2": (2, 1), "H3": (2, 2)}
    for h in HYPOTHESES:
        r, c = pos[h]
        for ctx, color in [("LO", LO_COLOR), ("GO", GO_COLOR)]:
            scores = pivot[pivot["Context"] == ctx].groupby(["Model Name", "Base Study ID"])[h].mean().unstack("Base Study ID")
            vals = []
            for m_i in order:
                if m_i not in scores.index:
                    vals.append(np.nan); continue
                v_i = scores.loc[m_i]
                diffs = []
                for m_j in order:
                    if m_i == m_j or m_j not in scores.index:
                        continue
                    diffs.append(np.nanmean((v_i - scores.loc[m_j]) ** 2))
                vals.append(np.nanmean(diffs) if diffs else np.nan)
            fig.add_trace(go.Bar(x=short_names, y=vals, name=f"{ctx} context", marker_color=color, showlegend=(h == "H1")), row=r, col=c)
        fig.update_yaxes(title=f"Pairwise MSD ({h})", row=r, col=c)
    fig.update_xaxes(tickangle=45, tickfont=dict(size=10))
    fig.update_layout(height=1050, width=1500, title=dict(text="Model Agreement Overview", x=0.5, font=dict(size=26)), template="plotly_white", barmode="group")
    return _safe_write_plot(fig, output_dir, "07_model_agreement_dashboard", show=show, write_svg=write_svg)


def plot_context_score_distribution(df_long, output_dir=None, show=True, write_svg=False):
    """LO vs GO score distribution by study and hypothesis."""
    stats_df = df_long.groupby(["Base Study ID", "Context"])[HYPOTHESES].mean().reset_index()
    go_h1 = stats_df[stats_df["Context"] == "GO"].set_index("Base Study ID")["H1"].sort_values()
    order = list(go_h1.index)
    for study in sorted(df_long["Base Study ID"].unique()):
        if study not in order:
            order.append(study)
    fig = make_subplots(rows=3, cols=1, subplot_titles=[f"Hypothesis {h}" for h in HYPOTHESES], vertical_spacing=0.08, shared_xaxes=True)
    for i, h in enumerate(HYPOTHESES, start=1):
        for ctx, color, symbol in [("LO", LO_COLOR, "circle"), ("GO", GO_COLOR, "square")]:
            sub = stats_df[stats_df["Context"] == ctx].set_index("Base Study ID").reindex(order)
            fig.add_trace(go.Scatter(x=order, y=sub[h], mode="markers", name=ctx, marker=dict(color=color, symbol=symbol, size=9, opacity=0.75), showlegend=(i == 1)), row=i, col=1)
        fig.update_yaxes(title="score", range=[-1.05, 1.1], row=i, col=1)
    fig.update_xaxes(tickangle=45, tickfont=dict(size=10), row=3, col=1)
    fig.update_layout(height=1300, width=1500, title=dict(text="HPC Averaged Hypothesis Comparison (LO vs GO)", x=0.5, font=dict(size=24)), template="plotly_white")
    return _safe_write_plot(fig, output_dir, "08_context_score_distribution", show=show, write_svg=write_svg)


def plot_leave_one_out_consensus(df_long, output_dir=None, show=True, write_svg=False):
    """Leave-one-out literature consensus contribution for LO and GO."""
    lit = df_long[df_long["Study Type"].isin(["empirical", "other", "theoretical", "computational"])]
    lo_mat = calculate_msd_matrix(lit[lit["Context"] == "LO"], pivot_on="Base Study ID")
    go_mat = calculate_msd_matrix(lit[lit["Context"] == "GO"], pivot_on="Base Study ID")
    lo_inf = calculate_leave_one_out_influence(lo_mat)
    go_inf = calculate_leave_one_out_influence(go_mat)
    fig = make_subplots(rows=2, cols=1, subplot_titles=("LO Context", "GO Context"), vertical_spacing=0.15)
    for idx, (inf, label, color) in enumerate([(lo_inf, "LO", LO_COLOR), (go_inf, "GO", GO_COLOR)], start=1):
        sub = pd.DataFrame({"Study": list(inf.keys()), "Value": list(inf.values())}).sort_values("Value")
        fig.add_trace(go.Bar(x=sub["Study"], y=sub["Value"], marker_color=color, name=label, showlegend=False), row=idx, col=1)
        fig.update_yaxes(title="MSD contribution", row=idx, col=1)
    fig.update_xaxes(tickangle=45, tickfont=dict(size=9))
    fig.update_layout(title=dict(text="Leave-One-Out Consensus Contribution", x=0.5), height=850, template="plotly_white")
    return _safe_write_plot(fig, output_dir, "09_leave_one_out_consensus", show=show, write_svg=write_svg)


def plot_raw_score_distribution(df_long, output_dir=None, show=True, write_svg=False):
    """Box/point distribution for LO-H1..GO-H3 raw averaged scores."""
    fig = go.Figure()
    for ctx in CONTEXTS:
        for h in HYPOTHESES:
            vals = df_long[df_long["Context"] == ctx][h].dropna()
            fig.add_trace(go.Box(y=vals, name=f"{ctx}-{h}", boxpoints="all", jitter=0.15, pointpos=0, marker=dict(size=4, opacity=0.55)))
    fig.update_layout(title=dict(text="Global Score Cloud", x=0.5), yaxis=dict(title="Score [-1, 1]", range=[-1.1, 1.1]), height=600, template="plotly_white")
    return _safe_write_plot(fig, output_dir, "10_raw_score_distribution", show=show, write_svg=write_svg)


def plot_context_comparison(df_long, output_dir=None, show=True, write_svg=False):
    """Three-panel empirical/literature LO-vs-GO context comparison."""
    emp = df_long[df_long["Study Type"].isin(["empirical", "other"])].copy()
    pivot = emp.groupby(["Base Study ID", "Context"])[HYPOTHESES].mean().unstack("Context")
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


def plot_average_paper_msd(df_long, output_dir=None, show=True, write_svg=False):
    """Average paper MSD comparison for LO and GO."""
    lit = df_long[df_long["Study Type"].isin(["empirical", "other", "theoretical", "computational"])]
    lo_mat = calculate_msd_matrix(lit[lit["Context"] == "LO"], pivot_on="Base Study ID")
    go_mat = calculate_msd_matrix(lit[lit["Context"] == "GO"], pivot_on="Base Study ID")
    msd_df = pd.DataFrame({"LO": lo_mat.mean(axis=1), "GO": go_mat.mean(axis=1)}).dropna().sort_values("LO")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=msd_df.index, y=msd_df["LO"], mode="markers", marker=dict(color=LO_COLOR, size=10, symbol="circle", line=dict(width=0.5, color="black")), name="LO"))
    fig.add_trace(go.Scatter(x=msd_df.index, y=msd_df["GO"], mode="markers", marker=dict(color=GO_COLOR, size=10, symbol="square", line=dict(width=0.5, color="black")), name="GO"))
    fig.update_xaxes(tickangle=45, tickfont=dict(size=10))
    fig.update_yaxes(title="Average MSD", zeroline=True, zerolinecolor="black")
    fig.update_layout(title=dict(text="Average Paper MSD Comparison (LO vs GO)", x=0.5, font=dict(size=20)), template="plotly_white", height=650)
    return _safe_write_plot(fig, output_dir, "12_average_paper_msd", show=show, write_svg=write_svg)


def plot_study_shift_bars(df_long, output_dir=None, show=True, write_svg=False):
    """Horizontal bars: mean absolute context shift by study."""
    pivot = df_long.groupby(["Base Study ID", "Study Type", "Context"])[HYPOTHESES].mean().reset_index()
    lo = pivot[pivot["Context"] == "LO"].set_index("Base Study ID")[HYPOTHESES]
    go_scores = pivot[pivot["Context"] == "GO"].set_index("Base Study ID")[HYPOTHESES]
    shift = (go_scores - lo).abs().mean(axis=1).reset_index(name="Mean Abs Shift")
    type_map = pivot[["Base Study ID", "Study Type"]].drop_duplicates()
    shift = shift.merge(type_map, on="Base Study ID", how="left").sort_values("Mean Abs Shift", ascending=True)
    fig = go.Figure()
    for stype in shift["Study Type"].fillna("unknown").unique():
        sub = shift[shift["Study Type"].fillna("unknown") == stype]
        fig.add_trace(go.Bar(y=sub["Base Study ID"], x=sub["Mean Abs Shift"], orientation="h", name=str(stype), marker_color=TYPE_COLORS.get(str(stype), TYPE_COLORS["unknown"])))
    fig.update_layout(title=dict(text="Mean Absolute Context Shift (|GO - LO|) by Study", x=0.5), xaxis_title="Mean absolute shift", yaxis_title="Study", barmode="group", height=850, template="plotly_white")
    return _safe_write_plot(fig, output_dir, "13_study_shift_bars", show=show, write_svg=write_svg)

# --- CELL ---


# Resolve CSV. This keeps your Drive path, but also works with an uploaded Colab CSV or the attached test CSV.
if __name__ == "__main__":
    CSV_PATH = "examples/hpc_table_final.csv"