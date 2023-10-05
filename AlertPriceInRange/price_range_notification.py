#!/usr/bin/env python
# coding: utf-8

# In[163]:


import sqlite3
import pandas as pd
import os
import datetime as datetime
import numpy as np
from dotenv import dotenv_values
from binance.client import Client
import requests
import random
import yfinance as yf
import sys 
import math


# In[164]:


is_auto=True
api_source='yahoo'
#api_source='bn'

no_last_items=1
no_set=5
x_now=datetime.datetime.now()


config_path=r'E:\AB_DB\Script_ImportData\.env'
data_base_file=r'E:\AB_DB\Script_ImportData\Database\alert_price_db.sqlite3'

# In[165]:


if is_auto==True:
    if len(sys.argv)==2:
       print(sys.argv[1] ) 
       api_source=sys.argv[1] 
        
       with open('readme.txt', 'w') as f:
        for i in range(len(sys.argv)):
         f.write(sys.argv[i]+"\n") 
    else:
        raise Exception("take api_source as param bn or yahoo")


#exit()


# In[ ]:





# In[166]:


buildtime = x_now.strftime('%d%b%y_%H%M')
print(buildtime)


# In[167]:



config_values= dotenv_values(dotenv_path=config_path)
api_key = config_values['bn_key']
api_secret =config_values['bn_secrete']
client=Client(api_key,api_secret)

line_token = config_values['line_token']


# In[168]:



print("Connect SQLite")
conn = sqlite3.connect(os.path.abspath(data_base_file))

sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))


# In[169]:


if api_source=='bn':
    sql_price_range="select * from symbol_price_info where is_active=1 and api_source='bn'"

elif api_source=='yahoo':
    sql_price_range="select * from symbol_price_info where is_active=1 and api_source='yahoo'"
    
df=pd.read_sql_query(sql_price_range, conn)
df['symbol_pair']=df.apply( lambda x: f"{x.symbol_x}{x.symbol_pair}",axis=1)

#sample_list=['ACWI','82823.HK','BMSCITH.BK','BMSCG.BK']
# df=df.query('symbol_x in @sample_list')

print(df)

#close conection from selecting fist
# conn.close()


# In[170]:


# get price from binace

# get price from yahoo
# https://aroussi.com/post/python-yahoo-finance
# https://github.com/ranaroussi/yfinance

current_price_dict={}
list_symbol=[]

if api_source=='bn':
    for index,item in df.iterrows():
        current_price =(client.get_symbol_ticker(symbol=item["symbol_pair"]))['price']
        # current_price=random.randint(1, 30)
        current_price_dict[item["symbol_key"]]= round( float(current_price),4)
        list_symbol.append(item["symbol_key"])
          
        
#auto_adjust = True
elif api_source=='yahoo':
    fund_symbols=df['symbol_x'].tolist()
    fund_keys=df['symbol_key'].tolist()
    
    symbol_str=' '.join(fund_symbols )
    print(symbol_str)
    list_current_price = yf.download( tickers = symbol_str,threads = True,
                                 group_by=True,period = "1d",prepost = True)
    list_fund= list(zip(fund_keys,fund_symbols))
    for x in list_fund:
     current_price_dict[x[0]]=round( list_current_price[x[1]]['Close'][0],2)
     list_symbol.append(x[0])

print(current_price_dict )  


# In[171]:


def get_last_record():
    conn = sqlite3.connect(os.path.abspath(data_base_file))

    df_all_last_update=pd.DataFrame()

    for item in list_symbol:
        sql=f"select * from notification_transaction where symbol_key='{item}' order by datetime desc limit 1"
        df_item=pd.read_sql_query(sql, conn)
        df_all_last_update=pd.concat([df_all_last_update,df_item])
        #print(df_item)
    return df_all_last_update


# In[172]:


df_all_prev=get_last_record()
df_all_prev


# In[173]:


print(list_symbol)


# In[174]:


dict_prev_item={}
for  symb in  list_symbol:
    df_temp=df_all_prev.query("symbol_key==@symb")
    #print(df_temp)
    str_prev_msg=None
    prev_price=None
    # print(df_temp)
    if  df_temp.empty==False:
      temp=df_temp.loc[0]
      str_prev_msg=f"{temp['idx_pos']}# {temp['msg']}"
      prev_price=  temp['price']

    dict_prev_item[symb]=(str_prev_msg,prev_price)
