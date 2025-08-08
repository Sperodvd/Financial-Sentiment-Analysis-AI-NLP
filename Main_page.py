import streamlit as st


about_page = st.Page(
    page="pages/Title_page.py",
    title="About",
    icon=":material/info:",
    default=True,
)

project_page = st.Page(
    page="pages/Sentiment_analysis.py",
    title="Financial SentimentAnalysis",
    icon=":material/analytics:",
)
pg = st.navigation(pages=[about_page, project_page])
pg.run()
