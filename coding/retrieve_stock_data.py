# filename: retrieve_stock_data.py
import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'NVDA'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2024-03-23', end='2024-04-23')
print(tickerDf)