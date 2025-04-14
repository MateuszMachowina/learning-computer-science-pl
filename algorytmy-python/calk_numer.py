def f(x):
    return x**2
p = 1
q = 4

def calk_numeryczne(p, q):
    pole = 0
    i=p
    while i < q:
        pole+=(f(i) + f(i+0.0001))*0.0001/2
        i+=0.0001
    return pole
print(calk_numeryczne(1,4))

def calka(x):
    return x**3/3  #odwrotnosc pochodnej
print(calka(q) - calka(p))
