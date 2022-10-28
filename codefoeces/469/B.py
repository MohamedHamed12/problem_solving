from  sys import stdin
def test(problem):
    pass
def solve(problem):
    pass

    


p,q,l,r=list(int(i) for i in stdin.readline().split())
if l==r==0: print(1)
else:
    arr=[];tm=0
    tot=[0]*1001
    for i in range(p):
        arr.append( list(int(i) for i in stdin.readline().split()))
    for i in range(q):
        a,b=( list(int(i) for i in stdin.readline().split())) 
        for m,n in arr:
            if a>m:continue
            else:
                tmin=max(l,m-b);tmax = min(n-a,r)
                for j in range(tmin,tmax+1):
                 if tot[j]!=0:continue
                 else:tot[j]=1;tm+=1

    print(tm)