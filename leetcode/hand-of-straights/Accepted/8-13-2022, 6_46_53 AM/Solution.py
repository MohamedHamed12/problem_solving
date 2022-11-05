// https://leetcode.com/problems/hand-of-straights

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
           return False
        hand.sort()
        while len(hand)>0:
            cur = []
            cur.append(hand.pop())
            for i in range(len(hand)-1, -1, -1):
                if len(cur) == groupSize:
                    break
                if hand[i] == cur[len(cur)-1]-1:
                    cur.append(hand[i])
                    hand.pop(i)
            if len(cur) != groupSize:
                return False
        return True 
#         c=Counter(hand)
#         s=sorted(set(hand))
#         sm=len(hand)
#         if sm%k!=0:return False
        
#         g=tmp=c[s[0]]
#         for i in range(1,len(s)):
#             if c[s[i]]-tmp<0:return False
#             tmp=c[s[i]]-tmp
#             g+=tmp
#         if sm//k==g:return True
#         else:return False