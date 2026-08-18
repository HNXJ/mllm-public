import argparse
from jmllm.vis.plotting import run_all_visualizations

def main():
    parser = argparse.ArgumentParser(description="Run MLLM Manuscript Visualizations")
    parser.add_argument("--csv_path", default=None, help="Path to 90-column hpc_table_final.csv")
    parser.add_argument("--scores_csv", default=None, help="Path to raw scores.csv (will auto-convert)")
    parser.add_argument("--reports_dir", default=None, help="Directory to save report HTML/SVGs")
    args = parser.parse_args()
    run_all_visualizations(csv_path=args.csv_path, scores_path=args.scores_csv, reports_dir=args.reports_dir)

if __name__ == "__main__":
    main()
