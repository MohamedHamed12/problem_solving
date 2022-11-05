// https://leetcode.com/problems/car-fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
          b=list(zip(position,speed))
          b=sorted(b,reverse=True)
          tmp=float('inf')
          tot=0
          for i ,j in b:
                if j<=tmp:
                    tot+=1
                    tmp=j
          return (tot)