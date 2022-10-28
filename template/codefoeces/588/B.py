
import math


def solve(num):
    result=set()
    tot=1
    #for to get prime factorization of the number
    for i in range(2,int(math.sqrt(num))+1):
        while num%i==0:
            result.add(i)
            num//=i
    if num>1:result.add(num)
    for i in result:
        tot*=i 
    print(tot)
        


# input number to test
num=int(input())
solve(num)