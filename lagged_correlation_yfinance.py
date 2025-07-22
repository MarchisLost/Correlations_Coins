import yfinance as yf
import pandas as pd
import numpy as np

# Define coins and Yahoo tickers
coins = {
    'BTC': 'BTC-EUR',
    'ETH': 'ETH-EUR',
    'SOL': 'SOL-EUR'
}

# Download hourly data
data = yf.download(
    list(coins.values()),
    start="2024-01-01",
    end="2024-07-01",
    interval="1h",
    group_by='ticker',
    auto_adjust=False
)

# Extract 'Close' prices
close_prices = pd.DataFrame({
    symbol: data[ticker]['Close'] for symbol, ticker in coins.items()
})

# Drop rows with missing values
close_prices.dropna(inplace=True)


# Function to compute lagged correlations
def compute_lagged_correlation(df, coin1, coin2, max_lag=24):
    result = {}
    series1 = df[coin1]
    series2 = df[coin2]
    for lag in range(0, max_lag + 1):
        shifted_series1 = series1.shift(lag)
        corr = shifted_series1.corr(series2)
        result[lag] = corr
    best_lag = max(result, key=result.get)
    return best_lag, result[best_lag], result


# Run lagged correlation for all pairs
results = {}
symbols = list(coins.keys())
for i in range(len(symbols)):
    for j in range(len(symbols)):
        if i != j:
            c1, c2 = symbols[i], symbols[j]
            lag, corr, full_corr = compute_lagged_correlation(close_prices, c1, c2)
            results[(c1, c2)] = {
                'best_lag_hours': lag,
                'max_correlation': corr
            }

# Print results
print("\n=== Optimal Lagged Correlations (in hours) ===")
for pair, vals in results.items():
    print(f"{pair[0]} → {pair[1]}: Best lag = {vals['best_lag_hours']}h, Correlation = {vals['max_correlation']:.4f}")
