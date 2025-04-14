def szybko(a, n):
    if n == 0:
        return 1
    if n%2 == 1:
        return a * szybko(a, n-1)   # np. 2^3 = 2 * 2^2
    else:
        wynik = szybko(a,n/2)
        return wynik * wynik        # np. 2^4 = 2^2 * 2^2

print(szybko(2,5))

#złożoność logarytmiczna
