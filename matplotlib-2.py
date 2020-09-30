import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf


data = yf.download("AAPL", start="2019-09-26", end="2020-09-27")

x1 = []
y1 = []

x2 = []
y2 = []

# plot 30 week ma each Friday


for item in data.T:
    x1.append(item)
    x2.append(item)


for item in data.Close:
    y1.append(item)
    y2.append(item * 1.5)


for open in data.Close:
    print(open)


plt.plot(x1, y1, label="line 1")
plt.plot(x2, y2, label="line 2")


plt.xlabel('Date')
plt.ylabel('Price ($)')

plt.title('Apple Stock ')

plt.show()
