# About
This project involved the price range notification of stocks downloaded from Binance, Yahoo like S&P500, and ETH as given the price range definition. we can schedule the script to run in order to notify the current price range at the time periodically.

## Framwork and Tool
* Python >= 3.9 :  [yfinance](https://pypi.org/project/yfinance/ ) ,[python-binance ](https://pypi.org/project/python-binance/) ,[python-dotenv](https://pypi.org/project/python-dotenv/)
* [How to setup and enable BinanceAPI](https://github.com/technqvi/AssetPriceFeeding)
* [SQLite](https://www.sqlite.org/index.html) : alert_price_db.sqlite3 , there are 2 tables 1.symbol_price_info 2.notification_transaction
* [Line Notifcation](https://notify-bot.line.me/doc/en/)

## Script Section
The figure below to describe simply how to setup and configure stock name and range definition on the database.
<img width="763" alt="define-range" src="https://github.com/technqvi/AlertPriceInRange/assets/38780060/46cdc6d0-debf-4f83-8ff5-bb3d5d7925f6">

## [price_range_notification.ipynb)](https://github.com/technqvi/AlertPriceInRange/blob/master/price_range_notification.ipynb) | [price_range_notification.py](https://github.com/technqvi/AlertPriceInRange/blob/master/price_range_notification.py)
* Load symbol name and range list from database.
* Get price from datasource like Binanace, Finance.Yahoo.
* Find price level as defined range to current price and  compare current price to price of prev notification to caculate rate of chage as percent format.
* Save into database and send message via line notification.


### Database and Window Batch
* [alert_price_db.sqlite3](https://github.com/technqvi/AlertPriceInRange/blob/master/alert_price_db.sqlite3)
* [Batch_Binance_AlertPriceInRange.bat](https://github.com/technqvi/AlertPriceInRange/blob/master/Batch_Binance_AlertPriceInRange.bat) : Pull data from binance like ETH,BTC,MATIC to set price movement notification.
* [Batch_Yahoo_AlertPriceInRange.bat)](https://github.com/technqvi/AlertPriceInRange/blob/master/Batch_Yahoo_AlertPriceInRange.bat) : : Retrive data from [finance.yahoo.com](https://finance.yahoo.com/quote/sPY) like S&P500(SPY ETF) to set price movement notification.