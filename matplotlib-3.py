import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta


def calcLastFriDate(date):
    lastFriDate = 0
    dayNum = date.weekday()

    if dayNum > 4:
        dayNum = dayNum - 4
        lastFriDate = date - timedelta(days=dayNum)

    elif dayNum < 4:
        dayNum = dayNum + 2
        lastFriDate = date - timedelta(days=dayNum)

    return lastFriDate


def calc20WeekSma(date):
    last20FridaysDates = []
    last20FridaysClosingPrice = []

    # calcs date of prev friday
    lastFriDate = calcLastFriDate(date)

    # generate dates of 20 fridays before
    for i in range(0, 20):
        last20FridaysDates.append(lastFriDate - timedelta(days=7 * i))

    data = yf.download("AAPL", start="2019-09-26", end="2020-09-27")

    print(last20FridaysDates)

    sum = 0

    for price in last20FridaysClosingPrice:
        sum += price

    return sum/20


data = yf.download("AAPL", start="2019-09-26", end="2020-09-27")

x1 = []
y1 = []


# 30 week sma
x2 = []
y2 = []


for item in data.T:
    x1.append(item)
    x2.append(item)


for item in data.Close:
    y1.append(item)


print(calc20WeekSma(datetime.today()))


for index, date in enumerate(x1):
    # y2.append(calc20WeekSma(date))
    # print(calc20WeekSma(date))
    pass


plt.plot(x1, y1, label="line 1")
# plt.plot(x2, y2, label="line 2")


plt.xlabel('Date')
plt.ylabel('Price ($)')

plt.title('Apple Stock ')

# plt.show()
