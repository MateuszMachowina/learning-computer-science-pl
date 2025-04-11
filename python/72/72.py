napisy = []
with open("napisy.txt") as plik:
    for linia in plik:
        a, b = linia.split()
        c = []
        c.extend([a,b])
        napisy.append(c)

#1
print("zad.1")
licznik = 0
for i in range(200):
    para = napisy[i]
    if len(para[0]) >= 3*len(para[1]) or len(para[1]) >= 3*len(para[0]):
        licznik+=1
        if licznik == 1:
            print(para)
print(licznik)

#2
print("zad.2")
def nalezy(a,b):                #zakldam ze a ma byc krotszy od b
    for i in range(len(a)):
        if a[i] != b[i]:
            return 0
    return 1

def koncowka(a, b):
    return (b[len(a):len(b)])

for i in range(200):
    para = napisy[i]
    if nalezy(para[0], para[1]) == 1:
        print(para, koncowka(para[0], para[1]))
    elif nalezy(para[1], para[0]) == 1:
        print(para, koncowka(para[1], para[0]))

#3
print("zad.3")

def koniec(a,b):
    k = ""
    if len(a) > len(b):
        a = a[len(a) - len(b)::]
    else:
        b = b[len(b) - len(a)::]
    for i in range(len(a)-1,-1,-1):
        if a[i] == b[i]:
            k=a[i]+k
        else:
            break
    return k

max = 0
max_id = []
for i in range(200):
    para = napisy[i]
    k = koniec(para[0],para[1])
    if len(k) >= max:
        max = len(k)
        max_id.append(i)
    if len(k) == 15:
        print(para)
print(max)

