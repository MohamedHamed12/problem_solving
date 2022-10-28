n=int(input())
top=int(input())
b=True
for i in range(n):
  dright,dleft=map(int,input().split())
  if top!=dleft and top!=7-dleft and top!=dright and top!=7-dright:
    pass
  else:
    b=False
if b :
  print("YES") 
else :
  print("NO")