def mlt(a,b):
  rem=0
  m=[]

  for i in range(len(b)-1,-1,-1):
    
    for j in range(len(a)-1,-1,-1):

      tem=int(b[i])*int(a[j])+rem
      try:
        ind=(len(a)-j-1+len(b)-i-1)
        tem+=m[-(ind+1)]
        m[-(ind+1)]=tem%10
        rem=int(tem/10)
      except:
        m.insert(0,tem%10)
        rem=int(tem/10)
    if rem!=0:
      try:
         tem+=m[-(ind+2)]
      except:

        m.insert(0,rem)
  print("".join(map(str, m)))
   


while True:
  try:
    a=(input())
  except:
    break

  b=(input())
  mlt(a,b)
