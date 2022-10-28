from collections import deque
from  sys import stdin
def test(problem):
    pass
def solve(n,l):
    # l=deque(l)
    print(l[1]-l[0],l[-1]-l[0])
    for i in range(1,n-1):
        mn=min(l[i]-l[i-1],l[i+1]-l[i])
        mx=max(l[i]-l[0],l[-1]-l[i])
        print(mn,mx)
    print(l[-1]-l[-2],l[-1]-l[0])


    


n=int(input())
l=tuple(int(i) for i in stdin.readline().split())
solve(n,l)