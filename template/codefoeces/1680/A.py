for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    tem=max(a,c)
    if tem<=b and tem <=d:
        print(tem)
    else :
        print(a+c)