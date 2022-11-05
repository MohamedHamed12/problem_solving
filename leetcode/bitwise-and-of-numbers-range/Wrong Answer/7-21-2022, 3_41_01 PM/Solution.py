// https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, a: int, b: int) -> int:
   
 

        n1=a.bit_length()
        n2=b.bit_length()
        if  n1!=n2 :
            return 0
        else:
            ind=n1-1
            while ind>0 :
                b1=a&(1<<ind)
                b2=b&(1<<ind)
                if b1!=b2 :
                   return 1<<(ind+1)
                ind-=1
            return a