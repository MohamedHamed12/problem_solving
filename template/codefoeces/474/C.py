import collections
import heapq
import sys
import math
import itertools
import bisect
from io import BytesIO, IOBase
import os
from tabnanny import check
######################################################################################
#--------------------------------------funs here-------------------------------------#
######################################################################################
def values(): return tuple(map(int, sys.stdin.readline().split()))
def inlsts(): return [int(i) for i in sys.stdin.readline().split()]
def inp(): return int(sys.stdin.readline())
def instr(): return sys.stdin.readline().strip()
def words(): return [i for i in sys.stdin.readline().strip().split()]
def chars(): return [i for i in sys.stdin.readline().strip()]
######################################################################################
#--------------------------------------code here-------------------------------------#
######################################################################################
import math
class Point():
  def __init__(self,x,y):
    self.x = x
    self.y = y
def rotate(point,origin, n):
    ox, oy = origin.x, origin.y
    px, py = point.x, point.y
    qx = ox +cosn[n] * (px - ox) - sinn[n] * (py - oy)
    qy = oy + sinn[n]* (px - ox) + cosn[n] * (py - oy)
    r=Point( qx, qy)
    return r
def mid(point1,point2):
     a=(point1.x+point2.x)/2
     b=(point1.y+point2.y)/2
     return a, b
def lenght(point1,point2):
    return math.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)
def Is_Squre(point1,point2,point3,point4):
    tmp=[point1,point2,point3,point4]
    for i in range(4):
      for j in range(i+1,4):
        if tmp[i].x==tmp[j].x and tmp[j].y==tmp[i].y:return False
    def check(point1,point2,point3,point4):
      if mid(point1,point2)==mid(point3,point4):
          if abs(lenght(point1,point2)-lenght(point3,point4))<=10**-4:
                if (point1.y-point2.y)*(point3.y-point4.y) ==-((point3.x-point4.x)*(point1.x-point2.x)):return True

    if check(point1,point2,point3,point4):return True
    if check(point1,point3,point2,point4):return True
    if check(point1,point4,point3,point2):return True
    

def solve():
    global cosn,sinn
    cosn=[1,0,-1,0];sinn=[0,1,0,-1]
    var=[[x,y,z,a] for x in range(4) for y in range(4) for z in range(4) for a in range(4)]
    for i in range(inp()):
        ans=float('inf')
        tmp=[]
        for i in range(4):
            a,b,x,y=values()
            tmp.append((Point(a,b),Point(x,y)))
        for a in var:
            if Is_Squre(*[ rotate(tmp[i][0],tmp[i][1],a[i])   for i in range(4)]):ans=min(ans,sum(a))

        print(ans if ans!=float('inf') else -1)



if __name__ == "__main__":
        solve()



# def f(x, y, a, b, n):   
#     return a + (x - a) * cos[n] - (y - b) * sin[n], b + (x - a) * sin[n] + (y - b) * cos[n]
# def check(p):
#     d = {}
#     for i in range(len(p) - 1):
#         for j in range(i + 1, len(p)):
#             dist = (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
#             d[dist] = d.get(dist, 0) + 1
#     if len(d) != 2:
#         return 0
#     a, b = sorted(d)
#     return 2 * a == b and d[a] == 4 and d[b] == 2





# cos, sin = [1, 0, -1, 0], [0, 1, 0, -1]
# variants=[[x, y, z, a] for x in range(4) for y in range(4) for z in range(4) for a in range(4)]
# for t in range(int(input())):
#     moles, ans = [list(map(int, input().split())) for x in range(4)], 13
#     for a in variants:
#         if check([f(moles[i][0], moles[i][1], moles[i][2], moles[i][3], a[i]) for i in range(4)]):
#             ans = min(ans, sum(a))
#     print(ans if ans != 13 else -1)