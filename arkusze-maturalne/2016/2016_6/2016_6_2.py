slowa = []
klucze = []
with open("dane_6_2.txt") as plik:
    for linia in plik:
        a, b = linia.split()
        b=int(b)
        if b > 26:
            b=b%26
        slowa.append(a)
        klucze.append(b)

for x in range(len(slowa)):
    a=slowa[x]
    k=klucze[x]
    for i in range(len(a)):
        t=ord(a[i]) - k
        if t < 65:
            t+=26
        print(chr(t), end="")
    print() 
