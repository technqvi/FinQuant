#!/usr/bin/env python
# coding: utf-8

# In[2]:


from binance.client import Client
from dotenv import dotenv_values
from datetime import datetime
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os
import sqlite3
import requests


# In[11]:


is_py=True
is_new_entry=False
x_cryptocompare='y'

path_config=r'D:\AB_DB\Script_ImportData'
path_data=path_config+"\\Crypto_File"
db_path=path_config+"\\Database\\crypto_db.db"

today_now=datetime.now()
timeframe="4h" 

buildtime = datetime.now().strftime('%d%m%y_%H%M')

print(path_config)
print(path_data)
print(db_path)


# In[12]:


cols=["datetime","open","high","low","close","volume"]
cols_number=["open","high","low","close","volume"]
cols_last=["datetime","open","high","low","close","volume"]

cols_crypto_ohlc=["datetime","open","high","low","close",]
cols_crypto_vol=["datetime","volume"]


# In[13]:


config_values= dotenv_values(dotenv_path=f'{path_config}\\.env')
api_key = config_values['bn_key']
api_secret =config_values['bn_secrete']
client=Client(api_key,api_secret)



# In[14]:


cryptocompare_key=config_values['cryptocompare_key']
headers = {'Authorization': 'Bearer ' + cryptocompare_key}


# In[15]:


ok=False

if is_py:
    print("Enter start date as yyyy-mm-dd(2019-01-01)")
    start_param = input("Enter start : ")

    print("Enter end date as yyyy-mm-dd(2022-01-01) if today ,press enter")
    end_param = input("Enter end : ") or ''
    
    print("Load Cryptocompare y|n")
    x_cryptocompare = input("Enter: ") or 'y'

    start=start_param
    if end_param == '':
     end=today_now.strftime("%Y-%m-%d")
    else:
     end=end_param  


    try:
        start_dt=datetime.strptime(start, "%Y-%m-%d")
        end_dt=datetime.strptime(end,"%Y-%m-%d")
        if start_dt>=end_dt:
           raise Exception(f"Error : {start_dt} can't be greater or equal to {end_dt}")
    except Exception as ex:
        raise ex



    print(f"Do you want to retrive data from {start_dt} to {end_dt} ?")
    press_y=input(f"Press y=True and n=False : ") 
    if press_y.lower()=='y':
     ok=True
    else:
     exit()
else: 
    start='2022-08-10'
    end= today_now.strftime("%Y-%m-%d")
    
limit_days=(( datetime.strptime(end,"%Y-%m-%d") )- ( datetime.strptime(start, "%Y-%m-%d") )).days 
limit_days=limit_days+1
    
print(f"{start} - {end}={limit_days}")


# In[16]:


print("Connect SQLite")
conn = sqlite3.connect(os.path.abspath(db_path))


# In[18]:


if is_new_entry:

    sql="select * from crypto_meta_info where is_new = 1 and api_source='binance'"
    sql_cpx="select * from crypto_meta_info where  is_new=1  and api_source='cryptocompare'"
else:

    sql="select * from crypto_meta_info where  is_new=0 and is_active=1 and api_source='binance'"
    sql_cpx="select * from crypto_meta_info where  is_new=0 and is_active=1 and api_source='cryptocompare'"

sql_valid=False
try:
 print("Load Binance")
 
 print(sql)
 print(sql_cpx)
 
 dfCryptos_MetaData = pd.read_sql_query(sql, conn)
 dfCryptos_MetaData=dfCryptos_MetaData[['name','symbol','category','pair','api_source']]   
 print(dfCryptos_MetaData.info())
 print(dfCryptos_MetaData.head())   
    
    
 print("Load Cryptocompare")
 dfCompare_MetaData = pd.read_sql_query(sql_cpx, conn)  
 dfCompare_MetaData=dfCompare_MetaData[['name','symbol','category','pair','all_volume','api_source']]
 print(dfCompare_MetaData.info())
 print(dfCompare_MetaData.head())   


 sql_valid=True 

except Exception as ex:
 raise  ex




# # Binance API

# In[19]:


list_not_found=[]
# get data from Binance API
for index,item in  dfCryptos_MetaData.iterrows():
  try:  
    symbol=item['symbol']
    stablecoin=item['pair']
    name=item['name']
    product=f"{symbol}{stablecoin}"
    # check bn_symbols.txt
    print(f"{symbol} : {start} and {end}")
    df= pd.DataFrame(client.get_historical_klines(product,timeframe,start,end))
    
    df_ohlcv=df.iloc[:,:6]
    df_ohlcv.columns=cols

    df_ohlcv["datetime"]=pd.to_datetime(df_ohlcv["datetime"],unit="ms")
    df_ohlcv[cols_number]=df_ohlcv[cols_number].astype("float")
    df_ohlcv=df_ohlcv[cols_last]
    
    print(df_ohlcv.head())
    print(df_ohlcv.tail())
    
    file_data=f'{symbol}.csv'
    path_file=os.path.join(path_data,file_data)
    df_ohlcv.to_csv(path_file, header=True, index=False)
    #file_data=f'{symbol}.txt'
    #df_ohlcv.to_csv(path_file, header=True, index=False, sep=',', mode='a')
   

    
  except Exception as ex:
    print(f'{symbol}: {ex}')
    list_not_found.append(f'{symbol} - {name}')
    
print('list not found symbol')
for item in list_not_found:
 print(item)


# # Cryptocompare API

# In[56]:


if x_cryptocompare=='y':

    x_not_found=[]
    for index,item in  dfCompare_MetaData.iterrows():

     try:  
        name=item['name']
        # name='BTC'

        symbol=item['symbol']

        pair=item['pair']
        required_all_vols=item['all_volume']

        url = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym={name}&tsym={pair}&limit={limit_days}"
        print(url)
        json_ohlc=requests.get(url, headers=headers).json()

        df_ohlc=pd.DataFrame(json_ohlc['Data']['Data'])
        df_ohlc=df_ohlc.query('close>0')
        df_ohlc['datetime'] = [datetime.fromtimestamp(d) for d in df_ohlc.time]
        if required_all_vols==1:

            df_ohlc=df_ohlc[cols_crypto_ohlc]
            print("Require all volume")
            url_vol=f"https://min-api.cryptocompare.com/data/symbol/histoday?fsym={name}&tsym={pair}&limit={limit_days}"
            print(url_vol)
            json_vol=requests.get(url_vol, headers=headers).json()   

            df_vol=pd.DataFrame(json_vol['Data'])
            df_vol['datetime'] = [datetime.fromtimestamp(d) for d in df_vol.time]
            df_vol=df_vol.drop(columns=['time'])
            df_vol=df_vol[['datetime','total_volume_total']]
            df_vol=df_vol.rename(columns={'total_volume_total':'volume'})

            print(df_vol.info())
            print(df_vol.head())

            df_cypto_compare=pd.concat([df_ohlc,df_vol['volume']],axis=1)

        elif required_all_vols==0:

          df_ohlc=df_ohlc.rename(columns={'volumeto':'volume'})
          df_cypto_compare=df_ohlc[cols_crypto_ohlc+['volume']]

        print(df_cypto_compare.info())
        print(df_cypto_compare.head())


        xfile_data=f'{symbol}.csv'
        xpath_file=os.path.join(path_data,xfile_data)
        df_cypto_compare.to_csv(xpath_file, header=True, index=False)

     except Exception as ex:
          print(f'{symbol}: {ex}')
          x_not_found.append(f'{symbol} - {name}')



# In[ ]:




