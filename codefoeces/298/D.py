import math
import  sys
from collections import defaultdict ,Counter,deque
from  bisect import  bisect_left
def values(f):return  tuple(map(int,f.readline().split()))
def value():return  tuple(map(int,sys.stdin.readline().split()))
def inlst(f):return  list(map(int,f.readline().split()))
def inlsts(f):return  deque(map(int ,f.readline().split()))
def inlss():return  deque(map(int ,sys.stdin.readline().split()))
def inlstb(f):return  deque((pow(2,int(i)) for i in f.readline().split()))
def inp(f):return  int(f.readline())

def solve():
    # f=open('/home/mohamed/Documents/w.txt')
    n,m,k=value()
    l1=sorted(inlss())
    l2=sorted(inlss())
    # print(l1)
    # print(l2)

    j=n-1

    for i in range(m-1,-1,-1):
        if j==-1:return "NO"
        if l2[i]>=l1[j]:j-=1

    if j == -1: return "NO"
    else:return "YES"



sys.stdout.write(str(solve())+'\n')
'''
15 15 10
4 5 9 1 4 6 4 1 4 3 7 9 9 2 6
6 6 7 7 2 9 1 6 10 9 7 10 7 10 9
'''

'''
7 4
4727447


7 7
4211147

4 1000000000
7747
'''