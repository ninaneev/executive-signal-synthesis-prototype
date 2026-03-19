from pathlib import Path

from src.classify import apply_classification
from src.cluster import cluster_signals
from src.ingest import load_signals, normalize_signals


def evaluate():
    df = load_signals()
    df = normalize_signals(df)
    df = apply_classification(df)
    total_signals = len(df)

    clustered = cluster_signals(df)
    total_clusters = len(clustered["cluster"].unique())

    cross_source = 0

    for c in clustered["cluster"].unique():
        sources = clustered[clustered["cluster"] == c]["source"].unique()
        if len(sources) > 1:
            cross_source += 1

    compression_ratio = total_signals / total_clusters
    cross_source_ratio = cross_source / total_clusters
    high_urgency_signals = int((clustered["urgency"] == "high").sum())

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    report_path = output_dir / "evaluation_report.md"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# ESS Evaluation Report\n\n")
        f.write("## Metrics\n\n")
        f.write(f"- Total signals: {total_signals}\n")
        f.write(f"- Total clusters: {total_clusters}\n")
        f.write(f"- Cross-source clusters: {cross_source}\n")
        f.write(f"- Cross-source ratio: {cross_source_ratio:.2f}\n")
        f.write(f"- Signal compression ratio: {compression_ratio:.2f}\n")
        f.write(f"- High-urgency signals: {high_urgency_signals}\n\n")
        f.write("## Interpretation\n\n")
        f.write(
            "These metrics are exploratory and indicate whether heterogeneous signals "
            "are being compressed into fewer patterns without losing cross-source overlap.\n"
        )

    print("Total signals:", total_signals)
    print("Total clusters:", total_clusters)
    print("Cross-source clusters:", cross_source)
    print("Cross-source ratio:", cross_source_ratio)
    print("Signal compression ratio:", compression_ratio)
    print("High-urgency signals:", high_urgency_signals)
    print(f"Evaluation report generated at: {report_path}")

    return {
        "total_signals": total_signals,
        "total_clusters": total_clusters,
        "cross_source_clusters": cross_source,
        "cross_source_ratio": cross_source_ratio,
        "signal_compression_ratio": compression_ratio,
        "high_urgency_signals": high_urgency_signals,
        "report_path": str(report_path),
    }


if __name__ == "__main__":
    evaluate()
