// https://leetcode.com/problems/successful-pairs-of-spells-and-potions

import bisect
import math
class Solution:
    def successfulPairs(self, spells, potions, success) :
        n=len(potions)
        potions=sorted(potions)
        tot=[]
    

        for i in spells:
            tem=math.ceil(success/i)
            tem=bisect.bisect_left(potions,tem)
            tot.append(n-tem)
            
            # tem=0
            # for j in potions:
            #   t=i*j
            #   if t>=success:
            #       tem+=1
            # tot.append(tem)

        return tot

        
