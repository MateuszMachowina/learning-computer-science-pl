tablica = []
with open("przyklad.txt") as plik:
    for linia in plik:
        tablica.append(linia.split())

# 1
print("zad.1")  # mozna uzyc funkcji max(tablica), min(tablica)
max = 0
min = 255
for x in range(200):
    for y in range(320):
        a = int(tablica[x][y])
        if a > max:
            max = a
        if a < min:
            min = a
print(max, min)

# 2
print("zad.2")


def os_sym(a):
    for i in range(320):
        tyl = 319 - i
        if a[i] != a[tyl]:
            return 0
    return 1


ilosc = 0
for wiersz in tablica:
    if os_sym(wiersz) == 0:
        ilosc += 1
print(ilosc)

# 3
print("zad.3")
ilosc = 0
for x in range(200):
    for y in range(320):
        a = int(tablica[x][y])
        if x > 0:
            b = int(tablica[x - 1][y])
        else:
            b = int(tablica[x][y])
        if x < 199:
            c = int(tablica[x + 1][y])
        else:
            c = int(tablica[x][y])
        if y > 0:
            d = int(tablica[x][y - 1])
        else:
            d = int(tablica[x][y])
        if y < 319:
            e = int(tablica[x][y + 1])
        else:
            e = int(tablica[x][y])

        if abs(a - b) > 128 or abs(a - c) > 128 or abs(a - d) > 128 or abs(a - e) > 128:
            ilosc += 1
print(ilosc)

# 4
print("zad.4")
max = 0
for x in range(320):
    ilosc = 1
    for y in range(199):
        if tablica[y][x] == tablica[y + 1][x]:
            ilosc += 1
        if tablica[y][x] != tablica[y + 1][x]:
            if max < ilosc:
                max = ilosc
            ilosc = 1
print(max)
