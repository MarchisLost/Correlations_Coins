import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

url_coin_list = "https://api.coingecko.com/api/v3/coins/list"

url_btc_history = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from=1721429982&to=1753036460"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": api_key
}

response = requests.get(url_btc_history, headers=headers)

print(response.text)

# with open("coins_list.txt", "w", encoding="utf-8") as f:
#     f.write(response.text)
