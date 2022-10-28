
l=[]
for i in range (int(input())):
    m=list(map(int ,input().split()))
    l.append(m)

      
      
tot =0
for i in l:
      for j in l:
          if i==j:
            continue
          else:
            if  i[0]==j[1]:
              tot+=1
print(tot)