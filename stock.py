import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sb
import yfinance as yf  # Assuming yfinance for data API

sb.set_theme()

"""
STUDENT CHANGE LOG & AI DISCLOSURE:
----------------------------------
1. Did you use an LLM (ChatGPT/Claude/etc.)? [Yes/No]
2. If yes, what was your primary prompt?
----------------------------------

I didn't use AI to write my code, the only thing I did was search for commands that I didn't remeber on google
"""

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        """Downloads data from yfinance and triggers return calculation."""
        data = yf.download(self.symbol, start=self.start, end=self.end)
        data = self.calc_returns(data)
        return data

    def calc_returns(self, df):
        """Adds 'Change', close to close and 'Instant_Return' columns to the dataframe."""
        # Requirement: Use vectorized pandas operations, not loops.
        df["Change"] = (df["Close"] - df["Close"].shift(1)) / df["Close"].shift(1)
        df["Instant_Return"] = (np.log(df["Close"]).diff().round(4))
        return df
    
    def add_technical_indicators(self, windows=[20, 50]):
        """
        Add Simple Moving Averages (SMA) for the given windows
        to the internal DataFrame. Produce a plot showing the closing price and SMAs. 
        """
        for window in windows:
            sma = self.data['Close'].rolling(window=window).mean()
            self.data[f'SMA_{window}'] = sma
            plt.plot(sma, label=window)

        plt.title("SMA vs Date")
        plt.ylabel("SMA")
        plt.xlabel("Date")
        plt.legend()
        plt.show()

    def plot_performance(self):
        """Plots cumulative growth of $1 investment."""
        first = self.data["Close"].iloc[0]
        pct = (self.data["Close"] - first) / first * 100
        plt.plot(self.data.index, pct)
        plt.title(f"Performance of Stock")
        plt.ylabel("Percent Gain / Loss %, relative to first day")
        plt.xlabel("Time")
        plt.legend()
        plt.show()

    def plot_return_dist(self):
        sb.histplot(self.data["Instant_Return"].dropna(), bins=50, kde=True, stat="density")
        plt.title("Hist Instant Return")
        plt.ylabel("Density")
        plt.xlabel("Instant Return")
        plt.legend()
        plt.show()

def main():
    # Example usage:
    aapl = Stock("AAPL")
    aapl.plot_performance()
    aapl.add_technical_indicators()
    aapl.plot_return_dist()

if __name__ == "__main__":
    main()