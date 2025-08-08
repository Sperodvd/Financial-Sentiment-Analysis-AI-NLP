Stock Sentiment Analysis Dashboard
An interactive web application built with Streamlit that fetches recent news for a given stock ticker from the Newsdata.io API, performs sentiment analysis on the headlines using a Hugging Face transformer model, and displays the aggregated sentiment.

This project is designed to be hosted live using a free API tier that permits public, non-commercial use.

Features
Recent News Data: Fetches news articles from the Newsdata.io REST API. (Note: The free tier has a 12-hour delay.)

AI-Powered Sentiment Analysis: Uses a pre-trained transformer model to classify news headlines as POSITIVE, NEGATIVE, or NEUTRAL.

Interactive Dashboard: A simple, clean user interface for entering a stock ticker and viewing results.

Aggregated Score: Displays an overall sentiment score for a quick, at-a-glance understanding.

Detailed Breakdown: Shows individual headlines and their assigned sentiment.

Tech Stack
Framework: Streamlit

Language: Python 3.8+

Data Source: Newsdata.io API (Free tier is suitable for hosted portfolio projects)

Libraries:

streamlit - For the web app interface.

requests - For making HTTP requests to the news API.

pandas - For data manipulation and display.

transformers - For loading the sentiment analysis model from Hugging Face.

torch or tensorflow - As a backend for the transformers library.

Setup and Installation
1. Clone the Repository
git clone [https://github.com/your-username/stock-sentiment-analyzer.git](https://github.com/your-username/stock-sentiment-analyzer.git)
cd stock-sentiment-analyzer

2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies
pip install -r requirements.txt

(You will need to create a requirements.txt file containing the libraries listed in the Tech Stack section).

4. Set Up Free API Key
Go to Newsdata.io and register for a free API key. No credit card is required.

Create a file named .env in the root of the project directory.

Add your API key to the .env file like this:

NEWSDATA_API_KEY="YOUR_API_KEY_HERE"

Note: You will need to install python-dotenv (pip install python-dotenv) and load this in your Python script.

How to Run the Application
Once the setup is complete, run the following command in your terminal:

streamlit run app.py

The application should now be open and running in your web browser.

Deployment (DevOps)
This application is designed for easy, free deployment on platforms like Streamlit Community Cloud.

Push to GitHub: Ensure your project, including the requirements.txt file, is pushed to a public GitHub repository.

Deploy on Streamlit Cloud:

Connect your GitHub account to Streamlit Community Cloud.

Deploy the app directly from your repository.

In the advanced settings, add your NEWSDATA_API_KEY to the Streamlit secrets manager. This keeps your key secure and out of your public code.