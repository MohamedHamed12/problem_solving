// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        n=len(m);o=len(m[0])
        mm=[i[:] for i in m]

        for i in range(n):
            for j in range(o):
                if mm[i][j]==0:
                    for h in range(o):
                        m[i][h]=0
                    for k in range(n):
                        m[k][j]=0
                        