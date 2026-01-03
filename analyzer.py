import numpy as np

#Step 1: Create a function to calculate Log returns
def volatility_calculator(df, window = 12):
    #Step 2: Utilize np.log to handle the vector math per column
    df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))

    #Step 3: Calculate the rolling volatility
    df['Volatility'] = df['Log_Return'].rolling(window=window).std() * np.sqrt(252) #I am multiplying by sqrt(252) to annualize the dailty stdev

    return df
