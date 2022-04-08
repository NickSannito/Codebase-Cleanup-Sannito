


print("CRYPTO REPORT...")


from app.utils import to_usd
from app.my_mod import fetch_crypto_data


symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
parsed_response = fetch_crypto_data(symbol)

tsd = parsed_response["Time Series (Digital Currency Daily)"]

dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]


print(symbol)
print(latest_date)
print(latest['4a. close (USD)'])
print(to_usd(float(latest['4a. close (USD)'])))
