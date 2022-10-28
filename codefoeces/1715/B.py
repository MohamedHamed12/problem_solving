


n=int(input())

for i in range(n):
        n,k,b,s=tuple(map(int,input().split()))
        ll=[0]*n
        if k*b<=s:
            m=min(s,k*b+k-1)
            ll[-1]=m
            s-=m
        else:
                print(-1)
                continue
        for i in range(n-2,-1,-1):
            if k-1 <s:
                ll[i]=k-1;s-=k-1
            else:
                ll[i]=s
                s=0
                break

        
        if s!=0:print(-1)
        else:print(*ll)