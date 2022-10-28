import sys
from collections import Counter

for i in range(int(input())):
    n = int(input())
    l = list(map(int, sys.stdin.readline().split()))
    c = Counter(l)
    tot = 0
    for i  in c:
        tot+=c[i]-1 if c[i]>1 else 0
    if tot%2!=0:
        tot+=1
    print(n-tot)