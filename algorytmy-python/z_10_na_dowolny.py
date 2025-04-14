def znaki(liczba):                      #dla systemow wiekszych od 10
    if liczba == '10':
        return 'A'
    if liczba == '11':
        return 'B'
    if liczba == '12':
        return 'C'
    if liczba == '13':
        return 'D'
    if liczba == '14':
        return 'E'
    if liczba == '15':
        return 'F'
    return liczba

def z_dzies(liczba, system):
    wynik=""
    while liczba > 0:                   #dzielimy dopóki liczba > 0
        znak=str(liczba%system)         #reszta z dzielenia
        wynik=znaki(znak) + wynik       #kazda nowa reszte z dzielenia dajemy na przod
        liczba//=system                 #dzielimy liczbe przez system, bez przecinka
    return wynik

print(z_dzies(5543,16))

