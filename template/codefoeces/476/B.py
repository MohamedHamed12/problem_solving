# import math
# from  sys import stdin
# def get(x,y):
    
#         return math.comb(x,y)/pow(2,x)
# def count(a):
#     numplus=0
#     numq=0
#     for i in range(len(a)): 
#         # if a[i]=='+':
#         #     numplus+=1
#         if a[i]=='-':
#                 numplus+=1
#         elif a[i]=='?':
#             numq+=1
#     tem=[]
#     tem.append(numplus)
#     if numq>0 :tem.append(numq)
#     return tem
# def solve(a,b):
#     la=count(a)
#     lb=count(b)
#     if len(lb)==1 :
#         return  1 if la[0]==lb[0] else 0    
#     else :
#         x=lb[1];tot=abs(lb[0]-la[0])
        
        
#         if tot<=x :
#             # y=x%tot
#             # if y%2==0:
#                 return get(x,tot)
#             # else:
#             #     return 0
#         else:
#             # if tot==0:return
#             return 0
    
# a=stdin.readline()
# b=stdin.readline()
# print(f'{solve(a,b):1.12f}')
 
import math

from functools import lru_cache
# @lru_cache(None)
def inp(): return input()
def fn(a,b):
    n=b.count('?')
    r=a.count('+')-b.count('+')
    m=(0 if n<r or r<0 else math.comb(n,r)/(1<<n))
    print(f'{m:1.12f}')

@lru_cache(None)
def main():
    n=inp()
    m=inp()
    (fn(n,m))
    
if __name__=="__main__":
    main()