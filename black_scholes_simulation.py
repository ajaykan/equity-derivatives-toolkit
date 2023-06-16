import pandas as pd
import datetime as dt
import numpy as np
from scipy.stats import norm

# example simulation for AAPL

def tte(): # return time until end of year expressed as percentage
    today = dt.date.today()
    eoy = dt.date(dt.date.today().year, 12, 31)
    pct = (eoy-today).days
    return pct / 365

PRICE = 185

STRIKE = 180

VOLATILITY = 0.1776 # 60 day historical volatility (https://www.alphaquery.com/stock/AAPL/volatility-option-statistics/60-day/historical-volatility)

RFR = pow(np.e, 0.0383) # continous risk-free rate where current 1-year risk-free rate is 3.83%

DIV = pow(np.e, 0.0052) # continous dividend yield where current annual yield is 3.83%


ticker = "AAPL"

tte_ = tte()

todays_options_data = pd.read_csv("data/{ticker}/{date}.csv".format(ticker=ticker, date=str(dt.date.today())))

d1 = (np.log(PRICE/STRIKE) + tte_ * (RFR - DIV + 0.5*VOLATILITY**2)) / (VOLATILITY * np.sqrt(tte_))

d2 = d1 - (VOLATILITY * np.sqrt(tte_))

price_call = PRICE * pow(np.e, -DIV*tte_) * norm.cdf(d1) - STRIKE * pow(np.e, -RFR*tte_) * norm.cdf(d2)
price_call = PRICE *  norm.cdf(d1) - STRIKE * pow(np.e, -RFR*tte_) * norm.cdf(d2)


price_put = STRIKE * pow(np.e, -RFR*tte_) * norm.cdf(-d2) - PRICE * pow(np.e, -DIV*tte_) * norm.cdf(-d1)

print(price_call)
print(price_put)

# print(todays_options_data['expiration'].unique())