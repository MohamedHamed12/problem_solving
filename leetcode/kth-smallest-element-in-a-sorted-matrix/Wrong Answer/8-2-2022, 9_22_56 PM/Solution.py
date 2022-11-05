// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix);m=len(matrix[0])
        i=(-1+k)//m
        j=(-1+k)%m
        return matrix[i][j]