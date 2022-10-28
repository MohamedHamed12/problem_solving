
from  bisect import  bisect_left
def values():return  tuple(map(int,input().split()))
def inlst():return  list(map(int,input().split()))
def inp():return  int(input())


def solve():
    n=inp()
    l=inlst()
    d={}

    arr=[]
    l2=inlst()
    for i in range(n):
        d[l2[i]]=i
    for i in range(n):
        arr.append(d[l[i]])
    # print(arr)
    tmp=arr[0]
    for i in range(1,n):
        if arr[i]>tmp:tmp=arr[i]
        else:return n-i
    return 0
    # lst=[arr[0]]
    # for i in range(1,n):
    #     if arr[i]>lst[-1]:lst.append(arr[i])
    #     else:
    #         lst[bisect_left(lst,arr[i])]=arr[i]
    return n-len(lst)




print((solve()))
#
# n, m = values()
# a = input()
# b = input()
# ans = 0
# mod = 998244353
# count = 0
# r = n - m
# for i in range(m):
#     if b[i] == '1': count += 1
#     if r + i >= 0:
#         if a[i + r] == '1':
#             ans = (ans + count * pow(2, m - i - 1, mod)) % mod
# return ans