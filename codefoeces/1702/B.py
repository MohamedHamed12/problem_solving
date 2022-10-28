from  sys import stdin
def test(problem):
    pass
def solve(s):
    q=set()
    i=0;tot=0
    while i<len(s):
       while i<len(s) and len(q)<3:
          q.add(s[i])
          i+=1
    #    i-=1
       while i<len(s) and s[i] in q:
            i+=1
       tot+=1
       q.clear()
    print(tot)


    

n=int(input())
for i in range(n):
    w= stdin.readline().strip()
    solve(w)