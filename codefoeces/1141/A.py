l=list(map (int,(input().strip().split())))
n=l[0]
m=l[1]
tot=0


if n==m :
    print(0)

elif(m%n==0):
    
    q=m/n
    while q>1 and (q%3==0 or q%2==0 ):
        if q%3==0 :
            tot=tot+1
            q=q/3
        else:
            tot=tot+1
            q=q/2

    if q==1 :
        print(tot)
    else:
        print(-1)

else:
    
    print(-1)