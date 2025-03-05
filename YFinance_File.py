import yfinance as yf
import pandas as pd

def YahooData2returns(YahooData):
    # YahooData = data from Yahoo Finance
    # Steps:
    # Extract 'Adj Close' column
    # Extract values from 'Adj Close' column to transform to a simple array
    # Calculate and return the lagged returns

    pricevec = YahooData.values
    n = len(pricevec)
    ratiovec = pricevec[1:n]/pricevec[:n-1]
    returns = ratiovec - 1
    return returns


def get_stock_data(symbol):
    data = yf.download(symbol)
    print(data)
    prices = data['Close']
    return prices

# Example usage
prices = get_stock_data('GS')
print(type(prices))
pricevec = prices.values

# Compute the returns
n = len(pricevec)
ratiovec = pricevec[1:n] / pricevec[:n-1]

def get_returns(pricevec):
    n = len(pricevec)
    ratiovec = pricevec[1:n] / pricevec[:n-1]
    returns = ratiovec - 1  # assuming the return calculation is (price_t / price_t-1) - 1
    return returns

# Example of using get_returns
returns = get_returns(pricevec)
print(returns)

# Steps
# Download data
# Extract 'Adj Close' column
# Extract values from 'Adj Close' column to transform to a simple array
# Calculate and return the lagged returns
