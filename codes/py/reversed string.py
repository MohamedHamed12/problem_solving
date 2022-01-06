for i in range(int(input())):
    n = int(input())
    m = list(map(int, input().split()))
    # print(sorted(m))
    # print(sorted(m[:int(len(m)/2)])[::-1])
    print("Yes") if(m[:int(len(m)/2)] == sorted(m[:int(len(m)/2)])[::-1]
                    and m[int(len(m)/2):] == sorted(m[int(len(m)/2):])) else print("No")
    # print(m[int(len(m)/2):])
