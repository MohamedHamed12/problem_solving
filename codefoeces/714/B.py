from  sys import stdin
def test(problem):
    pass
def solve(n,l):
    if n<=2:return "YES"
    a=min(l);b=max(l)
    tem=b-a
    # if tem%2==1:return "NO"
    for i in range(n):
        if l[i]==a or l[i]==b or(tem%2==0 and(l[i]-tem//2==a or l[i]+tem//2==b)):
            continue
        else :return "NO"

    return "YES"


n=int(input())

l=list(int(i) for i in stdin.readline().split())
    
print(solve(n,l))