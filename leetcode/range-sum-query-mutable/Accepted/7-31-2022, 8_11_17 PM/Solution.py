// https://leetcode.com/problems/range-sum-query-mutable

class BITTree:
	"""
	Implementation of Binary Indexed Tree/Fenwick Tree

	Time:
		create:  O(n*log(n))
		update:  O(log(n))
		get_sum: O(log(n))
	Memory: O(n)
	"""

	def __init__(self, nums: List[int]):
		self.bi_tree = [0] * (len(nums) + 1)
		self.n = len(nums)
		for i in range(self.n):
			self.update(i + 1, nums[i])

	def update(self, index: int, value: int):
		while index <= self.n:
			self.bi_tree[index] += value
			index += self.low_bit(index)

	def get_sum(self, index: int) -> int:
		prefix = 0
		while index > 0:
			prefix += self.bi_tree[index]
			index -= self.low_bit(index)
		return prefix

	@staticmethod
	def low_bit(bit: int) -> int:
		return bit & -bit


class NumArray:

	def __init__(self, nums: List[int]):
		self.nums = nums
		self.bi_tree = BITTree(nums)

	def update(self, i: int, val: int):
		self.bi_tree.update(i + 1, val - self.nums[i])
		self.nums[i] = val

	def sumRange(self, left: int, right: int) -> int:
		return self.bi_tree.get_sum(right + 1) - self.bi_tree.get_sum(left)
# class NumArray:
#     nums = []
#     s = 0
#     l = 0
    
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.s = sum(nums)
#         self.l = len(nums)

#     def update(self, index: int, val: int) -> None:
#         self.s -= self.nums[index]
#         self.nums[index] = val
#         self.s += self.nums[index]

#     def sumRange(self, left: int, right: int) -> int:
#         if right - left > self.l // 2:
#             ans = sum(self.nums[:left]) + sum(self.nums[right + 1:])
#             return self.s - ans
#         else:
#             return sum(self.nums[left: right + 1])

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