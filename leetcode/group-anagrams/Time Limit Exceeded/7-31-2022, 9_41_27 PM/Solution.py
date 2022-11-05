// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i=0
        tot=[]
        while strs:
            tem=[strs.pop(0)]
            j=0
            while j<len(strs):
                if  sorted(list(strs[j]))== sorted(list(tem[0])):
                    tem.append(strs.pop(j))
                else:j+=1
            tot.append(tem)
        return tot

                # i+=1