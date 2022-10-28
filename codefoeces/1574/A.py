for i in range(int(input())):
    n=int(input())
    
    h=1
    for j in range(n):
        m=2*n
        while m>0:
            print(h*'(',end="")
            print(h*')',end="")
            # while 2*h> m-2*h
            m-=2*h
            if m<2*h:
                h=int(m/2)
        print()

        h=j+2