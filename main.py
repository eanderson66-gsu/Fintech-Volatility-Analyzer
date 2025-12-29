#Test

#Import Functions
from data_fetcher import finance_data_fetch

#Test Paypal fetch
my_data = finance_data_fetch("PYPL")
print(my_data.head())