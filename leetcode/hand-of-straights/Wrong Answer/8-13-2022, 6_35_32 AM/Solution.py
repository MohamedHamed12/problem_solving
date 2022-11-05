// https://leetcode.com/problems/hand-of-straights

class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        c=Counter(hand)
        s=sorted(set(hand))
        sm=len(hand)
        if sm%k!=0:return 0
        g=0
        for i in range(len(s)):
            if c[s[i]]-c[s[i-1]]<0:return -1
            g+=c[s[i]]-c[s[i-1]]
        if sm//k==g:return True
        else:return False