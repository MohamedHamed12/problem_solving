import math
n,m=map(int,input().split(" ")) 
l1=list(map(int,input().split(" ")))

second =l1.copy()
for i in range(len (l1)):
  l1[i]=math.ceil(int(l1[i])/m)



l1.reverse()
maxx=l1.index(max(l1))
maxx=len(l1)-maxx
print(maxx)