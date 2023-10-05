# About
This is a project involving using Binance API to retrive trading transaction to do further analytics. There are 2 approaches to implement , Both are same things but run on differnt enviroment  as figure below
#### On Google Cloud with Analystics Services
1. Cloud Function get trading transaction from Binance using [python-biance](https://pypi.org/project/python-binance/)
2. Load transaction data into BigQuery.
3. Spark-Serverless get  trading transaction  from BigQuery to summarize daily buy/see and save result into another on BigQuery.
4. Generate report as excel file.

#### On Local Server with python script
1. Get trading transaction from Binance using [python-biance](https://pypi.org/project/python-binance/).
2. Save transaction data into SQLite.
3. Get  trading transaction  from SQLite to summarize daily buy/see and generate report as excel file.
![image](https://github.com/technqvi/BinanceTranReport/assets/38780060/fa11a1bd-c91e-4fc4-b2be-d918fc2332d5)

#### Prerequisite
*  create sqlite database and table as [schema link](https://github.com/technqvi/BinanceTranReport/blob/master/bigquery_sqlite_table_schema/sqlite%20table.txt)  as DB_BN_MyTrade.db
* Read how to do it in more detail on the first section as link above  [Binance API and Key Manage](https://github.com/technqvi/AssetPriceFeeding) 
* Register binacnace account and enalbe Binance API 
* Create .env file so that ww can store bn_key=??  and bn_secrete=??.
* Install  [python-dotenv](https://pypi.org/project/python-dotenv/) and [python-biance](https://pypi.org/project/python-binance/)

# Main Section
## [BN_MyTrade_Data.ipynb](https://github.com/technqvi/BinanceTranReport/blob/master/BN_MyTrade_Data.ipynb)
* List Crypto Trading Symbol  and Loop through each symbol to perform the the following steps
  * To get recent transaction from Binance, you need to get transacetion that timestamp is greater that  last transaction from database.  
  * Invoke  client.get_my_trades(symbol=symbol,startTime='') to get the most up-to-date transaction from Binance
  * Transform data align with hist_trade table schema
  * Append data into dataframe
 * Load dataframe to SQLite ( Bigquery as alternative target)
 
## [BN_MyTrade_Analystics.ipynb](https://github.com/technqvi/BinanceTranReport/blob/master/BN_MyTrade_Analystics.ipynb)
 * List transaction by given periond such as start=01-01-2023 and end=30-04-2023 from database.
 * Summarize analystics report as excel file as below.
   * Aggragate transcation to summarize buy and sell total transaction value.
   * Calculate Total Buy/Sell Profit/Lost
   * Simulate Sell On Buy transactiond (Buy and Sell on same symbol).
   * Test Simulate Sell with Same Qty of Buy At The Current Price.
## Binance Buy/Sell on Google Analystics
### [bn_buy_sell_summary_py_bigquery.ipynb](https://github.com/technqvi/BinanceTranReport/blob/master/bn_buy_sell_summary_py_bigquery.ipynb)
* It is used on  Cloud composer (Google Data Analystics Platform) to summarize trading transaction into table on Bigguery on daily basis.
* The steps performed include: 
  * Read data from BigQuery  by bigquery client. 
  * Use Pandas To perform data transformation and aggreagration.
  * Save data to BigQuery by bigquery client . 
 
### [bn_buy_sell_summary_pyspark_bigquery.py](https://github.com/technqvi/BinanceTranReport/blob/master/bn_buy_sell_summary_pyspark_bigquery.py)   
* It is the same output as [bn_buy_sell_summary_py_bigquery.ipynb](https://github.com/technqvi/BinanceTranReport/blob/master/bn_buy_sell_summary_py_bigquery.ipynb) but run job on on  Spark Serverless on DataProc instead.
* For Python-Dev who is familiar with pandas package,  spark >=3.2 gives you ability to use same code to run on SPark Enviroment , but you have to change on importing the package to execute code a bit 

change from
```
import pandas as pd
}
```  
to

```
import pyspark.pandas as pd
}
```  

* [Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/index.html) 
* The steps performed include: 
  * Retrieve data from BigQuery using spark.read.format('bigquery') .
  * Convert Spark-Dataframe to_Pandas-Dataframe by using pandas_on_spark() (spark >=3.2 :Make it more convenient for python-dev to migrate job to apache spark environment).
  * Use Pandas-Dataframe  perform data transformation and aggreagration instead.  
  * Convert it back to  Spark-Dataframe and  write data  to BigQuer using Spark-Dataframe.write.format("bigquery"). 
   
# Option Section
#### [BN-SQLite-BQ.ipynb](https://github.com/technqvi/BinanceTranReport/blob/master/BN-SQLite-BQ.ipynb)
Transfer Binance Transaction from SQLite to Bigquery.
#### [BN_ExcelToSQLite.ipynb](https://github.com/technqvi/BinanceTranReport/blob/master/BN_ExcelToSQLite.ipynb)
Transfer Binance Transaction exported from Binance Historical Trading  to SQLite.
#### [bigquery_sqlite_table_schema](https://github.com/technqvi/BinanceTranReport/tree/master/bigquery_sqlite_table_schema)
Define schema of all tables both SQLite and BigQuery

# Reference
### [SQLite](https://www.sqlite.org/index.html)
#### Tutorial
* [Binance Python API – A Step-by-Step Guide](https://algotrading101.com/learn/binance-python-api-guide/)
* [A Gentle Introduction to the Python Binance API](https://www.section.io/engineering-education/a-gentle-introduction-to-the-python-binance-api/)
#### Python Libary  [python-biance](https://pypi.org/project/python-binance/) | [python-dotenv](https://pypi.org/project/python-dotenv/) | [google-cloud-bigquery](https://pypi.org/project/google-cloud-bigquery/)  (option)

 
 
 
 