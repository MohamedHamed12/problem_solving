from sys import stdin, stdout
n,q=map(int,input().split())
l=list(map(int,stdin.readline().split()))
 
l=sorted(l,reverse=True)
l.insert(0,0)
tot=0
for i in range(n+1):
      tot+=l[i]
      l[i]=tot
for i in range(q):
      x,y=map(int,stdin.readline().split())
      
 
      k=(l[x]-l[x-y])
      stdout.write(str(k)+"\n")