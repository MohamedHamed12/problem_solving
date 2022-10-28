for i  in range(int(input())):
      n,m=map(int,input().split())
      l=list(map(int,input().split()))
      tot=sum(l)-m
      tot=tot if tot >0 else 0
      print(tot)