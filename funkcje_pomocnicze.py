import Bledne_IP_Exception

def sprawdz_ip(ip):

    print(ip)
    licznik = 0
    pozycja = []
    slesz = -1
    while licznik < len(ip):
        if (ip[licznik] < "0" or ip[licznik] > "9") and ip[licznik] != "." and ip[licznik] != "/":
            print("p")
            raise Bledne_IP_Exception(ip);



        if ip[licznik] == ".":
            pozycja.append(licznik)
        if ip[licznik] == "/":
            slesz = licznik
        licznik += 1

    if(len(ip)==slesz):
        raise Bledne_IP_Exception()






    if len(pozycja) != 3 or slesz == -1:
        print("p")
        raise Bledne_IP_Exception(ip);


    licznik = 0
    oktety = []
    oktet=""
    for x in pozycja:
       tmp = x

       while licznik < x:
           oktet +=ip[licznik]
           licznik +=1
       if oktet[0] == "0":
           print("p")
           raise Bledne_IP_Exception(ip);

       oktet = int(oktet)
       oktety.append(oktet)
       oktet = ""
       licznik += 1

    while licznik < slesz:
        oktet +=ip[licznik]
        licznik +=1
    if oktet[0] =="0":
        print("p")
        raise Bledne_IP_Exception(ip);

    oktet = int(oktet)
    oktety.append(oktet)
    licznik +=1
    maska =""
    while licznik < len(ip):
        maska +=ip[licznik]
        licznik +=1
    if maska[0] == "0":
        print("p")
        raise Bledne_IP_Exception(ip);

    maska = int(maska)
    if maska <= 0 or maska >32:
        print("p")
        raise Bledne_IP_Exception(ip);


    for x in oktety:
        if x >255 or x < 1:
            print("p")
            raise Bledne_IP_Exception(ip);


    oktety.append(maska)
    return oktety

def oblicz_adres_sieci(ip,maska):
    licznik = 0
    adres_sieci = []

    while licznik <=31:

        if (ip[licznik]== 1) and (maska[licznik]==1):
            adres_sieci.append(1)
        else:
            adres_sieci.append(0)

        licznik +=1
    return adres_sieci

def zamiana_na_postac_binarna(liczba):
    liczba_binarna = []
    for x in liczba:
        licznik = 8
        while licznik >0 or  x > 0:
            cos = x%2
            liczba_binarna.append(cos)
            x /= 2
            x = int(x)
            licznik -=1


    nowa_lista = []
    licznik = 7
    licznik1 = 0
    licznik2 = 0
    zmienna = len(liczba_binarna)
    zmienna = zmienna -1

    if zmienna != 31:
        while zmienna >=licznik1:
            nowa_lista.append((liczba_binarna[zmienna]))
            zmienna -=1
    else:
        while licznik1 <len(liczba):

            while licznik >=licznik2:

                nowa_lista.append(liczba_binarna[licznik])
                licznik -=1
            licznik1 += 1
            licznik2 = 8*(licznik1)
            licznik = 8*(licznik1+1)-1


    return nowa_lista

def zmiana_formatu_maski(maska):
    postac_binarna_maski = []
    licznik = maska
    while licznik > 0:
        postac_binarna_maski.append(1)
        licznik -= 1

    licznik = 31 - maska
    while licznik >= 0:
        postac_binarna_maski.append(0)
        licznik -= 1
    return postac_binarna_maski

def zamiana_na_postac_dziesietna(liczba ):
    postac_dziesietna = []
    licznik = 0
    wartosc = 0

    for x in reversed(liczba):
        x = int(x)
        wartosc = wartosc + x*2**licznik

        if licznik%7 == 0 and licznik != 0:
            postac_dziesietna.append(wartosc)
            wartosc = 0
            licznik = 0
        else:
            licznik +=1

    return postac_dziesietna

def oblicz_adres_broadcast(ip,maska):
    licznik = 0
    adres_rozgloszeniowy = []
    while licznik <= 31:
        if maska[licznik] == 1:
            adres_rozgloszeniowy.append(ip[licznik])
        else:
            adres_rozgloszeniowy.append(1)
        licznik +=1
    return adres_rozgloszeniowy

def max_liczba_hostow(maska):
    max_hostow = 2**(32-maska) - 2
    return max_hostow

def oblicz_adres_pierwszego_hosta(adres_sieci_dziesietnie):

    adres_pierwszego_hosta_f = []
    for x in adres_sieci_dziesietnie:
        adres_pierwszego_hosta_f.append(x)
    if adres_pierwszego_hosta_f[0] != 255:
        adres_pierwszego_hosta_f[0] +=1
    else:
        adres_pierwszego_hosta_f = []

    return adres_pierwszego_hosta_f

def oblicz_adres_ostatniego_hosta(adres_rozgloszeniowy):
    adres_ostatniego_hosta_f = []
    for x in adres_rozgloszeniowy:
        adres_ostatniego_hosta_f.append(x)
    if adres_ostatniego_hosta_f[0] != 0:
        adres_ostatniego_hosta_f[0] -=1
    else:
        adres_ostatniego_hosta_f = []

    return adres_ostatniego_hosta_f


