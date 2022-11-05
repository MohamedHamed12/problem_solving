// https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, a: int, b: int) -> int:
   
 
        n1=a.bit_length()
        n2=b.bit_length()
        if  n1!=n2 :
            return 0
        elif a==b:return a
        else:
            ind=1
            while (a>>ind) != (b>>ind) :
                ind+=1
                
            return (a>>ind)<<ind