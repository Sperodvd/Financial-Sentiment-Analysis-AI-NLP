import streamlit as st
import pandas as pd
from src.news_fetcher import fetch_news
from src.sentiment_analyzer import analyze_headlines
from src.utils import aggregate_sentiment
from datetime import datetime, timedelta
import plotly.express as px
from wordcloud import WordCloud
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="Financial Sentiment Analysis", layout="wide")

st.title("Financial Sentiment Analysis")
st.write("Enter a stock ticker to analyze recent news sentiment. (Data may be delayed up to 12 hours.)")


ticker = st.text_input("Stock Ticker (e.g., AAPL, TSLA, GOOGL)")
if st.button("Fetch News & Analyze"):
    if not ticker:
        st.error("Please enter a stock ticker.")
    else:
        try:
            articles = fetch_news(ticker)
            if not articles:
                st.warning("No news found for this ticker.")
            else:
                df = pd.DataFrame(articles)
                df['date'] = pd.to_datetime(df['pubDate']).dt.date
                df['sentiment'] = analyze_headlines(df['title'].tolist())

                score = aggregate_sentiment(df['sentiment'].tolist())
                st.metric("Overall Positive Sentiment", f"{score}%")

                st.dataframe(df[['date', 'title', 'sentiment']].rename(
                    columns={'date': 'Date', 'title': 'Headline', 'sentiment': 'Sentiment'}
                ))

                # Bar graph for sentiment counts (horizontal)
                sentiment_counts = df['sentiment'].value_counts().reindex(['NEGATIVE', 'NEUTRAL', 'POSITIVE'], fill_value=0)
                st.subheader("Sentiment Distribution")
                import plotly.express as px
                fig = px.bar(
                    sentiment_counts.reset_index(),
                    x='sentiment', y='count',
                    labels={'sentiment': 'Sentiment', 'count': 'Count'},
                    color='sentiment',
                    color_discrete_map={'NEGATIVE': 'red', 'NEUTRAL': 'gray', 'POSITIVE': 'green'}
                )
                fig.update_layout(yaxis={'categoryorder':'array', 'categoryarray':['NEGATIVE', 'NEUTRAL', 'POSITIVE']})
                st.plotly_chart(fig, use_container_width=True)

                # Word cloud (if you want to keep it)
                st.subheader("Key Topics in News Headlines")
                text = " ".join(df['title'].tolist())
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
                buf = BytesIO()
                wordcloud.to_image().save(buf, format='PNG')
                st.image(buf.getvalue(), use_column_width=True)
        except Exception as e:
            st.error(f"Error: {e}")