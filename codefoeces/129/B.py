from collections import defaultdict
from  sys import stdin

#fun to solve the problem
def solve(l):
    d=defaultdict(list)
    tem=[]
    for u,v in l:
        d[u].append(v)
        d[v].append(u)
    b=True
    tot=0
    while b:
        b=False
        for i in d:
            if len(d[i])==1:
                b=True
                t=d[i].pop()
                # d[t].remove(i)
                tem.append(i)
        if b:tot+=1
        for i in d:
            if not i:continue
            for j in tem:
                if j in d[i]:d[i].remove(j)
        tem.clear


    print(tot)
    return
    

    
    


#input number of inputs
a,b=list(int(i) for i in stdin.readline().split())
tot=[]
for i in range(b):
    tot.append(list(int(i) for i in stdin.readline().split()))
solve(tot)