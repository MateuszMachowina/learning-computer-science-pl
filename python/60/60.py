def nwd(a,b):
    while a!=b:
        if a > b:
            a = a-b
        if b > a:
            b = b - a
    return a

liczby = []
with open("liczby.txt") as plik:
    for linia in plik:
        liczba = linia.strip()
        liczby.append(int(liczba))

#zad.1
licznik = 0
ost = 0
przedost = 0
for liczba in liczby:
    if liczba < 1000:
        licznik+=1
        przedost = ost
        ost = liczba
print(f"zad.1\nilosc: {licznik}, ostatnia: {ost}, przedostatnia: {przedost}")

#zad.2
print("zad.2")
for liczba in liczby:
    lista = []
    for dzielnik in range(1, liczba+1):
        if liczba%dzielnik == 0:
           lista.append(dzielnik)
        dzielnik+=1
    if len(lista) == 18:
        print(f"liczba: {liczba}, dzielniki: {lista}")

#zad.3
print("zad.3")
najw=0
for liczba in liczby:
    licznik=0
    for i in liczby:
        if nwd(liczba,i) == 1:
            licznik+=1
    if licznik == len(liczby)-1 and liczba > najw:
        najw=liczba
print(najw)

