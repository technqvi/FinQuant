#!/usr/bin/env python
# coding: utf-8

# In[9]:


import yfinance as yf
import investpy
import matplotlib.pyplot as plt

from datetime import datetime
import pandas as pd

import numpy as np

import os
import glob

from my_fin_common_libs import ABFromCSV

#https://github.com/ranaroussi/yfinance
# https://aroussi.com/post/python-yahoo-finance
# https://github.com/ranaroussi/yfinance


# Eexclude  'Name' column


# In[16]:


is_py=True
auto_ab=True

is_new=False


start_param="2023-01-01"
end_param=end= datetime.now().strftime("%Y-%m-%d")


if is_new:
 sheet_name='NewYahoo'
else:
 sheet_name='Yahoo'   
   
print(f"Mode={is_new} will get data from {sheet_name}")


# In[17]:


# yfinanace for world fund
list_cols=['Ticker','Date','Open','High','Low','Close','Volume']
list_cols_number=['Open','High','Low','Close','Volume']

root_path=r'D:\AB_DB\Script_ImportData'

data_path=os.path.join(root_path,'Fund_File')


metadata_file=os.path.join(data_path,"List_Fund_Import.xlsx")
output_path=os.path.join(data_path,"AB_Fund_World.csv")


xPathDict={}
xPathDict['db_path']=r"D:\AB_DB\AB_Fund_World"
xPathDict['ab_format_path']=r"D:\AB_DB\Script_ImportData\AB-Wizard.format"

xPathDict['data_path']=os.path.join(data_path,'AB_*.csv')




# # Veryfy file&folder

# In[18]:


pathList=[metadata_file,xPathDict['db_path'],xPathDict['ab_format_path']]
notFoud_pathList=[ path for path in pathList  if os.path.exists(path)==False  ]
if len(notFoud_pathList)>0:
    raise Exception(notFoud_pathList)
else:
    print(f"{pathList} are existing")
    
if len(glob.glob(xPathDict['data_path']))==0:
   raise Exception(f"Not found any AB_*.csv in {data_path}")
else:
    print(f"There is one AB_*.csv in {data_path}")


# In[19]:


if is_py:
    print("Enter start date as yyyy.mm.dd(2019-01-01)")
    start_param = input("Enter start : ")

    print("Enter end date as yyyy.mm.dd(2022-01-01) if today ,press enter")
    end_param = input("Enter end : ") or ''

    if start_param!='':
      start=start_param
    
    if end_param == '':
     end_param=datetime.now().strftime("%Y-%m-%d")
    

print(start_param)
print(end_param)
    


# # yfinance

# In[20]:


if True:

    print("################################Start Download from Yahoo========================================")

    df_ticker=pd.read_excel(metadata_file,sheet_name=sheet_name)
    print("World Investing")
    df_ticker =df_ticker.replace(np.nan, '', regex=True)
    print(df_ticker)

    list_not_found=[]

    df=pd.DataFrame(columns=list_cols)

    for index,item in df_ticker.iterrows():

       try:

        ticker=item['Ticker']
        print(ticker)

        dfx = yf.download(ticker, start=start_param, end=end_param)
        if (dfx.empty==False) or (dfx is not None):
            dfx['Ticker'] = ticker
            dfx=dfx.reset_index()
            dfx=dfx[list_cols]
            df=pd.concat([df,dfx])
            print(dfx.tail())
        else:
            print(f"{ticker} No data found for this date range, symbol may be delisted")
            list_not_found.append(ticker) 


       except Exception as ex:
          print(str(ex))
          list_not_found.append(ticker)  

    # df=df.rename(columns={'Adj Close':'Close'})

    df[list_cols_number]=df[list_cols_number].round(2)
    print("Save file as csv.")

    df.to_csv(output_path,index=False)
    print()

    print("################################End Download from Yahoo========================================")

    print("World fund : Not found symbol")
    print(list_not_found)


# # Export to AB automatically

# In[8]:


if auto_ab:
    isSussessful=ABFromCSV.import_files_to_Amibroker(xPathDict)
    print(isSussessful)
    


# In[ ]:




