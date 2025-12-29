#Step 1: Retrieve the Financial Data
import yfinance as yf

#Step 2: Create a Function to pull specific Data per Stock
def finance_data_fetch (ticker_symbol):
    #Step 2A: Display a message indicating which stock data is printing
    print ("The system is downloading data for ", (ticker_symbol), "!" )
    #Step 2B: Pull 2 years of data and store it in a variable
    stock_data = yf.download(ticker_symbol, period = "2y")

    return stock_data

