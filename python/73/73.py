with open("tekst.txt") as plik:
    tekst=plik.readline()
    tekst=tekst.split()
print(tekst)

#1
print("zad.1")
licznik = 0
for i in range(len(tekst)):
    wyraz = tekst[i]
    for j in range(len(wyraz)-1):
        a=wyraz[j]
        b=wyraz[j+1]
        if a == b:
            licznik+=1
            break
print(licznik)

#2
print("zad.2")
litery = [0] * 27
wszystko = 0
for i in range(len(tekst)):
    wyraz = tekst[i]
    for j in range(len(wyraz)):
        litery[ord(wyraz[j])-65]+=1
        wszystko+=1
for i in range(26):
    print(f"{chr(65+i)}: {litery[i]} ({round(litery[i]/wszystko*100,3)}%)")

#3
print("zad.3")
def samogloska(a):
    if a == "A" or a == "E" or a == "I" or a == "O" or a == "U" or a == "Y":
        return True
    return False

def dl(a):
    dlug = 0
    max = 0
    for i in range(len(a)):
        if samogloska(a[i]) == False:
            dlug += 1
            if dlug > max:
                max = dlug
        else:
            dlug = 0
    return max

max = 0
zmiany = 0
ilosc_max = 0
for i in range(len(tekst)):
    wyraz = tekst[i]
    dlugosc = dl(wyraz)
    if dlugosc == max:
        ilosc_max+= 1
    if dlugosc > max:
        max = dlugosc
        aktualny = wyraz
        ilosc_max = 1

print(f"max. dlugosc: {max}, ilosc takich: {ilosc_max}, {aktualny}")
