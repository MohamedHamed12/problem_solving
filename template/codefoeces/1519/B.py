for i in range(int(input())):                 #for i in range t
    x,y,k=map(int,input().split())            #input vars
    if x>=y :                                 #to get the longest length if it x or y no matter
         x,y=x,y                              #the longest length will take 1
    else :                                    #the anthor wil take the same as lenght
          x,y=y,x

    if (x-1)+(x)*(y-1)==k:
        print("YES")
    else:
        print("NO")