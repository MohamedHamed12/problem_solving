for i in range(int(input())):
    n = int(input())
    tem = (n & -n)
    if n < 3:
        print(3)
    else:
        if n == tem:
            print(tem+1)
        else:
            print(tem)