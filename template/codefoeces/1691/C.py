

for i in range(int(input())):
  # n=int(input())
  n,k=map(int,input().split())
  s=input()
  num=s.count("1")
  tot=0
  if num==1:
    i =s.index("1")
    j=n-s.rfind("1")-1
    if k>=j:
      k-=j
      tot+=1
      num-=1
    elif k>=i:
        k-=i
        tot+=10
        num-=1
    tot+=num*11
    print(tot)

  elif num>1:
    i =s.index("1")
    j=n-s.rfind("1")-1
    if k>=j:
      k-=j
      tot+=1
      num-=1
    if k>=i:
        k-=i
        tot+=10
        num-=1
    tot+=num*11
    print(tot)


    
    # 0101 1010 0
    # print(i,j)
  else:

    print(0)

#   odd=even=0
#   # h=0
#   # k=h+1
#   tot=0
#   for i in l:
#     if i%2==0:
#       even+=1
#     else:
#       odd+=1
#   # while k <n :
#   #   if (l[h]+l[k])%2==0 or k-h>1:
#   #     h=k
#   #     k+=1
#   #   else:
#   #     tot+=1
#   #     k+=1
#   print(min(odd,even))