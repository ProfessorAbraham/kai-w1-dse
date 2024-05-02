import pandas as pd
import matplotlib.pyplot as plt
import talib
import pynance as pn

# Load and prepare the data
# Replace 'YOUR_STOCK_TICKER' with the actual ticker symbol of the stock you want to analyze
stock_data = pn.data.get('C:\\Users\\Professor Ab\\OneDrive - amu.edu.et\\Desktop\\Data Science\\kai-w1-dse\\data\\raw_analyst_ratings.csv')
# You can also read your data from a CSV file if you have it stored locally

# Calculate basic technical indicators using TA-Lib
# Example: Moving average
stock_data['SMA_50'] = talib.SMA(stock_data['Close'], timeperiod=50)
stock_data['SMA_200'] = talib.SMA(stock_data['Close'], timeperiod=200)
# You can calculate other indicators like RSI, MACD, etc., using similar functions from TA-Lib

# Use PyNance for financial metrics
returns = pn.returns.returns(stock_data['Close'])

# Visualize the data
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['SMA_50'], label='50-Day SMA')
plt.plot(stock_data['SMA_200'], label='200-Day SMA')
plt.legend()
plt.title('Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
