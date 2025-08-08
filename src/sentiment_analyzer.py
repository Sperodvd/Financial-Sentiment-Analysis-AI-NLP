from transformers import pipeline

def get_sentiment_pipeline():
    try:
        return pipeline("sentiment-analysis", model="ProsusAI/finbert")
    except Exception:
        return pipeline("sentiment-analysis")

sentiment_pipeline = get_sentiment_pipeline()

def analyze_headlines(headlines):
    results = sentiment_pipeline(headlines)
    return [res["label"].upper() for res in results]