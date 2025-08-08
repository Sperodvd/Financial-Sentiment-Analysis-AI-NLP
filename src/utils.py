import pandas as pd

def aggregate_sentiment(sentiments):
    counts = pd.Series(sentiments).value_counts(normalize=True)
    if "POSITIVE" in counts:
        return int(counts["POSITIVE"] * 100)
    return 0