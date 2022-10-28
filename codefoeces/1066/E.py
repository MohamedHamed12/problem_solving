

def values():return  tuple(map(int,input().split()))


def solve():

    n,m=values()
    a=input()
    b=input()
    ans=0
    mod=998244353
    count=0
    r=n-m
    for i in range(m):
        if b[i]=='1':count+=1
        if r+i>=0:
            if a[i+r]=='1':
             ans=(ans+count*pow(2,m-i-1,mod))%mod
    return ans



print((solve()))