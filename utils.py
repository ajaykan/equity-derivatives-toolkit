import datetime
import numpy as np

# handling dates/delta

def str_to_date(date):  # returns date not datetime
    date = date.split("-")
    date = list(map(int, date))
    return datetime.date(date[0], date[1], date[2])

def date_to_str(date):
    year = str(date.year)
    month = date.month
    if month < 10:
        month = "0" + str(month)
    month = str(month)
    day = date.day
    if day < 10:
        day = "0" + str(day)
    day = str(day)
    return "{year}-{month}-{day}".format(year=year, month=month, day=day)

def date_concat(date): # returns string, concat version of date 2020-07-24 -> 7/24/20 
    if isinstance(date, str):
        date = str_to_date(date)
    month = str(date.month)
    day = str(date.day)
    year = str(date.year % 100)
    return("{month}/{day}/{year}".format(month=month, day=day, year=year))


def nearest_expiry(expirations, date): # takes as input list of expiration dates, and date, returns expiration with (expiry - dates) < 3 days
    for expiry in expirations:
        expiry = str_to_date(expiry)
        delta = (expiry - date).days
        if abs(delta) <= 3:
            return expiry
    return ValueError("No expiration within 3 days of date")



# stock price data

def moving_average(ticker_obj, days): # past real days
    assert (days > 1), "MA >= 2 days"
    
    days = int(round(days * (5/7)))
    delta = str(days) + "d"
    hist = ticker_obj.history(period=delta)

    return round(np.mean(hist["Close"]), 2)