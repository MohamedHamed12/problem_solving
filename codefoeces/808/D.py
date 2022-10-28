from collections import defaultdict
from  bisect import  bisect_left
def values():return  tuple(map(int,input().split()))
def inlst():return  list(map(int,input().split()))
def inp():return  int(input())


def solve(n,l,s):
            st = set()
            t=s//2
            d=defaultdict(int)
            d2 = defaultdict(int)
            for i in l:
                d[i]+=1
            tmp=0
            for i in l:
                d[i]-=1
                d2[i]+=1
                tmp += i

                if t==tmp:return "YES"
                if t-tmp>0 and d[t-tmp]>0:return "YES"
                if tmp -t> 0 and d2[ tmp-t] > 0: return "YES"



            return "NO"


n=inp()
l=inlst()

s=sum(l)
if (s//2)*2!=s:print("NO")
else:print((solve(n,l,s)))