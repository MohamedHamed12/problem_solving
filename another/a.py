# ﷽
from math import comb
def test2(x):
   cnt=0
   for i in range(x+1,2*x+1):
      if bin(i)[2:].count('1')==k:
         cnt+=1
   return cnt
def get(x):
   total=0
   x_bin= bin(x)[2:]
   len_bin=len(x_bin)
   rem_ones=k
   for i,j in enumerate( x_bin):
      len_bin-=1

      if rem_ones<0 or rem_ones>len_bin:break
      if j=='1':
        
         total+=comb(len_bin,rem_ones)
         rem_ones-=1
      
   return total
   
def solve():
    global k
    n,k=map(int,input().split())
    l=0;r=2**62
    while l<r:
        x=(l+r)//2
        if get(2*x)-get(x)>=n:r=x
        else:l=x+1
   #  print(l,get(2*l)-get(l),test2(l))
    print(l)


   
  
if __name__ == "__main__":
    for i in range(int(input())):
       solve()






