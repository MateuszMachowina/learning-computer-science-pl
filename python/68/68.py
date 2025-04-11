a = []
b = []
with open("dane_napisy.txt") as plik:
    for linia in plik:
        x, y = linia.split()
        a.append(x)
        b.append(y)

def jednolity(a):
    zasada = a[0]
    for i in range(1,len(a)):
        if a[i] != zasada:
            return 0
    return 1

def czy_nalezy(a,x):
    for i in range(len(a)):
        if a[i] == x:
            return 1
    return 0

def zbior(a):
    lista=[]
    for i in range(len(a)):
        if czy_nalezy(lista, a[i]) == 0:
            lista.append(a[i])
    sort(lista)
    return lista

def sort(a):
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i+1] < a[i]:
                a[i+1], a[i] = a[i], a[i+1]
#zad.1
ilosc=0
for i in range(1000):
    if jednolity(a[i]) and zbior(a[i]) == zbior(b[i]) and len(a[i]) == len(b[i]):
        ilosc+=1
print(ilosc)

#zad.2
ilosc=0
for i in range(1000):
    if zbior(a[i]) == zbior(b[i]) and len(a[i]) == len(b[i]):
        ilosc+=1
print(ilosc)

#zad.3
c=[]
for i in range(1000):
    c.append(a[i])
    c.append(b[i])
max=0
for i in range(2000):
    ilosc=0
    for j in range(2000):
        if zbior(c[i]) == zbior(c[j]) and len(c[i]) == len(c[j]):
            ilosc+=1
        if ilosc > max:
            max=ilosc
print(max)


