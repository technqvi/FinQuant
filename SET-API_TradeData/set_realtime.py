#!/usr/bin/env python
# coding: utf-8

# In[6]:


from settrade_v2 import Investor
from settrade_v2.errors import SettradeError
import configparser
import time
# https://developer.settrade.com/open-api/api-reference/reference/sdkv2/python/market-mqtt-realtime-data/4_subscribeCandlestick


# In[3]:


configParser = configparser.RawConfigParser()   
configFilePath = 'user-info.properties'
configParser.read(configFilePath)

app_id = configParser.get('STT-OPENAPI-AUTH', 'app-id-caf')
app_secret = configParser.get('STT-OPENAPI-AUTH', 'app-secret-caf')
app_code = configParser.get('STT-OPENAPI-AUTH', 'app-code-caf')
broker_id = configParser.get('STT-OPENAPI-AUTH', 'broker-id-caf')
is_auto_queue = False

# print(app_id)
# print(app_secret)
# print(app_code)
# print(broker_id)
# In[ ]:


investor = Investor(
                app_id=app_id,                                 
                app_secret=app_secret, 
                broker_id=broker_id,
                app_code=app_code,
                is_auto_queue = True)

realtime = investor.RealtimeDataConnection()

# Callback function for subscribing AOT's bid offer
def get_realtime_data(message):
    
    print(message)
    print("================================================================================")

# This is subscriber object
# subscriber = realtime.subscribe_price_info("SET50", on_message = my_message)
subscriber = realtime.subscribe_candlestick("S50Z23", "60m", on_message = get_realtime_data)
subscriber.start() 

# run main thread forever
while True:
    time.sleep(1)

