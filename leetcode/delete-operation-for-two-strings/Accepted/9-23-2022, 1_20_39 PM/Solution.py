// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
       
        n1=len(word1);     n2=len(word2)
        memo={}
        def rec(i,j):
            if i==n1 :return n2-j 
            if j==n2:return n1-i
            if (i,j) in memo:return memo[(i,j)]
            
            if word1[i]==word2[j]:  ret=rec(i+1,j+1)
            else: ret=min(rec(i+1,j),rec(i,j+1))+1
               
            memo[(i,j)]=ret
            return ret
        return rec(0,0)
        