import yfinance as yf
import datetime

# START UTILITY

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

# END UTILITY


class Portfolio:

    # Has list of positions and list of options

    def __init__(self, lst_pos=[], lst_opt=[]):
        self.lst_pos = lst_pos
        self.lst_opt = lst_opt

    def addPos(self, pos):
        assert(isinstance(pos, Position))
        self.lst_pos.append(pos)

    def addOpt(self, opt):
        assert(isinstance(opt, Option))
        self.lst_opt.append(opt)


class Position:

    valid = True
    
    def __init__(self, ticker_obj):
        object_type = type(yf.Ticker('AMD'))
        try:
            assert(isinstance(ticker_obj, object_type))
        except:
            self.valid = False
            print("Enter valid ticker_obj")
            return
        
        # meta
        self.obj = ticker_obj

        # stock info
        self.ticker = self.obj.info['symbol']
        self.annual_div = 0
        
        # indicators
        # self.ind_ma = ma_test(self.obj)

        # positions
        self.share_count = 0
        self.avg_cost = 0
        self.net_cost = 0 # just shares * avg cost
    
    
    # def update_ma(self):
    #     ind_ma = ma_test(self.obj)


    def add_position(self, share_count, avg_cost):
        self.share_count += share_count
        self.net_cost += share_count * avg_cost
        self.avg_cost = round(self.net_cost / self.share_count, 2)

    def __str__(self):
        return("""
        
        MA test: bool

        Shares: {shares}
        Avg. Cost: {cost}

        """.format(shares=self.share_count, cost=self.avg_cost))
        

class Option:


    def __init__(self, ticker_obj, expiry, strike, put):
        self.obj = ticker_obj
        if isinstance(expiry, str):
            expiry = str_to_date(expiry)

        assert(isinstance(ticker_obj, type(yf.Ticker("AMD")))), "Option error: invalid ticker_obj"
        # assert(date_to_str(expiry) in ticker_obj.options), "Option error: invalid expiry"
        
        try:
            expiration = nearest_expiry(self.obj.options, expiry)
            self.expiry = expiration
        except:
            raise ValueError("No expiry found within 3 days of date")

        self.strike = strike
        self.put = put # bool
        
    def dte(self):
        today = datetime.date.today()
        delta = self.expiry - today
        if delta.days < 0:
            return("Option expired")
        return delta.days

    def option_data(self): # returns dataframe of options info
        exp_date = date_to_str(self.expiry)
        chain = self.obj.option_chain(exp_date)
        if self.put:
            chain = chain.puts
        else:
            chain = chain.calls
        option_data = chain[chain['strike'] == self.strike]
        return option_data

    def expired(self): # returns bool
        today = datetime.date.today()
        if today <= self.expiry:
            return False
        return True