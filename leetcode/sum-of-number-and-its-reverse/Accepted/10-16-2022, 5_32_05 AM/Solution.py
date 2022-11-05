// https://leetcode.com/problems/sum-of-number-and-its-reverse

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def r(x):  return int(str(x)[::-1])
  
        for i in range(num+1):
            if i+r(i)==num:return True
        return False