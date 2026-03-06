from pathlib import Path
from src.ingest import load_signals, normalize_signals
from src.classify import apply_classification
from src.cluster import cluster_signals
from src.synthesize import synthesize_clusters


def generate_brief():
    df = load_signals()
    df = normalize_signals(df)
    df = apply_classification(df)
    df = cluster_signals(df)

    summary = synthesize_clusters(df)

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "sample_decision_brief.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Executive Decision Brief\n\n")
        f.write("## Top Emerging Signals\n\n")

        for cluster_id, details in summary.items():
            f.write(f"### Pattern {cluster_id}\n")
            f.write(f"- Signal Count: {details['count']}\n")
            f.write(f"- Sources: {', '.join(details['sources'])}\n")
            f.write(f"- Example: {details['sample_issue']}\n")
            f.write(f"- Evidence IDs: {', '.join(details['evidence_ids'])}\n\n")

        f.write("## Suggested Executive Actions\n\n")
        f.write("- Review repeated friction points across sources.\n")
        f.write("- Investigate signals with possible churn or revenue risk.\n")
        f.write("- Prioritize clusters that appear in multiple business contexts.\n")

    print(f"Executive brief generated at: {output_file}")


if __name__ == "__main__":
    generate_brief()