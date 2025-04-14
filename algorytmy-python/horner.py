wspolczynniki = [2,1,3]
stopien = len(wspolczynniki)-1
x=2


def horn_rekur(wsp, stp, x):
    if stp == 0:                                    # jezeli stopien = 0
        return wsp[0]                               # to zwraca pierwszy wspolczynnik
    return x*horn_rekur(wsp, stp-1, x) + wsp[stp]   # potem z kazdym krokiem mnozy x razy
                                                    # cała funkcje o stopniu mniejszym o 1, dodaje nastepny wspolczynnik
# np. mamy 2x^2 + x + 3
# czyli x(2x + 1) +3 ---> x*horn(wspolczynnik, stopien-1 ,x) + wsp[stp]
# tu jest dobrze wytłumaczone: https://eduinf.waw.pl/inf/alg/006_bin/0003.php


def horn_iter(wsp, stp, x):
    wartosc = wsp[0]
    i=1
    while i <= stp:
        wartosc = x*wartosc + wsp[i]
        i+=1
    return wartosc


print(horn_iter(wspolczynniki, stopien, x))
print(horn_rekur(wspolczynniki, stopien, x))
