x = [1,3,4,5,6,10,12,15,17,20,25,27,30]

def binarne_iter(x, szuk):
    prawy = len(x)-1
    lewy = 0
    while lewy <= prawy:
        srodek = (lewy+prawy)//2
        if szuk == x[srodek]:
            return srodek
        if szuk > x[srodek]:
            lewy = srodek
        else:
            prawy = srodek


def binarne_rekur(lista, lewy, prawy, szukana):
    srodek = (lewy + prawy)//2
    if lewy <= prawy:
        if szukana > lista[srodek]:
            return binarne_rekur(lista, srodek-1, prawy, szukana)
        if szukana < lista[srodek]:
            return binarne_rekur(lista, lewy, srodek+1, szukana)
        else:
            return srodek

print(binarne_rekur(x, 0, len(x), 15))
print(binarne_iter(x, 15))
