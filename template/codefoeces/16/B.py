# import collections
d={}
tot=0
n,m=map(int,input().split())
for i in range(m):
  a,b=map(int,input().split())
  if b not in list(d.keys()):
   d[b]=a
  else:
    d[b]+=a
ds=dict(sorted(d.items()).__reversed__())
k=list(ds.keys())
i=0
# print(d[k[i]])  ``
# print(n)
while(n>0 and i<len(k)):
  if n>= ds[k[i]]:
    n-=ds[k[i]]

    tot+=k[i]*ds[k[i]]
  
  else:
    tot+=k[i]*n

    n=0
  i+=1
print(tot)