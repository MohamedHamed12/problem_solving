# from math import gcd
# from  sys import stdin
    
# def solve(n,l,r):
#     s=set()
#     ind=1
#     tot=[]
#     for ind in range(1,n+1):
#         for i in range(l,r+1):
#             m=gcd(i,ind)
#             if m not in s:
#                 tot.append(i)
#                 s.add(m)
#                 break
#             if len (tot)==n:break
#         if len (tot)==n:break

#     if len (tot)==n:
#             print("YES")
#             print(*tot)
#     else:
#             print("NO")




    


# for i in range(int(input())):
    
#   n,l,r=list(int(i) for i in stdin.readline().split())
#   solve(n,l,r)
# # from math import gcd

# # ind=1
# # for i in [1000 ,1002, 1005, 1008, 1010, 1014, 1015 ,1016, 1017]:
# #     print(gcd(i,ind))
# #     ind+=1
import math


def solve():
    ans = []
    b=True

    for i in range(1, n+1):
        x=math.ceil(l/i)*i
        if x<=r:ans.append(x)
        else:
            b=False
            break
    if b:
        print("YES")
        print(*ans)
    else:
        print("NO")

        # x = r - r % i
#         if x < l:
#             print("NO")
#             return 
#         ans.append(x)
 
#     print("YES")
#     print(*ans)
# #  
 
for _ in range(int(input())):
    n, l, r = map(int, input().split())
    solve()