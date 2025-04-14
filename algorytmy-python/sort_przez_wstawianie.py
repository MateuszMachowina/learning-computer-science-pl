def wstawianie(a):
    for i in range(1,len(a)):              # dla kazdej liczby po kolei
        for j in range(i,0,-1):            # leci w lewo i szuka dla niej odpowiedniego miejsca
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            #print(a)

    return a

a = [99,34,224,64,633,68,11,2,7,534,97,55]
print(wstawianie(a))
