wyrazy = []
with open("sygnaly.txt") as plik:
    for linia in plik:
        a=linia.strip()
        wyrazy.append(a)

#1
print("4.1")
przeslanie=""
for i in range(39,1000,40):
    a=wyrazy[i]
    przeslanie+=a[9]
print(przeslanie)

#2
print("4.2")
max_id=0
max=0
for i in range(0,1000):
    wyraz=wyrazy[i]
    zbior=[]
    for j in range(0, len(wyraz)):
        litera=wyraz[j]
        # spr=1
        # for k in range(0, len(zbior)):
        #     if zbior[k] == litera:
        #         spr=0
        #         break
        # if spr == 1:
        #     zbior.append(litera)
        if not litera in zbior:
            zbior.append(litera)
    if len(zbior) > max:
        max = len(zbior)
        max_id = i
print(wyrazy[max_id], max)

#3
print("4.3")
dobre=[]
for i in range(0,1000):
    wyraz=wyrazy[i]
    wartosci=[]
    min=150
    max=0
    for j in range(0, len(wyraz)):                  #chr() z kodu na litere
        kod=ord(wyraz[j])                           #ord() z litery na kod
        if kod > max:
            max=kod
        if kod < min:
            min=kod
    if abs(max-min) < 11:
        dobre.append(wyraz)
for i in range(0, len(dobre)):
    print(dobre[i])