print(dict_prev_item)


# In[175]:


def find_range(item):
   symbol_key=item['symbol_key'] 

   p=current_price_dict[symbol_key]
   print(f'{symbol_key} : {p}') 

   priceList_str= item["price_range"].strip().split(",")
   priceList=[ float(x) for x in priceList_str]
   list.sort(priceList) 
   print(priceList)
     
   log_info={}

   log_info['datetime']=(x_now).strftime("%Y-%m-%d %H:%M:%S")
   log_info['symbol_key']=symbol_key   
   log_info['price']=p
   log_info['all_ranges']= item["price_range"]
   
   range_length=len(priceList)
   log_info['no_ranges']=range_length+1
   
   position=0;
   for index in range(0,range_length):   
     # print("iterate:",index)
     if (index==0) and (p<priceList[index]):
            position= 1
            log_info['msg']=f"{symbol_key}:{p} < {priceList[index]}"
            
     elif (index>0) and (index< range_length ) and ( p>=priceList[index-1] and p<=priceList[index] ):
            position=  index+1
            log_info['msg']= f"{priceList[index-1]} <= ({p}) >= {priceList[index] }"
          
     elif   (index==range_length-1) and (p>priceList[index])    :
            position= range_length+1
            log_info['msg']= f"{symbol_key}:{p} > {priceList[index]}"
   
   print( log_info['msg'])   
    
   # write prev log info         
   if  symbol_key in dict_prev_item:

        msg,prev_p=dict_prev_item[symbol_key]

        if msg is not None and prev_p is not None :
         log_info['prev_msg']=msg   
         log_info['prev_price']= prev_p
         log_info['prev_pct_chg']= round( (p-prev_p)/prev_p*100 ,1)
        else:
         log_info['prev_msg']=None   
         log_info['prev_price']=None   
         log_info['prev_pct_chg']=None
         
    
   log_info['idx_pos']=position 
   log_info['idx_pct']= round( log_info['idx_pos']/log_info['no_ranges']*100,1)  
                
   # else:
   #      raise Exception("There are someting wrong!!!!")
        
   print(log_info)
   print("===========================================================")
   return log_info 
   
df['transaction']=df.apply(find_range,axis=1)  


# In[176]:


print(df)


# In[177]:


list_trans=[]
for index,item in df.iterrows():
    list_trans.append(item['transaction'])
df_tran=pd.DataFrame(list_trans)

df_tran['idx_pos']=df_tran['idx_pos'].astype('int')


print(df_tran.info())
df_tran


# In[178]:


def insertMultipleItems(recordList):
    try:
        sqliteConnection = sqlite3.connect(os.path.abspath(data_base_file))
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """
        INSERT INTO notification_transaction
        (datetime, symbol_key,price,all_ranges,no_ranges,
         msg,prev_msg,prev_price,prev_pct_chg,idx_pos,idx_pct) 
         VALUES (?,?,?, ?, ?,?,?,?,?,?,?);
         """

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Add transaction successfully")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into product table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


recordsToInsert=list(df_tran.to_records(index=False))
insertMultipleItems(recordsToInsert)


# In[179]:


df_all_last_update=get_last_record()

#df_all_last_update=df_all_last_update[['datetime','symbol_key','price','prev_price','prev_pct_chg','msg','prev_msg','idx_pct','idx_pos','all_ranges']]
df_all_last_update=df_all_last_update[['datetime','symbol_key','price','prev_price','prev_pct_chg','msg','idx_pos','all_ranges']]
df_all_last_update.fillna("-",inplace=True)
df_all_last_update.info()
df_all_last_update


# In[180]:


#!/usr/local/bin/python3
import requests
url = 'https://notify-api.line.me/api/notify'
token = line_token
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


# In[181]:


no_split=math.ceil(len(df_all_last_update)/no_set)
print(no_split)
info_array = np.array_split(df_all_last_update,no_split)
for info in info_array:
    string_msg=info.to_string(index=False,header=True)
    string_msg='\n'+string_msg
    print(len(string_msg))
    r = requests.post(url, headers=headers, data = {'message':string_msg})
    print (r.text)
    print("===========================================") 


# In[ ]:





# In[ ]:





# In[ ]:




