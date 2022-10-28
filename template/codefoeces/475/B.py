from collections import defaultdict
def instr():return input()
def solve():
    d=defaultdict(list)
    n,m=tuple(map(int,input().split()))
    s1=instr()
    s2=instr()
    l=[0]*(n*m)
    for i in range(n):
        for j in range(m-1):
            if s1[i]=='>':
               d[m*i+j].append(m*i+j+1);l[m*i+j+1]+=1
            else:
               d[m*i +j+1].append(m*i+j);l[m*i+j]+=1
               
    for i in range(n-1):
        for j in range(m):
            if s2[j]=='v':
               d[m*i+j].append(m*(i+1)+j);l[m*(i+1)+j]+=1
            else:
               d[m*(i+1)+j].append(m*i+j);l[m*i+j]+=1
       
    for i in range(m*n):
        if d[i]==0 or l[i]==0:return 'NO'
    return ('YES')
print(solve())

'''
4 6
<><>
v^v^v^
NO

[Program finished]
'''