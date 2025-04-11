lista = []
with open("liczby.txt") as plik:
    for linia in plik:
        a = linia.strip()
        lista.append(a)
# 1
ilosc_liczb = 0
for i in range(len(lista)):
    ilosc1 = 0
    ilosc0 = 0
    for j in range(len(lista[i])):
        if lista[i][j] == '0':
            ilosc0 += 1
        elif lista[i][j] == '1':
            ilosc1 += 1
    if ilosc0 > ilosc1:
        ilosc_liczb += 1
print(f"zad.1: \n{ilosc_liczb}")

# 2
ilosc2 = 0
ilosc8 = 0
for i in range(len(lista)):
    n = len(lista[i])
    if lista[i][n - 1] == '0':
        ilosc2 += 1
    if lista[i][n - 1] == '0' and lista[i][n - 2] == '0' and lista[i][n - 3] == '0':
        ilosc8 += 1
print(f"zad.2: \npodzielne przez 2: {ilosc2} \npodzielne przez 8: {ilosc8}")

# 3
max_dl = 0
max_str = "0"
min_dl = 99
min_str = "11111111111111111111111111111111111111111111111111111111111111111111111111111"
for i in range(len(lista)):
    if len(lista[i]) > max_dl:
        max_dl = len(lista[i])
        max_str = lista[i]
        max_id = i
    if len(lista[i]) < min_dl:
        min_dl = len(lista[i])
        min_str = lista[i]
        min_id = i
    if len(lista[i]) == len(max_str):
        for x in range(len(lista[i])):
            wiekszy = 0
            if lista[i][x] == '1' and max_str[x] == '0':
                wiekszy = 1
                break
            if lista[i][x] == '0' and max_str[x] == '1':
                break
        if wiekszy == 1:
            max_id = i
            max_str = lista[i]
    if len(lista[i]) == len(min_str):
        mniejszy = 0
        for x in range(len(lista[i])):
            if lista[i][x] != min_str[x]:
                if lista[i][x] == '0' and min_str[x] == '1':
                    mniejszy = 1
                    break
                if lista[i][x] == '1' and min_str[x] == '0':
                    break
        if mniejszy == 1:
            min_id = i
            min_str = lista[i]
print(f"zad.3: \nmax: {max_id+1} \nmin: {min_id+1}")

