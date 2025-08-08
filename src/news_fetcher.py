import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
API_KEY = os.getenv("NEWSDATA_API_KEY")

def fetch_news(ticker, days_back=7):
    url = (
        f"https://newsdata.io/api/1/news?apikey={API_KEY}"
        f"&q={ticker}&language=en&category=business"
    )
    response = requests.get(url)
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    if response.status_code != 200:
        raise Exception("Failed to fetch news data.")
    data = response.json()
    if "results" not in data:
        raise Exception("No news results found.")
    # Filter articles by pubDate in Python
    from_date = (datetime.utcnow() - timedelta(days=days_back)).date()
    articles = [
        {"title": item["title"], "pubDate": item.get("pubDate", "")}
        for item in data["results"]
        if "title" in item and "pubDate" in item
    ]
    filtered = [
        a for a in articles
        if a["pubDate"] and datetime.strptime(a["pubDate"][:10], "%Y-%m-%d").date() >= from_date
    ]
    return filtered