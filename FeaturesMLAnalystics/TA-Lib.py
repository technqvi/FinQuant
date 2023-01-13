import pandas as pd
from ta.utils import dropna
import ta.trend as ta_trend
import ta.momentum as ta_mmt
import ta.others as ta_other
import ta 

df=pd.read_csv('data/SPY-TALib-AB.csv',parse_dates=['Date/Time'],
                         index_col='Date/Time',dayfirst=True)
df.info()


ab_indy='RSI15'
ta_indy=f'{ab_indy}-TA'
df=df[['Close',ab_indy]]

# df[ta_indy]=ta_trend.ema_indicator(close=df['Close'],window=10,fillna=True).round(2)
# df[ta_indy]=ta_trend.macd(close=df['Close'], window_slow=20, window_fast=10, fillna=True).round(2)
df[ta_indy]=ta_mmt.rsi(close=df['Close'],window=15,fillna=15).round(2)
#df[ta_indy]=ta.volatility.donchian_channel_mband()
df['diff']=df[ab_indy]-df[ta_indy]

df.to_csv('AB-TA.csv')