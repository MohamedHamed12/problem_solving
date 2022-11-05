// https://leetcode.com/problems/replace-elements-in-an-array

class Solution:
   def arrayChange(self, nums, operations ) :
        nums=sorted(nums);n=len(nums)
        operations=sorted(operations);op=len(operations)
        i=j=0
        while i<n and j<op:
            if nums[i]== operations[j][0]:
                nums[i]=operations[j][1]
                j+=1
                i+=1
            elif nums[i]> operations[j][0]:
                j+=1
            elif nums[i]<operations[j][0]:
                i+=1
        return nums
        