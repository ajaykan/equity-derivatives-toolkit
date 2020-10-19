from classes import Option
import utils
import yfinance as yf
import datetime as dt

tracked = []

sample_date_future = dt.date(2022, 1, 15)
fb = yf.Ticker("FB")

leap = Option(fb, sample_date_future, 290, True)
print(leap)

class Option_Tracker():

    def __init__(self, option):
        # assert(type(option) == Option)
        self.date_init = utils.date_to_str(dt.date.today)
        self.last_price = 0