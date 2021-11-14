import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import time 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

api_key = '4UDXO21HX6QAZ911'

while True:
	print("""Parite Ogrenme => 1 \n Alim yapma => 2 \n Satim yapma => 3 """)
	mainquery = input("Hangi islemi yapmak istiyorsunuz ? ")
 
	if mainquery == "1" :
		cls()
		print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB\nBitcoin => BTC""")
		while True:
			currency =  ["TRY","USD","EUR","GBP","JPY","DKK","RUB","BTC"]#sayi1
			currency1 = ["TRY","USD","EUR","GBP","JPY","DKK","RUB"]#sayi2
			sayi1 = input('1. Para Birimini Giriniz :')
			sayi1buyuk = sayi1.upper()
	
			if sayi1buyuk in currency:
				cls()
				print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB""")
				while True:
					sayi2 = input('2. Para Birimini Giriniz :')
					sayi2buyuk = sayi2.upper()
					if sayi2buyuk in currency1:				
				
						#HTML'den veriyi alma  
						url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={sayi1}&to_currency={sayi2}&apikey={api_key}'.format(sayi1 = sayi1.upper(),sayi2 = sayi2.upper() ,api_key = api_key)
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
						Oran = Exchange2 + 3 
						Degisim = new_string4[Exchange2].replace("Exchange","Oran")
						Oran1 = float(new_string4[Oran])
						#Ekrana yazidirma
						time.sleep(2)
						cls()
						print(Replace_From_Currency,":",new_string4[Parabirimi])
						print(Replace_To_Currency,":",new_string4[Parabirimi1])
						#print(Degisim,":",new_string4[Oran])
						print("1 "+sayi1buyuk + " = " + str(Oran1) + " " + sayi2buyuk)
						break				
					else:
						cls()
						print("Lutfen 2. para birimini dogru girin. ")
						time.sleep(1)
						cls()
						print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB""")
						continue		
				break
			else :
				cls()
				print("Lutfen 1. para birimini dogru girin. ")
				time.sleep(1)
				cls()
				print("""Tl => TRY\nDolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB""")
				continue
	elif mainquery == "2" :
		cls()
		while True:
			currency1 = ["USD","EUR","GBP","JPY","DKK","RUB"]
			print("""Dolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB""")
			alimsecim = input("Alim yapilacak para birimini secin: ")
			alimsecimbuyuk = alimsecim.upper()
			if alimsecimbuyuk in currency1:
				while True:
					cls()
					miktarsecim = input("Alinacak " + alimsecimbuyuk + " miktarini girin: ")
					if miktarsecim.isdigit():
						url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=TRY&to_currency={sayi1}&apikey={api_key}'.format(sayi1 = alimsecimbuyuk ,api_key = api_key)
						my_request = urllib.request.urlopen(url)
						my_HTML = my_request.read().decode("utf8")
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
						Parabirimi1 = new_string4.index("{para}".format(para = alimsecimbuyuk))
						Replace_From_Currency = new_string4[From_Currency].replace("From_Currency","1. Para Birimi")
						Replace_To_Currency = new_string4[To_Currency].replace("To_Currency","2. Para Birimi")
						Exchange2 =  new_string4.index("Exchange")
						Rate2 =  new_string4.index("Rate")
						Oran = Exchange2 + 3 
						Degisim = new_string4[Exchange2].replace("Exchange","Oran")
						Oran1 = float(new_string4[Oran])
						#Ekrana yazidirma
						time.sleep(2)
						cls()
						kesirlisayi = int(miktarsecim)/Oran1
						print(miktarsecim + " " + alimsecimbuyuk + " almak icin gereken para " + str(float(f'{kesirlisayi:.3f}')) + " TL")
						break				
					else:
						cls()
						print("Lutfen sayi giriniz")
						time.sleep(1)
						cls()
						continue	
				break
			else:
				cls()
				print("Lutfen para birimini dogru girin: ")
				time.sleep(0.9)
				cls()
				continue
	elif mainquery == "3" :
		break
		cls()
		while True:
			currency1 = ["USD","EUR","GBP","JPY","DKK","RUB"]
			print("""Dolar => USD\nEuro => EUR\nPound => GBP\nJapon Yeni => JPY\nDanimarka Kronu => DKK\nRuble => RUB""")
			satimsecim = input("Satim yapilacak para miktarini girin: ")
			satimsecimbuyuk = satimsecim.upper()
			if satimsecimbuyuk in currency1:
				while True:
					cls()
					miktarsecim = input("Satilacak " + satimsecimbuyuk + " miktarini girin: ")
					if miktarsecim.isdigit():
						url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={sayi1}&to_currency=TRY&apikey={api_key}'.format(sayi1 = satimsecimbuyuk ,api_key = api_key)
						my_request = urllib.request.urlopen(url)
						my_HTML = my_request.read().decode("utf8")
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
						Parabirimi1 = new_string4.index("{para}".format(para = satimsecimbuyuk))
						Replace_From_Currency = new_string4[From_Currency].replace("From_Currency","1. Para Birimi")
						Replace_To_Currency = new_string4[To_Currency].replace("To_Currency","2. Para Birimi")
						Exchange2 =  new_string4.index("Exchange")
						Rate2 =  new_string4.index("Rate")
						Oran = Exchange2 + 3 
						Degisim = new_string4[Exchange2].replace("Exchange","Oran")
						Oran1 = float(new_string4[Oran])
						#Ekrana yazidirma
						time.sleep(2)
						cls()
						kesirlisayi = int(miktarsecim)*Oran1
						print(miktarsecim + " " + satimsecimbuyuk + " satinca eline gececek para " + str(float(f'{kesirlisayi:.3f}')) + " TL")
						break				
					else:
						cls()
						print("Lutfen sayi giriniz")
						time.sleep(1)
						cls()
						continue	
				break
			else:
				cls()
				print("Lutfen para birimini dogru girin: ")
				time.sleep(0.9)
				cls()
				continue
		############
		break		
	else:
		cls()
		print("Lutfen dogru islem numarasini giriz")
		###########
		continue