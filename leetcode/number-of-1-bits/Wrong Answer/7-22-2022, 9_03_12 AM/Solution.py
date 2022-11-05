// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
                ind=n.bit_length()-2
                count=1
                while ind>=0:
                    tem=(1<<ind)&n
                    if tem!=0:
                        count+=1
                    ind-=1
                return count
