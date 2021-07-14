from binance.client import Client
import time

# api_key ve api_secret bilgilerini içeri aktarma
all_keys = open("./bilgiler.txt","r").read().splitlines()
api_key = all_keys[0]
api_secret = all_keys[1]

client = Client(api_key, api_secret)

mumlar = client.get_klines("EHTUSDT", Client.KLINE_INTERVAL_15MINUTE)

print(mumlar)