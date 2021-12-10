import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import time

#Degiskenler 
api_key = '4UDXO21HX6QAZ911'
sayilar = ["1","2","3"]
currency1 = ["TRY","USD","EUR","GBP","JPY","DKK","RUB","BTC"]
currency2 = ["TRY","USD","EUR","GBP","JPY","DKK","RUB"]


#Ekrani temizler 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def oran_hesaplama(url):
    my_request = urllib.request.urlopen(url)
    my_HTML = my_request.read().decode("utf8")
    soup = BeautifulSoup(my_HTML, 'html.parser')
    x = soup.get_text()
    new_string = x.replace('"',' ')
    new_string1 = new_string.split()
    if "Exchange" in new_string1:
        Exchange1 =  new_string1.index("Exchange")
        del new_string1[Exchange1]
        Exchange2 =  new_string1.index("Exchange")
        Oran = new_string1[Exchange2+3]
        return Oran
    else:
        return 0
 
def islem_sorgu():
    while True:
        print("""Parite Ogrenme => 1 \nAlim yapma => 2 \nSatim yapma => 3 """)
        mainquery = input("Hangi islemi yapmak istiyorsunuz ? ")
        if mainquery in sayilar:
            return int(mainquery)
            cls()
            break
        else:
            cls()
            print("Girdiginiz deger yanlis !!")
            time.sleep(2)
            cls()
            continue
     
def parite_ogrenme1():
    while True:
        cls()
        print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB\nBitcoin => BTC""")
        sayi1 = input('1. Para Birimini Giriniz :')
        if sayi1.upper() in currency2:
            cls()
            return sayi1.upper()
            break
        else:
            cls()
            print("Girdiginiz deger yanlis !!")
            time.sleep(2)
            cls()
            continue
 
def parite_ogrenme2():
    while True:
        cls()
        print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB""")
        sayi2 = input('2. Para Birimini Giriniz :')
        if sayi2.upper() in currency2:
            cls()
            return sayi2.upper()
            break
        else:
            cls()
            print("Girdiginiz deger yanlis !!")
            time.sleep(2)
            cls()
            continue

def alim_1():    
    while True:
        print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB\nBitcoin => BTC""")
        birim2 = input('Alinacak para birimini seciniz:')
        if birim2.upper() in currency1:
            return birim2.upper()
            cls()
            break
        else:
            cls()
            print("Girdiginiz deger yanlis !!")
            time.sleep(2)
            cls()
            continue

def alim_2():
    while True:
        cls()
        sayi2 = input('Alinacak ' + str(alim_1) +" miktarini giriniz:" )
        if sayi2.isdigit():
            return sayi2
        else:
            print("Girdiginiz deger yanlis !!")
            time.sleep(2)
            cls()
            continue

def satim1():
    while True:
        cls()
        print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB\nBitcoin => BTC""")
        birim1=input("Satilacak para birimini secin :")
        if birim1.upper() in currency1:
            return birim1.upper()
            cls()
            break
        else:
            cls()
            print("Girdiginiz deger yanlis !!")
            time.sleep(2)
            continue

def satim2():
    while True:
        cls()
        Miktar = input('Satilacak ' + str(satim_1) +" miktarini giriniz:")
        if Miktar.isdigit():
            return Miktar
            break
        else:
            cls()
            print("Girdiginiz deger yanlis !!")
            time.sleep(2)
            cls()
            continue

cls()
islem_sorgu_sonuc = islem_sorgu()
 
if islem_sorgu_sonuc == 1:
    cls()
    para_birimi_1 = parite_ogrenme1()
    para_birimi_2 = parite_ogrenme2()
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={sayi1}&to_currency={sayi2}&apikey={api_key}'.format(sayi1 = para_birimi_1,sayi2 = para_birimi_2,api_key = api_key)
    islem_sorgu_sonuc_parite=oran_hesaplama(url)
    print("Bir " + para_birimi_1 +" "+ islem_sorgu_sonuc_parite +" "+ para_birimi_2) 

elif islem_sorgu_sonuc == 2:
    cls()
    alim_1 = alim_1()
    alim_2 = alim_2()
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={sayi1}&to_currency={sayi2}&apikey={api_key}'.format(sayi1 = str(alim_1).upper(),sayi2 = "TRY",api_key = api_key)
    islem_sorgu_sonuc_alim=oran_hesaplama(url)
    alim_oran =float(str(alim_2))*float(islem_sorgu_sonuc_alim)
    print(str(alim_2) + " Tane " + str(alim_1) + " Almak icin gereken miktar " + str(alim_oran) + " TRY")

elif islem_sorgu_sonuc == 3:
    cls()
    satim_1 = satim1()
    satim_2 = satim2()
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={sayi1}&to_currency={sayi2}&apikey={api_key}'.format(sayi1 = satim_1.upper(),sayi2 = "TRY",api_key = api_key)
    islem_sorgu_sonuc_satim = oran_hesaplama(url)
    satim_Oran = float(islem_sorgu_sonuc_satim)*float(satim_2)
    print("1 " + satim_1 + " Satinca eline gececek para " + str(satim_Oran) + " TRY")
