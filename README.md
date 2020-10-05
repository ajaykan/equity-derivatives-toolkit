# Theta Strategy

This repo contains tools I designed/use to sell cash-secured puts (CSP). These tools use probability to optimize your likelihood of profit. Documentation will be updated as needed.	

`classes.py`: user defined objects	
  - `Position`: user position in one stock	
  - `Option`: stock option with vaalid expiry in future	
  - `Portfolio`: collection of positions and options	
  
  
Lagging Indicators:
 - exponential/moving averages
 - trading ranges
 - moving average convergence divergence (MACD)
 - relative strength index (RSI)
 - support levels

`short_put.py`: allows user to find optimal entry to sell CSP, uses specific statistics

  - Moving Averages (MA):
    - Looks at typical short put days til expiration (DTE): 15-45 days. Calculates moving average of 15, 45, (and 200 days). Then, recalculate these variables as percent difference compared to current market price. This gives a good idea of where the stock is trading in relation to its recent range.

  - Relative Minimums (Supports):
    - Takes in numerical representation of price/time graph, finds all relative min over past time interval. Relative min data can be used to estimate the existence of support levels, and set strikes appropriately. These will be used as probabilistic variables to determine short strike. 

  - Trading Range: 
    - Use a security's 30, 50 day price range to determine its relative 'valuation' and when a stock trades within a certain percent of its range, it could be an indicator to sell a put with a strike price towards/at the lower bound
  
  - MACD:
    - Indicator of security under/over bought

Assumptions:
- 3 day MA to measure price
- Relying on multiple indicators can improve probability of profit


Options pricing accuracy can vary during market hours
Tracked option data updated daily EOD to external database
