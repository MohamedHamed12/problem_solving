// https://leetcode.com/problems/sum-of-prefix-scores-of-strings

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d=defaultdict(int)
        tot=[0]*len(words)
        for i in words:
            for j in range(1,len(i)+1):d[i[:j]]+=1
        ind=0
        for i in words:
            for j in range(1,len(i)+1):
                tot[ind]+=d[i[:j]]
            ind+=1
        return tot