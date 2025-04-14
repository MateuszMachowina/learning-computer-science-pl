def na10(a):
    x = 2**(len(a)-1)
    wynik = 0
    for i in range(len(a)):
        znak = int(a[i])
        wynik += znak*x
        x //= 2
    return wynik

print(na10("01110000000"))
