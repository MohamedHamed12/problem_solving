# import math
# from  sys import stdin
# def test(problem):
#     pass
# def solve(n,l):
#     tot=0
#     for i in range(n):
#         if i%2==0:
#             tot+=math.comb(n-1,i)*l[n-i-1]
#         else:
#             tot-=math.comb(n-1,i)*l[n-i-1]

#     print(tot)


# for i in range(int(input())):
#     n=int(stdin.readline())
#     l=list(int(i) for i in stdin.readline().split())
#     solve(n,l)   
 

from bisect import bisect as b
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for j in range(1,n):
        k=[]
        for i in range(1,len(l)):
            k.append(l[i]-l[i-1])
        k.sort()
        l=k[b(k,0):]
        if len(l)<n-j:
            l.insert(0,0)
    if len(l)==1:
        print(l[0])