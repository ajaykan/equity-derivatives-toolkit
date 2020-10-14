# Theta Strategy

This repo contains tools I designed/use to sell cash-secured puts (CSP). These tools use probability to optimize your likelihood of profit. Documentation will be updated as periodically.	

`classes.py`: user defined objects	
  - `Position`: user position in one stock	
  - `Option`: stock option with vaalid expiry in future	
  - `Portfolio`: collection of positions and options	
  
  
Uses lagging indicators including but not limited to: exponential/moving averages, moving average convergence divergence (MACD), relative strength index (RSI). Analyzes price action using trading ranges and by approximating support/resistance levels.

`short_put.py`: allows user to find optimal entry to sell CSP by analyzing price movement

  - Moving Averages (MA):
    - Looks at typical short put days til expiration (DTE): 15-45 days. Calculates moving average of 15, 45, and 200 days. Returns value as percent deviation from market value.

  - Relative Minimums (Supports):
    - Takes in numerical representation of price/time graph, finds all relative min over past time interval. Relative min data can be used to estimate the existence of support levels to set strikes appropriately. Used as probabilistic variables to determine short strike. 

  - Trading Range: 
    - Use a security's 30, 50 day price range to determine its relative 'valuation' and when a stock trades within a certain percent of its range, it could be an indicator to sell a put with a strike price towards/at the lower bound



/n

Options pricing accuracy can vary during market hours
Tracked option data updated daily EOD to external database
