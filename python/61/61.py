def arytm(ciag):
    r = ciag[1] - ciag[0]
    for i in range(len(ciag)-1):
        if ciag[i+1] - ciag[i] != r:
            return False
    return True

def roznica(ciag):
    r = ciag[1] - ciag[0]
    return r

def roznica3(ciag):
    if ciag[1]-ciag[0] == ciag[2]-ciag[1]:
        r=ciag[1]-ciag[0]
    if ciag[1]-ciag[0] != ciag[2]-ciag[1] and ciag[2]-ciag[1] != ciag[3]-ciag[2]:
        return ciag[1]
    if ciag[1]-ciag[0] != ciag[2]-ciag[1] and ciag[2]-ciag[1] == ciag[3]-ciag[2]:
        return ciag[0]

    for i in range(2,len(ciag)-1):
        if ciag[i]-ciag[i-1] != r:
            if ciag[i-1]-ciag[i-2] != r:
                return ciag[i-1]
            else:
                return ciag[i]

def szescian(liczba):
    i=1
    while i*i*i <= liczba:
        if i*i*i == liczba:
            return liczba
        i+=1

ciagi = []
with open("ciagi.txt") as file:
    while True:
        linia = file.readline()
        if not linia:
            break
        n = int(linia.strip())

        linia = file.readline()
        if not linia:
            break
        ciag = [int(x) for x in linia.split()]
        ciagi.append(ciag)

#zad.1
licznik=0
max=0
for ciag in ciagi:
    if arytm(ciag) == True:
        licznik+=1
        if roznica(ciag) > max:
            max=roznica(ciag)
print(f"zad.1\nilosc c.arytmetycznych: {licznik}, najw. roznica: {max}")

#zad.2
szesciany = []
for ciag in ciagi:
    for liczba in ciag:
        if szescian(liczba) == liczba:
            szesciany.append(liczba)
print(f"zad.2\n{szesciany}")

#zad.3
ciagi = []
with open("bledne.txt") as file:
    while True:
        linia = file.readline()
        if not linia:
            break
        n = int(linia.strip())

        linia = file.readline()
        if not linia:
            break
        ciag = [int(x) for x in linia.split()]
        ciagi.append(ciag)
print("zad.3")
for ciag in ciagi:
    print(roznica3(ciag))


