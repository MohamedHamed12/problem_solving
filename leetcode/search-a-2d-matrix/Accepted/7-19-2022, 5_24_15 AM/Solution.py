// https://leetcode.com/problems/search-a-2d-matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False