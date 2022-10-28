for t in range(int(input())):
    n,k=map(int,input().split())
    l=[] 
    for i in range(n):
        l.append(list(map(int,input().split())))
    p=False
    tot=0
    for i in range(n):
        tot=0
        for j in range(n):
            if  abs(l[i][0]-l[j][0])+abs(l[i][1]-l[j][1])<=k :

                    tot+=1
        if tot==n:
                p=True
                break
    if p:
        print(1)
    else:
        print(-1)