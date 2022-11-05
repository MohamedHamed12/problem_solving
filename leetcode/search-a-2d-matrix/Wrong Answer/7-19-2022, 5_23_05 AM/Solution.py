// https://leetcode.com/problems/search-a-2d-matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if target in matrix[i]:
                return matrix[i].index(target)
        return -1