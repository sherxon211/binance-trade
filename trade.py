from binance.client import Client
import time

all_keys = open("bilgiler.txt","r").read().splitlines()
api_key = all_keys[0]
api_secret = all_keys[1]

client = Client(api_key, api_secret)

#son 4 harfi alma
'''site3 = "www.yahoo.com"
print(site3[-4:])'''

#info = client.get_all_tickers()
#print(info)

#depth = client.get_order_book(symbol='ETHUSDT')
#print(depth)

#candles = client.get_klines(symbol='MITHUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
#print(candles)

#prices = client.get_all_tickers()
#print(prices)

#info_account = client.get_account()
#print(info_account)

  #f.write(price["symbol"]+" :"+ price["price"]+"\n")
            #print(price["symbol"]+" :"+ price["price"])
        #f.write("-"*30+">>"+time.strftime('%c')+"\n")



def percent_count(x,y):
    x = float(x)
    y = float(y)
    percent = (x-y)/x*100
    return percent

while True:
    eski_liste = []
    yeni_liste = []

    prices = client.get_all_tickers()
    for price in prices:
        if price["symbol"].endswith("USDT"):
            eski_liste.append(price)

    time.sleep(900)

    prices = client.get_all_tickers()
    for price in prices:
        if price["symbol"].endswith("USDT"):
            yeni_liste.append(price)

    liste1 = []
    liste2 = []
    tokens = []

    for a in eski_liste:
        deger = a["price"]
        liste1.append(deger)
    for b in yeni_liste:
        deger2 = b["price"]
        liste2.append(deger2)
    for c in eski_liste:
        deger3 = c["symbol"]
        tokens.append(deger3)

    for x,y in zip(liste1, liste2):
        endeks = liste1.index(x)
        x = float(x)
        y = float(y)
        if abs((x-y)/x*100) >= 6:
            for e in tokens:
                if endeks==tokens.index(e):
                    print(f"{e} tokenini {x} fıyatdan satın alabiliriniz!!!")
        else:
            continue
                
    print("15 dakika oladu!")



