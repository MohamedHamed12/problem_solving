
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    a=input()
    b=input()
    yo=[]
    for i in range(n):
        if a[i]!=b[i]:yo.append(i)
    if len(yo)%2:print(-1)   
    else:
        if len(yo)==2:
            if yo[1]==yo[0]+1:print(min(x,2*y))
            else:print(y)
        else:
            print((len(yo)//2)*y)