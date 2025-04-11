y = 19 + 61/125 + 32 + 2/3
x = 8
p_prostokata = x*y


def f(x):
    return x**4/500 - x**2/200 - 3/250
def g(x):
    return -x**3/30 + x/20 + 1/6

#czesc_dolna
p1=0
step = 0.00001
x=2
while x < 10:
    p1+=abs(step*g(x))
    x+=step
#czesc_gorna
p2=0
x=2
while x < 10:
    p2+=abs(step*f(x))
    x+=step
print(p1+p2)

#2
def przeciwprost(a,b):
    return (a**2 + b**2)**0.5
obwod = 8 + y + 8
x = 2
step = 8/1000
while x < 10:
    obwod+=przeciwprost(step,g(x)-g(x+step))
    obwod+=przeciwprost(step,f(x)-f(x+step))
    x+=step
print(obwod)

#3
x = 9.75
step = 0.25
ilosc = 0
suma = 0
while x > 2:
    dl = (abs(f(x) - g(x)))//1
    if dl > 0:
        ilosc+=1
        suma+=dl
    x-=step
print(suma)



