def case1(a,b,x,y,n):
 
    if b-n>=y:
        b=b-n
        
    else:
        n=n-(b-y)
        a=a-n if a-n>=x else x
        b=y
    return(a*b)
def case2(a,b,x,y,n):
    if a-n>=x:
        a=a-n
        
    else:
        n=n-(a-x)
        b=b-n if b-n>=y else y
        a=x
    return(a*b)
for i in range(int(input())):
    l=[]
    a,b,x,y,n=map(int,input().split())

 
    l.append(case1(a,b,x,y,n))
  
    
    l.append(case2(a,b,x,y,n))
    print(min(l))