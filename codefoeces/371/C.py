from  sys import stdin
from typing import Counter
def test(problem):
    pass

def count(s):
    l=[0,0,0]
    for i in s:
        if i=='B':l[0]+=1
        if i=='S':l[1]+=1
        if i=='C':l[2]+=1
    return l
def solve():
    global have ,price,tot,money
    # num=0
    d=count(s)
    l=0;r=10**20
    while r-l>1:
        m=(l+r)//2
        cost=0
        for i in range(3):cost+=max(m*d[i]-have[i],0)*price[i]
        if money>=cost:l=m
        else:r=m
    print(l)
   
    

    

tot=0
s=input().strip()
have=list(int(i) for i in stdin.readline().split())
price=list(int(i) for i in stdin.readline().split())
money=int(input())
solve()
# print(tot)
    
 

# d={"B":0,"S":0,"C":0}
# s=str(input())
# for i in range(len(s)):
#     d[s[i]]+=1
# a,b,c=map(int,input().split())
# u,v,w=map(int,input().split())
# m=int(input())


# l,r=0,10**20
# while r-l>1:
#     x=(l+r)//2
#     y=u*max(d["B"]*x-a,0)+v*max(d["S"]*x-b,0)+w*max(d["C"]*x-c,0)
#     if y<=m: l=x
#     else: r=x
# print(l)

 # while True:
    #     # tem=0
    #     for i in range(3):
    #         if have[i]>=d[i]:
    #                 have[i]-=d[i]
    #                 # tem+=1
    #         else:
    #             money-=(d[i]-have[i])*price[i]
    #             if money<0:return
    #             have[i]=0
    #             # tem+=1
    #     tot+=1
    #     if sum(have)==0:
    #             g=0
    #             for i in range(3):
    #                 g+=price[i]*d[i]

    #             tot+=money//g
    #             return
    #     if  have.count(0)==1:
    #         mn=sorted(have)[1]



    # rem=[0,0,0]
    # ind=0
    # for i in d:
    #     m=have[ind]
    #     have[ind]=have%d[i]
    #     rem[ind]=m-have*d[i]

    #     ind+=1
    # mn=min(have)
    # num+=mn
    # for i in range(3):have[i]-=m
    # while sum(have)>0: