

for i in range(int(input())):
    n,m,k=map(int,input().split())
    l1=sorted(list(input()))
    l2=sorted(list(input()))
    h=0;w=0
    tot=""
    temh=0
    temw=0
    while h<n and w<m:
        if temh==k:
             temh=0
             tot+=l2[w]
             temw+=1
             w+=1
        elif temw==k:
            temw=0
            tot+=l1[h]
            temh+=1
            h+=1

        



        elif l1[h]<l2[w]:
                tot+=l1[h]
                h+=1
                temh+=1
                temw=0
        else:
                tot+=l2[w]
                w+=1
                temw+=1
                temh=0
       

    print(tot)