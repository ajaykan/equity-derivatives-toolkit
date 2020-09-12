from classes import Position, Option
import utils

import datetime
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

basket = ["AMD", "AMZN", "FB", "GOOG", "DIS", "JPM"]

ticker_objs = []
for i in basket:
    ticker_objs.append(yf.Ticker(i))

amd = ticker_objs[0]
amzn = ticker_objs[1]
fb = ticker_objs[2]
goog = ticker_objs[3]
dis = ticker_objs[4]
jpm = ticker_objs[5]

exp = ticker_objs[0].options

options = ticker_objs[0].option_chain(exp[3]) # option chain for 9/10/2020

# TOOLS

def price_range(ticker_obj, days): # returns tuple (min, max, real days)
    assert(days > 0), "Number of days > 0"

    delta = int(round(days * (5/7)))
    delta = str(delta) + "d"
    hist = ticker_obj.history(period=delta)
    high = max(hist['High'])
    low = min(hist['Low'])
    return (low, high, int(delta))


def price_by_date(ticker_obj, date, time="Close"): # time: {Open, High, Low, Close}
    today = datetime.date.today()
    if type(date) is str:
        date = utils.str_to_date(date)
    delta = (today - date).days + 2
    if delta < 0:
        return "Invalid date"
    delta = str(delta) + "d"    
    hist = ticker_obj.history(period=delta)
    try:
        hist = hist.loc[date]
        return hist[time]
    except:
        return "Non trading day"


def moving_average(ticker_obj, days): # past real days
    assert (days > 1), "MA >= 2 days"
    
    days = int(round(days * (5/7)))
    delta = str(days) + "d"
    hist = ticker_obj.history(period=delta)

    return round(np.mean(hist["Close"]), 2)


def ma_data(ticker_obj, lst_days): # CONSOLIDATE w above and below
    ma = []
    for i in lst_days:
        ma.append(moving_average(ticker_obj, i))
    current_price = moving_average(ticker_obj, 3)
    pct_diff = []
    for i in ma:
        val_diff = current_price - i
        pct_chg = round(val_diff / i * 100, 2)
        pct_diff.append(pct_chg)

    return (ticker_obj, current_price, lst_days, ma, pct_diff) # [ticker, price, [days], [averages], [pct_diff]]


def ma_test(ticker_obj): # returns boolean
    days = [50, 200]
    ma = ma_data(ticker_obj, days)
    ma = ma[3]
    return ma[0] > ma[1]


# VISUALIZATIONS

def past_price(ticker_obj, days): # past real days, automatically displays graph
    delta = int(round(days * (5/7)))
    delta = str(delta) + "d"
    hist = ticker_obj.history(period=delta)
    start_date = utils.date_to_str(hist.index[0].date())
    today = utils.date_to_str(datetime.date.today())
    
    close = list(hist['Close'])
    days_list = [i for i in range(len(close))]
    df = pd.DataFrame({"Price": close, "Days": days_list})
    
    plot = sb.lineplot(x="Days", y="Price", data=df)
    plot.set(xlabel=("{start} to {today} ~ {days} days").format(start=utils.date_concat(start_date), today=utils.date_concat(today), days=days))
    plot.set(ylabel=str(ticker_obj.info['symbol'] + " Price"))
    plt.show()
    return
        

# WORKSPACE

amd_pos = Position(amd)
aapl_pos = Position(yf.Ticker("AAPL"))
aapl_pos.add_position(100, 450)
aapl_pos.add_position(200, 420)

sample_date_future = datetime.date(2020, 10, 16)
sample_date_future_2 = datetime.date(2020, 9, 11)


bought = Option(fb, sample_date_future, 290, True)

print(bought)

