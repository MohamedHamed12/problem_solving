// https://leetcode.com/problems/binary-search

class Solution(object):
    def search(self, nums, target):
       try:
          return nums.index(target)
       except:
          return -1