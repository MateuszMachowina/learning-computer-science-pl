obrazy = []
pionowe = []
poziome = []
with open("dane_obrazki.txt") as plik:
    for wyraz in range(200):
        obraz = []
        pion=""
        for j in range(21):
            if j != 20:
                a=plik.readline()
                obraz.append(a[0:20])
                pion+=a[20]
            if j == 20:
                poziome.append(plik.readline().strip())
        obrazy.append(obraz)
        pionowe.append(pion)
        plik.readline()

#zad.1
ile_rewersow = 0
max=0
for obraz in obrazy:
    czarne = 0 #1 to czarny
    biale = 0
    for linia in obraz:
        for wyraz in linia:
            if wyraz== '1':
                czarne+=1
            if wyraz== '0':
                biale+=1
    if czarne > biale:
        ile_rewersow+=1
        if czarne > max:
            max=czarne
print(f"zad.1\nilosc: {ile_rewersow}, max: {max}")

#zad.2
print("zad.2")
licznik=0
zrobione = False
for obraz in obrazy:
    gorna = obraz[0:10] #dziele obraz na gore i dol
    dolna = obraz[10:20]
    cz1 = []
    cz2 = []
    for linia in gorna:
        cz1.append(linia[0:10]) #dodaje pierwsze 10 cyfer z linii
        cz2.append(linia[10:20])
    cz3 = []
    cz4 = []
    for linia in dolna:
        cz3.append(linia[0:10])
        cz4.append(linia[10:20])
    if cz1 == cz2 == cz3 == cz4:
        if zrobione != True:
            for linia in obraz:
                print(linia)
            zrobione=True
        licznik+=1
print(f"ilosc: {licznik}")

#zad.3 i zad.4

poprawne=0
naprawialne=0
nienaprawialne=0
max_bledow=0
nr_obrazu=0
zad4 = []
for obraz in obrazy:
    temp_linia = 0
    temp_rzad = 0
    temp_zbior = []
    dobre_rzedy=0
    dobre_linie=0
    bledy=0
    iteracja_pozioma=0
    for linia in obraz:
        suma_linia=0
        for x in range(len(linia)):
            suma_linia+=int(linia[x])
        if (suma_linia + int(pionowe[nr_obrazu][iteracja_pozioma]))%2==0:
            dobre_linie+=1
        else:
            bledy+=1
            temp_linia=iteracja_pozioma
        iteracja_pozioma+=1
    for rzad in range(20):
        suma_rzedu=0
        for linia in obraz:
            suma_rzedu+=int(linia[rzad])
        if (suma_rzedu + int(poziome[nr_obrazu][rzad]))%2==0:
            dobre_rzedy+=1
        else:
            bledy+=1
            temp_rzad=rzad
    if dobre_rzedy == 20 and dobre_linie == 20:
        poprawne+=1
    if dobre_rzedy >=19 and dobre_linie >=19 and dobre_linie+dobre_rzedy<40:
        naprawialne+=1
        if dobre_rzedy==19 and dobre_linie == 20:   #blad w bitach parzystosci poziomych
            temp_zbior.extend((nr_obrazu+1, 21, temp_rzad+1))
        else:
            temp_zbior.extend((nr_obrazu+1, temp_linia+1, temp_rzad+1))
        zad4.append(temp_zbior)
    if dobre_rzedy < 19 or dobre_linie < 19:
        nienaprawialne+=1
    if bledy > max_bledow:
        max_bledow=bledy
    nr_obrazu+=1

print(f"zad.3\npoprawne: {poprawne},\nnaprawialne: {naprawialne},")
print(f"nienaprawialne: {nienaprawialne}, \nmax bledow: {max_bledow}")
print(f"zad.4\nnr obrazow: {zad4}")
