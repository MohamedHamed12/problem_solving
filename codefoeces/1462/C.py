for i in range(int(input())):
    n=int(input())
    if(n<10):
        print(n)
    else:
        b=True
        l=[9]
        while n>sum(l):
            if l[len(l)-1]-1==0:
                print(-1)
                b=False
                break
            elif n<sum(l)+l[len(l)-1]-1:
                l.append(n-sum(l))

            else:
                l.append(l[len(l)-1]-1)
        if b:
            for i in reversed(l):
                print(i,end="")
            print()