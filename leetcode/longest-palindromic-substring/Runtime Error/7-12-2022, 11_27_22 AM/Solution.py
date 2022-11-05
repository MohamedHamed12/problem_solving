// https://leetcode.com/problems/longest-palindromic-substring

class Solution(object):
    def lengthOfLIS(self, nums):
        sub = [nums[0]]
        nums = nums[1:]
        for n in nums:
          if sub[-1]<n:
            sub.append(n); continue
          sub[bisect.bisect_left(sub,n)] = n
        return len(sub)