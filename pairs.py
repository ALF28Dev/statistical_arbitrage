from backtest_engine import backtest_engine
import yfinance as yf
import matplotlib.pyplot as plt

class spread():
    def __init__(self, ticker_one, ticker_two, period, interval):
        self.stock_one = yf.Ticker(ticker_one)
        self.stock_two = yf.Ticker(ticker_two)
        self.stock_one_price = self.stock_one.history(period=period, interval=interval).reset_index()
        self.stock_two_price = self.stock_two.history(period=period, interval=interval).reset_index()
        self.spread = self.stock_one_price["Close"]-self.stock_two_price["Close"]
        # self.spread = self.stock_one_price["Close"]/self.stock_two_price["Close"] price ratio formula
        self.new = self.stock_one_price[['Date']].copy()
        self.new["Spread"] = self.spread
        self.get_bollinger_bands()  

    def output_dataframe(self):
        return self.new

    def get_sma(self, prices, rate):
        return prices.rolling(rate).mean()

    def get_bollinger_bands(self, rate=15):
        sma = self.get_sma(self.new["Spread"], rate)
        std = self.new["Spread"].rolling(rate).std()
        self.new["bollinger_up"] = sma+std*2
        self.new["bollinger_down"] = sma-std*2 
        self.new["middle"] = sma

    def show_spread(self):
        plt.plot(self.new["Spread"])
        plt.plot(self.new["bollinger_up"], label='Bollinger Up', c='g')
        plt.plot(self.new["bollinger_down"], label='Bollinger Down', c='r')
        plt.plot(self.new["middle"], label='sma', c='b')
        plt.legend()
        plt.show()

prices = spread("GOOG","AMZN","max","1d")
prices.show_spread()
backtest = backtest_engine(prices.output_dataframe())
backtest.iterate()
backtest.plot_results()
backtest.plot_return()
