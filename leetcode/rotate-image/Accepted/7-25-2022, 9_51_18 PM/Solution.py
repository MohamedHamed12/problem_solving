// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(m)
        tem=[x[:] for x in m]

        for i in range(n):
            for j in range(n):
                m[i][j]=tem[n-j-1][i]
        