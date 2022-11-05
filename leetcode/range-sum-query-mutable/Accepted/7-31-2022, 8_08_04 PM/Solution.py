// https://leetcode.com/problems/range-sum-query-mutable

class NumArray:
    nums = []
    s = 0
    l = 0
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.s = sum(nums)
        self.l = len(nums)

    def update(self, index: int, val: int) -> None:
        self.s -= self.nums[index]
        self.nums[index] = val
        self.s += self.nums[index]

    def sumRange(self, left: int, right: int) -> int:
        if right - left > self.l // 2:
            ans = sum(self.nums[:left]) + sum(self.nums[right + 1:])
            return self.s - ans
        else:
            return sum(self.nums[left: right + 1])

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.num=nums
#         tem=0
#         self.s=[0]
#         for i in range(len(nums)):
#             tem+= self.num[i]
#             self.s.append(tem)
            
            
         
        

#     def update(self, index: int, val: int) -> None:
#         brev=self.num[index]
#         self.num[index]=val
#         m=val-brev
#         for i in range(index+1,len(self.s)):
#             self.s[i]+=m
        

#     def sumRange(self, left: int, right: int) -> int:
#         return self.s[right+1]-self.s[left]
#                 # return sum(self.num[left:right+1])

        


# # Your NumArray object will be instantiated and called as such:
# # obj = NumArray(nums)
# # obj.update(index,val)
# # param_2 = obj.sumRange(left,right)