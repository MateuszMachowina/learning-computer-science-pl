
liczby = []
with open("liczby.txt") as plik:
    for linia in plik:
        a=linia.strip()
        liczby.append(int(a))

#zad.1
    licznik_glowny = 0
    for liczba in liczby:
        if liczba % 2 == 0:
            continue
        licznik_wew= 0
        dzielnik = 3
        while dzielnik * dzielnik < liczba:
            if liczba % dzielnik == 0:
                licznik_wew+=1
            while liczba % dzielnik == 0:
                    liczba//=dzielnik
            dzielnik+=1
        if liczba > 1:  #bo liczba dzieli sie przez siebie jeszcze a dzielnik jest max. jej pierwiastkiem
            licznik_wew+=1
        if licznik_wew == 3:
            licznik_glowny+=1
    print(f"zad.1: {licznik_glowny}")

#zad.2
licznik=0
for liczba in liczby:
    liczba=str(liczba)
    sprawdz=0
    if len(liczba)%2 == 0:
        dlugosc = len(liczba)//2
    else:
        dlugosc = (len(liczba)//2) +1
    for i in range(dlugosc):
        if liczba[i] == liczba[-i]:
            sprawdz=+1
    if len(liczba)%2 == 0:
       if sprawdz == dlugosc:
           licznik+=1
    else:
        if sprawdz == dlugosc-1:
            licznik+=1
print(f"zad.2: {licznik}")

#zad.3
def iloczyn(n):
    wynik=1
    for i in range(len(n)):
        wynik*=int(n[i])
    return wynik

def moc(n):
    x = iloczyn(n)
    p = 1
    while x > 9:
        x = iloczyn(str(x))
        p+=1
    return p

print("zad.3")
for i in range(1, 9):
    licznik = 0
    for liczba in liczby:
        liczba = str(liczba)
        if moc(liczba) == i:
            licznik+=1
    print(f"Moc: {i}  Ilosc: {licznik}")










