slowa = []
with open("dane_6_1.txt") as plik:
    for linia in plik:
        slowa.append(linia.strip())
k=107
k = k%26
def cezar(a,k):
    for i in range(len(a)):
        t=ord(a[i]) + k
        if t > 90:
            t-=26
        print(chr(t), end="")  #end="" bez entera drukuje
    print(end = "\n")  #moglby byc print() po prostu

for i in range(len(slowa)):
    cezar(slowa[i], k)

