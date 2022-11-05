// https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1);n2=len(s2)
        if n2<n1:return False
        d1=[0]*26
        d2=[0]*26
        for i in range(n1):
            d1[ord(s1[i])-97]+=1
        for i in range(n1):
            d2[ord(s2[i])-97]+=1
        i=n1
        while i<n2:
            if d1==d2:return True 
            d2[ord(s2[i])-97]+=1
            d2[ord(s2[i-n1])-97]-=1
            i+=1
        if d1==d2:return True 
        return False