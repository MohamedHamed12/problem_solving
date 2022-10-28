from  sys import stdin
def test(problem):
    pass
def solve(sm,b):
    s=set()
    for i in range(b,0,-1):
        tem=i&-i
        if sm-tem>=0:
            sm-=tem
            s.add(i)
    if sm:print(-1)
    else:
        print(len(s))
        print(*s)
      


a,b=list(int(i) for i in stdin.readline().split())
    
solve(a,b)