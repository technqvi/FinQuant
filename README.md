# About
This repository contains several scripts involving analyzing fund performance like percentage of change  , rank of score that we will use to consider the investment strategy.
![image](https://github.com/technqvi/FinQuant/assets/38780060/f5431981-4ba6-4747-b860-fda733a8daa7)

# Tutorial :Python DataAnalytics For Fund Investment 
- [Github](https://github.com/technqvi/MyYoutube-Demo)
- [Youtube](https://www.youtube.com/playlist?list=PLIxgtZc_tZWOS9sHx9ModQ0ESX_nXkKM6)

## How to runt file for analytics
* Check library imported on the first cell of each jupyter lab file  on python or anaconda enviroment
Run each cell 
* Some files need csv file to run , you can  use sample file attached on this project to test run

# Main Section

## [World-Focus-16tNow.csv](https://github.com/technqvi/FinQuant/blob/master/World-Focus-16tNow.csv)
To run any file in this project to get result , we can use a sample csv file.

## [TopAssetROC.ipynb](https://github.com/technqvi/FinQuant/blob/master/TopAssetROC.ipynb)
 This file demonstrates how to get price data such as  fund ,crypto, stock  from [https://finance.yahoo.com/](https://finance.yahoo.com/) using  [yfinance](https://pypi.org/project/yfinance/) as given period to find fund's return  and take them to plot bar chart by Plotly library to show fund  performance .

## [AssetV2-Mini-ComparePerf.ipynb](https://github.com/technqvi/FinQuant/blob/master/AssetV2-Mini-ComparePerf.ipynb) (New Version) | [AssetV1-Full-ComparePerf.ipynb](https://github.com/technqvi/FinQuant/blob/master/AssetV1-Full-ComparePerf.ipynb") (Old verion)
This file shows you how to compare the percentage of fund's return and take it to calculate rank to score the fund on particular period.

## [TradeSimulation](https://github.com/technqvi/FinQuant/tree/master/TradeSimulation)
Simulate buy/sell as spefic period to find percentage ofClick link detail

## [my_fin_common_libs](https://github.com/technqvi/FinQuant/tree/master/my_fin_common_libs)
This folder contain common library used on  [TopAssetROC.ipynb](https://github.com/technqvi/FinQuant/blob/master/TopAssetROC.ipynb)  and  [AssetV2-Mini-ComparePerf.ipynb](https://github.com/technqvi/FinQuant/blob/master/AssetV2-Mini-ComparePerf.ipynb)

## [CountTrendByLookingBackOnIndy.ipynb](https://github.com/technqvi/FinQuant/blob/master/CountTrendByLookingBackOnIndy.ipynb)
- Count consecutive bars of price or technical indicator to identify price movement direction such as up or down. 
- Use Histogram to show the distribution of how many continue bars of uptrend and downtrend fall into ranges.

## [FindCorrelation.ipynb](https://github.com/technqvi/FinQuant/blob/master/FindCorrelation.ipynb)
How to find a correlation of a linear relationship between several funds to find which fund has high/low relation to making a decision on diversification of your investment.
## [Asset-Indy-Analystics.ipynb](https://github.com/technqvi/FinQuant/blob/master/Asset-Indy-Analystics.ipynb) 
Find the distribution of  technical indicators of Asset  by using Histogram like MACD,RSI and summarize the set of data values to describe statistical methods like minimum, first quartile, median, third quartile, and maximum by Box-plot.

## [Asset-RangeDist-PriceVol.ipynb](https://github.com/technqvi/FinQuant/blob/master/Asset-RangeDist-PriceVol.ipynb)
Find percentage of High, Low , Middle price to  trading range of given period such 10 days,25 days.

## [Any_To_AB.ipynb](https://github.com/technqvi/FinQuant/blob/master/Any_To_AB.ipynb)
Format csv file imported from [Efinance-Thai](www.efinancethai.com) and [Investing.com](https://www.investing.com/).  For investing.com , you can download historical data as the following steps
 - go to symbol   ex. https://www.investing.com/indices/nq-100-futures-chart
 - click General Tab => Historical Data   https://www.investing.com/indices/nq-100-futures-historical-data
 - download data
 This outcome is used for import to [AMibroker](https://www.amibroker.com/)

 # Additional Section
 
 ### [Find ROC Month](https://github.com/technqvi/FinQuant/tree/master/ROCMonth)
 find rate of change (percentage of return ) on monthly timeframe of list of particular years.
 ### [FeaturesMLAnalystics](https://github.com/technqvi/FinQuant/tree/master/FeaturesMLAnalystics)
 - explore data to create feature engineerin  with technical indicator of stock  to find relationship these features.
 - write AFL scriop on [Amibroker software](https://www.amibroker.com/) to generate trading signal logic with serveral  technical indicators  like RSI.'
###  [TA-Ind](https://github.com/technqvi/FinQuant/tree/master/TA-Indy)
create technical analysis indicator on pandas dataframe like Moving Average, EMA,MACD/Signal/RIS using [TA](https://technical-analysis-library-in-python.readthedocs.io/en/latest/)  powerd by  [GitHub Bukosabino](https://github.com/bukosabino/ta)

### [PythonToAB](https://github.com/technqvi/FinQuant/tree/master/PythonToAB)
Use python to get data from Amibroker to do something.

### [fin_date](https://github.com/technqvi/FinQuant/tree/master/fin_data)
There are several csv files used as inpurt to run jupyter file for  analytics report.
 
