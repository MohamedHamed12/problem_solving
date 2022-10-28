from collections import deque
from  sys import stdin
def test(problem):
    pass

def solve():
    dp=deque()
    n=int(input())

    l1=deque(int(i) for i in stdin.readline().split())
    n1=l1.popleft()
    l11=deque( l1)
    l2=deque(int(i) for i in stdin.readline().split())
    n2=l2.popleft()
    l22=deque(l2)
    tot=0
    while l1 and l2:
        h1,h2=l1.popleft(),l2.popleft()
        if h1>h2:
            l1.append(h2)
            l1.append(h1)
        else:
            l2.append(h1)
            l2.append(h2)
        tot+=1
        g=l1.copy()
        g.append(-1)
        g+=l2
        if g in dp:
            print(-1)
            return 
        else:dp.append(g)
    if l1:print(tot,1)
    else:print(tot,2)
    return 
    


solve()

    
# if __name__ == '__main__':
#     ncards = int(input())
#     a = list(map(int, input().split()))[1:]
#     b = list(map(int, input().split()))[1:]
#     s = set()
#     count = 0
    
#     while (len(a) != 0 and len(b) != 0):
#         st = ""
#         for i in a: st+=str(i)
#         st+="."
#         for j in b: st+=str(j)
#         if (st in s):
#             count = -1
#             break
#         else:
#             s.add(st)
#             count += 1
#             x = a.pop(0)
#             y = b.pop(0)
#             if (x < y):
#                 b.extend([x, y])
#             else:
#                 a.extend([y, x])
#     if (count == -1):
#         print(count)
#     else:
#         print(count, ("1" if len(b) == 0 else "2"))