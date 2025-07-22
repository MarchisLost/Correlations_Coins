import pandas as pd
import yfinance as yf
# import seaborn as sns
# import matplotlib.pyplot as plt

# Define coins and Yahoo tickers
coins = {
    'BTC': 'BTC-EUR',
    'ETH': 'ETH-EUR',
    'SOL': 'SOL-EUR'
}

# Download the data
data = yf.download(list(coins.values()), start="2024-01-01", end="2024-07-01", group_by='ticker', auto_adjust=False, interval="1h")

# Extract 'Adj Close'
adj_close = pd.DataFrame({symbol: data[ticker]['Close'] for symbol, ticker in coins.items()})

# Drop rows with missing data
adj_close.dropna(inplace=True)

# Calculate correlation
correlation = adj_close.corr()

print("Correlation matrix:")
print(correlation)

# sns.heatmap(correlation, annot=True, cmap='coolwarm')
# plt.title("Crypto Price Correlation")
# plt.show()
