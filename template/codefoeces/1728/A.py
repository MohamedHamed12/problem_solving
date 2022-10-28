
def solve():
    nn = int(input())
    l=[int(i) for i in input().split()]
    return l.index(max(l))+1


for i in range(int(input())):
        print(solve())
'''
3
3
1 1 1
1
9
2
4 7


'''