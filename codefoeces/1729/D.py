
   


import sys


for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ll = tuple(map(int, sys.stdin.readline().split()))
    hh = tuple(map(int, sys.stdin.readline().split()))

    tt = []
    tot = 0
    for i in range(n):
        tt.append(hh[i]-ll[i])
    tt = sorted(tt)
    lft = 0
    r = n-1
    while lft < r:

        if tt[lft] + tt[r] < 0:
            lft += 1
            continue
        else:
            tot+=1
            r -= 1
            lft+=1
      
        
    print(tot)