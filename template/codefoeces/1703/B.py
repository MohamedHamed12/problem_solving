from  sys import stdin
from typing import Counter

    


for i in range(int(input())):
    n=input()
    s=input().strip()
    c=Counter(s)
    tot=0
    for i in c:
        tot+=c[i]+1
    print (tot)