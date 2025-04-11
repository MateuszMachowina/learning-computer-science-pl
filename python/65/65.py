liczniki = []
mianowniki = []
with open("dane_ulamki.txt") as plik:
    for linia in plik:
        licz , mianow = linia.split()
        liczniki.append(int(licz))
        mianowniki.append(int(mianow))

def nwd(a,b):
    while a !=b:
        if a > b:
            a=a-b
        if b > a:
            b=b-a
    return a


#zad.1 czegos tu brakuje
min=12000
mianownik_min=99999
licznik_min=0
for i in range(1000):
    if liczniki[i]/mianowniki[i] < min:
        min=liczniki[i]/mianowniki[i]
        mianownik_min=mianowniki[i]
        licznik_min=liczniki[i]
print(f"zad.1\n{licznik_min}, {mianownik_min}")

#zad.2
nieskracalne=0
for i in range(1000):
    a = liczniki[i]
    b = mianowniki[i]
    ilosc=0
    while a%nwd(a,b)==0 and nwd(a,b) >1:
        a//=nwd(a,b)
        ilosc+=1
    if ilosc == 0:
        nieskracalne+=1
print(f"zad.2\n{nieskracalne}")

#zad.3 czegos zabraklo
suma=0
for i in range(1000):
    a = liczniki[i]
    b = mianowniki[i]
    suma+=a//nwd(a,b)
print(f"zad.3\n{suma}")

#zad.4
suma_ulamkow=0
suma_licznikow=0
potezny_mianownik=2*2*3*3*5*5*7*7*13
for i in range(1000):
    a = liczniki[i]
    b = mianowniki[i]
    b*=potezny_mianownik/mianowniki[i]
    a*=potezny_mianownik/mianowniki[i]
    suma_ulamkow+=a/b
    suma_licznikow+=a
print(f"suma ulamkow: {suma_ulamkow}, licznik tego ulamka {suma_licznikow}")
