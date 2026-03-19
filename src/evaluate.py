from src.ingest import load_signals
from src.cluster import cluster_signals


def evaluate():
    df = load_signals()
    total_signals = len(df)

    clustered = cluster_signals(df)

    total_clusters = len(clustered["cluster"].unique())

    cross_source = 0

    for c in clustered["cluster"].unique():
        sources = clustered[clustered["cluster"] == c]["source"].unique()
        if len(sources) > 1:
            cross_source += 1

    compression_ratio = total_signals / total_clusters

    print("Total signals:", total_signals)
    print("Total clusters:", total_clusters)
    print("Cross-source clusters:", cross_source)
    print("Cross-source ratio:", cross_source / total_clusters)
    print("Signal compression ratio:", compression_ratio)


if __name__ == "__main__":
    evaluate()