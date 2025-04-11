liczby1 = []
with open("liczby1.txt") as plik:
    for linia in plik:
        a = linia.strip()
        liczby1.append(a)


#def na_dzies(a):            #cos nie dziala
#    stp = len(a)-1
#    wynik=0
#    for i in range(stp):
#        wynik+=int(a[i])*(2**stp)
#        stp-=1
#    return wynik

def horner(wsp, stp, x):
    wartosc = int(wsp[0])
    i = 1
    while i <= stp:
        wartosc = x*wartosc + int(wsp[i])
        i+=1
    return wartosc

def z_dzies(liczba, system):
    wynik = ""
    while liczba > 0:
        znak = str(liczba%system)
        wynik = znak + wynik
        liczba //= system
    return int(wynik)

#1
print("zad.1")
min=999999999
max=0
for i in range(1000):
    liczba = horner(liczby1[i], len(liczby1[i]) - 1, 8)
    if liczba < min:
        min = liczba
    if liczba > max:
        max = liczba
print(f"max: {z_dzies(max,8)}, min: {z_dzies(min,8)}")

#2
print("zad.2")
liczby2 = []
liczby2str = []
with open("liczby2.txt") as plik:
    for linia in plik:
        a = linia.strip()
        liczby2.append(int(a))
        liczby2str.append(a)

licznik=0
start_max = 0
i = 0
max = 0
while i < 998:
    if liczby2[i] > liczby2[i+1]:
        start = i+1
        licznik+=1
    if liczby2[i+1] <= liczby2[i+2]:
        licznik+=1
    if liczby2[i+1] > liczby2[i+2]:
        if licznik > max:
            max = licznik
            start_max = liczby2[start]
        licznik = 0
    i+=1
print(max, start_max)

#3
print("zad.3")
ile_rown = 0
ile_wieksz = 0
for i in range(1000):
    a = horner(liczby1[i], len(liczby1[i]) - 1, 8)
    if a == liczby2[i]:
        ile_rown += 1
    if a > liczby2[i]:
        ile_wieksz += 1
print(ile_rown, ile_wieksz)

#4
print("zad.4")
ile_w8 = 0
ile_w10 = 0
for i in range(1000):
    w8 = str(z_dzies(liczby2[i],8))
    w10 = str(liczby2[i])
    for j in range(len(w8)):
        if w8[j] == "6":
            ile_w8 += 1
    for j in range(len(w10)):
        if w10[j] == "6":
            ile_w10 += 1
print(ile_w8, ile_w10)
