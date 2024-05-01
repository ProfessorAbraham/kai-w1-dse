import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import pyfolio as pf
import warnings

# Silence warnings
warnings.filterwarnings('ignore')

# Get the data for MSFT from Yahoo Finance
msft = yf.Ticker("MSFT")

# Get all stock info
msft_info = msft.info

# Print some basic info about the stock
print("Name:", msft_info['longName'])
print("Industry:", msft_info['industry'])
print("Sector:", msft_info['sector'])
print("Country:", msft_info['country'])

# Fetch historical data for MSFT
hist = msft.history(period="max")

# Display the first and last few rows of historical data
print("First few rows of historical data:")
print(hist.head())
print("Last few rows of historical data:")
print(hist.tail())

# Plotting historical data
fig = px.line(hist, x=hist.index, y=['Close', 'Open', 'High', 'Low'], title='Microsoft Stock Analysis')
fig.show()

# Show actions (dividends, splits, capital gains)
msft_actions = msft.actions
print("Actions:")
print(msft_actions)

# Get the number of outstanding shares
outstanding_shares = msft.info['sharesOutstanding']
print("Number of outstanding shares:", outstanding_shares)

# Show financials
# Income statement
income_stmt = msft.financials.loc['Income Statement']
print("Income statement:")
print(income_stmt)

# Quarterly income statement
quarterly_income_stmt = msft.financials.loc['Quarterly Income Statement']
print("Quarterly income statement:")
print(quarterly_income_stmt)

# Balance sheet
balance_sheet = msft.balance_sheet
print("Balance sheet:")
print(balance_sheet)

# Quarterly balance sheet
quarterly_balance_sheet = msft.quarterly_balance_sheet
print("Quarterly balance sheet:")
print(quarterly_balance_sheet)

# Cash flow statement
cashflow = msft.cashflow
print("Cash flow statement:")
print(cashflow)

# Quarterly cash flow statement
quarterly_cashflow = msft.quarterly_cashflow
print("Quarterly cash flow statement:")
print(quarterly_cashflow)

# Show holders
major_holders = msft.major_holders
print("Major holders:")
print(major_holders)

institutional_holders = msft.institutional_holders
print("Institutional holders:")
print(institutional_holders)

# Show recommendations
recommendations = msft.recommendations
print("Recommendations:")
print(recommendations)

# Upgrades and downgrades
upgrades_downgrades = msft.upgrades_downgrades
print("Upgrades and downgrades:")
print(upgrades_downgrades)

# Show future and historic earnings dates
earnings_dates = msft.earnings_dates
print("Earnings dates:")
print(earnings_dates)

# ISIN code - *experimental*
isin = msft.isin
print("ISIN code:", isin)

# Options expirations
options_expirations = msft.options
print("Options expirations:")
print(options_expirations)

# News
news = msft.news
print("News:")
print(news)

# Get option chain for specific expiration
opt = msft.option_chain('2024-05-01')
print("Option chain for specific expiration (2024-05-01):")
print(opt)
