import utils

import datetime
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

def nearest_strike_by_pct_otm(ticker, pct_otm, expiry): # nearest OTM strike on a particular expiry; pct_otm = 0.03 := 3% OTM, pct_otm < 0 := ITM put
    current_price = utils.moving_average(ticker, 3)
    otm_strike_price = current_price * (1-pct_otm)
    strikes = ticker.option_chain(expiry).puts["strike"] # all strikes for a given expiry
    dist_to_strike = list(map(lambda x: round(abs(x - otm_strike_price), 3), strikes))
    index = np.where(dist_to_strike == min(dist_to_strike))   
    # print(current_price)
    # print(otm_strike_price)
    return strikes[index[0][0]]


def data_by_ticker_and_pct_otm(ticker, pct_otm): # return list of (expiry, nearest strike, put option cost, DTE, ROI) for each expiry in ticker.options
    recent_price = utils.moving_average(ticker, 3)
    print(str(ticker.info['symbol']) + " 3-day MA: %s; OTM %s pct" %(str(recent_price), str(pct_otm*100)))
    today = datetime.date.today()
    data = []

    for date in ticker.options:
        strike = nearest_strike_by_pct_otm(ticker, pct_otm, date)
        option_chain = ticker.option_chain(date).puts
        option_price = option_chain.loc[option_chain['strike'] == strike]['lastPrice'].iloc[0]
        dte = (utils.str_to_date(date) - today).days
        roi = round(option_price / recent_price, 4)
        data.append((date, strike, option_price, dte, roi))
    return data



def display_data(tickers, pct_otm): # display CSP ROI of a set of tickers vs DTE
    for i in tickers:
        data = data_by_ticker_and_pct_otm(i, pct_otm)
        symbol = str(i.info['symbol'])
        dte = []
        roi = []
        for i in data:
            dte.append(i[3])
            roi.append(i[4])   
        plt.plot(dte, roi, label=symbol)
        plt.title("ROI vs DTE %s pct OTM CSP" %(str(pct_otm*100)))
        plt.grid()
        plt.legend()    
    plt.show()


# general basket
basket = ["AMD", "AAPL", "T", "TSLA", "NIO", "PLTR", "SPY", "QQQ", "TQQQ"]
basket1 = {}
for i in basket:
    basket1[i] = yf.Ticker(i)


# etfs and indices
indices_etfs = ["SPY", "QQQ", "TQQQ", "XLF", "EEM"]
basket2 = {}
for i in indices_etfs:
    basket2[i] = yf.Ticker(i)


# Workspace

display_data(basket2.values(), 0.05)
