

# def test(problem):
#     pass
# def solve(s):
#     n=len(s)
#     i=0
#     qq=[]
#     right=0;left=0
#     q=0
#     for i in range(n):
#         if s[i]=='(':
#             right+=1
#         elif s[i]==')':
#             left+=1
#         elif s[i]=='?':
#             q+=1
#             qq.append()
#         if left>right:
#             if q>0:
#                 q-=1
#                 qq.pop()
#                 right+=1
#             else:
#                 return "NO"
#     if q>2:
#             return "NO"
#     elif q==2 and qq[-1]-qq[-2]!=1:
       

#             return "NO"
#     else:
#             return "YES"

    


# n=int(input())
# for i in range(n):
#     s=input()
#     print(solve(s))
import math
 
t = int(input())
 
for i in range(t):
    text = input()
    q = 0
    pos = []
    count = 0
    # if text[0] == ')' or text[-1] == '(':
    #     print("NO")
    #     continue
 
    for char in text[1:-1]:
        if char == '(':
            count -= 1
        if char == ')':
            count += 1
        if char == '?':
            q += 1
        if count == q:
            count = 0
            q = 0
    if (abs(count) != q):
        print('NO')
    else:
        print('YES')
    # print(pos)