def afiniczny(litera, A, B):
    litera = ord(litera) - 97
    litera*= A
    litera+= B
    if litera>25:
        litera= litera % 26
    return chr(litera+97)

with open("tekst.txt") as plik:
    for linia in plik:
        tekst = linia.split()

norm = []
szyfr = []
with open("probka.txt") as plik:
    for linia in plik:
        a,b = linia.split()
        norm.append(a)
        szyfr.append(b)

#1
print("zad.1")
for i in range(len(tekst)):
    wyraz = tekst[i]
    if wyraz[0] == "d" and wyraz[len(wyraz)-1] == "d":
        print(wyraz)

#2
print("zad.2")
for i in range(len(tekst)):
    wyraz = tekst[i]
    if len(wyraz) >= 10:
        zwrot=""
        for j in range(len(wyraz)):
            zwrot+=afiniczny(wyraz[j], 5, 2)
        print(zwrot)

#3
print("zad.3")
def szuk(norm, szyfr):
    for i in range(26):
        for j in range(26):
            wyraz = ""
            for k in range(len(norm)):
                wyraz+=afiniczny(norm[k],i,j)
            if wyraz == szyfr:
                return i,j

for i in range(5):
    print(f"[{i+1}] - szyfrujacy: {szuk(norm[i], szyfr[i])} - deszyfrujacy: {szuk(szyfr[i], norm[i])}")

