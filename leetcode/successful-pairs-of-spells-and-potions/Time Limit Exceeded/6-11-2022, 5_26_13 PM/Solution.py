// https://leetcode.com/problems/successful-pairs-of-spells-and-potions

class Solution:
    def successfulPairs(self, spells, potions, success) :
        tot=[]
    

        for i in spells:
            tem=0
            for j in potions:
              t=i*j
              if t>=success:
                  tem+=1
            tot.append(tem)

        return tot