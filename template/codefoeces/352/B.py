from collections import defaultdict, deque
from  sys import stdin,stdout
def test(problem):
    pass
def solve(problem):
    pass

    


n=int(input())
d=defaultdict(lambda:[0])
l=list(int(i) for i in stdin.readline().split())
tot=0
for i in range(n):
    val=l[i]
    if len(d[val])>2:
        if i-d[val][2]==d[val][0]:
            d[val][2]=i
        else:
            d[val]=[-1]
            tot-=1
    elif len(d[val])==2:
            d[val][0]=i-d[val][1]
            d[val].append(i)
    elif d[val][0]!=-1:
            d[val].append(i)
# tot=deque()
print(len(d)+tot)
for i in sorted(d):
    if d[i][0]!=-1:
        stdout.write(f"{i} {d[i][0]}\n")

# print(len(tot))
# for i,j in tot:
#     print(i,j)