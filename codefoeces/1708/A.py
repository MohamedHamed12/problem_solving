from  sys import stdin
def test(problem):
    pass
def solve(n,l):
        
        m=l[0]
        for i in range(1,n):
            # if l[i]-l[i-1]==1:return "YES"
            if l[i]%l[0]==0:
                continue
            else:return "NO"
        return "YES"



    


for i in range(int(input())):
    n=int(stdin.readline())
    l=list(int(i) for i in stdin.readline().split())
    print(solve(n,l))