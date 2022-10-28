n,h=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in l:
  if i <= h:
    count+=1
  else:
    count+=2
print(count)