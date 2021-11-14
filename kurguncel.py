import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import time
api_key = '4UDXO21HX6QAZ911'
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def oran_hesaplama(url,sayi1buyuk,sayi2buyuk):

    my_request = urllib.request.urlopen(url)
    my_HTML = my_request.read().decode("utf8")
    #HTML verisini parse etme
    soup = BeautifulSoup(my_HTML, 'html.parser')
    x = soup.get_text()
    old_string = x
    new_string = old_string.replace('{',' ')
    new_string1 = new_string.replace('}',' ')
    new_string2 = new_string1.replace('"',' ')
    new_string3 = new_string2.replace(',',' ')
    new_string4 = new_string3.split()
    Exchange1 =  new_string4.index("Exchange")
    Rate1 =  new_string4.index("Rate")
    del new_string4[Exchange1]
    From_Currency =  new_string4.index("From_Currency")
    To_Currency = new_string4.index("To_Currency")
    Parabirimi = new_string4.index("{para}".format(para = sayi1buyuk))
    Parabirimi1 = new_string4.index("{para}".format(para = sayi2buyuk))
    Replace_From_Currency = new_string4[From_Currency].replace("From_Currency","1. Para Birimi")
    Replace_To_Currency = new_string4[To_Currency].replace("To_Currency","2. Para Birimi")
    Exchange2 =  new_string4.index("Exchange")
    Rate2 =  new_string4.index("Rate")
    Oran = Exchange2 + 3 #para biriminin oldugu yer
    Degisim = new_string4[Exchange2].replace("Exchange","Oran")
    Oran1 = float(new_string4[Oran])
    return Oran1
currency1 = ["TRY","USD","EUR","GBP","JPY","DKK","RUB","BTC"]#sayi1
currency2 = ["TRY","USD","EUR","GBP","JPY","DKK","RUB"]



while True:
    print("""Parite Ogrenme => 1 \nAlim yapma => 2 \nSatim yapma => 3 """)
    mainquery = input("Hangi islemi yapmak istiyorsunuz ? ")
    if mainquery == "1":

        while True:
            cls()
            print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB\nBitcoin => BTC""")
            sayi1 = input('1. Para Birimini Giriniz :')
            sayi1buyuk = sayi1.upper()
            if sayi1buyuk in currency1:
                cls()    
                while True:
                    print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB""")
                    sayi2 = input('2. Para Birimini Giriniz :')
                    sayi2buyuk = sayi2.upper()
                    if sayi2buyuk in currency2:
                        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={sayi1}&to_currency={sayi2}&apikey={api_key}'.format(sayi1 = sayi1buyuk,sayi2 = sayi2buyuk,api_key = api_key)
                        x = oran_hesaplama(url,sayi1buyuk,sayi2buyuk)
                        cls()
                        print("1 " + str(sayi1buyuk) + " = " + str(float(f'{x:.3f}')) + sayi2buyuk)
                        
                        break    
                    else:
                        cls()
                        print("Lutfen 2. para birimini dogru girin")    
                        time.sleep(1)
                        cls()
                        continue
                break

            else:
                cls()
                print("Lutfen para birimini dogru girin")    
                time.sleep(1)
                cls()
                continue
        break                                   
    elif mainquery == "2":
        while True:
            cls()
            print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB\nBitcoin => BTC""")
            birim2 = input('Alinacak para birimini seciniz:')
            birim2buyuk = birim2.upper()
            if birim2buyuk in currency1:
                cls()    
                while True:
                    sayi2 = input('Alinacak ' + birim2buyuk +" miktarini giriniz:" )
                    if sayi2.isdigit():
                        sayi1buyuk = "TRY"
                        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={sayi1}&to_currency={sayi2}&apikey={api_key}'.format(sayi1 = birim2buyuk,sayi2 = sayi1buyuk,api_key = api_key)
                        x = oran_hesaplama(url,sayi1buyuk,birim2buyuk)
                        tldegeri = x*int(sayi2)
                        cls()
                        print(sayi2 + " " + str(birim2buyuk) + " almak icin gereken miktar " + str(float(f'{tldegeri:.3f}')) + " TL")
                        
                        break    
                    else:
                        cls()
                        print("Lutfen sayi girin")    
                        time.sleep(1)
                        cls()
                        continue
                break

            else:
                cls()
                print("Lutfen para birimini dogru girin")    
                time.sleep(1)
                cls()
                continue
        break
    elif mainquery == "3":
        while True:
            cls()
            print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB\nBitcoin => BTC""")
            birim2 = input('Satilacak para birimini seciniz:')
            birim2buyuk = birim2.upper()
            if birim2buyuk in currency1:
                cls()    
                while True:
                    sayi2 = input('Satilacak ' + birim2buyuk +" miktarini giriniz:" )
                    if sayi2.isdigit():
                        sayi1buyuk = "TRY"
                        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={sayi1}&to_currency={sayi2}&apikey={api_key}'.format(sayi1 = birim2buyuk,sayi2 = sayi1buyuk,api_key = api_key)
                        x = oran_hesaplama(url,sayi1buyuk,birim2buyuk)
                        tldegeri = x*int(sayi2)
                        cls()
                        print(sayi2 + " " + str(birim2buyuk) + " satinca eline gececek miktar " + str(float(f'{tldegeri:.3f}')) + " TL")
                        break    
                    else:
                        cls()
                        print("Lutfen sayi girin")    
                        time.sleep(1)
                        cls()
                        continue
                break
            else:
                cls()
                print("Lutfen para birimini dogru girin")    
                time.sleep(1)
                cls()
                continue    
    



        break        
    else:
        cls()
        print("lutfen gecerli islemi giriniz ")
        time.sleep(1)
        cls()
        continue
