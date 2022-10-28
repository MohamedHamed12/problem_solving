
   
import math
import sys

for i in range(int(input())):
    x,y=tuple(map(int, sys.stdin.readline().split()))
 
    z=x*y
    n=math.ceil((z)**(1.0/3.0))
    m=n**3
    if  x%n==0 and y%n==0 and  z==m   : sys.stdout.write("YES\n" )    
    else: sys.stdout.write("NO\n")