#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import pandas as pd
import sqlite3
import os
import calendar
from datetime import datetime
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# In[41]:


# data_file=r"D:\PythonDev\MyQuantFinProject\Data\Tech-2Q17-Now.csv"
# mode='offline'

# from_month_str='2017-04-01'
# to_month_str='2022-12-31'


# In[42]:


def load_data(mode,from_month_str,to_month_str,data_file=None):


    # In[43]:


    # def load_offline_data():
    if os.path.exists(data_file):
      print(data_file)
    else:
      raise Exception(f"Not found {data_file}")  

    print("Load Price Data")

    df = pd.read_csv(data_file,index_col='Date/Time',parse_dates=['Date/Time'],dayfirst=True)
    df.index.set_names('date',inplace=True)
    df=df.rename(columns={'Ticker':'symbol','close':'price'})

    df=df[['symbol','price']]

    list_fund_name=df['symbol'].unique().tolist()  

    print(df.head())
    print(df.tail())

    #Check first idex >=from_str and last date=to_str 


    # In[44]:


    # def load_online_data():
    #https://github.com/ranaroussi/yfinance
    # data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")
    # fund_symbols=df['symbol_x'].tolist()
    # fund_keys=df['symbol_key'].tolist()

    # symbol_str=' '.join(fund_symbols )
    # print(symbol_str)
    # list_current_price = yf.download( tickers = symbol_str,threads = True,
    #                              group_by=True,period = "1d",prepost = True)
    # list_fund= list(zip(fund_keys,fund_symbols))
    # for x in list_fund:
    #  current_price_dict[x[0]]=round( list_current_price[x[1]]['Close'][0],2)
    #  list_symbol.append(x[0])


    # In[45]:


    print("Seperate dataframe  by symbol ")
    dictPriceOfFund={}
    unavaiable_funds=[]

    print(list_fund_name)
    for name in list_fund_name:

      fund_df=df.query('symbol==@name')
      fund_df=fund_df[['price']]
      fund_df=fund_df.loc[from_month_str:to_month_str,:]  
      fund_df.sort_index(inplace=True)  
      if len(fund_df)  >0:
          dictPriceOfFund[name]=fund_df
          print(f"============================={name}=============================")  
          print(fund_df.head(3))   
          print(fund_df.tail(3))  
      else:

          unavaiable_funds.append(name)

    if len(unavaiable_funds)>0:
      raise Exception(f"There are some funds are not data {unavaiable_funds}")



    # In[46]:


    return dictPriceOfFund


    # In[ ]:




