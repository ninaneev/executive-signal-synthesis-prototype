def synthesize_clusters(df):
    summary = {}

    for cluster_id in sorted(df["cluster"].unique()):
        cluster_df = df[df["cluster"] == cluster_id]

        summary[cluster_id] = {
            "count": len(cluster_df),
            "sources": list(cluster_df["source"].unique()),
            "sample_issue": cluster_df.iloc[0]["text"],
            "evidence_ids": list(cluster_df["id"].head(5))
        }

    return summary