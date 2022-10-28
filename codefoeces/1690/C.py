for i in range(int(input())):
    n=int(input())
    l1=(list(map(int, input().split())))
    l2=(list(map(int, input().split())))
    print(l2[0]-l1[0],end= " ")
    for i in range(1,n):
        print(l2[i]-max(l1[i],l2[i-1]),end=" ")
        # if l1[i+1]>=l2[i]:
        #     print(l2[i]-l1[i])
        # else:
        #     print(l2[i]-l2[i])
    print()