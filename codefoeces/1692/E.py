n = int(input())
for i in range(n):
    length, target = map(int, input().split())
    list1 = [int(x) for x in input().split()]
    first, maximum = 0, 0
    end = 0
    sum1 = 0
    if sum(list1) == target:
        print(0)
        continue
    elif sum(list1) < target:
        print("-1")
        continue
    for end in range(length):
        sum1 += list1[end]
        while first < end and sum1 > target:
            sum1 -= list1[first]
            first += 1
        maximum = max(maximum, end - first + 1)
    print(length - maximum)