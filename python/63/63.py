ciagi = []
with open("ciagi.txt") as plik:
    for linia in plik:
        a = linia.strip()
        ciagi.append(a)

#1
print("zad.1")
for i in range(1000):
    wyraz = ciagi[i]
    dl = (len(wyraz)//2)
    w1 = wyraz[:dl]
    w2 = wyraz[dl:]
    if w1 == w2:
        print(wyraz)

#2
print("zad.2")
licznik = 0
for i in range(1000):
    wyraz = ciagi[i]
    stan = 0
    for j in range(len(wyraz)-1):
        if wyraz[j] == '1' and wyraz[j+1] == '1':
            stan = 1
            break
    if stan == 0:
        licznik += 1
print(licznik)

#3
print("zad.3")

def na10(a):
    x = 2**(len(a)-1)
    wynik = 0
    for i in range(len(a)):
        znak = int(a[i])
        wynik += znak*x
        x //= 2
    return wynik

def pp(a):
    dzielnik = 2
    ile = 0
    while dzielnik < a:
        temp = a
        while a % dzielnik == 0:
            a //= dzielnik
            ile += 1
        a = temp
        if ile > 2:
            return 0
        dzielnik += 1
    if ile == 2:
        return 1
    return 0

ile = 0
min = 1000
max = 0
for i in range(1000):
   wyraz = ciagi[i]
   liczba = na10(wyraz)
   if pp(liczba) == 1:
       ile += 1
       if liczba > max:
           max = liczba
       if liczba < min:
           min = liczba
print(f"ilosc: {ile}, max: {max}, min: {min}")

#sito eratostanesa akurat sie tu nie przydalo ale warto je umiec
def eratostanes(max):
    sito = [True] *(max+1)
    pierwsze = []
    for i in range(2,max+1):
        if sito[i] == True:
            pierwsze.append(i)
            for j in range(i,max+1,i):
                sito[j] = False
    return pierwsze
