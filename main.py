#Test

#Import Functions
from data_fetcher import finance_data_fetch
from analyzer import volatility_calculator
from visualizer import plot_comparison

#Test running multiple Stocks
stocks = "SPY NVDA GOOG AMZN PYPL".split()

#Create a dictionary to hold results
data_results = {}

#Parse through each symbol/stock
for symbol in stocks:
    try:
        raw_df = finance_data_fetch(symbol)

        #Calculate the volatility for the stock
        analyzed_df = volatility_calculator(raw_df)

        #Store in dictionary
        data_results[symbol] = analyzed_df

    except Exception as e:
        print("Could not process {symbol:} {e}")

#To Visualize each Chart
print("Generating chart...")
plot_comparison(data_results)
