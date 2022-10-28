n,k=(map(int,input().split()))
if n%2==0:
  tot=int(n/2)
else:
  tot=int((n+1)/2)
if k<=tot:
  print(2*k-1)
else:
  k-=tot
  print(2*k)