n=int(input())
a=input()
pos=a[0]
tot=0
numOfR=0 ;   numOfU=0
for i in range(n):
    if a[i]=='U':
        numOfU+=1
    elif a[i]=='R':
        numOfR+=1
    if i+1<n:
        if numOfR==numOfU!=0 and a[i+1]!=pos :
            tot+=1
            pos=a[i+1]
print(tot)