# Options Strategy

This repo contains tools I designed/use to sell cash-secured puts (CSP). These tools determine likelihood of profit probabalistically. Uses lagging indicators including but not limited to: exponential/moving averages, moving average convergence divergence (MACD), relative strength index (RSI). Analyzes price action using trading ranges and by approximating support/resistance levels. Documentation will be updated periodically.	


#### `put-premium.py`
Allows user to compare ROI of selling various ROI

Uses 3-day moving average as reference point

Allows the user to define their percent out-the-money (OTM), used to determine the strike price

Tool graphs the price of put option at the corresponding strike price in relation to the days til expiration (DTE) to determine theoretical ROI

Graphs ROI vs DTE of entire 'basket' of stocks to allow easy comparison


#### `classes.py`
User defined objects to be referenced by future tools
  - `Position`: user position in one stock	
  - `Option`: stock option with vaalid expiry in future	
  - `Portfolio`: collection of positions and options	



<br/>
<br/>


Options pricing accuracy can vary during market hours
Tracked option data updated daily EOD to external database
Options_tracker used to track daily option price movement

#### Untracked files:
- option_tracker
- drip_mgmt
- income_inv
