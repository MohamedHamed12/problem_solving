import math 

for j in range (int(input())):
  a,b=map(int ,input().split())
  c=math.sqrt(pow(a,2)+pow(b,2))
  if a==0 and b==0:
    print(0)
  elif (c-int(c)==0):
    print(1)
  else:
    print(2)