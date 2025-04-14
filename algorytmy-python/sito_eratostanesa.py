sito = [True for i in range(10**6)] #10**6 to 10 do szóstej czyli 1000000
pierwsze = []
for i in range(2, 10**6):
    if sito[i] == True:
        pierwsze.append(i)
        sito[i]=False
        x=i
        while x < 10**6:   #for x in range(i, 10**6,i) zaczyna od i, nie przekroczy 10**6, zwieksza sie o i
            sito[x]=False
            x+=i
for liczba in range(len(pierwsze)):
    print(pierwsze[liczba])
