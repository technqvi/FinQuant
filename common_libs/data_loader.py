#!/usr/bin/env python
# coding: utf-8

# In[18]:


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


# In[19]:


# data_file=r"D:\PythonDev\MyQuantFinProject\Data\Tech-2Q17-Now.csv"
# mode='offline'

# from_month_str='2017-04-01'
# to_month_str='2022-12-31'


# In[29]:


def load_offline_data(from_month_str,to_month_str,data_file=None):

    list_fund_name=[]

    print("Load Price Data")

    df = pd.read_csv(data_file,index_col='Date/Time',parse_dates=['Date/Time'],dayfirst=True)
    df.index.set_names('date',inplace=True)
    df=df.rename(columns={'Ticker':'symbol','close':'price'})
    
    df=df.loc[from_month_str:to_month_str,:]

    df=df[['symbol','price']]

    list_fund_name=df['symbol'].unique().tolist()  

    print(df.head(3))
    print(df.tail(3))
    return df,list_fund_name   



# In[30]:


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


# In[31]:


def load_data_groupby_symbol(mode,from_month_str,to_month_str,data_file=None):
    print("Seperate dataframe  by symbol ")
    dictPriceOfFund={}
    unavaiable_funds=[]
    
    df,list_fund_name=load_offline_data(from_month_str,to_month_str,data_file)
    
    print(f'List Fund : {list_fund_name}')
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
    
    return dictPriceOfFund,list_fund_name
   


# In[33]:


# dictPriceOfFund,list_fund_name=load_data_groupby_symbol ('offline',from_month_str,to_month_str,data_file)

# df,list_fund_name=load_offline_data(from_month_str,to_month_str,data_file)


# In[ ]:




