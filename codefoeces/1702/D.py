import math
from  sys import stdin

def solve(s,p):
    l=[0]*26
    n=len(s)
    tot=0
    for i in range(n):
       m=ord(s[i])
       l[ m-97]+=1
       tot+=m-96
    i=25
    while i>=0 and tot>p:
        if l[i]>0:
            if tot-p>=l[i]*(i+1):
               tot-=l[i]*(i+1)
               l[i]=0
            else:
                u=math.ceil( (tot-p)/(i+1))
                tot-=u*(i+1)
                l[i]-=u
        else:i-=1
    r=""
    for i in s:
        if (l[ord(i)-97])>0:
            r+=i
            l[ord(i)-97]-=1

    return r

 
    

    


for i in range(int(input())):
    s=stdin.readline().strip()
    p=int(input())
    print(solve(s,p))