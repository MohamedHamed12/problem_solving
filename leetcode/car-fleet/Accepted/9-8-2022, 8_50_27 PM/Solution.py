// https://leetcode.com/problems/car-fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
          b=list(zip(position,speed))
          b=sorted(b,reverse=True)
          tmp=b[0][1]
          pos=b[0][0]
 
          tot=0
          for i ,j in b:
            if j<=tmp:
                tot+=1
                tmp=j
                pos=i
            elif j>tmp:
                if (target-i)/j > (target-pos)/tmp:
                    tot+=1
                    tmp=j
                    pos=i
          return (tot)