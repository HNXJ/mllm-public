import plotly.graph_objects as go
import numpy as np
import random

def create_mllm_v3_flowchart():
    """
    Refactored MLLM pipeline visualization (v3).
    Style: Grey nodes (50-70% alpha), White lines, Gold text (#CFB87C).
    Logic: Parallel vision analysis with 4 Qwen2.5-VL instances.
    """
    random.seed(42)
    
    # Color palette
    GOLD = "#CFB87C"
    GREY = "rgba(128, 128, 128, 0.6)"
    WHITE = "rgba(255, 255, 255, 0.8)"
    GLOW_GREY = "rgba(200, 200, 200, 0.9)"

    # Base coordinates (Step increment = 40 units)
    # [x, y, z, color, shape, metadata]
    nodes = {
        "PDF Source": [0, 0, 0, GREY, "sphere", "Input: Research Papers"],
        "PyMuPDF (Extract)": [40, 0, 0, GREY, "cube", "Step 1: Text & Page Rects"],
        "Parallel Dispatch": [80, 0, 0, GREY, "sphere", "Step 2: ThreadPoolExecutor"],
        
        # Parallel Vision Nodes (Stochastic Deviance ±20°)
        "Qwen2.5-VL (P4475)": [120, 15, 10, GREY, "sphere", "Vision 1: 8-bit / DeepRead"],
        "Qwen2.5-VL (P4476)": [120, 5, -5, GREY, "sphere", "Vision 2: 8-bit / DeepRead"],
        "Qwen2.5-VL (P4477)": [120, -5, 10, GREY, "sphere", "Vision 3: 8-bit / DeepRead"],
        "Qwen2.5-VL (P4478)": [120, -15, -5, GREY, "sphere", "Vision 4: 8-bit / DeepRead"],
        
        "Unified Markdown": [160, 0, 0, GREY, "sphere", "Step 3: Text + Visuals Consolidation"],
        "TextCompressor": [200, 0, 0, GREY, "cube", "Step 4: Semantic Chunking (-40%)"],
        
        "deepseek-r1-70b (P4474)": [240, 0, 15, GREY, "sphere", "Step 5: Reasoning (LM Studio)"],
        "Evaluation Loop": [280, 0, 0, GREY, "sphere", "Step 6: Recursive Chunking Logic"],
        
        "Master JSON": [320, 0, 0, GREY, "cube", "Step 7: Structured Output"],
        "Evaluation Reports": [360, 0, 0, GREY, "sphere", "Output: HPC/ADB/SCZ Scores"]
    }

    edges = [
        ("PDF Source", "PyMuPDF (Extract)", "Ingest"),
        ("PyMuPDF (Extract)", "Parallel Dispatch", "Segments"),
        ("Parallel Dispatch", "Qwen2.5-VL (P4475)", "Load 1"),
        ("Parallel Dispatch", "Qwen2.5-VL (P4476)", "Load 2"),
        ("Parallel Dispatch", "Qwen2.5-VL (P4477)", "Load 3"),
        ("Parallel Dispatch", "Qwen2.5-VL (P4478)", "Load 4"),
        ("Qwen2.5-VL (P4475)", "Unified Markdown", "OCR Data"),
        ("Qwen2.5-VL (P4476)", "Unified Markdown", "OCR Data"),
        ("Qwen2.5-VL (P4477)", "Unified Markdown", "OCR Data"),
        ("Qwen2.5-VL (P4478)", "Unified Markdown", "OCR Data"),
        ("PyMuPDF (Extract)", "Unified Markdown", "Raw Text"),
        ("Unified Markdown", "TextCompressor", "Process"),
        ("TextCompressor", "deepseek-r1-70b (P4474)", "Reasoning"),
        ("deepseek-r1-70b (P4474)", "Evaluation Loop", "Inference"),
        ("Evaluation Loop", "Master JSON", "Consolidate"),
        ("Master JSON", "Evaluation Reports", "Finalize")
    ]

    fig = go.Figure()

    # --- Add Nodes ---
    for name, data in nodes.items():
        symbol = 'circle' if data[4] == "sphere" else 'square'
        # Node Trace
        fig.add_trace(go.Scatter3d(
            x=[data[0]], y=[data[1]], z=[data[2]],
            mode='markers+text',
            text=[name],
            textposition="top center",
            hovertext=[data[5]],
            marker=dict(
                size=18, 
                color=data[3], 
                symbol=symbol, 
                opacity=0.6,
                line=dict(color=GLOW_GREY, width=2)
            ),
            textfont=dict(color=GOLD, size=11),
            name=name
        ))

    # --- Add Edges ---
    for start, end, label in edges:
        p1, p2 = nodes[start], nodes[end]
        fig.add_trace(go.Scatter3d(
            x=[p1[0], p2[0]], y=[p1[1], p2[1]], z=[p1[2], p2[2]],
            mode='lines',
            line=dict(color=WHITE, width=2),
            showlegend=False
        ))
        
        # Stochastic label placement
        mx, my, mz = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2
        fig.add_trace(go.Scatter3d(
            x=[mx], y=[my], z=[mz], 
            mode='text', 
            text=[label], 
            textfont=dict(color='rgba(255,255,255,0.6)', size=9), 
            showlegend=False
        ))

    # Layout Updates
    fig.update_layout(
        title=dict(
            text="MLLM Parallelized Pipeline v3: Multi-Qwen Vision Architecture", 
            font=dict(color=GOLD, size=24), 
            x=0.5
        ),
        paper_bgcolor='black',
        plot_bgcolor='black',
        scene=dict(
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title='', showbackground=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title='', showbackground=False),
            zaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title='', showbackground=False),
            bgcolor='black',
            aspectmode='manual',
            aspectratio=dict(x=4, y=1, z=1),
            camera=dict(
                eye=dict(x=0, y=-2.8, z=0.5), # Angled side view
                up=dict(x=0, y=0, z=1),
                center=dict(x=0, y=0, z=0)
            )
        ),
        margin=dict(l=0, r=0, b=0, t=60),
        showlegend=False
    )

    output_html = "./workspace/MLLM_Local/mllm_plantation_architecture_3d_v3.html"
    fig.write_html(output_html)
    print(f"v3 Flowchart saved to {output_html}")

if __name__ == "__main__":
    create_mllm_v3_flowchart()
