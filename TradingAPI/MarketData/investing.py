#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:36:34 2022

Sample code for using the investing.com API.

@author: gandrade
"""

# Import Libraries
import numpy as np
import pandas as pd

# Data visualization
import plotly.graph_objs as go
import plotly.io as pio

pio.renderers.default = "browser"
#pio.renderers.default = "svg"


#######################
## investing.com
#######################

import investpy as ipy

ipy.search_quotes('MSFT')

df = ipy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')

search_result = ipy.search_quotes(text='apple', products=['stocks'],
                                       countries=['united states'], n_results=1)
print(search_result)

recent_data = search_result.retrieve_recent_data()
historical_data = search_result.retrieve_historical_data(from_date='01/01/2019', to_date='01/01/2020')
information = search_result.retrieve_information()
default_currency = search_result.retrieve_currency()
technical_indicators = search_result.retrieve_technical_indicators(interval='daily')

search_result = ipy.search_quotes(text='VOO', n_results=1)
print(search_result)

recent_data = search_result.retrieve_recent_data()
historical_data = search_result.retrieve_historical_data(from_date='01/01/2019', to_date='01/01/2020')
information = search_result.retrieve_information()
default_currency = search_result.retrieve_currency()
technical_indicators = search_result.retrieve_technical_indicators(interval='daily')