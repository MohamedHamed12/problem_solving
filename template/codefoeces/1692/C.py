# import sys
# from collections import Counter

# # from ff import solve


def ssolve(l):
    m = 0
    l1 = []
    l2 = []
    m = 0
    for i in range(8):
        if '#' in l[i]:
            co= l[i].count('#')
            if co== 2:
                m = 1
            elif m == 1 and l[i].count("#") == 1:
                print(i+1, l[i].index('#')+1)
                return 0

      
    


for i in range(int(input())):
    input()
    l = []
    for i in range(8):
        tem = ((input().strip()))
        l.append(tem)
    ssolve(l)