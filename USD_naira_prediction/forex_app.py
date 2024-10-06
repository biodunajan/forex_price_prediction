# FOREX(USD/Naira) Price Prediction Using LSTM Model

# import the necessary libraries and dependencies
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
from pandas import set_option
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import streamlit as st

# create a date range
start = '2002-01-01'
end = dt.datetime.now()

# retrieve market data of current ticker symbol
print('This is the table with HLOC, Volume, Adj Close prices')
data = yf.download('USDNGN=X', start=start, end=end)
set_option("display.width", 100)

df = pd.DataFrame(data)
target_variable = df['Adj Close']

# converting data to a pandas dataframe
df_forex = pd.DataFrame(target_variable)

# visualizing the USD-NGN Adj close-price
fig, axs = plt.subplots(1,1,figsize=(10,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1}, constrained_layout=True)
df_forex.plot()
plt.tight_layout()
plt.title('USD/NGN FOREX from 2004 to Date(18 Years)', fontsize=5)
plt.show()

# Data understanding and exploration using visualization technique
# Moving average to smooth out short term fluctuation and gain insights into the long-term trends

# obtaining a short-term and long-term moving/rolling average for buy/sell trading strategies
ma_months = [60, 90, 120, 180]

for ma in ma_months:
    column_name = f"MA for {ma} days"
    df_forex_2 = df_forex
    df_forex_2[column_name] = df_forex_2['Adj Close'].rolling(ma).mean()
    print(df_forex_2.tail(n=2))


# visualizing all 4 moving averages for USD-NGN pair closing price
plt.figure(figsize=(16,8))

plt.plot(df_forex['Adj Close'], label='Closing Price')
plt.plot(df_forex['MA for 60 days'], label='60-Day Moving Average')
plt.plot(df_forex['MA for 90 days'], label='90-Day Moving Average')
plt.plot(df_forex['MA for 120 days'], label='120-Day Moving Average')
plt.plot(df_forex['MA for 180 days'], label='180-Day Moving Average')
plt.title('USD-NGN Pair Closing Price and Moving Averages: 2004 to Date', fontsize=12)
plt.xlabel('Time', fontsize=5)
plt.ylabel('Price', fontsize=5)
plt.legend(loc=2, fontsize=5)

plt.tight_layout()
plt.show()
