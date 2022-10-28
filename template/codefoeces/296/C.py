from collections import deque


def value():return  tuple(map(int,input().split()))
def inlst() :return  list(map(int,input().split()))
# def solve(n):


if __name__ == '__main__':
    n,m,k=value()
    lst=inlst()
    dp=[0]*(n+1)
    dptmp=[0]*(m+1)
    deq=deque()
    for i in range(m):
        deq.append(value())

    for i in range(k):

        x,y=value()
        dptmp[x-1]+=1
        dptmp[y]-=1
    for j in range(1,m+1):
        dptmp[j]+=dptmp[j-1]
    for i in range( m ):
            l,r,d=deq[i]
            dp[l-1]+=d*dptmp[i]
            dp[r]-=d*dptmp[i]
    # for i in range(1,n+1):
    #     dp[i]+=dp[i-1]

    tmp=0
    for i in range(n):
        tmp+=dp[i]

        lst[i]+=tmp
    print(*lst)







#
# def solve(n):
#     y=n//3
#     if n%2==0:
#         return 1+(y//2)
#     else:
#         return ((y+1)//2)