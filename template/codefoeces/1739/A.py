


for i in range(int(input())):
        aa,b=map(int,input().split())
        if aa==3 and( b==3 or b==2 ):print(2,2)
        elif aa==2 and( b==3 or b==2 ):print(2,2)
        else:print(1,1)