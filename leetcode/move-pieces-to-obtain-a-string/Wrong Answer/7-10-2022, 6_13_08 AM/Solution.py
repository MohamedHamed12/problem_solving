// https://leetcode.com/problems/move-pieces-to-obtain-a-string

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        j=0
        for i in range(len(start)):
            if start[i]=='_':continue
             
            else:
                while  target[j]=='_':
                    j+=1
                    if j>len(target)-1:
                      return False
               
                if start[i]!=target[j]:return False
                elif start[i]=='R':
                    if j<i:return False
                elif start[i]=='L':
                        if j>i:return False
                            
                j+=1
        while j<len(target):
            if j!='_':return False
            j+=1
        return True
            # for j in target:
            #     if j =='_':continue
            #     elif i