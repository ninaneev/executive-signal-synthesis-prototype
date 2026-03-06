from ingest import load_signals, normalize_signals
from classify import apply_classification
from cluster import cluster_signals
from synthesize import synthesize_clusters


def generate_brief():
    df = load_signals()
    df = normalize_signals(df)
    df = apply_classification(df)
    df = cluster_signals(df)

    summary = synthesize_clusters(df)

    with open("outputs/sample_decision_brief.md", "w") as f:
        f.write("# Executive Decision Brief\n\n")

        for cluster_id, details in summary.items():
            f.write(f"## Pattern {cluster_id}\n")
            f.write(f"- Signal Count: {details['count']}\n")
            f.write(f"- Sources: {details['sources']}\n")
            f.write(f"- Example: {details['sample_issue']}\n\n")

    print("Executive brief generated.")


if __name__ == "__main__":
    generate_brief()