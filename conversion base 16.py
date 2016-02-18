res=[]
tab=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
tot=""
n=int(input("Rentrez le nombre en base 10 : "))
while n>15:
    res.append(n%16)
    n=n//16
res.append(n)
res=res[::-1]
for i in range(0,len(res)):
    tot=tot+" "+str(tab[res[i]])
print(tot)
