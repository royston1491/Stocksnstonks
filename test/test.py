import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials
start_date = str()

mystock0 = yf.Ticker('TSLA')
stock0historical = mystock0.history(period="max", interval="1d",)
print (stock0historical)
