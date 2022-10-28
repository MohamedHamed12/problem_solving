
import collections
import sys






nn=int(sys.stdin.readline())
for i in range(nn):
            n = int(sys.stdin.readline())
            ll=collections.deque((map(int, sys.stdin.readline().split())))
            tot=[0]*n
            tot[0]+=1
            for i in range(1,n) : 
                if ll[i]>tot[i-1]:tot[i]=tot[i-1]+1
                else:tot[i]=ll[i]
            print(sum(tot))