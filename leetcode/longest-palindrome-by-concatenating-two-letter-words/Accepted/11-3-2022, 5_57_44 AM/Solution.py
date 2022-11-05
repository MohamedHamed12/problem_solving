// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
            d=defaultdict(lambda :0)
            tot=0
            for i in words :
               
                if d[i[::-1]]>0 :
                    tot+=4
                    d[i[::-1]]-=1
                    if d[i[::-1]]==0:d.pop(i[::-1])
                else:d[i]+=1
            for x in words:
                if d[x]!=0 and x[0]==x[1]:tot+=2 ;break
            return tot
            