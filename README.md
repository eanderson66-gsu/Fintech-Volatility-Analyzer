# Fintech Stock Price Volatility Analyzer

## Overview:
A data analytics tool that analyzes the risk profile of major Fintech stocks (PayPal, Visa, Square, Coinbase). This project calculates **Log Returns** and **Annualized Rolling Volatility** to identify market stress periods.

## Key Visualizations:
*Figure 1: Comparison of 21-Day Rolling Volatility across major Fintech assets.*

## Tech Stack:
* **Python 3.10+**
* **Pandas & NumPy** (Data Manipulation & Log Calculations)
* **YFinance** (Real-time Market Data API)
* **Matplotlib & Seaborn** (Data Visualization)

## How to Run:
1.  Clone the repository:
    ```bash
    git clone [https://github.com/eanderson66-gsu/Fintech-Volatility-Analyzer.git](https://github.com/eanderson66-gsu/Fintech-Volatility-Analyzer.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the analysis:
    ```bash
    python main.py
    ```

## 🧠 Methodology
* **Log Returns:** Used instead of simple percentage changes for statistical normalization.
* **Rolling Window:** A 21-day window was selected to represent one trading month.
* **Annualization:** Daily volatility is multiplied by $\sqrt{252}$ to derive annualized risk metrics.
