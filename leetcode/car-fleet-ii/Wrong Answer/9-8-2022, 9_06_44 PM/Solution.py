// https://leetcode.com/problems/car-fleet-ii

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
          tmp=cars[0][1]
          pos=cars[0][0]
          tot=[]
          for i ,j in cars[::-1]:
                if j<=tmp:
                    tot.append(-1)
                    tmp=j
                    pos=i
                elif j>tmp:
                   
                        tot.append((pos-i)/(j-tmp))
                        tmp=j
                        pos=i
                    
         
          return tot[::-1]