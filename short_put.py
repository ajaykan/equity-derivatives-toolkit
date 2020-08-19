import yfinance as yf
import datetime
import matplotlib
import numpy as np

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


# UTILITY

def str_to_date(date):
    date = date.split("-")
    date = list(map(int, date))
    return datetime.date(date[0], date[1], date[2])

# END


def price_range(ticker_obj, days): # returns tuple (min, max, days)
    assert(days > 0), "Number of days > 0"

    delta = str(days) + "d"
    hist = ticker_obj.history(period=delta)
    high = max(hist['High'])
    low = min(hist['Low'])
    return (low, high, days)

def price_by_date(ticker_obj, date, time="Close"): # time: {Open, High, Low, Close}
    today = datetime.date.today()
    if type(date) is str:
        date = str_to_date(date)
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

def moving_average(ticker_obj, days): # past trading days
    assert (days > 1), "MA >= 2 days"

    delta = str(days) + "d"
    hist = ticker_obj.history(period=delta)
    return round(np.mean(hist["Close"]), 2)


past_date = datetime.date(2020, 10, 15)

def list_ma(ticker_obj, lst_days):
    ma = []
    for i in lst_days:
        ma.append(moving_average(ticker_obj, i))
    current_price = moving_average(ticker_obj, 3)

    return (ticker_obj, current_price, lst_days, ma)

days = [15, 30, 60, 120]

def composite_weighting(ticker_obj, lst_days):
    return 

print(list_ma(jpm, days))