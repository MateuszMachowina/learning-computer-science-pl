import math

def funkcja(x):
    return (x-2)*(x-5)

def bisekcja(lewo, prawo, dokladnosc):
   if funkcja(lewo)*funkcja(prawo) > 0:
        return "Funkcja nie ma miejsc zerowych w tym zakresie"
   while abs(lewo - prawo) > dokladnosc:
        x = (lewo + prawo)/2
        if funkcja(lewo)*funkcja(x) < 0:
            prawo=x
        else:
            lewo=x
        if abs(funkcja(x)) < dokladnosc:
            return x
print(bisekcja(2,6,0.001))

