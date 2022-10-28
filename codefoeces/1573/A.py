for i in range(int(input())):
    tot=0
    k=0
    n=int(input())
    m=input()
    
    for j in range(n-1,-1,-1):
        if int(m[j])>0:
            tot+=k+int(m[j])
            k=1
        else:
            k=1
    print(tot)