import math
from collections import defaultdict ,Counter
from  bisect import  bisect_left
def values():return  tuple(map(int,input().split()))
def inlst():return  list(map(int,input().split()))
def inp():return  int(input())

def solve():
        kk=inp()
        k=([chr(97+i) for i in range(kk)])
        s=list(input())
        st=set(s)
        n=len(s)
        if math.ceil(n/2)<kk:return 'IMPOSSIBLE'
        m=n//2 if n%2==0 else 1+n//2
        for i in range(m-1,-1,-1):
                if s[i]=='?' and s[n-i-1]=='?':
                      ind=len(k)-1

                      while k[ind]  in st:
                              ind -=1
                              if ind ==0:break
                      s[i]=s[n-i-1]=k[ind]


                elif s[i]=='?':
                    if s[n-i-1] in k:
                      s[i]=s[n-i-1]


                    else:
                      return 'IMPOSSIBLE'
                elif s[n-i-1] == '?':

                        if s[i] in k:
                                s[n - i-1]=s[i]


                        else:
                           return 'IMPOSSIBLE'
                if s[i]==s[n-i-1] and s[i] in k:
                    pass

                else:
                    return 'IMPOSSIBLE'
                st.add(s[i])
        if '?' in st:st.remove('?')
        if   len(st)!=kk:return 'IMPOSSIBLE'
        return "".join(s)



print(solve())