n=int(input())
l = list(map(int,input().strip().split()))[:n]
l.sort(reverse=True)
for i in range(0,n-2):
  if l[i]<l[i+1]+l[i+2]:
    print("YES")
    break
else:
  print("NO") 








""" l=[]
for i in range (0,n):
  element=input()
  l.append

l.sort()

print(l)
 """