slowa = []
klucz = []
with open("szyfr1.txt") as plik:
    for i in range(6):
        slowa.append(plik.readline().strip())
    klucz = plik.readline().split()

#1
print("zad.1")

def szyfr(a,k):
    nowy = []
    zwrot = ""
    for i in range(len(a)):
        nowy.append(a[i])
    for i in range(len(a)):
        s = int(k[i])
        nowy[i], nowy[s-1] = nowy[s-1], nowy[i]
    for i in range(len(nowy)):
        zwrot+=nowy[i]
    return zwrot

for i in range(6):
    print(szyfr(slowa[i], klucz))

#2
print("zad.2")
klucz = []
with open("szyfr2.txt") as plik:
    slowo = plik.readline().strip()
    klucz = plik.readline().split()

l = 0
while l < 10:
    for i in range(len(klucz)):
        klucz.append(klucz[i])
    l+=1

print(szyfr(slowo, klucz))

#3
print("zad.3")
klucz = [6, 2, 4, 1, 5, 3]
l = 0
while l < 11:
    for i in range(len(klucz)):
        klucz.append(klucz[i])
    l+=1
with open("szyfr3.txt") as plik:
    slowo = plik.readline().strip()

def deszyfr(a,k):
    nowy = []
    zwrot = ""
    for i in range(len(a)):
        nowy.append(a[i])
    for i in range(49,-1,-1):
        s = int(k[i])
        nowy[i], nowy[s-1] = nowy[s-1], nowy[i]
    for i in range(len(nowy)):
        zwrot+=nowy[i]
    return zwrot

print(deszyfr(slowo, klucz))
