
# Plenty of Financial & Quantitative Projects 
Click link below to see more detail.
## [FinQuant](https://github.com/technqvi/FinQuant)

## [AssetPriceFeeding](https://github.com/technqvi/FinQuant/tree/master/AssetPriceFeeding)
## [BinanceTranReport](https://github.com/technqvi/FinQuant/tree/master/BinanceTranReport)
## [AlertPriceInRange](https://github.com/technqvi/FinQuant/tree/master/AlertPriceInRange)
## [TradeSimulation](https://github.com/technqvi/FinQuant/tree/master/TradeSimulation)
## [FinMarketStreaming](https://github.com/technqvi/FinQuant/tree/master/FinMarketStreaming)
## [SET-API_TradeData](https://github.com/technqvi/FinQuant/tree/master/SET-API_TradeData)

# Tutorial :Python DataAnalytics For Fund Investment 
- [Github](https://github.com/technqvi/MyYoutube-Demo)
- [Youtube](https://www.youtube.com/playlist?list=PLIxgtZc_tZWOS9sHx9ModQ0ESX_nXkKM6)

## About FinQuant 
* This is the main repository contains several scripts regarding how to use ETF-Fund data like close price or even technical analysis indicators to perform data analytics statistically.
* We use  various approaches such as percentage of change, rank of the score, and outperforming average return and buy/sell simulation to calculate percent return of funds.

 ![overview](https://github.com/technqvi/FinQuant/assets/38780060/72e29a90-f674-4481-9265-1bdb8f94233a)

### [funds_buyhold_return_std__perf.ipynb](https://github.com/technqvi/FinQuant/blob/master/funds_buyhold_return_std__perf.ipynb)
* It is to invest in ETF Fund with Buy Hold Strategy.
* We buy on the first day of the starting month and apply the percentage of change and standard deviation function on the dataframe  whereby  performing the rolling calculation as the given period.
* Calculate score based on the 2 following criteria to select fund to invest on given period (Weekly,Monthly,Yearly) and total period(Start-To-End).
  * Percentage of return  and its rank (Higher total score , greater performance)
  * Standard deviation and its rank ( Higher total score , worse performance)
* Put all of them to quantify total final score. to find which fund to invest.

### [funds_buyhold_perf_analystics.ipynb](https://github.com/technqvi/FinQuant/blob/master/funds_buyhold_perf_analystics.ipynb)
* It is to invest in ETF Fund with Buy Hold Strategy.
* We buy on the first day of the starting month and apply the pct_change function on the dataframe  to find the percent return of close price month on month  whereby  performing the rolling  calculation  as the given period.
* Calculate score based on the 2 following criteria to select fund to invest on given period.
  * 1.Percentage of fund performance return 
  * 2.Rank ( calculated from Percentage of fund performance return)
* Put them all together (both conditions) to average score of these funds to find which fund to invest.


### [funds_buysell_perf_analystics.ipynb.ipynb](https://github.com/technqvi/FinQuant/blob/master/funds_buysell_perf_analystics.ipynb) 
* It is to invest in ETF Fund wih Buy&Sell on given TimeFrame.
* We buy on the first trading day of the month and sell all on the last trading day of the month and calculate the percentage of close price between both for each month.
* Calculate score based on the 3 following criteria to select fund to invest on given period.
  * 1.Percentage of fund performance return 
  * 2.Rank ( calculated from Percentage of fund performance return)
  * 3.Fund Outperperformed average as flag
* Put them all together (1-3 criteria) to average score of these funds to find which fund to invest.


## Additional Section

### [Demo-FinQuantLib](https://github.com/technqvi/FinQuant/tree/master/Demo-FinQuantLib)



#### [TopAssetROC.ipynb](https://github.com/technqvi/FinQuant/blob/master/TopAssetROC.ipynb)
 This file demonstrates how to get price data such as  fund ,crypto, stock  from [https://finance.yahoo.com/](https://finance.yahoo.com/) using  [yfinance](https://pypi.org/project/yfinance/) as given period to find fund's return  and take them to plot bar chart by Plotly library to show fund  performance .

#### [Any_To_AB.ipynb](https://github.com/technqvi/FinQuant/blob/master/Any_To_AB.ipynb)
Format csv file imported from [Efinance-Thai](www.efinancethai.com) and [Investing.com](https://www.investing.com/).  For investing.com , you can download historical data as the following steps
 - go to symbol   ex. https://www.investing.com/indices/nq-100-futures-chart
 - click General Tab => Historical Data   https://www.investing.com/indices/nq-100-futures-historical-data
 - download data
 This outcome is used for import to [AMibroker](https://www.amibroker.com/)

#### [CountTrendByLookingBackOnIndy.ipynb](https://github.com/technqvi/FinQuant/blob/master/CountTrendByLookingBackOnIndy.ipynb)
- Count consecutive bars of price or technical indicator to identify price movement direction such as up or down. 
- Use Histogram to show the distribution of how many continue bars of uptrend and downtrend fall into ranges.

#### [FindCorrelation.ipynb](https://github.com/technqvi/FinQuant/blob/master/FindCorrelation.ipynb)
How to find a correlation of a linear relationship between several funds to find which fund has high/low relation to making a decision on diversification of your investment.
#### [Asset-Indy-Analystics.ipynb](https://github.com/technqvi/FinQuant/blob/master/Asset-Indy-Analystics.ipynb) 
Find the distribution of  technical indicators of Asset  by using Histogram like MACD,RSI and summarize the set of data values to describe statistical methods like minimum, first quartile, median, third quartile, and maximum by Box-plot.

#### [Asset-RangeDist-PriceVol.ipynb](https://github.com/technqvi/FinQuant/blob/master/Asset-RangeDist-PriceVol.ipynb)
* Find percentage of Middle price  calculated by (High+Low)/2 of the last n periods  of trading range of given period such 10 days,25 days.
* [Donchian channel](https://en.wikipedia.org/wiki/Donchian_channel)

 #### [Find ROC Month](https://github.com/technqvi/FinQuant/tree/master/ROCMonth)
 find rate of change (percentage of return ) on monthly timeframe of list of particular years.
 #### [FeaturesMLAnalystics](https://github.com/technqvi/FinQuant/tree/master/FeaturesMLAnalystics)
 - explore data to create feature engineerin  with technical indicator of stock  to find relationship these features.
 - write AFL scriop on [Amibroker software](https://www.amibroker.com/) to generate trading signal logic with serveral  technical indicators  like RSI.'

### [my_fin_common_libs](https://github.com/technqvi/FinQuant/tree/master/my_fin_common_libs)
This folder contain common library used on  [TopAssetROC.ipynb](https://github.com/technqvi/FinQuant/blob/master/TopAssetROC.ipynb)  and  [AssetV2-Mini-ComparePerf.ipynb](https://github.com/technqvi/FinQuant/blob/master/AssetV2-Mini-ComparePerf.ipynb)

### [World-Focus-16tNow.csv](https://github.com/technqvi/FinQuant/blob/master/World-Focus-16tNow.csv)
Sample csv file as input.
