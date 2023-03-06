
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import datetime
import pandas as pd

ticker = 'SPY'
period1 = int(time.mktime(datetime.datetime(2020, 12, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2023, 3, 3, 23, 59).timetuple()))
interval = '1d'

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'


df = pd.read_csv(query_string)
print(df)