#!/usr/bin/env python
# coding: utf-8

# In[161]:


import pandas as pd
import numpy as np
from datetime import datetime,timedelta


# In[162]:


# from_month_str='2021-01-01'
# to_month_str='2022-12-31'
# feq ='Q'  # support month,quater,year


# In[163]:


def build_asset_timeseries(from_month_str,to_month_str,feq ):


# In[164]:


    period_index=pd.date_range(start=from_month_str,end=to_month_str, freq=feq)
    print(period_index)


    # In[165]:


    fundPerfByPeriod_df=pd.DataFrame(index=period_index,columns=['Start_Date'])
    fundPerfByPeriod_df.reset_index(drop=False,inplace=True)
    fundPerfByPeriod_df.columns=['End_Date','Start_Date']
    fundPerfByPeriod_df=fundPerfByPeriod_df[['Start_Date','End_Date']]


    # In[166]:


    for index,row in fundPerfByPeriod_df.iterrows():
        if index==0:
           fundPerfByPeriod_df.iloc[0,0]=datetime.strptime(from_month_str,'%Y-%m-%d')
        else:
            prev_end_date= fundPerfByPeriod_df.iloc[index-1,1]
            start_date=prev_end_date + timedelta(days = 1)
            fundPerfByPeriod_df.iloc[index,0]=start_date    
    fundPerfByPeriod_df['Start_Date']=pd.to_datetime(fundPerfByPeriod_df['Start_Date'],format='%Y-%m-%d %H:%M:%S')
    fundPerfByPeriod_df["NoMonth"]=((fundPerfByPeriod_df["End_Date"]-fundPerfByPeriod_df["Start_Date"])/np.timedelta64(1, 'M')).round(0)
    fundPerfByPeriod_df["NoMonth"]=fundPerfByPeriod_df["NoMonth"].astype('int')
    fundPerfByPeriod_df['Period']= fundPerfByPeriod_df.apply( lambda item:f"{item['Start_Date'].strftime('%b')}{item['Start_Date'].strftime('%y')}_{item['End_Date'].strftime('%b')}{item['End_Date'].strftime('%y')}"  ,axis=1  )
    fundPerfByPeriod_df.info()
    print(fundPerfByPeriod_df)


    # In[167]:


    return fundPerfByPeriod_df


# In[ ]:




