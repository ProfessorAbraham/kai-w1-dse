import pandas as pd
import numpy as np
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import yfinance as yf

# Load news and stock datasets
news_data = pd.read_csv('news_data.csv')  # Replace 'news_data.csv' with the actual filename
stock_data = yf.download('AAPL', start='2021-01-01', end='2021-12-31')

# Data Preparation
# Normalize Dates
news_data['Date'] = pd.to_datetime(news_data['Date'])
stock_data['Date'] = pd.to_datetime(stock_data.index)
merged_data = pd.merge(news_data, stock_data, on='Date', how='inner')

# Sentiment Analysis
# Example using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

merged_data['Sentiment'] = merged_data['Headline'].apply(get_sentiment)

# Calculate Stock Movements
merged_data['Daily_Returns'] = merged_data['Close'].pct_change() * 100

# Correlation Analysis
# Aggregate Sentiments
daily_sentiments = merged_data.groupby('Date')['Sentiment'].value_counts(normalize=True).unstack().fillna(0)
daily_sentiments['Average_Sentiment'] = (daily_sentiments['Positive'] - daily_sentiments['Negative']) * 100

# Calculate Correlation
correlation = np.corrcoef(daily_sentiments['Average_Sentiment'], merged_data['Daily_Returns'])

print("Correlation between average daily sentiment and daily stock returns:", correlation[0, 1])
