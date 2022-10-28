t,n=map(int,input().split())
l=list(map(int,input().split()))
count=0
if l[n-1]==1:
  count+=1
if int((t+1)/2 >=n):
   lt=n-1
   for i in range(n,n+lt):
     if l[i]==1 and l[n-(i-lt)-1]==1:
       count+=2
   for i in range(2*n-1,t):
     if l[i]==1 :
       count+=1
else:
  lt=(t-n)
  for i in range(n,t):
          if l[i]==1 and l[n-(i-n)-2]==1:
            count+=2

  
  for i in range(0,n-lt-1):
     if l[i]==1 :
       count+=1
print(count)