import argparse
from mllm.vis.plotting import run_all_visualizations

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run MLLM Visualizations")
    parser.add_argument("--csv_path", default=None, help="Path to aggregated scores CSV")
    parser.add_argument("--reports_dir", default=None, help="Directory to save report HTML/SVGs")
    args = parser.parse_args()
    run_all_visualizations(csv_path=args.csv_path, reports_dir=args.reports_dir)
