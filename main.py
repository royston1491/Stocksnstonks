import kivy
from kivy.app import App
import yfinance as yf
import pandas as pd
import csv

from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.lang import Builder

from line_splitter import LineSplitter

kivy.require('1.0.6')  # replace with your current kivy version !


# Class for main screen
class MainWindow(Screen):
    # Function for api call and storage of data using user input
    def lookup(self):
        #os.remove("result.csv")
        tickers_list = self.ids.ticker_box.text
        start_date = self.ids.start_box.text
        end_date = self.ids.end_box.text
        data = pd.DataFrame()
        data = yf.download([tickers_list], start=start_date, end=end_date, auto_adjust=True)
        data.to_csv('result.csv')

# Results Screen
class SecondWindow(Screen):
    # Function for taking data and displaying to the user
    # output currently needs formating
    def myruntime(self,):
        line_splitter = LineSplitter()
        with open('result.csv', 'r') as csvfile:
            for line in csvfile.readlines():
                for item in line_splitter.split(line, ","):
                    self.results_box.add_widget(Label(text=item))

# Manages trasition between screens listed at top of .kv
class WindowManager(ScreenManager):
    pass


# Allows for use of .kv not sharing name with app
kv = Builder.load_file("StonksnStocks.kv")


class StonksnStocks(App):
    def build(self):
        return kv


if __name__ == '__main__':
    StonksnStocks().run()