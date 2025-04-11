def wczytanie(tekst, system):
    godziny = []
    temperatury = []
    with open(tekst) as plik:
        for linia in plik:
            godz, temp = linia.split()
            godziny.append(int(godz, system))
            temperatury.append(int(temp, system))
    return godziny, temperatury

g1, t1 = wczytanie("dane_systemy1.txt", 2)
g2, t2 = wczytanie("dane_systemy2.txt", 4)
g3, t3 = wczytanie("dane_systemy3.txt", 8)

#zad1

min1 = min(t1)
min2 = min(t2)
min3 = min(t3)

print("Zad.1:")
print(f"Minimum w stacji S1: {format(min1, 'b')}")
print(f"Minimum w stacji S2: {format(min2, 'b')}")
print(f"Minimum w stacji S3: {format(min3, 'b')}")

#zad2

oczekiwana = 12
licznik = 0

for i in range(len(g1)):
    if oczekiwana != g1[i] and oczekiwana != g2[i] and oczekiwana != g3[i]:
        licznik+=1
    oczekiwana+=24
print("Zad.2:")
print(f"Zegar był niepoprawny {licznik} razy.")

#zad3

def liczenie(lista1, lista2, lista3):
    licznik = 1
    maks1= lista1[0]
    maks2= lista2[0]
    maks3= lista3[0]
    for i in range(len(lista1)):
        if lista1[i] > maks1 or lista2[i] > maks2 or lista3[i] > maks3:
            licznik+=1
            if lista1[i] > maks1:
                maks1 = lista1[i]
            if lista2[i] > maks2:
                maks2 = lista2[i]
            if lista3[i] > maks3:
                maks3 = lista3[i]
    return licznik
print("Zad.3:")
print(f"Dni rekordowe: {liczenie(t1, t2, t3)}")

#zad4

