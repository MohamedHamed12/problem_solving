for i in range(int(input())):
    n=int(input())
    if n%3==0:
        tem=(n+3)//3
        print(tem-1,tem,tem-2)
    elif n%3==1:
        tem=(n-1+3)//3
        print(tem-1,tem+1,tem-2)
    elif n%3==2:
        tem=(n-2+3)//3
        print(tem-1+1,tem+1,tem-2)