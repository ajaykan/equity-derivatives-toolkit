from classes import Option
import yfinance as yf
import datetime as dt

tracked = []

sample_date_future = dt.date(2022, 1, 15)
fb = yf.Ticker("FB")

leap = Option(fb, sample_date_future, 290, True)
print(leap)
