
# l1=[]
# s=input()
# if s[1]=='>':
#     l1.append(s[2]);l1.append(s[0])
# else: 
#     l1.append(s[0]);l1.append(s[2])
# l2=[]
# s=input()
# if s[1]=='>':
#     l2.append(s[2]);l2.append(s[0])
# else: 
#     l2.append(s[0]);l2.append(s[2])
# l3=[]
# s=input()
# if s[1]=='>':
#     l3.append(s[2]);l3.append(s[0])
# else: 
#     l3.append(s[0]);l3.append(s[2])
# if l1[0]==l2[0] :
#     print(l1[0],end="")
#     print("".join(l3))
# elif l1[0]==l3[0] :
#     print(l1[0],end="")
#     print("".join(l2))
# elif l2[0]==l3[0] :
#     print(l2[0],end="")
#     print("".join(l1))
# else:print("Impossible")

 

 
    
 

  
# # a=input()
# # if a[1]=='>':print("yes")
# # else:print("no")


def solve():

    d={'A':0, 'B':0, 'C':0}
    for i in range(3):
        a=input()
        if a[1]=='<':
            d[a[2]]+=2
        else:
            d[a[0]]+=2    
    d=sorted(d.items(),key=lambda x:x[1])
    l=[]
    a=""
    for i,j in d:
        if j in  l:
            
            print("Impossible")
            return
        a+=i;l.append(j)

    print(a)
solve()