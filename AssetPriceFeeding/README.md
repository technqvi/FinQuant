
# About
This repositoy involved in feeding price data from a variety of financial sources , such as Fund, Stock , Index and Crypto.
![image](https://github.com/technqvi/AssetPriceFeeding/assets/38780060/7275f960-4c72-4275-916b-e1091671a702)

## [cryptos_api_to_file.ipynb](https://github.com/technqvi/AssetPriceFeeding/blob/master/cryptos_api_to_file.ipynb) |  [cryptos_api_to_file.py](https://github.com/technqvi/AssetPriceFeeding/blob/master/cryptos_api_to_file.py)
* Retrive crypto price from Binance and Crytocompare by passing symbol stored in SQLite database as parameter in order to invoke API function.
* There are 2 cypto data provider sources  that enable you to get price data as belows.
  - Binance-API : [python-binance](https://python-binance.readthedocs.io/en/latest/) is used to get cryto price from Binance . This package is unofficial Python wrapper for [the Binance exchange REST API v3](https://binance-docs.github.io/apidocs/spot/en)
  - Cryptocompare-API : Get the current price of any cryptocurrency via [GET/POST Request Method](https://www.geeksforgeeks.org/get-post-requests-using-python/) to [Cryptocompare-API](https://min-api.cryptocompare.com/documentation)
* Enable API and Get Credential Ket for access to API.
  - [Enable Binance API](https://www.binance.com/en-ZA/support/faq/how-to-create-api-360002502072)
  - [Crypto Compare API Document](https://min-api.cryptocompare.com/documentation)
* Store API key(cryto compare) and key and secret(binance) on .env and use [dotenv](https://pypi.org/project/python-dotenv/) to retrieve them
.env file , it has to look like the below.
```
bn_key=xxxx
bn_secrete=yyyy
cryptocompare_key=zzzz
```


## [yfinance_to_file_autoAB.ipynb](https://github.com/technqvi/AssetPriceFeeding/blob/master/yfinance_to_file_autoAB.ipynb) | [yfinance_to_file_autoAB.py](https://github.com/technqvi/AssetPriceFeeding/blob/master/yfinance_to_file_autoAB.py)
* Pull any asset price data such as ETF-Fund,Index,Crypto,Currentcy,Bond from  [Finance Yahoo](https://finance.yahoo.com/) using [yfinance](https://github.com/ranaroussi/yfinance)
* List any desired symbol in CSV file so that it can be refered to each symbol for retrieving data from Finance Yahoo 
* Save data as csv and import it into [AmiBroker - Technical Analysis Software](https://www.amibroker.com/) automatically. However you don't have this software installed on your labtop, you skip this part.

## [yfinance_invespy-to_file.ipynb](https://github.com/technqvi/AssetPriceFeeding/blob/master/yfinance_invespy-to_file.ipynb)
* This file has been deprecated due to the fact that investpy is unable to get data from investing.com any longer due to something changed on investing.com API services.
## [my_fin_common_libs](https://github.com/technqvi/AssetPriceFeeding/tree/master/my_fin_common_libs)
It is responsible for importing data price from csv file  to Amibroker automatically.



