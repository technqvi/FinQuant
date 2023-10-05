#!/usr/bin/env python
# coding: utf-8

# In[8]:


from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import pyspark.pandas as ps
from datetime import datetime, timedelta,date


# In[9]:


spark = SparkSession.builder \
  .appName("BN-BuySell")\
  .enableHiveSupport()\
  .getOrCreate()
print(spark.conf.get('spark.jars'))

# spark = SparkSession.builder \
#   .appName('BN-BuySell')\
#   .config('spark.jars', 'gs://spark-lib/bigquery/spark-bigquery-latest.jar') \
#   .getOrCreate()


spark


# In[10]:


spark.conf.set("spark.sql.repl.eagerEval.enabled",True)
spark.conf.set('spark.sql.execution.arrow.pyspark.enabled', True)


# In[14]:


today=date.today()
#today=datetime(2022,9,7)
report_date=datetime(today.year,today.month,today.day)
created_date=datetime.now()
created_date=created_date.strftime("%Y-%m-%d %H:%M")
created_date=datetime.strptime(created_date, "%Y-%m-%d %H:%M")

print(f'BuySell as of {report_date} at {created_date}')


# In[15]:


date_from=datetime(2022,9,1)
date_to=report_date+timedelta(days=1)

date_str_from=date_from.strftime('%Y-%m-%d')
date_str_to=date_to.strftime('%Y-%m-%d')

print(f"Query Buy/Sell : {date_str_from} - {date_str_to}")


# In[16]:


x_filter=f"datetimeUTC>='{date_str_from}'and datetimeUTC<'{date_str_to}'"
print(x_filter)
trasnsDF = spark.read.format('bigquery')\
.option("table",'pongthorn.FinDW.bn_hist_trade') \
.option("filter",x_filter).load()

print(trasnsDF.printSchema())
print(trasnsDF.select('datetimeUTC','symbol_pair','type','price','qty','qty'))



# In[17]:


df_trans=trasnsDF.to_pandas_on_spark()
print(df_trans.info())
print(df_trans[['datetimeUTC','symbol_pair','type','price','qty','total']].head())


# # Find Summary Buy & Sell

# In[18]:


print("Agg transaction")
groupby_cols=['symbol','type']
agg_cols=['qty','total']
df_summary=df_trans.groupby(groupby_cols,as_index=False)[agg_cols].sum()
df_summary['avg_price']=df_summary['total']/df_summary['qty']

# df_summary['report_date']=report_date.strftime("%Y-%m-%d %H:%M:%S")
# df_summary['created_date']=created_date.strftime("%Y-%m-%d %H:%M:%S")
df_summary['report_date']=report_date
df_summary['created_date']=created_date

df_summary=df_summary.sort_values(by=['report_date','symbol','type'])

print(df_summary.info())


# In[19]:


decimals = ps.Series([5, 5, 4], index=['qty', 'total', 'avg_price'])
df_summary=df_summary.round(decimals)
print(df_summary)


# In[20]:


summaryDF=df_summary.to_spark()
# print(summaryDF.printSchema())
summaryDF


# # Add Summary to your GCS bucket on daily basis

# In[21]:


listSummaryDF = spark.read.format('bigquery').option("table",'pongthorn.FinDW.bn_bs_summary').load()
print(listSummaryDF.printSchema())
if listSummaryDF.rdd.isEmpty():
    print("no before add new transation.")


# In[22]:


#spark.conf.set('temporaryGcsBucket', "temp_bucket_gcs_to_bq_pongthsa")
# gcs_bucket = 'temp_bucket_spark_pongthorn'
summaryDF.write \
  .format("bigquery") \
  .option("writeMethod","direct") \
  .option("table","pongthorn.FinDW.bn_bs_summary") \
  .mode('append') \
  .save()

#  .option("temporaryGcsBucket", gcs_bucket) \


# In[ ]:




