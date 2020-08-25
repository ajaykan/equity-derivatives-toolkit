# Theta Strategy

This repo contains tools I designed/use to sell cash-secured puts (CSP) for consistent income. These tools use probability to optimize your likelihood of profit. Documentation will be updated as needed.

`classes.py`: user defined objects
  - `Position`: user position in one stock
  - `Option`: stock option with vaalid expiry in future
  - `Portfolio`: collection of positions and options

`short_put.py`: allows user to find optimal entry to sell CSP

`income_mgmt.py`: based on positions in a portfolio; dynamically enable DRIP on certain positions. Allows user to adjust annual income by to preference
