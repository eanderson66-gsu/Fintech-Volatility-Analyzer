import matplotlib.pyplot as plt
import seaborn as sns

#Create the function for displaying the stock's charts
def plot_comparison(data_results):
    #Set Style
    sns.set_theme(style = "whitegrid")
    plt.figure(figsize=(12,6))

    #Loop through the dictionary to plot each stock
    for stock, df in data_results.items():

        plt.plot(df.index, df['Volatility'], label=f"{stock} Volatility")

    #This is for professional Formatting
    plt.title("Stock Volatility Comparison (21-Day Period)", fontsize = 16)
    plt.xlabel("Date", fontsize = 12)
    plt.ylabel("Annualized Volatility (%)", fontsize = 12)
    plt.legend()

    #This is for display
    plt.tight_layout()
    plt.show()
