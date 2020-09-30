import yfinance as yf

msft = yf.Ticker("MSFT")


data = yf.download("AAPL", start="2019-01-01", end="2020-04-30")

# print(msft.info['sector'])


print(data)
