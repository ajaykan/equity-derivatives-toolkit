# Theta Strategy

This repo contains tools I designed/use to sell cash-secured puts (CSP). These tools use probability to optimize your likelihood of profit. Documentation will be updated as needed.	

`classes.py`: user defined objects	
  - `Position`: user position in one stock	
  - `Option`: stock option with vaalid expiry in future	
  - `Portfolio`: collection of positions and options	

`short_put.py`: allows user to find optimal entry to sell CSP

- Moving Averages:
    - Looks at typical short put days til expiration (DTE), 15-45 days. Calculates moving average of 15, 45, and 200 days. Then, recalculate these variables as percent difference compared to current market price. This gives a good idea of where the stock is trading in relation to its

Relative Minimums (Supports):
Takes in numerical representation of price/time graph, finds all relative min over past time interval. Relative min data can be used to estimate the existence of support levels, and set strikes appropriately. 


These will be used as probabilistic variables to determine short strike. 

`income_mgmt.py`: based on positions in a portfolio; dynamically enable DRIP on certain positions. Allows user to adjust annual income by to preference
