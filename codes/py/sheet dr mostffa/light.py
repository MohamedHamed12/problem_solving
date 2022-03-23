import math 

n=int(input())
while(n!=0):
  h=math.sqrt(n)
  if h==int(h):
    print('yes')
  else:
    print('no')
  n=int(input())
