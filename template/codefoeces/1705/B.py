from  sys import stdin
def test(problem):
    pass
def solve(n,l):
    
    i=0
    while i<n and l[i]==0:
        i+=1
    l=l[i:-1]
    nzero=l.count(0)
    tot=sum(l)
    print( tot+nzero)
    

    


for i in range(int(input())):
    n=int( stdin.readline())

    l=list(int(i) for i in stdin.readline().split())
    
    solve(n,l)

# n=[1,2,3]
# print(n[:-1])