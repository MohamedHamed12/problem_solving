// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        amount=sorted(amount)
        if amount[2]==amount[1]:return amount[2]+math.ceil(amount[0]/2)
        if amount[0]==0:return max( amount)
        a=amount[2]//2
        if amount[2]%2==1:b=a+1
        else :b=a
        amount[1]-=b
       
        amount[0]-=a
        t=min(max( amount[0], amount[1]),amount[0]+ amount[1])
        if t<0:t=0
        return amount[2]+t
        