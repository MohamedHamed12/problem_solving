for i in range(int(input())):
    r,c=map(int,input().split())
    l=[]
    b=True
    nemptycol=0
    nemptyrow=0
    for i in range(r):
        s=input()
        l.append(s)
        if b and s=='E'*c:
            nemptyrow+=1
        else:
            b=False
    j=0
    
    while j<c:
        s2=""
        for i in l:
            s2+=i[j]
        if s2=='E'*r:
            j+=1
            nemptycol+=1
            pass
        else:
            break
    if l[nemptyrow][nemptycol]=='R':
        print("YES")
    else:
        print("NO")