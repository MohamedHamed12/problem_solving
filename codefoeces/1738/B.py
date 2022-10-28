import math
 
 
for i in range(int(input())):
    n ,m=map(int,input().split())
    l=list(map(int,input().split()))
    if len(l)==1: print("Yes") ;continue
    ln=n-m+1
    last=math.ceil(l[0]/ln)
    if last+l[0]>l[1]:print("No") ;continue 
    b=True
    for i in range(1,m):
        if l[i]-l[i-1]<last:
            print("No") 
            b=False; break 
        else:last=l[i]-l[i-1]
    if b:print( "Yes")