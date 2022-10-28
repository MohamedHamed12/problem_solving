def getmax(a,b,c,t):
  if b==0 and c==0 and t>0:
    t+=1
  if b==0 or c==0:
    return max(a,b+c+t)
  else :
    return max(a,b+c-1+t)
tot=0 ;p=''
up=0;down=0
tem=0
n=int(input())
l=list(map(int,input().split()))
for i in range(1,len(l)):
  if l[i]>l[i-1]:
    if p=='up':
        up+=1
    else:
        p="up"
       
        tot=getmax(tot,up,down,tem)
        up=2+tem
        tem=0
        down=0
  elif l[i]==l[i-1] :
    
    tem+=1

  else :
       
    if p=='down':
      down+=1
    else:
      p='down'
       
      tot=getmax(tot,up,down,tem)
      down=2+tem
      tem=0
tot=getmax(tot,up,down,tem)
if tot==0:
  print(1)
else:
  print(tot)