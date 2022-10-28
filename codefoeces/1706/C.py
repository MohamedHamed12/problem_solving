# import math
from  sys import maxsize, stdin
def test(problem):
    pass
def solve(n,l):
   
    cool=[]
    for i in range(1,n-1):
        cool.append(max(max(l[i-1],l[i+1])+1-l[i],0))
    if n%2==1:
        print(sum(cool[::2]))
        return
    else:
        left=0
        right=sum(cool[1::2])
        m=right
        for i in range(0,n-2,2):
            
            left+=cool[i]
            right-=cool[i+1]
            m=min(m,right+left)

        print(m)
        return 
    
    print(tot)
for i in range(int(input())):
    n=int(input())  
    l=list(int(i) for i in stdin.readline().split())
    
    solve(n,l)

# l=[1,2,3,4,5,6]
# print(l[1::2])

# tot=0
    # if n%2==1:
    #     for i in range(n-1):
    #         if i%2==1:
    #             tot+=max(max(l[i-1],l[i+1])+1-l[i],0)

    # else:
    #     tem1=[]
    #     t1,t2=0
    #     tem2=[]
    #     for i in range(1,n-1):
    #         if i%2==1:
    #             t=max(max(l[i-1],l[i+1])+1-l[i],0)
    #             t1+=t
    #             tem1.append(t)
    #         else:
    #             t=max(max(l[i-1],l[i+1])+1-l[i],0)
    #             t2+=t
    #             tem2.append(t)
    #     r=maxsize
    #     for i in range(1,n-1):
    #         ind=i//2
    #         h=0;k=0
    #         if i%2==1:h+=tem1[ind]
    #         else:k+=tem1[ind]
    #         # ind=i//2
    #         r=min(t1-h+t2-k,r)
    #         # r=min(sum(tem1[:ind])+sum(tem2[ind:]),r)

    #     tot=r 
    # print(tot)