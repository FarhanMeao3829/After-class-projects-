tuppie1 = (1,5,2,4,5,8,9,8,3)

tuppie2 = (10,20,30,40,50,60,70,80,90)

re = ()

for i in range(0,len(tuppie1)):
    x = tuppie1[i] * tuppie2[i]
    re = re + (x,)

print(re)