def solve(n,k,l):
    if n<=2:
        print(0)
    if k==1:
        if n%2==0:
            print(-1+n//2)
            
        else:
            print(n//2)
        return
    tot=0
    for i in range(1,n-1):
      if l[i]>l[i-1]+l[i+1]:
        tot+=1
    print(tot)




for  i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    solve(n,k,l)