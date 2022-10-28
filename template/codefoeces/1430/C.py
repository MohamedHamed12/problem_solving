for i in range(int(input())):
    n=int(input()) 
    print(2) 
    if n>2:
        
        print(n-2,n)
        print(n-1,n-1)
        for i in range(n-3):
            print(n-3-i,n-1-i)
    elif n==2:
        print(n-1,n)