// https://leetcode.com/problems/move-pieces-to-obtain-a-string

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        j=0
        for i in range(len(start)):
            if i=='_':continue
                
            else:
                while  j=='_':j+=1
                if i!=j:return False
                j+=1
        return True
            # for j in target:
            #     if j =='_':continue
            #     elif i