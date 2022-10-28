from collections import  Counter


def solve(arr, x):

    d = Counter()
    for i in arr:
        d.update(Counter(i))
    d.update(Counter(x))
    for i in d:
        if d[i] % 2 == 1:
            return i


for _ in range(int(input())):
    n = int(input())
    arr = [list(input().strip()) for _ in range(2*n)]
    x = input().strip()
    print(str(solve(arr, x)))