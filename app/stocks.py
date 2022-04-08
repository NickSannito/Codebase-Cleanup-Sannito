

print("STOCKS REPORT...")


from app.utils import to_usd
from app.my_mod import fetch_stocks_data


symbol = input("Please input a stock symbol (default: 'NFLX'): ") or "NFLX"
df = fetch_stocks_data(symbol)

latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))

