
 
 
from collections import defaultdict, deque
from  sys import stdin
 
def solve(h,ss):
    d=defaultdict(lambda:[float('inf'),-1],{})
    for ind,j in enumerate(ss):
        d[j][0]=min(d[j][0],ind)
        d[j][1]=max(d[j][1],ind)
    for i in range(h):
        a,b=stdin.readline().split()
        
        if d[a][0]<=d[b][-1] :print ("Yes")
        else: print ("No")



 
for i in range(int(stdin.readline())):
    oo=stdin.readline()
    k,h=[int(i) for i in stdin.readline().split()]
    ss=stdin.readline().split()    
    solve(h,ss)