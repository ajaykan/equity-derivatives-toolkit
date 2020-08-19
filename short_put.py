import yfinance as yf
import datetime

basket = ["AAPL", "MSFT", "FB", "NVDA", "AMD", "V"]

ticker_objs = []
for i in basket:
    ticker_objs.append(yf.Ticker(i))

exp = ticker_objs[0].options

options = ticker_objs[0].option_chain(exp[3]) # option chain for 9/10/2020

# hist = aapl.history(period='3mo')

def price_range(ticker_obj, weeks): # returns tuple (min, max, no. months)
    time = str(weeks) + "wk"
    hist = ticker_obj.history(period=time)
    high = max(hist['High'])
    low = min(hist['Low'])
    return (low, high, weeks)

print(price_range(ticker_objs[0], 6))

def price_by_date(ticker_obj, date):
    today = datetime.date.today()
    if type(date) is str:
        date = str_to_date(date)
    delta = today - date
    return delta

def str_to_date(date):
    date = date.split("-")
    date = list(map(int, date))
    return datetime.date(date[0], date[1], date[2])

print(price_by_date(ticker_objs[0], exp[3]))