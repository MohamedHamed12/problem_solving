// https://leetcode.com/problems/water-and-jug-problem

class Solution:
    def canMeasureWater(self, a: int, b: int, c: int) -> bool:
        if c%a==0 or c%b==0 :return True
    
        if a%2== b%2:
         if c%2==0:return True
        if a%2!= b%2:
            if c%2!=0:return True
        return False
        