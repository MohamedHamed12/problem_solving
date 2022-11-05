// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount=sorted(amount)
        a=amount[2]//2
        if amount[2]%2==0:b=a+1
        else :b=a
        if amount[1]>b: amount[1]-=b
        else:amount[1]=0
        if amount[0]>a: amount[0]-=a
        else:amount[0]=0
        return amount[2]+max(amount[0],amount[1])
        