from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


def cluster_signals(df, n_clusters=3):
    if df.empty:
        raise ValueError("Cannot cluster an empty signal set.")

    clustered = df.copy()
    cluster_count = max(1, min(n_clusters, len(clustered)))

    vectorizer = TfidfVectorizer(stop_words="english")
    x = vectorizer.fit_transform(clustered["text"])

    model = KMeans(n_clusters=cluster_count, random_state=42, n_init=10)
    clustered["cluster"] = model.fit_predict(x)

    return clustered
