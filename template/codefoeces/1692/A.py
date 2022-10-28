import sys
  
for i in range(int(input())):
    l=list(map(int,sys.stdin.readline().split()))
    a=l[0]
    l=sorted(l)
    print(3-l.index(a))