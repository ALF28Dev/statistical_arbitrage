import matplotlib.pyplot as plt

class backtest_engine():
    def __init__(self, data):
        self.data = data
        self.data["position_open"] = None
        self.data["position_close"] = None
        self.open_price = None
        self.total_return = 0
        self.cumulative_return = []
        self.position_open = False
        self.entry_price = None

    def iterate(self):
        for index, row in self.data.iterrows():
            if row["Spread"] > row["bollinger_up"] and self.position_open == True:
                self.data.at[index, "position_close"] = row["Spread"]
                self.position_open = False
                profit = row["Spread"]-self.open_price
                self.total_return+=profit
                self.cumulative_return.append(self.total_return)
                print(self.total_return)
            if row["Spread"] < row["bollinger_down"] and self.position_open == False:
                self.data.at[index, "position_open"] = row["Spread"]
                self.position_open = True    
                self.open_price = row["Spread"]

    def plot_results(self):
        plt.plot(self.data["Spread"])
        plt.plot(self.data["position_open"], marker="v", color="green")
        plt.plot(self.data["position_close"], marker="^", color="red")
        plt.show()

    def plot_return(self):
        plt.plot(self.cumulative_return)
        plt.show()
