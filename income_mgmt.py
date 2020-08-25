from classes import Portfolio, Position

import yfinance as yf


def position_income(pos):
    assert(isinstance(pos, Position))

    share_count = pos.share_count
    annual_div = pos.annual_div

    return annual_div * share_count


def createPortfolio(share_dict): # takes in dict: {ticker (str): (num shares (int), avg cost (float)}, returns Portfolio obj
    positions = []
    for ticker, data in share_dict.items():
        pos = Position(yf.Ticker(ticker)) # create position with ticker
        pos.add_position(data[0], data[1])


aapl_div = 3.04
k = Position(yf.Ticker("AAPL"))
k.annual_div = aapl_div

k.add_position(150, 300)

print(position_income(k))



