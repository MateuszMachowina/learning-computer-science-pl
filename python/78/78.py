#1
print("zad.1")

def skrot1(wiad):
    algorytm = "ALGORYTM"
    S = []
    for i in range(len(algorytm)):
        S.append(ord(algorytm[i]))
    if len(wiad)%8 != 0:
        for i in range(8-len(wiad)%8):
            wiad+="."
    dl = len(wiad)
    il_partii = len(wiad)//8
    wynik = ""
    for i in range(il_partii):
        porcja = wiad[i*8:(i+1)*8]
        for j in range(8):
            S[j] = (S[j] + ord(porcja[j]))%128
    for i in range(8):
        wynik = wynik + chr(65 + (S[i])%26)
    return dl, S, wynik

wiad = "12345678abcdefgh"
for i in range(2):
    porcja = wiad[i*8:(i+1)*8]

with open("wiadomosci.txt") as plik:
    a = plik.readline()
print(skrot1(a))

#2
print("zad.2")
szyfry = []
with open("podpisy.txt") as plik:
    for linia in plik:
        a = linia.split()
        szyfry.append(a)

def A(d,n,y):
    x = (y*d)%n
    return chr(x)

zad2= []
for i in range(len(szyfry)):
    szyfr = szyfry[i]
    wynik = ""
    for j in range(len(szyfr)):
        a = int(szyfr[j])
        wynik += A(3,200,a)
    zad2.append(wynik)
print(zad2)

#3
print("zad.3")
def skrot(wiad):
    algorytm = "ALGORYTM"
    S = []
    for i in range(len(algorytm)):
        S.append(ord(algorytm[i]))
    if len(wiad)%8 != 0:
        for i in range(8-len(wiad)%8):
            wiad+="."
    dl = len(wiad)
    il_partii = len(wiad)//8
    wynik = ""
    for i in range(il_partii):
        porcja = wiad[i*8:(i+1)*8]
        for j in range(8):
            S[j] = (S[j] + ord(porcja[j]))%128
    for i in range(8):
        wynik = wynik + chr(65 + (S[i])%26)
    return wynik

swiad = []
with open("wiadomosci.txt") as plik:
    for linia in plik:
        a = linia.strip()
        swiad.append(skrot(a))

zad3 = []
for i in range(len(swiad)):
    if swiad[i] == zad2[i]:
        print(i+1, " ", swiad[i], " wiarygodna")
        zad3.append(i+1)
    else:
        print(i+1, " ", swiad[i], " zmieniona")
print(zad3)
