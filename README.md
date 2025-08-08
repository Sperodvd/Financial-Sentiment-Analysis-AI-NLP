# Financial Sentiment Analysis Dashboard

An interactive web application built with Streamlit that fetches recent news for a given stock ticker from the Newsdata.io API, performs sentiment analysis on the headlines using a Hugging Face transformer model, and displays the aggregated sentiment.

This project is designed to be hosted live using a free API tier that permits public, non-commercial use.

## Features

- **Recent News Data:** Fetches news articles from the Newsdata.io REST API. (Note: The free tier has a 12-hour delay.)
- **AI-Powered Sentiment Analysis:** Uses a pre-trained transformer model to classify news headlines as POSITIVE, NEGATIVE, or NEUTRAL.
- **Interactive Dashboard:** A simple, clean user interface for entering a stock ticker and viewing results.
- **Aggregated Score:** Displays an overall sentiment score for a quick, at-a-glance understanding.
- **Detailed Breakdown:** Shows individual headlines and their assigned sentiment.

## Tech Stack

- **Framework:** Streamlit
- **Language:** Python 3.8+
- **Data Source:** Newsdata.io API (Free tier is suitable for hosted portfolio projects)
- **Libraries:** streamlit, requests, pandas, transformers, torch, python-dotenv

## Setup and Installation

1. **Clone the Repository**
    ```bash
    git clone <your-repo-url>
    cd "Financial Sentiment Analysis Dashboard"
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    # or
    source venv/bin/activate  # On macOS/Linux
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Free API Key**
    - Register at [Newsdata.io](https://newsdata.io/) for a free API key.
    - Create a `.env` file in the project root:
      ```
      NEWSDATA_API_KEY=your_actual_api_key_here
      ```

5. **Run the Application**
    ```bash
    streamlit run app.py
    ```

6. **Run Tests (Optional)**
    ```bash
    pytest tests/
    ```

## Deployment

- Push your code to GitHub.
- Deploy on [Streamlit Community Cloud](https://streamlit.io/cloud) (connect your repo, set the API key in secrets).