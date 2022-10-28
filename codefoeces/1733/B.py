
 


import sys


for _ in range(int(input())):
   nn,x,y=tuple(map(int, sys.stdin.readline().split()))
   if x==y==0:print (-1);continue
   if x!=0 and y!=0:print(-1);continue
   x=max(x,y)
   if (nn)<=x:print(-1);continue
   if (nn-1)%x!=0:print (-1);continue
   ll=[]
   tmp=1
   for i in range((nn-1)//x):
        for j in range(x):
          
           ll.append(tmp)
        tmp=len(ll)+2
        # if len(l)==n-1:break
   print(*ll)