for m in range(int(input())):
    n,k=map(int, input().split())
    s=input()
    d=[0]*(n+1)
    for i in range(n) :
        if s[i]=='W':
            d[i+1]+=1
        d[i+1]+=d[i]
    ans=1e18
    for i in range(n-k+1):
        ans=min(ans,d[k+i]-d[i])
    print(ans)