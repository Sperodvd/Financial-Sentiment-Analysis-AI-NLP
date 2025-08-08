Product Requirements Document (PRD)
Real-Time Stock Sentiment Analysis Dashboard
Author: Gemini
Date: July 30, 2025
Version: 1.1

1. Overview
This document outlines the requirements for the Stock Sentiment Analysis Dashboard. This interactive web application will provide retail investors and financial enthusiasts with a simple tool to gauge market sentiment for a specific publicly traded stock. By entering a stock ticker, users can view an aggregated sentiment score derived from recent news headlines, helping them make more informed decisions.

2. Problem Statement
Retail investors are often overwhelmed by the sheer volume of financial news. It's difficult to read through dozens of articles to get a sense of whether the current sentiment is positive, negative, or neutral. A simple, data-driven tool is needed to aggregate this sentiment into an easily digestible score, providing a quick snapshot of the market's mood.

3. Goals & Objectives
Primary Goal: To empower retail investors by providing a simple, near real-time sentiment analysis tool for individual stocks.

Objectives:

Develop a user-friendly interface that requires no financial or technical expertise to use.

Integrate with a reliable, free-to-host news API to fetch relevant financial news.

Utilize a pre-trained machine learning model to accurately classify the sentiment of news headlines.

Present the aggregated sentiment in a clear, visual, and intuitive manner.

Clearly communicate any data latency to the user.

4. Target Audience
Primary: Retail investors and stock market hobbyists who manage their own portfolios.

Secondary: Financial students, analysts, and journalists looking for a quick sentiment pulse check.

5. Features & Scope
Version 1.0 (MVP)
Feature ID

Feature Name

Description

Priority

F-01

Stock Ticker Input

A text input field where the user can enter a valid stock ticker symbol (e.g., AAPL, TSLA, GOOGL).

Must-Have

F-02

Fetch News Button

A button that initiates the analysis process.

Must-Have

F-03

Sentiment Analysis Engine

The backend logic that fetches news from the REST API, processes each headline through the sentiment model, and calculates an overall score. Note: The free API has a 12-hour data delay, which should be noted in the UI.

Must-Have

F-04

Overall Sentiment Display

A clear visual indicator (e.g., a metric, gauge, or progress bar) that displays the aggregated sentiment score (e.g., 75% Positive).

Must-Have

F-05

Headline Display Table

A table that lists the recent news headlines used for the analysis, along with their individual sentiment classification (Positive, Negative, Neutral).

Must-Have

F-06

Responsive UI

The application must be usable on both desktop and mobile devices.

High

F-07

Error Handling

The app should gracefully handle invalid ticker symbols or API failures with a user-friendly message.

High

6. Technical Requirements
Frontend/Hosting: Streamlit

Programming Language: Python

Data Source: Newsdata.io API (Free tier allows for hosted, non-commercial use with a 12-hour delay).

Machine Learning Model: A pre-trained sentiment analysis model from the Hugging Face transformers library (e.g., distilbert-base-uncased-finetuned-sst-2-english or a finance-specific model like FinBERT).

7. Success Metrics
User Engagement: Number of unique users and analyses run per day.

User Feedback: Qualitative feedback gathered from users on the tool's usefulness and accuracy.

Performance: The end-to-end analysis time (from button click to result display) should be under 5 seconds.

8. Future Considerations (Post-MVP)
Historical Sentiment Charting: Allow users to view sentiment trends over time (e.g., last 7 days, 30 days).

Upgrade to Paid API: For real-time data, upgrade to a paid API plan.

Source Filtering: Allow users to include or exclude specific news sources from the analysis.