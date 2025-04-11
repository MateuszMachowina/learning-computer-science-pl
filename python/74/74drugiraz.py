hasla = []
with open("hasla.txt") as plik:
    for linia in plik:
        a = linia.strip()
        hasla.append(a)

print("zad.1")
lz = 0
for i in range(200):
    haslo = hasla[i]
    dl = len(haslo)
    lw = 0
    for j in range(dl):
        znak = haslo[j]
        if znak >= "0" and znak <= "9":
            lw += 1
    if lw == dl:
        lz += 1
print(lz)

print("zad.2")
zad2 = []
for i in range(200):
    start = hasla[i]
    for j in range(i+1,200):
        if start == hasla[j] and start not in zad2:
            zad2.append(start)
for i in range(len(zad2)):
        for j in range(i,len(zad2)):
            if zad2[i] > zad2[j]:
                zad2[i], zad2[j] = zad2[j], zad2[i]
print(zad2)

print("zad.3")
def sort(a,b,c,d):
    zbior = [a,b,c,d]
    for i in range(4):
        for j in range(i,4):
            if zbior[i] > zbior[j]:
                zbior[i], zbior[j] = zbior[j], zbior[i]
    if zbior[1]-zbior[0]==1 and zbior[2]-zbior[1]==1 and zbior[3]-zbior[2]==1:
        return 1
    return 0
licznik = 0
for i in range(200):
    haslo = hasla[i]
    dl = len(haslo)
    for j in range(dl-3):
        a = ord(haslo[j])
        b = ord(haslo[j+1])
        c = ord(haslo[j+2])
        d = ord(haslo[j+3])
        if sort(a,b,c,d) == 1:
            licznik += 1
            break           #nie zapomnij o break bo niektore hasla moga miec kilka takuch elementow
print(licznik)              #a my mamy policzyc ile jest tych hasel a nie elementow

print("zad.4")
def warunki(a):
    numer = 0
    mala = 0
    duza = 0
    for i in range(len(a)):
        if numer == 0:
            if a[i] >= "0" and a[i] <= "9":
                numer = 1
        if mala == 0:
            if a[i] >= "a" and a[i] <= "z":
                mala = 1
        if duza == 0:
            if a[i] >= "A" and a[i] <= "Z":
                duza = 1
    if (mala+duza+numer) == 3:
        return 1
    return 0

licznik = 0
for i in range(200):
    haslo = hasla[i]
    if warunki(haslo) == 1:
        licznik += 1
print(licznik)

