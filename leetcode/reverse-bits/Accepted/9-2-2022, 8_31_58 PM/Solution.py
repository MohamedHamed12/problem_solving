// https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        n = '{:032b}'.format(n) # convert into to binary string
        n = n[::-1]             # reverse string
        n = int(n, 2)           # convert string into integer base 2
        return n