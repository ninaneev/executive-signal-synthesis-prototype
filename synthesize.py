def synthesize_clusters(df):
    summary = {}

    for cluster_id in df["cluster"].unique():
        cluster_df = df[df["cluster"] == cluster_id]
        summary[cluster_id] = {
            "count": len(cluster_df),
            "sources": list(cluster_df["source"].unique()),
            "sample_issue": cluster_df.iloc[0]["text"]
        }

    return summary