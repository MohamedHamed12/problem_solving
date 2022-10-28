from collections import deque
from  sys import stdin ,stdout
import sys
# sys.setrecursionlimit(1500)
# def test(problem):
#     pass
def solve(n,q,l):
    ind=n-1
    k=0 if l[-1]>1 else 1
    s=[]
    for i in range(n-1,-1,-1):
        if l[i]>k and k<q:
            k+=1
            s.append('1')
        elif l[i]<=k:
            s.append('1')

        else:
            s.append('0')

    # s=s[::-1]
     
      
    sys.stdout.write("".join(reversed(s)) +'\n')


    


for i in range(int(input())):
    n,q=list(int(i) for i in stdin.readline().split())
    l=deque(int(i) for i in stdin.readline().split())
    solve(n,q,l)