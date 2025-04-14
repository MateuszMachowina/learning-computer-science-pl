def prosta(x):
    return 2*x + 5

def polozenie(x,y):
    if prosta(x) == y:
        nalezy = 'tak'
    else:
        nalezy = 'nie'
    return nalezy

print(polozenie(2,9))
