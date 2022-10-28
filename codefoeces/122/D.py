import math
import  sys
from collections import defaultdict ,Counter,deque
from  bisect import  bisect_left
def values(f):return  tuple(map(int,f.readline().split()))
def value():return  tuple(map(int,sys.stdin.readline().split()))
def inlst(f):return  list(map(int,f.readline().split()))
def inlsts(f):return  deque(map(int ,f.readline().split()))
def inlstb(f):return  deque((pow(2,int(i)) for i in f.readline().split()))
def inp(f):return  int(f.readline())

def solve():
    # f=open('/home/mohamed/Documents/w.txt')
    n,k=value()
    # s=list(f.readline())
    s=list(sys.stdin.readline().strip())
    for i in range(n):
        if k==0:break
        if i<n-2 and s[i] == '4' and s[i + 1] == '4' and s[i + 2] == '7' and (i+1)%2==1:
            if k % 2 == 1:s[i+1] = '7'
            break

        elif i<n-1 and s[i]=='4' and s[i+1]=='7':
            if    (i+1)%2==1:
                if i<n-2 and  s[i+2]=='7':
                    if k%2==1:s[i+1]='4'
                    break
                else:
                  s[i+1] = '4'

            else: s[i]='7'
            k -= 1


    return "".join(s)

sys.stdout.write(str(solve())+'\n')


'''
7 4
4727447


7 7
4211147

4 1000000000
7747
'''