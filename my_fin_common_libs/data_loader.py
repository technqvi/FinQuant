#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
import yfinance as yf


# In[2]:


from_month_str='2022-12-01'
to_month_str='2022-12-08'

data_file=r"D:\PythonDev\MyQuantFinProject\Data\Tech-2Q17-Now.csv"

list_analystics_cols=['symbol','price']


# In[7]:


def load_online_data(from_month_str,to_month_str,data_list):
    list_not_found=[]
    list_yahoo_cols=['Close']
    df=pd.DataFrame(columns=list_analystics_cols)
    print(df)
    for ticker in data_list:
     try:
        dfx = yf.download(ticker, start=from_month_str, end=to_month_str)
        if (dfx.empty==False) or (dfx is not None):

            dfx=dfx[list_yahoo_cols]  # remove unwanted columns  as dedire requirement
            dfx.insert(0, "symbol", ticker, True)
            dfx.columns=list_analystics_cols #rename column  list cols lenght must match excactly original columns lenght 
            print(dfx.info())

            df=pd.concat([df,dfx],ignore_index=False )
            df.index.set_names('date',inplace=True)

            print(dfx.tail())
        else:
            print(f"{ticker} No data found for this date range, symbol may be delisted")
            list_not_found.append(ticker) 


     except Exception as ex:
          print(str(ex))
          list_not_found.append(ticker)  

    return df


# data_list=['AAXJ','3010.HK']
# df=  load_online_data(from_month_str,to_month_str,data_list)
# print(df)


# In[29]:


def load_offline_data(from_month_str,to_month_str,data_file=None):

    list_fund_name=[]

    print("Load Price Data")

    df = pd.read_csv(data_file,index_col='Date/Time',parse_dates=['Date/Time'],dayfirst=True)
    df.index.set_names('date',inplace=True)
    df=df.rename(columns={'Ticker':list_analystics_cols[0],'close':list_analystics_cols[1]})
    
    df=df.loc[from_month_str:to_month_str,:]

    df=df[list_analystics_cols]

    list_fund_name=df['symbol'].unique().tolist()  

    print(df.head(3))
    print(df.tail(3))
    return df,list_fund_name   



# In[30]:





def group_data_by_symbol(from_month_str,to_month_str,df,list_fund_name):
    print("Seperate dataframe  by symbol as dictionary")
    dictPriceOfFund={}
    unavaiable_funds=[]
    
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
    
    return dictPriceOfFund
   


# df,list_fund_name=load_offline_data(from_month_str,to_month_str,df,list_fund_name)
# dictPriceOfFund,list_fund_name=load_data_groupby_symbol ('offline',from_month_str,to_month_str,df,list_fund_name)

# df,list_fund_name=load_offline_data(from_month_str,to_month_str,data_file)


# In[ ]:




