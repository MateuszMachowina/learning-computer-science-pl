osobniki = []
with open("dane_geny.txt") as plik:
    for linia in plik:
        a = linia.strip()
        osobniki.append(a)

#1
print("zad.1")
gatunki = []
max = 0
for i in range(1000):
    dl = len(osobniki[i])
    if dl not in gatunki:
        gatunki.append(dl)
    licznik = 0
    for j in range(1000):
        if len(osobniki[j]) == dl:
            licznik+=1
    if licznik > max:
        max = licznik
print(len(gatunki), max)

#2
print("zad.2")
gutgeny = []
for i in range(1000):
    gutchlop = ""
    a = osobniki[i]
    stan = "stop"
    for j in range(len(a)-1):
        reszta = a[j+1:len(a)]
        if a[j] == "A" and a[j+1] == "A":
            stan = "start"
        if a[j] == "B" and a[j+1] == "B" and stan == "start":
            gutchlop+=a[j]
            gutchlop+=a[j+1]
            stan = "stop"
        if stan == "start" and "BB" in reszta:
            gutchlop+= a[j]
    gutgeny.append(gutchlop)
licznik = 0
for i in range(1000):
    a = gutgeny[i]
    for j in range(len(a)-5):
        if "BCDDC" in a:
            licznik+=1
            break
print(licznik)

#3
print("zad.3")
max_dl = 0
max_gen = 0
for i in range(1000):
    ile_genow = 0
    a = osobniki[i]
    stan = "stop"
    dl = 0
    for j in range(len(a)-1):
        if a[j] == "A" and a[j+1] == "A":
            stan = "start"
        if a[j] == "B" and a[j+1] == "B" and stan == "start":
            stan = "stop"
            dl+=2
            ile_genow+=1
            if dl > max_dl:
                max_dl = dl
            dl = 0
        if stan == "start":
            dl+=1
    if ile_genow > max_gen:
        max_gen = ile_genow
print(max_gen, max_dl)

#4
print("zad.4")
def palindrom(a):
    for i in range(len(a)//2):
        if a[i] != a[len(a)-i-1]:
            return 0
    return 1

guttyl = []
for i in range(1000):
    gutchlop = ""
    a = osobniki[i][::-1]           #odwrocony bedzie dzieki temu [::-1]
    stan = "stop"
    for j in range(len(a)-1):
        reszta = a[j+1:len(a)]
        if a[j] == "A" and a[j+1] == "A":
            stan = "start"
        if a[j] == "B" and a[j+1] == "B" and stan == "start":
            gutchlop+=a[j]
            gutchlop+=a[j+1]
            stan = "stop"
        if stan == "start" and "BB" in reszta:
            gutchlop+= a[j]
    guttyl.append(gutchlop)

#odporne
odporne = 0
for i in range(len(guttyl)):
    a = guttyl[i]
    if a == gutgeny[i]:
        odporne+=1

#silnie_odporne
silnie_odporne = 0
for i in range(len(osobniki)):
    a = osobniki[i]
    if palindrom(a) == 1:
        silnie_odporne+=1

print(odporne, silnie_odporne)




