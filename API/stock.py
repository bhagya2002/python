# import yahoo finacne data
import yfinance as yf

# get list of user stock(s) they want to see
user_stocks = list(input("What stock(s) do you want to look into: ").split())

# range of stocks searched
for i in range(len(user_stocks)):
    stock = yf.Ticker(user_stocks[i])

    # show actions (dividends, splits)
    print(stock.quarterly_earnings)
