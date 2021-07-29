from binance.client import Client
import os
import time
from win10toast import ToastNotifier

# api_key ve api_secret bilgilerini içeri aktarma
api_key = os.environ.get('binance_key')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)

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


# ne kadar zam yapıldığını yüzdelik olarak hesaplama
# def percent_count(x,y):
#     x = float(x)
#     y = float(y)
#     percent = (x-y)/x*100
#     return percent

# windows bildirim için
toaster = ToastNotifier()

print("Program başlatıldı...")

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
        if (y-x)/x*100 >= 5:
            for e in tokens:
                if endeks==tokens.index(e):
                    toaster.show_toast("Bilgilendirme",f"{e} tokenini {y} fıyatdan satın alabiliriniz!!!", threaded=True, icon_path=None, duration=5)
                    toaster.notification_active()
                    print(f"{e} tokenini {y} fıyatdan satın alabiliriniz!!!")
                    with open("Hype_tokens.txt","a") as f:
                        f.write(f"{e} tokenini {y} fıyatdan satın alabiliriniz!!!"+" Tarih: ")
                        f.write("-"*30+">>"+time.strftime('%c')+"\n")
        else:
            continue

    print("15 dakika oldu!")



