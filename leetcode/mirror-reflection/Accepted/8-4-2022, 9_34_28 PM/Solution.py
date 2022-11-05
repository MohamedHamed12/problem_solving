// https://leetcode.com/problems/mirror-reflection

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        L = lcm(p,q)
        if (L%(2*p))==0:return 0
        else:
            if (L//q)%2==1:return 1
            else:return 2 
#                 while True :
#                     if q==0:return 0

#                     if p%( 2*q)==0:return 2
#                     elif p%( q)==0:return 1
#                     else: q=p-q
#         L = lcm(p,q)

#         if (L//q)%2 == 0:
#             return 2

#         return (L//p)%2