

import collections
import sys


def gget(x1, y1, x2, y2, x3, y3):
    if x1 == x2 and y1 == y3 or x1 == x3 and y1 == y2:
        return True


 


for i in range(int(sys.stdin.readline())):
    nn =int(sys.stdin.readline())
    x1, y1, x2, y2, x3, y3 = collections.deque((map(int, sys.stdin.readline().split())))
    hh, k = collections.deque((map(int, sys.stdin.readline().split())))
    x, y = -1, -1
    if gget(x1, y1, x2, y2, x3, y3):
        x, y = x1, y1
    elif gget(x2, y2, x3, y3, x1, y1):
        x, y = x2, y2
    elif gget(x3, y3, x1, y1, x2, y2):
        x, y = x3, y3
    if (x == 1 and y == 1) or (x == nn and y == nn) or (x == 1 and y == nn) or (x == nn and y == 1):
        if hh==x or k==y:print("YES");continue
             
        else: print("NO");continue
            
    if x % 2 == hh % 2 or y % 2 == k % 2: print("YES");continue
        

    print("NO");continue