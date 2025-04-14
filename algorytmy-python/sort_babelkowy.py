
def bubble(a):
    for i in range(len(a)):
        for j in range (len(a)-1):
            if a[j+1] < a[j]:
                a[j], a[j+1] = a[j+1], a[j]
            #print(a)
    return a

a = [99,34,224,64,633,68,11,2,7,534,97,55]
print(bubble(a))

