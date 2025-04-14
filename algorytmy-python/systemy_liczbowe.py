def zamiana_z_10(a,n):
    wynik=""
    while a > 0:
        wynik=str(a%n)+wynik
        a//=n
    return wynik
    # + warunki dla wiekszych systemow od 10 (czyli A = 10, B = 11, ...)
print(zamiana_z_10(10, 2))

def rekur_horner(x, wsp, stp):        # x - system, wsp - wspolczynniki jako lista, stp - len(lista)-1
    if stp == 0:                      # na 10 z dowolnego
        return wsp[0]
    else:
        return x*(rekur_horner(x,wsp,stp-1)) + wsp[stp]

wsp = [1,0,1,0]
print(rekur_horner(2,wsp,len(wsp)-1))

def iter_horner(wsp, x):        # x - system, wsp - wspolczynniki jako string
    wynik = 0                   # na 10 z dowolnego
    for c in wsp:
        wynik *= x
        wynik += int(c)
    return wynik
print(iter_horner("1010",2))
