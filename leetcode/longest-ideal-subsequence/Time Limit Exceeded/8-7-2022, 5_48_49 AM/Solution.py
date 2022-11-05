// https://leetcode.com/problems/longest-ideal-subsequence

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
            arr=list(s)
            n = len(arr)
            lis = [1]*n

            for i in range(1, n):
                for j in range(0, i):
                    if abs(ord(arr[i]) - ord(arr[j]))<=k and lis[i] < lis[j] + 1:
                        lis[i] = lis[j]+1

            maximum = 0

            # Pick maximum of all LIS values
            for i in range(n):
                maximum = max(maximum, lis[i])

            return maximum
