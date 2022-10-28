for i in range(int(input())):
    n=int(input())
    numeven=0;numodd=0
    
    l=list(map(int,input().split()))
    minnum=max(l)
 
    for i in l:
        if i%2==0:
            numeven+=1
        else:
            # l.remove(i)
            numodd+=1
    if numeven==0:
        print(0)
    elif numodd>0:
        print(numeven)
    else:
 
      for i in l:
        
        if i%2==0:
            tem=0
            while i%2==0:
                i=int(i/2)
                tem+=1
            minnum=min(minnum,tem)
        
    
      print(minnum+numeven-1)