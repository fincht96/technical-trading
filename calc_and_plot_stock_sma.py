import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def calcLastFriDate(date):
 
    dayNum = date.weekday()
    
    
    lastFriDate = date - relativedelta(days= dayNum + 3) 

    return lastFriDate


def calcSma(date, stockData, numWeeks):
    sum = 0
    numReadingsLast20Weeks = 0

    # calcs date of prev friday
    lastFriDate = calcLastFriDate(date)

    for i in range(0,numWeeks):
        friDate = lastFriDate - relativedelta(weeks=(1*i))
        price = stockData.loc[stockData.index == friDate.strftime("%Y-%m-%d"), 'Close']
        if price.values.size > 0:
            sum += price.values[0]
            numReadingsLast20Weeks += 1

    return sum/numReadingsLast20Weeks


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

if __name__ == '__main__':

    numWeeks = 30
    ticker = "^FTSE"

    endDate = datetime.today()
    startDate = datetime.today() - relativedelta(years=1)

    stockData = yf.download(
        ticker , start=(startDate - relativedelta(weeks=numWeeks)).strftime("%Y-%m-%d"), end=endDate.strftime("%Y-%m-%d"), progress=False)

 
    x1 = []
    y1 = []


    mAX = []
    mAY = []

    for singleDate in daterange(startDate, endDate):

        stock = stockData.loc[stockData.index == singleDate.strftime("%Y-%m-%d"), 'Close']

        if stock.values.size > 0:
            x1.append(singleDate)
            y1.append(stock.values[0])
            mAX.append(singleDate)
            mAY.append(calcSma(singleDate, stockData, numWeeks))
            


    plt.plot(x1, y1, label= ticker + " Stock Price")
    plt.plot(mAX, mAY, label= str(numWeeks) + " Week MA")

    plt.xlabel('Date')
    plt.ylabel('Price ($)')

    plt.title(ticker + ' Stock')

    plt.show()

