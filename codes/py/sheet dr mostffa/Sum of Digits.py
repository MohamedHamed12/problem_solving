s=input()
count=0
tem=0
while len(s)>1:
  for i in s:
    tem+=int(i)
  count+=1
  s=str(tem)
  tem=0
print(count)

#https://codeforces.com/contest/102/submission/151525684
