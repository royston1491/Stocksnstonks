import kivy
from kivy.app import App
import yfinance as yf
import pandas as pd
import csv
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.lang import Builder


kivy.require('1.0.6')  # replace with your current kivy version !


class MainWindow(Screen):
    # call for stock history

    def lookup(self):
        #os.remove("result.csv")
        tickers_list = self.ids.ticker_box.text
        start_date = self.ids.start_box.text
        end_date = self.ids.end_box.text
        data = pd.DataFrame()
        data = yf.download([tickers_list], start=start_date, end=end_date, auto_adjust=True)
        data.to_csv('result.csv')


class SecondWindow(Screen):

    def myruntime(self,):

        label = self.ids.label_rows
        with open('result.csv', 'r') as csvfile:
            for line in csvfile.readlines():
                self.ids.label_rows.text += line


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("StonksnStocks.kv")


class StonksnStocks(App):
    def build(self):
        return kv


if __name__ == '__main__':
    StonksnStocks().run()
