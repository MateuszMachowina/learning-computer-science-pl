slowa = []
szyfry = []
bledy = []
with open("dane_6_3.txt") as plik:
    for linia in plik:
        a, b = linia.split()
        slowa.append(a)
        szyfry.append(b)
for x in range(len(slowa)):
    a=slowa[x]
    b=szyfry[x]
    k=ord(b[0])-ord(a[0])
    for i in range(len(a)):
        nk=ord(b[i])-ord(a[i])
        if nk != k and nk+26 !=k and nk-26 != k:
            bledy.append(slowa[x])
            break
print(bledy)

