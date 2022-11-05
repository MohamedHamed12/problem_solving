// https://leetcode.com/problems/best-poker-hand

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:return "Flush"
        totr=[]
        for i in set(ranks):
           totr.append( ranks.count(i))
        if max(totr)>=3:return "Three of a Kind"
        elif max(totr)>=2:return "Pair"
        else:return "High Card"
        
            
        