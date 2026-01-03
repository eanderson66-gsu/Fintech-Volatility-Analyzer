#Test

#Import Functions
from data_fetcher import finance_data_fetch
from analyzer import volatility_calculator

#Test running multiple Stocks
stocks = "SPY NVDA GOOG AMZN PYPL".split()

#Create a dictionary to hold results
data = {}

#Parse through each symbol/stock
for symbol in stocks:
    try:
        raw_df = finance_data_fetch(symbol)

        #Calculate the volatility for the stock
        analyzed_df = volatility_calculator(raw_df)

        #Store in dictionary
        data[symbol] = analyzed_df

    except Exception as e:
        print("Could not process {symbol:} {e}")

for symbol, df in data.items():
    volatility = df['Volatility'].iloc[-1]
    print(f"{symbol}: {volatility:.2%}")
