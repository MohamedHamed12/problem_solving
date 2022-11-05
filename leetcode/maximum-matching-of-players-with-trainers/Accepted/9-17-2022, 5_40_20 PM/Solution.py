// https://leetcode.com/problems/maximum-matching-of-players-with-trainers

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        a=sorted(players)
        b=sorted(trainers)
        j=0
        tot=0
        for i in b:
            if j==len(a):break
            if i>=a[j]:tot+=1;j+=1
        return tot
        