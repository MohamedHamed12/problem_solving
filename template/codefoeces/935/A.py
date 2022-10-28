n=int(input())
tot=1

for i in range(2,int(n/2)+1):
    if (n-i)%i==0:
        tot+=1
print(tot)