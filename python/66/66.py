zbiory_t = []
zbiory_l = []
with open("trojki.txt") as plik:
    trzy_liczby=[]
    liczby_l=[]
    for linia in plik:
        a, b, c = linia.split()
        d, e, f = int(a), int(b), int(c)
        trzy_liczby=[a,b,c]
        liczby_l=[d,e,f]
        zbiory_t.append(trzy_liczby)
        zbiory_l.append(liczby_l)

def suma_cyfr(a):
    wynik=0
    for i in range(len(a)):
        wynik+=int(a[i])
    return wynik

def czy_1(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

def czy_trojkatp(lista):
    a,b,c = lista[0], lista[1], lista[2]
    if a*a + b*b == c*c:
        return True
    return False
def warunek_trojkata(lista):
    a,b,c = lista[0], lista[1], lista[2]
    if a + b > c and c>a and c>b:
        return True
    if b + c > a and a>b and a>c:
        return True
    if c + a > b and b>a and b>c:
        return True
    return False

#zad.1
print("zad.1")
for i in range(1000):
    suma= suma_cyfr(zbiory_t[i][0]) + suma_cyfr(zbiory_t[i][1])
    liczba3 = int(zbiory_t[i][2])
    if suma == liczba3:
        print(zbiory_l[i])

#zad.2
print("zad.2")
for i in range(1000):
    if czy_1(zbiory_l[i][0]) and czy_1(zbiory_l[i][1]) and zbiory_l[i][2] == zbiory_l[i][0]*zbiory_l[i][1]:
        print(zbiory_l[i])

#zad.3
print("zad.3")
for i in range(999):
    if czy_trojkatp(zbiory_l[i]) and czy_trojkatp(zbiory_l[i+1]):
        print(f"{zbiory_l[i]} i {zbiory_l[i+1]}")

#zad.4
print("zad.4")
licznik=0
seria=0
max=0
for i in range(1000):
    if warunek_trojkata(zbiory_l[i]):
        licznik+=1
        seria+=1
        if seria> max:
            max=seria
    else:
        seria=0
print(f"ilosc: {licznik}, max seria: {max}")
