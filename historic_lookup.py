import yfinance as yf
import pandas as pd
from datetime import date


def historic_lookup():
    # log today's date
    today = date.today()
    while True:
        # Request user input for which stock to search
        ticker = input("What is the stock symbol for your query?:").upper()
        # Request Start and end date for query
        start_date = input("enter the start date (YYYY-MM-DD):")
        end_date = input("enter the end date (YYYY-MM-DD) for today type 't':")
        if end_date == "t":
            end_date = today

        # ticker =
        # start_date =
        # end_date =
        # if end_date == "t":
        #    end_date = today

        # Define the ticker list
        tickers_list = [ticker]

        # Create placeholder for data
        data = pd.DataFrame(columns=tickers_list)

        # Fetch the data
        for ticker in tickers_list:
            data = yf.download([ticker], start=start_date, end=end_date, auto_adjust=True)

        # Print first 5 rows of the data
        line_start = 0
        line_end = 5
        while True:
            print(data.iloc[line_start:line_end, :])
        # navigation for next 5
            navigation = input("press enter to load 5 more or 'q' to start again...")
            if navigation != str("q"):
                new_start = line_start + 5
                new_end = line_end + 5
                line_start = new_start
                line_end = new_end
                continue

            else:
                break

        continue

if __name__ == '__main__':
    historic_lookup()