
import sys


   

for i in range(int(input())):
    ss = sys.stdin.readline().strip()
    n=len(ss)
    if ss[0]>ss[-1]:
       l = sorted(enumerate(ss), key=lambda x: x[1], reverse=True)
    else:
        l = sorted(enumerate(ss), key=lambda x: x[1])
    tot=0
    m=[]
    b=False
    for i, j in l:

        if j == ss[0]:
            b = True
        if b:
           
            if m:tot+=abs(ord(j)-ord(ss[m[-1]-1]))
            m.append(i+1)
        if i==n-1:
          break        
    print(tot,len(m))
    print(*m)