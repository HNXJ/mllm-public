import json
from pathlib import Path

def render_plan(data, out_path):
    with open(out_path, "w") as f:
        f.write("# Developer Plan\n\n")
        f.write("## Section 1: Brainstorm\n")
        f.write(data.get("brainstorm", "") + "\n\n")
        f.write("## Section 2: Execution Plan Table\n\n")
        
        table = data.get("table", [])
        if not table:
            f.write("*No plan items.*\n")
            return
            
        headers = ["File", "Purpose", "Score", "Actions", "Rules", "Edits", "Notes", "Cautions"]
        f.write(" | ".join(headers) + "\n")
        f.write(" | ".join(["---"] * len(headers)) + "\n")
        for row in table:
            vals = [
                row.get("file", ""),
                row.get("purpose", ""),
                f"{row.get('score', 0)}/100",
                row.get("actions", ""),
                row.get("rules", ""),
                row.get("edits", ""),
                row.get("notes", ""),
                row.get("cautions", "")
            ]
            f.write(" | ".join(str(v).replace("\n", "<br>") for v in vals) + "\n")

def render_review(data, out_path):
    with open(out_path, "w") as f:
        f.write("# Developer Review\n\n")
        f.write("## Section 1: Review Summary\n")
        f.write(data.get("summary", "") + "\n\n")
        f.write("## Section 2: Codebase Evaluation Table\n\n")
        
        table = data.get("table", [])
        if not table:
            f.write("*No review items.*\n")
            return
            
        headers = ["File", "Purpose", "Score", "Assessment", "Warnings", "Design Choices", "Notes", "Cautions"]
        f.write(" | ".join(headers) + "\n")
        f.write(" | ".join(["---"] * len(headers)) + "\n")
        for row in table:
            vals = [
                row.get("file", ""),
                row.get("purpose", ""),
                f"{row.get('score', 0)}/100",
                row.get("assessment", ""),
                row.get("warnings", ""),
                row.get("design_choices", ""),
                row.get("notes", ""),
                row.get("cautions", "")
            ]
            f.write(" | ".join(str(v).replace("\n", "<br>") for v in vals) + "\n")

def render_progress(data, out_path):
    with open(out_path, "w") as f:
        f.write("# Developer Progress\n\n")
        f.write("## Section 1: Progress Summary\n")
        f.write(data.get("summary", "") + "\n\n")
        f.write("## Section 2: Implementation Progress Table\n\n")
        
        table = data.get("table", [])
        if not table:
            f.write("*No progress items.*\n")
            return
            
        headers = ["File", "Purpose", "Score", "Staged Edits", "Status", "Notes", "Cautions"]
        f.write(" | ".join(headers) + "\n")
        f.write(" | ".join(["---"] * len(headers)) + "\n")
        for row in table:
            vals = [
                row.get("file", ""),
                row.get("purpose", ""),
                f"{row.get('score', 0)}/100",
                row.get("staged_edits", ""),
                row.get("status", ""),
                row.get("notes", ""),
                row.get("cautions", "")
            ]
            f.write(" | ".join(str(v).replace("\n", "<br>") for v in vals) + "\n")

def main():
    root = Path(__file__).resolve().parents[1]
    
    plan_json = root / "plan.json"
    if plan_json.exists():
        with open(plan_json, "r") as f:
            render_plan(json.load(f), root / "plan.md")
            
    review_json = root / "review.json"
    if review_json.exists():
        with open(review_json, "r") as f:
            render_review(json.load(f), root / "review.md")
            
    progress_json = root / "progress.json"
    if progress_json.exists():
        with open(progress_json, "r") as f:
            render_progress(json.load(f), root / "progress.md")
            
    print("Rendered plan, review, and progress markdown views successfully.")

if __name__ == "__main__":
    main()
