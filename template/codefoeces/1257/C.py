for i in range (int(input())):
    t=int(input())
    s=t
    d={}
    l=list(map(int,input().split()) )
    
    
    
    for i in range(len(l)):
       try:
         
         d[l[i]].append(i)
         d[l[i]][0]=min(d[l[i]][-1]-d[l[i]][-2],d[l[i]][0])
         s=min(s,d[l[i]][0])
         
            
       except:
            d[l[i]]=[]
            d[l[i]].append(t)
            d[l[i]].append(i)
    
    if s==t:
        print(-1)
    else:
          print(s+1)