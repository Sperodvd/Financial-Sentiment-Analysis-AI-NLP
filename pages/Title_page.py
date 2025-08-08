import streamlit as st

st.set_page_config(page_title="About", layout="wide")

st.title("Financial Sentiment Analysis Dashboard")
st.markdown("""
## Overeview
This application allows you to analyze the sentiment of recent news headlines for any stock ticker using AI-powered sentiment analysis.

---

### Key Features
- Fetches recent news from Newsdata.io REST API for the selected stock ticker.
- Utilizes the Huggingface transformers library, specifically the ProsusAI/finbert model, to classify each headline as Positive, Negative or Neutral
- Visualizes the distribution of sentiment with interactive charts
- Highlights key topics in the news using a word cloud

### How to Use
1. Enter a stock ticker symbol (e.g., AAPL, TSLA, GOOGL) in the input box.
2. The app retrieves the latest business news headlines related to the ticker from Newsdata.io.
3. Each headline is analyzed for sentiment using the FinBERT transformer model, which is fined-tuned for financial text.
4. Results are displayed as an overall sentiment score, a breakdown of individual headlines, a sentiment distribution bar chart, and a word cloud of headline keywords.\

---

**Developed for educational purposes and designed to quickly gauge market sentiment around a particular stock utilizing latest advancement in natural language processing.**
""")