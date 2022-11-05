// https://leetcode.com/problems/minimum-window-substring

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:        
#         n=len(s);n2=len(t)
#         c=Counter(t)
#         c2=Counter(s[:n2])
#         ind=n2
#         l=0
#         tot=' '*n
#         def check():
#             for i in c:
#                 if  c[i]>c2[i]:return False
#             return True
        
#         while ind<n :
#             while ind<n:
#                 if check():break
#                 c2[s[ind]]+=1
#                 ind+=1
#             if check() and len(s[l-1:ind])<len(tot):tot=s[l:ind]
#             while True:
#                 if not check():break
#                 elif len(s[l:ind])<len(tot):tot=s[l:ind]
#                 c2[s[l]]-=1
#                 l+=1
#         if check() and n==n2:return s
#         return tot if tot!=' '*n else ''
import collections


class Solution(object):
    def minWindow(self, strFull, strChars):

        countRemaining = len(strChars)
        ansStart,ansEnd = 0, float('inf')
        targCharsRemaining = collections.deaultdict(int)
        
        for ch in strChars:
            targCharsRemaining[ch] +=1
        
        startIndex = 0

        for endIndex, ch in enumerate(strFull, 1):
            
            if targCharsRemaining[ch] > 0:
                countRemaining -= 1
                
            targCharsRemaining[ch] -=1
            
            if countRemaining == 0:
                
                while targCharsRemaining[strFull[startIndex]] < 0:
                    targCharsRemaining[strFull[startIndex]] += 1
                    startIndex +=1
                    
                if endIndex - startIndex < ansEnd - ansStart:
                    ansStart, ansEnd = startIndex, endIndex
                    
                targCharsRemaining[strFull[startIndex]] += 1
                startIndex += 1
                countRemaining += 1
                
        return strFull[ansStart:ansEnd] if ansEnd != float('inf') else ""
