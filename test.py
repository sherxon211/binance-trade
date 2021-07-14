from binance.client import Client
import time
import os

# api_key ve api_secret bilgilerini içeri aktarma
api_key = os.environ.get('test_key')
api_secret = os.environ.get('test_secret')

client = Client(api_key, api_secret)

mumlar = client.get_klines("EHTUSDT", Client.KLINE_INTERVAL_15MINUTE)

print(mumlar)