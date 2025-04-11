tekst = ""
with open("dokad.txt") as plik:
    tekst = plik.readline().strip()
klucz = "LUBIMYCZYTAC"


def vigenere(a, k):
    odjac = 0
    nowy = ""
    for i in range(len(a)):
        x = i
        while x > 11:
            x-=12
        klucz = ord(k[x-odjac])-65
        if a[i] != " " and a[i] != "." and a[i] != ",":
            temp = ord(a[i])-65
            temp += klucz
            while temp > 25:
                temp-=26
            temp = chr(temp+65)
            nowy += temp
        else:
            nowy += a[i]
            odjac += 1
            while odjac > 11:
                odjac -= 12
    return nowy

#1
print("zad.1")
print(vigenere(tekst, klucz))
ilosc = 0
for i in range(len(tekst)):
    if tekst[i] != " " and tekst[i] != "." and tekst[i] != ",":
        ilosc += 1
print((ilosc//12)+1)

#2
print("zad.2")

def deszyfr(a, k):
    nowy = ""
    x=0
    for i in range(len(a)):
        while x > len(k)-1:
            x-=len(k)
        klucz = ord(k[x])-65
        if a[i] != " " and a[i] != "." and a[i] != ",":
            temp = ord(a[i])-65
            temp -= klucz
            while temp < 0:
                temp+=26
            temp = chr(temp+65)
            nowy += temp
            x+=1
        else:
            nowy += a[i]
    return nowy

a = []
with open("szyfr.txt") as plik:
    a = plik.readline().split()
    b = plik.readline().strip()
tekst = ""
for i in range(len(a)):
    tekst+=a[i]
    tekst+=" "
print(deszyfr(tekst,b))

#3
print("zad.3")
ilosc = [0 for i in range(50)]
#ilosc = [0] * 50
for i in range(len(tekst)):
    indeks = ord(tekst[i])-65
    if tekst[i] != " " and tekst[i] != "." and tekst[i] != ",":
        ilosc[indeks]+=1
ko = 0
all = 0
for i in range(26):
    print(chr(i+65), ilosc[i])
    ko += ilosc[i]*(ilosc[i]-1)
    all += ilosc[i]
ko /= all*(all-1)
d = round(0.0285 / (ko - 0.0385),2)
print(d,"|",len(b))
