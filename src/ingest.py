# placeholder
import json
import pandas as pd


def load_signals(path="data/synthetic_business_signals.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)


def normalize_signals(df):
    df["text"] = df["text"].str.lower()
    return df