from bisect import  bisect_left
import sys
sys.setrecursionlimit(100000)


for item in range(int(input())):
    n,c,q=list(int(i) for i in sys.stdin.readline().split())
    s=sys.stdin.readline().strip()
    intervals=[]
    intervals=[];intervals.append([1,n])
    # lens=[]
    lens=[];lens.append(n)
    for j in range(c):
        a,b=list(int(i) for i in sys.stdin.readline().split())
        intervals.append((a,b))
        lens.append(b-a+1+lens[-1])
        # lens.append(b-a+1+lens[-1])

    for j in range(q):
        x=int(sys.stdin.readline())
        ind=bisect_left(lens,x)
        while x>n:
        # for ind in range(len(lens)-1,-1,-1):
        #     if x<=n:break
        #     if lens[ind-1]>=x:
            ind=bisect_left(lens,x)

            # a,b=
            # x=(x-lens[ind])+intervals[ind][]
            x=(x-lens[ind-1])-1+intervals[ind][0]
            # ind-=1
        print(s[x-1])