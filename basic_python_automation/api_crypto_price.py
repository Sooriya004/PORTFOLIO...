import requests
import json

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

response = requests.get(url)
data = response.json()

price = data["price"]

print("Bitcoin Price (USDT):", price)


# Save to file
with open("btc_price.json", "w") as file:
    json.dump(data, file, indent=4)

print("Price data saved to btc_price.json")
