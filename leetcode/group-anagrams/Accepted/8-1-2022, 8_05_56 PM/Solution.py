// https://leetcode.com/problems/group-anagrams

from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, l: List[str]) -> List[List[str]]:
        d=defaultdict(list)

        for i in l:
            d[tuple(sorted(Counter(i).items()))].append(i)
        tem=[]
        for i in d:
            tem.append(d[i])
        return tem
        
#    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = collections.defaultdict(list)
#         for s in strs:
#             h = [0]*26
#             for c in s:
#                 h[ord(c) - ord('a')] += 1
#             d[tuple(h)].append(s)
        
        # return the list of the values of the dictionary
        # each value represent the list of words with the same characters counting
        # if two words have the same characters counting they have the same anagram
        return list(d.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         i=0
#         tot=[]
#         while strs:
#             tem=[strs.pop(0)]
#             j=0
#             while j<len(strs):
#                 if  sorted(list(strs[j]))== sorted(list(tem[0])):
#                     tem.append(strs.pop(j))
#                 else:j+=1
#             tot.append(tem)
#         return tot

#                 # i+=1