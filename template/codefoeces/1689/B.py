
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l2=sorted(l)
    
    i=0
    if n==1:
        print(-1)
    else:
        for i in range(n):
            if l2[i]==l[i]:


                if i==n-1:
                    h=n-2
                    while h>0 and l2[h]==l[h]:
                        h-=1
                    l2[i],l2[h]=l2[h], l2[i]

                else:
                    l2[i],l2[i+1]=l2[i+1], l2[i]
        print(*l2)