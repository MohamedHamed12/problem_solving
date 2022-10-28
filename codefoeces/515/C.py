# from math import log
import math
# from ntpath import join
from  sys import stdin
def test(problem):
    pass
def solve(problem):
    pass

    


n=int(input())
t=[]
# t=[0]*10
l=list( input())
# for i in range(n):
    # tem=int(i)
    # if tem<2:continue
    # else:

for i in l:
    if i=='0' or i=='1':continue
    tem=math.log(int(i),2)
    if int(tem) ==tem :
        for j in range(int(tem)):
            t.append('2')
        if int(i)>2:
            t.append(str(int(i)-1))
    elif i=='6':
        t.append('5')
        t.append('3')
    
    elif i=='9':
        for i in range(2):
            t.append('3')
        t.append('7')
        t.append('2')
    else:
        t.append(i)
print("".join( sorted(t,reverse=True)))