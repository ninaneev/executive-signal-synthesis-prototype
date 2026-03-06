from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def cluster_signals(df, n_clusters=3):
    vectorizer = TfidfVectorizer(stop_words="english")
    x = vectorizer.fit_transform(df["text"])

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["cluster"] = model.fit_predict(x)

    return df