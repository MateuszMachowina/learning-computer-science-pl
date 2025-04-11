
def fib10(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == 2:
        return 1
    if a > 2:
        return fib10(a-1) + fib10(a-2)

def czy_1(a):
    if a == 1:
        return False
    i=2
    while i*i <= a:
        if a%i==0:
            return False
        i+=1
    return True

def ilosc1(a):
    ile=0
    for i in range(len(a)):
        if a[i] == '1':
            ile+=1
    return ile

#zad.1
print("zad.1")
for i in range(10,50,10):
   print(f"F{i} = {fib10(i)}")

#zad.2
print("zad.2")
for i in range(1,41):
   if czy_1(fib10(i)):
       print(fib10(i))

#zad.3 i 4
print("zad.3")
fibonacci_bin=[]
zad4 = []
for i in range(1,41):
    fibonacci_bin.append(bin(fib10(i))[2:])
for i in range(40):
    if ilosc1(fibonacci_bin[i]) == 6:
         zad4.append(fibonacci_bin[i])
    while len(fibonacci_bin[i]) != len(fibonacci_bin[39]):
        fibonacci_bin[i]='0' + fibonacci_bin[i]
    print(fibonacci_bin[i])
print(f"zad.4 \n {zad4}")

