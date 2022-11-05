// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, l: List[int], target: int) -> List[int]:
        i=0;j=len(l)-1
        while l[i]+l[j]!=target:
            if  l[i]+l[j]>target:j-=1
            else:i+=1
        return [i+1,j+1]
        # n=len(numbers)
        # s=set()
        # for i in range(n):
        #     if numbers[i] in s:continue
        #     s.add( numbers[i])
        #     tem=target-numbers[i]
        #     ind =bisect_right(numbers,tem)
        #     if numbers[ind-1]==tem:
        #         return [i+1,ind]
            # if tem in numbers[i+1:]:return [i+1,i+numbers[i+1:].index(tem)+2]
                       
        
                       