
def wybor(a):
    for i in range(len(a)):
        min=a[i]
        min_indeks=i
        for j in range(i+1, len(a)):            # wyszukuje najmniejsza wartosc od elementu pierwszego
            if a[j] < min:                      # i zamieniam go z pierwszym elementem
                min=a[j]
                min_indeks=j
        #print(f"{a} || a[i] = {a[i]}, a[min] = {a[min_indeks]}")
        a[i], a[min_indeks] = a[min_indeks], a[i]
    return a

a = [99,34,224,64,633,68,11,2,7,534,97,55]
print(wybor(a))
