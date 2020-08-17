import yfinance as yf


basket = ["AAPL", "MSFT", "FB", "NVDA", "AMD", "V"]

tickers = []
for i in basket:
    tickers.append(yf.Ticker(i))

# exp = aapl.options

# options = aapl.option_chain(exp[3]) # option chain for 9/10/2020

# hist = aapl.history(period='3mo')

def range(ticker, months):
    return

print(tickers)
