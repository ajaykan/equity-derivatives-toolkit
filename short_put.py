import datetime
import yfinance as yf
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


def price_range(ticker_obj, days): # returns tuple (min, max, real days)
    assert(days > 0), "Number of days > 0"

    delta = int(round(delta * (5/7)))
    delta = str(days) + "d"
    hist = ticker_obj.history(period=delta)
    high = max(hist['High'])
    low = min(hist['Low'])
    return (low, high, int(delta))


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


def moving_average(ticker_obj, days): # past real days
    assert (days > 1), "MA >= 2 days"
    
    days = int(round(days * (5/7)))
    delta = str(days) + "d"
    hist = ticker_obj.history(period=delta)

    return round(np.mean(hist["Close"]), 2)



def list_ma(ticker_obj, lst_days):
    ma = []
    for i in lst_days:
        ma.append(moving_average(ticker_obj, i))
    current_price = moving_average(ticker_obj, 3)

    return (ticker_obj, current_price, lst_days, ma) # [ticker, price, [days], [mas]]


def ma_test(ticker_obj):
    days = [50, 200]
    ma = list_ma(ticker_obj, days)
    ma = ma[3]
    return ma[0] > ma[1]



class Position:
    
    def __init__(self, ticker_obj):
        assert(isinstance(ticker_obj, type(yf.Ticker('AMD'))))
        
        self.obj = ticker_obj
        
        # technical indicators
        self.ind_ma = ma_test(self.obj)

        #positions
        self.shares = 0
        self.avg_cost = 0
        self.net_position = 0
    
    
    def update_ma(self):
        ind_ma = ma_test(self.obj)


    def add_position(self, share_count, avg_cost):
        self.shares += share_count
        self.net_position += share_count * avg_cost
        self.avg_cost = round(self.net_position / self.shares, 2)

    def __str__(self):
        return("""
        
        MA test: {bool}

        Shares: {shares}
        Avg. Cost: {cost}

        """.format(bool=self.ind_ma, shares=self.shares, cost=self.avg_cost))
        



amd_pos = Position(amd)
aapl_pos = Position(yf.Ticker("AAPL"))
aapl_pos.add_position(100, 450)
aapl_pos.add_position(200, 420)


print(aapl_pos)