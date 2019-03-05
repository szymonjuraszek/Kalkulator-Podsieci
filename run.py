import json
import funkcje_pomocnicze
import Bledne_IP_Exception
import socket
import sys




try:
    ip_i_maska=funkcje_pomocnicze.sprawdz_ip(sys.argv[1])

except IndexError:
    print("Pobieram adres komputera")

    zastepcze = socket.gethostbyname(socket.gethostname()) + "/16"



    ip_i_maska=funkcje_pomocnicze.sprawdz_ip(zastepcze)
except TypeError:
    print("Podano bledne IP!!!!!")
    exit(0);



ip = []
ip.append(ip_i_maska[0])
ip.append(ip_i_maska[1])
ip.append(ip_i_maska[2])
ip.append(ip_i_maska[3])
postac_binarna_ip = funkcje_pomocnicze.zamiana_na_postac_binarna(ip)

maska = ip_i_maska[4]
postac_binarna_maski = funkcje_pomocnicze.zmiana_formatu_maski(maska)
del ip_i_maska


print("IP:")
a=""
for x in postac_binarna_ip:
    x = str(x)
    a = a+x
    print(x,end="")

print("")
b =""
print("Maska")
for x in postac_binarna_maski:
    x = str(x)
    b = b + x
    print(x,end="")
print("")
c = ""
print("Adres sieci")
adres_sieci = funkcje_pomocnicze.oblicz_adres_sieci(postac_binarna_ip,postac_binarna_maski)
for x in adres_sieci:
    x = str(x)
    c = c + x
    print(x, end="")

print("")
d = ""
print("Postac dziesietna maski:")
postac_dziesietna_maski = funkcje_pomocnicze.zamiana_na_postac_dziesietna(postac_binarna_maski)
for x in reversed(postac_dziesietna_maski):
    x = str(x)
    d = d+x
    print(x+".",end="")

print("")
e =""
adres_rozgloszeniowy_binarnie = funkcje_pomocnicze.oblicz_adres_broadcast(postac_binarna_ip,postac_binarna_maski)
print("Adres rozgloszeniowy binarnie:")
for x in adres_rozgloszeniowy_binarnie:
    x = str(x)
    e = e + x
    print(x,end="")

print("")
f =""
print("Adres rozgloszenowy dziesietnie")
adres_rozgloszeniowy_dziesietnie = funkcje_pomocnicze.zamiana_na_postac_dziesietna(adres_rozgloszeniowy_binarnie)
for x in reversed(adres_rozgloszeniowy_dziesietnie):
    x = str(x)
    f= f+x
    print(x+".",end="")

print("")
g=""
max_liczba_hostow_dziesietnie = []
print("Maksymalna liczba hostow dziesietnie:")
max_liczba_hostow_dziesietnie.append(funkcje_pomocnicze.max_liczba_hostow(maska))
for x in max_liczba_hostow_dziesietnie:
    x = str(x)
    g = g + x
    print(x,end="")

print("")
h=""
max_liczba_hostow_binarnie = []
print("maksymalna liczba hostow binarnie:")
max_liczba_hostow_binarnie=funkcje_pomocnicze.zamiana_na_postac_binarna(max_liczba_hostow_dziesietnie)
for x in max_liczba_hostow_binarnie:
    x = str(x)
    h= h + x
    print(x,end="")

adres_sieci_dziesietnie = []
print("")
adres_sieci_dziesietnie = funkcje_pomocnicze.zamiana_na_postac_dziesietna(adres_sieci)

adres_pierwszego_hosta_dziesietnie = []
i=""
print("Adres pierwszego hosta dziesietnie:")
adres_pierwszego_hosta_dziesietnie = funkcje_pomocnicze.oblicz_adres_pierwszego_hosta(adres_sieci_dziesietnie)
for x in reversed(adres_pierwszego_hosta_dziesietnie):
    x = str(x)
    i=i+x
    print(x+".",end="")
cos = []
for x in reversed(adres_pierwszego_hosta_dziesietnie):
    cos.append(x)

print("")
j=""
print("Adres pierwszego hosta binarnie:")
adres_pierwszego_hosta_binarnie = funkcje_pomocnicze.zamiana_na_postac_binarna(cos)
for x in adres_pierwszego_hosta_binarnie:
    x = str(x)
    j = j + x
    print(x,end="")

print("")
adres_ostatniego_hosta_dziesietnie = []
print("Adres ostatniego hosta dziesietnie:")
adres_ostatniego_hosta_dziesietnie = funkcje_pomocnicze.oblicz_adres_ostatniego_hosta(adres_rozgloszeniowy_dziesietnie)
k = ""
for x in reversed(adres_ostatniego_hosta_dziesietnie):
    x = str(x)
    k = k + x
    print(x+".",end="")
obrocona_lisa = []
for x in reversed(adres_ostatniego_hosta_dziesietnie):
    obrocona_lisa.append(x)

print("")
adres_ostatniego_hosta_binarnie = []
print("Adres ostatniego hosta binarie:")
adres_ostatniego_hosta_binarnie = funkcje_pomocnicze.zamiana_na_postac_binarna(obrocona_lisa)
l = ""
for x in adres_ostatniego_hosta_binarnie:
    x = str(x)
    l = l+x
    print(x,end="")

print("")
print("Zapisywanie do pliku JSON:")
date = {}
date["adres_ostatniego_hosta_binarnie"] = k
date["adres_ostatniego_hosta_dziesietnie"] = l
date["ip_binarnie"]=a
date["maska_binarnie"]=b
date["adres_sieci_binarnie"]=c
date["maska_dziesietnie"]=d
date["adres_rozgloszeniowy_binarnie"]=e
date["adres_ozgloszeniowy_dziesietnie"]=f
date["max_liczba_hostow_dziesietnie"]=g
date["max_liczba_hostow_binarnie"]=h
date["adres_pierwszego_hosta_dziesietnie"]=i
date["adres_pierwszego_hosta_binarnie"]=j
file = open("dane.JSON","w")
json.dump(date,file,ensure_ascii=False)
file.close()