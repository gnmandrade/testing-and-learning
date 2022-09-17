#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:36:34 2022

Sample code for using Yahoo Finance.
Based on the tutorial in the page below:
https://towardsdatascience.com/python-how-to-get-live-market-data-less-than-0-1-second-lag-c85ee280ed93

@author: gandrade
"""

# Data visualization
import plotly.graph_objs as go
import plotly.io as pio

#pio.renderers.default = "browser"
pio.renderers.default = "svg"

# Import the Yahoo Finance API
import yfinance as yf


# Create object to study one stock
ticker = yf.Ticker("MSFT")
ticker.info

ticker.history(period='max')


# Download data for stocks
data = yf.download(tickers='UBER', period = '1d', interval = '1m', start='2022-04-13', end='2022-04-14')
print(data)


# Declare figure to plot
fig = go.Figure()

# Candelstick plot
fig.add_trace(go.Candlestick(x=data.index,
              open = data['Open'],
              high = data['High'],
              low = data['Low'],
              close = data['Close'],
              name = 'Market Data'))

# Add Titles
fig.update_layout(title = 'Live share price evolution',
                  yaxis_title = 'Stock Price (USD per share)')


# X-axes
fig.update_xaxes(
    rangeslider_visible = True,
    rangeselector = dict(
        buttons=list([
            dict(count=15, label='15m', step='minute', stepmode="backward"),
            dict(count=45, label='45m', step='minute', stepmode='backward'),
            dict(count=1, label='HTD', step='hour', stepmode='todate'),
            dict(count=3, label='3h', step='hour', stepmode='backward'),
            dict(step='all')
        ])
    )
)

# Show
fig.show()


# Download several tickers
tickers_list = ['MSFT','UBER']

df = yf.download(tickers = tickers_list, group_by = 'Ticker', period = '2d')
print(df)
df2 = df.stack(level=0).rename_axis(['Date','Ticker']).reset_index(level=1)
print(df2)

# Reading from the multindex dataframe
open_msft = df['MSFT'].loc[:,'Open']
print(open_msft)
df2.columns