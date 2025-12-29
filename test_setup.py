import yfinance as yf
import pandas as pd

#Test
data = yf.download("PYPL", period="1mo")
print("Ready")
print(data.tail())
print(data.head())