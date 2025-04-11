wspol = []
with open("funkcja.txt") as plik:
    for linia in plik:
        a,b,c,d = linia.split()
        a,b,c,d = float(a), float(b), float(c), float(d)
        wspol.append([a,b,c,d])

def f(x):
    if x >= 0 and x < 1:
        wsp = wspol[0]
        wynik = wsp[0] + wsp[1]*x + wsp[2]*(x**2) + wsp[3]*(x**3)
    if x >= 1 and x < 2:
        wsp = wspol[1]
        wynik = wsp[0] + wsp[1]*x + wsp[2]*(x**2) + wsp[3]*(x**3)
    if x >= 2 and x < 3:
        wsp = wspol[2]
        wynik = wsp[0] + wsp[1]*x + wsp[2]*(x**2) + wsp[3]*(x**3)
    if x >= 3 and x < 4:
        wsp = wspol[3]
        wynik = wsp[0] + wsp[1]*x + wsp[2]*(x**2) + wsp[3]*(x**3)
    if x >= 4 and x < 5:
        wsp = wspol[4]
        wynik = wsp[0] + wsp[1]*x + wsp[2]*(x**2) + wsp[3]*(x**3)
    return round(wynik, 5)
#1
print("zad.1")
print(f(1.5))

#2
print("zad.2")
max = -990
i = 0
while(i < 5):
    if f(i) > max:
        max = f(i)
        x_max = i
    i+=0.001
print(f"x: {x_max}, y: {max}")

#3
print("zad.3")
# mzer = []
# i = 0
# while(i < 5):
#     if f(i) < 0.00001 and f(i) > -0.00001:
#         mzer.append(round(i,5))
#         i+=0.2
#     i+=0.000001
# print(mzer)

def bis(a,b):
    eps = 0.00001
    while b-a > eps:
        sr = (a+b)/2
        if f(sr)*f(a) > 0:
            a = sr
            sr = (a+b)/2
        else:
            b = sr
            sr = (a+b)/2
    return round(a, 5)

print(f"m.zer = [{bis(0,1)}, {bis(2,3)}, {bis(3,4)}, {bis(4,5)}]")

