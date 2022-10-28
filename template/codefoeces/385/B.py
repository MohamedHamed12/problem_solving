# # # from  sys import stdin

# # # def solve(a):
# # #     n=len(a);tot=0
# # #     ind=0
# # #     for i in range(n):
# # #         if a[i] =='b':
# # #            if a[i:i+4]=="bear":
             
# # #               x=i+1
# # #               y=n-(i+3)                    
# # #               if ind>0:
# # #                     tot+=x*y-y*ind
# # #               else:
# # #                 tot+=x*y
# # #            ind+=1
# # #     return tot
    

# # # print(solve(input()))
# # # # n=int(input())
# # # # a,b=list(int(i) for i in stdin.readline().split())
# # # # for i in range(int(input())):
# # # #     l=list(int(i) for i in stdin.readline().split())
    
 
# # # # a="bearaabearc"
# # # # t=-1
# # # # # while:
# # # # print(a.find("bear"))
# import sys
# input = sys.stdin.readline
 
# s = list(input())
# s.pop(-1)
# s="".join(s)

# n = len(s)
# a = s.count('bear')
# if a == 0:
#     print(0)
# else:
#     c = 0
#     while a:
#         x = s.index('bear')
#         c += (x+1)*(n-x-3)
#         s = s[x+1:]
#         a -= 1
#         n -= x+1
#     print(c)

# # print(input()[:-1])
s = input()
 
sum = 0
for i in range(len(s)):
    j = s.find("bear", i)
    if(j == -1):
        break
    sum += len(s) - (j +3)
 
print(sum)