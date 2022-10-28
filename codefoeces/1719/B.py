
from io import BytesIO, IOBase

def solve():
    nn,kk=tuple(map(int, input().split()))
    if kk==0:
        print ("NO")
        return 
    l=[]
    for i in range(1,nn+1,2):
        if ((i+kk)*(i+1))%4==0:
            l.append((str(i),i+1))
        elif ((i+1+kk)*(i))%4==0:
            l.append((i+1,str(i)))
        else:
            print("NO")
            return 
    print("YES")
    for i in l:
        print(*i)




for i in range(int(input())):
        solve()