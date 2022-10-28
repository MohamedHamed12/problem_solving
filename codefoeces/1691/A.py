for i in range(int(input())):
  n=int(input())
  l=list(map(int,input().split()))
  odd=even=0
  # h=0
  # k=h+1
  tot=0
  for i in l:
    if i%2==0:
      even+=1
    else:
      odd+=1
  # while k <n :
  #   if (l[h]+l[k])%2==0 or k-h>1:
  #     h=k
  #     k+=1
  #   else:
  #     tot+=1
  #     k+=1
  print(min(odd,even))