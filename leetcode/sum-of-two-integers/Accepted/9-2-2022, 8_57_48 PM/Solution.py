// https://leetcode.com/problems/sum-of-two-integers

# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#        return a+b
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a&mask if b > mask else a