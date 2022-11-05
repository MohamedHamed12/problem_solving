// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
            l = 0;
            r = len(height) - 1
            tot = 0
            ml=0;mr=0
            while l < r:
                ml=max(ml,height[l])
                mr=max(mr,height[r])
                m = min(ml ,mr)
                if height[l] <= height[r]:

                    l += 1
                    tot += max(0, m - height[l])
                else:

                    r -= 1
                    tot += max(0, m - height[r])
            return tot