hasla = []
with open("hasla.txt") as plik:
    for linia in plik:
        a = linia.strip()
        hasla.append(a)

#1
print("zad.1")
numbers = []
for i in range(10):
    numbers.append(48+i)

licznik = 0
for i in range(len(hasla)):
  wyraz = hasla[i]
  ok=1
  for j in range(len(wyraz)):
    znak = wyraz[j]
    if ord(znak) not in numbers:
        ok=0
        break
    else:
        ok=1
  if ok == 1:
    licznik+=1
print(licznik)

#2
print("zad.2")
zad2 = []
for i in range(len(hasla)):
    licznik = 0
    szukany = hasla[i]
    for j in range(len(hasla)):
        aktualny = hasla[j]
        if szukany == aktualny:
            licznik+=1
    if licznik > 1 and szukany not in zad2:
        zad2.append(szukany)
zad2.sort()
print(zad2)

#3
print("zad.3")

def kolejne(a,b,c,d):
    if a == b-1 and b == c-1 and c == d-1:
        return True
    return False

licznik = 0
for i in range(len(hasla)):
    wyraz = hasla[i]
    for j in range(len(wyraz)-3):
        a = ord(wyraz[j])
        b = ord(wyraz[j+1])
        c = ord(wyraz[j+2])
        d = ord(wyraz[j+3])
        x = [a,b,c,d]
        x.sort()
        if kolejne(x[0], x[1], x[2], x[3]):
            licznik+=1
            break
print(licznik)

#4
print("zad.4")
licznik = 0
for i in range(len(hasla)):
    wyraz = hasla[i]
    num = 0
    mala = 0
    duza = 0
    for j in range(len(wyraz)):
        znak = wyraz[j]
        if znak >= "0" and znak <= "9":
            num=1
        if znak >= "a" and znak <= "z":
            mala=1
        if znak >= "A" and znak <= "Z":
            duza=1
    if num == 1 and mala == 1 and duza == 1:
        licznik+=1
print(licznik)

