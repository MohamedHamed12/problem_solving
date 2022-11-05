// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[]
        for i in range(n+1):
            count=0
            tem=i
            while tem!=0:
                if tem&1==1:
                    count+=1
                tem=tem>>1
            dp.append(count)
        return dp
             
          
        