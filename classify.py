import pandas as pd

def classify_signal(text):
    tags = {
        "signal_type": "friction",
        "urgency": "medium",
        "possible_churn_risk": False,
        "possible_revenue_risk": False
    }

    if "delay" in text or "confusion" in text:
        tags["urgency"] = "high"

    if "churn" in text or "cancel" in text:
        tags["possible_churn_risk"] = True

    if "enterprise" in text:
        tags["possible_revenue_risk"] = True

    return tags


def apply_classification(df):
    classifications = df["text"].apply(classify_signal)
    return df.join(classifications.apply(pd.Series))