liczby = []
with open("liczby.txt") as plik:
    for linia in plik:
        a=linia.strip()
        liczby.append(int(a))
#1
print("4.1")
ilosc=0
for i in range(500):
    liczba = liczby[i]
    while liczba % 3 == 0:
        liczba/=3
        if liczba == 1:
            ilosc+=1
print(ilosc)

#2
def silnia(a):
    if a == 0:
        return 1
    if a > 0:
        return a*silnia(a-1)

print("4.2")
for i in range(500):
    wyraz=str(liczby[i])
    litery=[]
    moc=0
    for j in range(len(wyraz)):
        cyfra=int(wyraz[j])
        moc+=silnia(cyfra)
    if moc == liczby[i]:
        print(liczby[i])

#3
print("4.3")
def nwd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

max=0
liczby.append(1)
for i in range(500):
    x = nwd(liczby[i], liczby[i+1])
    for j in range(i+1, 500):
        if x > 1:
            temp = x
            x = nwd(x, liczby[j])
        else:
            a=j-1
            break
    dlugosc = a-i
    if dlugosc > max:
        max = dlugosc
        max_wartosc = liczby[i]
        max_nwd = temp
print(f"max: {max_wartosc}, dlugosc: {max}, nwd: {max_nwd}")



