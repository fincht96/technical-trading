import yfinance as yf

msft = yf.Ticker("MSFT")


data = yf.download("AAPL", start="2019-01-01", end="2019-02-01")

# print(msft.info['sector'])


print(data)