#Test

#Import Functions
from data_fetcher import finance_data_fetch
from analyzer import volatility_calculator

#Test Paypal fetch
my_data = finance_data_fetch("PYPL")
print(my_data.head())

#Test the Volatility calculator
my_data = volatility_calculator(my_data)
print(my_data[['Close', 'Log_Return', 'Volatility']].tail())
